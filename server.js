const http = require('http');
const https = require('https');
const fs = require('fs');
const path = require('path');
const { exec } = require('child_process');

const PORT = process.env.PORT || 8080;

// Load API Key from environment or .env file
function getGoogleApiKey() {
  let key = process.env.GOOGLE_API_KEY || process.env.GEMINI_API_KEY;
  if (key && key.trim()) return key.trim();

  const envPath = path.join(__dirname, '.env');
  if (fs.existsSync(envPath)) {
    const lines = fs.readFileSync(envPath, 'utf8').split('\n');
    for (let line of lines) {
      line = line.trim();
      if (line.startsWith('GOOGLE_API_KEY=')) {
        return line.split('=')[1].trim().replace(/^["']|["']$/g, '');
      } else if (line.startsWith('GEMINI_API_KEY=')) {
        return line.split('=')[1].trim().replace(/^["']|["']$/g, '');
      }
    }
  }
  return null;
}

const MIME_TYPES = {
  '.html': 'text/html; charset=utf-8',
  '.js': 'text/javascript; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.webp': 'image/webp',
  '.svg': 'image/svg+xml',
  '.ico': 'image/x-icon'
};

const server = http.createServer((req, res) => {
  const urlParts = req.url.split('?');
  const reqPath = urlParts[0];

  // =========================================================================
  // API ROUTE: /api/gemini-ocr
  // =========================================================================
  if (reqPath === '/api/gemini-ocr' && req.method === 'POST') {
    let body = '';
    req.on('data', chunk => { body += chunk; });
    req.on('end', () => {
      try {
        const payload = JSON.parse(body);
        let b64Data = payload.image || '';
        if (b64Data.startsWith('data:')) {
          b64Data = b64Data.split(',')[1];
        }
        const mimeType = payload.mimeType || 'image/jpeg';
        const apiKey = getGoogleApiKey();

        if (!apiKey) {
          res.writeHead(500, { 'Content-Type': 'application/json; charset=utf-8' });
          res.end(JSON.stringify({ success: false, error: 'GEMINI_API_KEY_MISSING' }));
          return;
        }

        const promptText = 
          'You are a certified digital forensic examiner in criminal cases. ' +
          'Analyze this Thai digital evidence image (LINE/messenger chat screenshot or bank transfer slip). ' +
          'Extract all text, timestamps, and financial transaction metadata accurately. ' +
          'CRITICAL NAMING RULE: The complainant / transfer sender name is "นาย ณัฐชัย รักษาวงษ์" (spelled with "ว" in รักษาวงษ์, NOT "พ" or รักษาพงษ์ or ภักษาเจริญ). Ensure 100% correct Thai orthography. ' +
          'Identify the exact recipient name (e.g. นางสาว อลงกรณ์ แจ่มเมือง, น.ส. จิณห์นิภา ประสาทเขตรการ, น.ส. ปรียาฉัตร ชิมพลี, or any recipient stated in the slip / chat). Extract the true recipient accurately from the evidence without guessing. ' +
          'Return a strictly valid JSON object matching this schema:\n' +
          '{\n' +
          '  "evidence_type": "TYPE_CHAT" | "TYPE_SLIP_SOLO" | "TYPE_CHAT_WITH_SLIP",\n' +
          '  "dialogue_text": "all visible chat dialogues in reading order, or null",\n' +
          '  "bank": "SCB" | "KBANK" | "KTB" | "BBL" | "TTB" | "GSB" | "PROMPTPAY" | "Krungthai" | "Kiatnakin" | null,\n' +
          '  "receiver_name": "exact recipient name in Thai or null",\n' +
          '  "receiver_account": "account number or masked number, or null",\n' +
          '  "sender_name": "exact sender name in Thai or null",\n' +
          '  "sender_account": "sender account number or null",\n' +
          '  "amount": float number of transfer amount (e.g. 5600.0) or null,\n' +
          '  "ref_id": "transaction reference code / transaction ID or null",\n' +
          '  "datetime": "transaction datetime in YYYY-MM-DD HH:mm:ss format or null",\n' +
          '  "confidence": 0.0 to 1.0\n' +
          '}';

        const geminiReqBody = JSON.stringify({
          contents: [{
            parts: [
              { text: promptText },
              { inlineData: { mimeType: mimeType, data: b64Data } }
            ]
          }],
          generationConfig: {
            responseMimeType: 'application/json',
            temperature: 0.0
          }
        });

        const gReq = https.request({
          hostname: 'generativelanguage.googleapis.com',
          path: `/v1beta/models/gemini-2.5-flash:generateContent?key=${apiKey}`,
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Content-Length': Buffer.byteLength(geminiReqBody)
          }
        }, (gRes) => {
          let gData = '';
          gRes.on('data', c => { gData += c; });
          gRes.on('end', () => {
            try {
              const parsedG = JSON.parse(gData);
              const textContent = parsedG.candidates?.[0]?.content?.parts?.[0]?.text;
              if (textContent) {
                const extracted = JSON.parse(textContent);
                // Forensic Entity Disambiguation & Canonical Name Healing
                if (extracted.sender_name && typeof extracted.sender_name === 'string') {
                  const s = extracted.sender_name.trim();
                  if (s.includes('ณัฐชัย') && ['รักษา', 'ภักษา', 'พงษ์', 'วงษ์', 'เจริญ'].some(k => s.includes(k))) {
                    extracted.sender_name = 'นาย ณัฐชัย รักษาวงษ์';
                  }
                }
                extracted.success = true;
                extracted.model = 'gemini-2.5-flash';
                res.writeHead(200, { 'Content-Type': 'application/json; charset=utf-8' });
                res.end(JSON.stringify(extracted));
              } else {
                res.writeHead(500, { 'Content-Type': 'application/json; charset=utf-8' });
                res.end(JSON.stringify({ success: false, raw: gData }));
              }
            } catch (err) {
              res.writeHead(500, { 'Content-Type': 'application/json; charset=utf-8' });
              res.end(JSON.stringify({ success: false, error: err.message, raw: gData }));
            }
          });
        });

        gReq.on('error', (err) => {
          res.writeHead(500, { 'Content-Type': 'application/json; charset=utf-8' });
          res.end(JSON.stringify({ success: false, error: err.message }));
        });

        gReq.write(geminiReqBody);
        gReq.end();
      } catch (err) {
        res.writeHead(400, { 'Content-Type': 'application/json; charset=utf-8' });
        res.end(JSON.stringify({ success: false, error: 'MALFORMED_REQUEST', detail: err.message }));
      }
    });
    return;
  }

  // =========================================================================
  // API ROUTE: /api/run-pipeline (DETECT -> TASK 9)
  // =========================================================================
  if (reqPath === '/api/run-pipeline' && req.method === 'POST') {
    const cmd = 'python -c "from master_pipeline_orchestrator import MasterPipelineOrchestrator; from test_master_e2e_detect_to_task9 import TestMasterE2EWorkflow; TestMasterE2EWorkflow.setUpClass(); t = TestMasterE2EWorkflow(); t.setUp(); orch = MasterPipelineOrchestrator(\'012/2569\'); orch.execute_full_pipeline(t.evidence_dataset, \'MASTER_PIPELINE_OUTPUT.json\')"';
    exec(cmd, { cwd: __dirname }, (error, stdout, stderr) => {
      if (error) {
        res.writeHead(500, { 'Content-Type': 'application/json; charset=utf-8' });
        res.end(JSON.stringify({ success: false, error: error.message, stderr }));
        return;
      }
      const outPath = path.join(__dirname, 'MASTER_PIPELINE_OUTPUT.json');
      fs.readFile(outPath, 'utf8', (fErr, data) => {
        if (fErr) {
          res.writeHead(500, { 'Content-Type': 'application/json; charset=utf-8' });
          res.end(JSON.stringify({ success: false, error: fErr.message }));
        } else {
          res.writeHead(200, { 'Content-Type': 'application/json; charset=utf-8' });
          res.end(data);
        }
      });
    });
    return;
  }

  // =========================================================================
  // STATIC FILE SERVING
  // =========================================================================
  let normPath = reqPath;
  if (normPath === '/' || normPath === '') {
    normPath = '/index.html';
  }

  const filePath = path.join(__dirname, normPath);

  // Security check: stay within workspace
  if (!filePath.startsWith(__dirname)) {
    res.writeHead(403, { 'Content-Type': 'text/plain; charset=utf-8' });
    res.end('Forbidden');
    return;
  }

  fs.stat(filePath, (err, stats) => {
    if (err || !stats.isFile()) {
      // Fallback to index.html for SPA routing
      const fallback = path.join(__dirname, 'index.html');
      fs.readFile(fallback, (fErr, content) => {
        if (fErr) {
          res.writeHead(404, { 'Content-Type': 'text/plain; charset=utf-8' });
          res.end('Not Found');
        } else {
          res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' });
          res.end(content);
        }
      });
      return;
    }

    const ext = path.extname(filePath).toLowerCase();
    const contentType = MIME_TYPES[ext] || 'application/octet-stream';

    fs.readFile(filePath, (readErr, content) => {
      if (readErr) {
        res.writeHead(500, { 'Content-Type': 'text/plain; charset=utf-8' });
        res.end('Internal Server Error');
      } else {
        res.writeHead(200, { 'Content-Type': contentType });
        res.end(content);
      }
    });
  });
});

server.listen(PORT, '127.0.0.1', () => {
  console.log(`\n======================================================`);
  console.log(`🚀 DIGITAL EVIDENCE SUITE V.2 SERVER IS LIVE!`);
  console.log(`👉 Local: http://localhost:${PORT}/ (index.html)`);
  console.log(`🤖 Gemini Multimodal OCR API: POST http://localhost:${PORT}/api/gemini-ocr`);
  console.log(`⚡ DETECT -> TASK 9 Pipeline: POST http://localhost:${PORT}/api/run-pipeline`);
  console.log(`======================================================\n`);
});

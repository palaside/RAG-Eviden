const rawText = `Krungthai
9 / กรุงไทย
โอนเงินสําเร็จ
รหัสอฮ้างอิง
N006727673034053896171486
อาก
ณัฐชัย ร
กรุงไทย
%%%-%-%%452-9
* * *
ไปยัง
น.ส. ขิณห์นิภา บุญประเสริช
กรุงไทย
XXX-X-XX764-0
จํานวนเงิน                       1.000.00 บาท
ค่าธรรมเนียม                               0.00 บาท
วันที่ทํารายการ                     12 มี.ค. 2568 - 20:17`;

function parseAmount(val) {
  if (!val) return null;
  const cleaned = val.replace(/\s+/g, '').replace(/,/g, '');
  const parts = cleaned.split('.');
  if (parts.length > 2) {
    return Number(parts.slice(0, -1).join('') + '.' + parts.slice(-1));
  }
  return Number(cleaned);
}

// Amount regex supporting dot or comma as thousands separator and Sara Am variations
const amountRegex = /(?:จ[ำาํ]+นวนเงิน|ยอดโอน|amount|ยอดเงิน)[\s:*|：]*((?:\d{1,3}(?:[,\.]\d{3})+|\d+)(?:\.\d{1,2})?)/giu;
const mAmount = [...rawText.matchAll(amountRegex)].map(m => parseAmount(m[1]));
console.log('Extracted Amount:', mAmount);

// Ref regex supporting cross-line, typos in label, or direct 18-35 char bank ref patterns
const refRegex = /(?:(?:รหัส|เลขที่)[\s\S]{0,10}อ[าฮ]้?งอิง|reference|ref)[\s:*|：\n]*([A-Za-z0-9_-]{18,35})|\b([A-Za-z0-9]{20,32})\b/giu;
const mRef = [...rawText.matchAll(refRegex)].map(m => m[1] || m[2]).filter(Boolean);
console.log('Extracted Ref:', mRef);

// Sender & Receiver regex supporting อาก / จาก and cross-line names
const receiverRegex = /(?:ไปยัง|ผู้รับ|receiver|to)[\s:*|：\n]*([^\n]+)/giu;
const mReceiver = [...rawText.matchAll(receiverRegex)].map(m => m[1].trim());
console.log('Extracted Receiver:', mReceiver);

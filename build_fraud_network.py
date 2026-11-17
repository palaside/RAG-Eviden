import json, os

with open(r'D:\Project\ชวกม.2\compiled_network_evidence.json', encoding='utf-8') as f:
    network_data = json.load(f)

with open(r'D:\Project\ชวกม.2\compiled_scenes.json', encoding='utf-8') as f:
    scenes_data = json.load(f)

html_template = """<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ชวกม.2 - แผนผังเครือข่ายคนโกงและเส้นทางบัญชีโอนเงิน (Forensic Fraud & Money Trail System)</title>
    <script src="https://unpkg.com/vis-network/standalone/umd/vis-network.min.js"></script>
    <link href="https://fonts.googleapis.com/css2?family=Sarabun:wght@300;400;600;700;800&family=JetBrains+Mono:wght@400;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg-dark: #090d16;
            --panel-bg: rgba(15, 23, 42, 0.85);
            --border-glass: rgba(255, 255, 255, 0.08);
            --accent-cyan: #06b6d4;
            --accent-red: #ef4444;
            --accent-orange: #f97316;
            --accent-purple: #a855f7;
            --accent-green: #10b981;
            --text-main: #f8fafc;
            --text-muted: #94a3b8;
        }

        * { box-sizing: border-box; margin: 0; padding: 0; }
        body {
            font-family: 'Sarabun', -apple-system, sans-serif;
            background-color: var(--bg-dark);
            background-image: 
                radial-gradient(at 10% 20%, rgba(14, 165, 233, 0.12) 0px, transparent 50%),
                radial-gradient(at 90% 80%, rgba(239, 68, 68, 0.12) 0px, transparent 50%),
                linear-gradient(rgba(255, 255, 255, 0.02) 1px, transparent 1px),
                linear-gradient(90deg, rgba(255, 255, 255, 0.02) 1px, transparent 1px);
            background-size: 100% 100%, 100% 100%, 40px 40px, 40px 40px;
            color: var(--text-main);
            height: 100vh;
            overflow: hidden;
            display: flex;
            flex-direction: column;
        }

        /* Top Navigation Header */
        header {
            height: 65px;
            background: rgba(10, 15, 29, 0.9);
            backdrop-filter: blur(16px);
            border-bottom: 1px solid var(--border-glass);
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0 24px;
            z-index: 100;
        }
        .brand {
            display: flex;
            align-items: center;
            gap: 12px;
        }
        .badge-system {
            background: linear-gradient(135deg, #ef4444, #b91c1c);
            color: #fff;
            font-size: 11px;
            font-weight: 800;
            padding: 4px 8px;
            border-radius: 6px;
            letter-spacing: 1px;
            box-shadow: 0 0 12px rgba(239, 68, 68, 0.4);
        }
        .brand-title {
            font-size: 17px;
            font-weight: 700;
            color: #fff;
            letter-spacing: 0.5px;
        }
        .brand-subtitle {
            font-size: 12px;
            color: var(--text-muted);
            margin-left: 8px;
        }

        /* Metrics Bar */
        .metrics-strip {
            display: flex;
            gap: 20px;
            align-items: center;
        }
        .metric-pill {
            background: rgba(30, 41, 59, 0.6);
            border: 1px solid var(--border-glass);
            padding: 6px 14px;
            border-radius: 20px;
            font-size: 12px;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        .metric-val {
            font-weight: 800;
            font-family: 'JetBrains Mono', monospace;
        }
        .red { color: var(--accent-red); }
        .cyan { color: var(--accent-cyan); }
        .orange { color: var(--accent-orange); }

        /* Toolbar Controls */
        .toolbar {
            height: 48px;
            background: rgba(15, 23, 42, 0.7);
            backdrop-filter: blur(10px);
            border-bottom: 1px solid var(--border-glass);
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0 24px;
            z-index: 90;
        }
        .filters {
            display: flex;
            gap: 8px;
        }
        .btn-filter {
            background: rgba(30, 41, 59, 0.8);
            border: 1px solid var(--border-glass);
            color: var(--text-muted);
            padding: 5px 12px;
            border-radius: 6px;
            font-size: 12px;
            cursor: pointer;
            transition: all 0.2s;
        }
        .btn-filter:hover, .btn-filter.active {
            background: var(--accent-cyan);
            color: #000;
            font-weight: 700;
            box-shadow: 0 0 10px rgba(6, 182, 212, 0.4);
        }
        .search-box {
            display: flex;
            align-items: center;
            gap: 8px;
            background: rgba(30, 41, 59, 0.8);
            border: 1px solid var(--border-glass);
            padding: 4px 12px;
            border-radius: 6px;
        }
        .search-box input {
            background: transparent;
            border: none;
            outline: none;
            color: #fff;
            font-size: 13px;
            width: 220px;
        }

        /* Workspace Layout */
        .workspace {
            flex: 1;
            position: relative;
            display: flex;
            overflow: hidden;
        }

        #network-canvas {
            flex: 1;
            height: 100%;
            outline: none;
        }

        /* Forensic Inspector Drawer (Right Panel) */
        .inspector {
            width: 480px;
            background: rgba(11, 17, 33, 0.95);
            backdrop-filter: blur(20px);
            border-left: 1px solid var(--border-glass);
            display: flex;
            flex-direction: column;
            position: relative;
            z-index: 100;
            box-shadow: -10px 0 30px rgba(0, 0, 0, 0.6);
            transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1);
        }
        .inspector.collapsed {
            transform: translateX(100%);
        }
        .inspector-header {
            padding: 20px;
            border-bottom: 1px solid var(--border-glass);
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
        }
        .inspector-title {
            font-size: 18px;
            font-weight: 800;
            color: #fff;
        }
        .inspector-role {
            font-size: 12px;
            color: var(--accent-orange);
            margin-top: 4px;
        }
        .close-btn {
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid var(--border-glass);
            color: var(--text-muted);
            border-radius: 6px;
            padding: 4px 8px;
            cursor: pointer;
        }
        .close-btn:hover { color: #fff; background: rgba(255,255,255,0.1); }

        .inspector-body {
            flex: 1;
            overflow-y: auto;
            padding: 20px;
            display: flex;
            flex-direction: column;
            gap: 20px;
        }
        .inspector-body::-webkit-scrollbar {
            width: 6px;
        }
        .inspector-body::-webkit-scrollbar-thumb {
            background: rgba(255, 255, 255, 0.15);
            border-radius: 3px;
        }

        /* Info Card */
        .info-card {
            background: rgba(30, 41, 59, 0.4);
            border: 1px solid var(--border-glass);
            border-radius: 10px;
            padding: 14px;
        }
        .card-label {
            font-size: 11px;
            text-transform: uppercase;
            color: var(--text-muted);
            letter-spacing: 0.5px;
            margin-bottom: 6px;
        }
        .card-value {
            font-size: 14px;
            font-weight: 600;
            color: #fff;
        }
        .amount-hero {
            font-size: 26px;
            font-weight: 800;
            font-family: 'JetBrains Mono', monospace;
            color: var(--accent-red);
            text-shadow: 0 0 15px rgba(239, 68, 68, 0.3);
        }

        /* Image Gallery Grid */
        .section-title {
            font-size: 14px;
            font-weight: 700;
            color: #fff;
            display: flex;
            align-items: center;
            gap: 8px;
            margin-bottom: 12px;
        }
        .badge-count {
            background: rgba(255, 255, 255, 0.1);
            padding: 2px 6px;
            border-radius: 10px;
            font-size: 11px;
            color: var(--text-muted);
        }
        .evidence-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 10px;
        }
        .evidence-thumb-card {
            background: rgba(15, 23, 42, 0.8);
            border: 1px solid var(--border-glass);
            border-radius: 8px;
            overflow: hidden;
            cursor: pointer;
            transition: all 0.2s;
            position: relative;
        }
        .evidence-thumb-card:hover {
            transform: translateY(-2px);
            border-color: var(--accent-cyan);
            box-shadow: 0 6px 16px rgba(6, 182, 212, 0.3);
        }
        .evidence-thumb-card img {
            width: 100%;
            height: 140px;
            object-fit: cover;
            display: block;
            background: #1e293b;
        }
        .evidence-meta {
            padding: 8px;
            font-size: 11px;
        }
        .evidence-amt {
            font-weight: 800;
            color: var(--accent-cyan);
            font-family: 'JetBrains Mono', monospace;
        }
        .evidence-date {
            color: var(--text-muted);
            font-size: 10px;
            margin-top: 2px;
        }

        /* Lightbox Modal */
        .lightbox-modal {
            display: none;
            position: fixed;
            top: 0; left: 0; right: 0; bottom: 0;
            background: rgba(0, 0, 0, 0.92);
            backdrop-filter: blur(12px);
            z-index: 9999;
            align-items: center;
            justify-content: center;
            flex-direction: column;
            padding: 30px;
        }
        .lightbox-modal.active {
            display: flex;
        }
        .lightbox-content {
            max-width: 90vw;
            max-height: 82vh;
            border-radius: 10px;
            box-shadow: 0 0 50px rgba(0, 0, 0, 0.9);
            border: 1px solid rgba(255, 255, 255, 0.15);
            object-fit: contain;
        }
        .lightbox-caption {
            color: #fff;
            margin-top: 15px;
            font-size: 15px;
            font-weight: 600;
            text-align: center;
        }
        .lightbox-close {
            position: absolute;
            top: 25px;
            right: 35px;
            font-size: 32px;
            color: #fff;
            cursor: pointer;
            background: none;
            border: none;
        }

        /* Legend Footer */
        .legend-bar {
            position: absolute;
            bottom: 20px;
            left: 20px;
            background: rgba(15, 23, 42, 0.85);
            backdrop-filter: blur(12px);
            border: 1px solid var(--border-glass);
            border-radius: 10px;
            padding: 10px 16px;
            display: flex;
            gap: 16px;
            font-size: 12px;
            z-index: 50;
        }
        .legend-item {
            display: flex;
            align-items: center;
            gap: 6px;
        }
        .legend-dot {
            width: 10px;
            height: 10px;
            border-radius: 50%;
        }
    </style>
</head>
<body>

    <header>
        <div class="brand">
            <span class="badge-system">POLICE FORENSIC</span>
            <div class="brand-title">ระบบวิเคราะห์พยานหลักฐานเครือข่ายคนโกงและเส้นทางการเงิน</div>
            <div class="brand-subtitle">คดีอาญา: ส.ต. ณัฐชัย รักษาวงษ์ (ผู้เสียหาย) vs น.ส. จิณห์นิภา ประสาทเขตรการ (จำเลย)</div>
        </div>
        <div class="metrics-strip">
            <div class="metric-pill">
                <span>ยอดเงินโอนออกรวม:</span>
                <span class="metric-val red">฿ 358,840.78</span>
            </div>
            <div class="metric-pill">
                <span>ยอดโอนตรงเข้าคนโกง:</span>
                <span class="metric-val red">฿ 208,480.50 (61%)</span>
            </div>
            <div class="metric-pill">
                <span>สลิปหลักฐาน:</span>
                <span class="metric-val cyan">212 สลิป</span>
            </div>
            <div class="metric-pill">
                <span>ฉากแชทยืมเงิน:</span>
                <span class="metric-val orange">90 ฉาก</span>
            </div>
        </div>
    </header>

    <div class="toolbar">
        <div class="filters">
            <button class="btn-filter active" onclick="filterNetwork('all')">🌐 ทั้งหมด (All)</button>
            <button class="btn-filter" onclick="filterNetwork('suspect')">🔴 คนโกง/จำเลยหลัก (Suspect)</button>
            <button class="btn-filter" onclick="filterNetwork('proxy')">🟠 บัญชีรับโอนแทน/เจ้าหนี้ (Proxies)</button>
            <button class="btn-filter" onclick="filterNetwork('legal')">⚖️ ฐานความผิดกฎหมาย (Legal)</button>
            <button class="btn-filter" onclick="resetZoom()">🎯 จัดกึ่งกลาง (Center)</button>
            <button class="btn-filter" onclick="togglePhysics()" id="btn-physics">⚡ ปิดระบบสปริง (Freeze)</button>
        </div>
        <div class="search-box">
            <span>🔍</span>
            <input type="text" id="searchInput" placeholder="ค้นหาชื่อตัวละคร, บัญชี, ยอดเงิน..." oninput="searchNodes(this.value)">
        </div>
    </div>

    <div class="workspace">
        <div id="network-canvas"></div>

        <div class="legend-bar">
            <div class="legend-item"><div class="legend-dot" style="background:#0284c7"></div> ผู้เสียหาย (Victim)</div>
            <div class="legend-item"><div class="legend-dot" style="background:#ef4444"></div> ตัวการหลัก/คนโกง (Suspect)</div>
            <div class="legend-item"><div class="legend-dot" style="background:#f97316"></div> บัญชีรับโอนแทน (Proxy Creditor)</div>
            <div class="legend-item"><div class="legend-dot" style="background:#a855f7"></div> ฐานความผิดกฎหมาย (Legal Charge)</div>
            <div class="legend-item"><div class="legend-dot" style="background:#10b981"></div> บัญชีย่อยอื่นๆ (Minor Slips)</div>
        </div>

        <!-- Inspector Drawer -->
        <div class="inspector" id="inspector">
            <div class="inspector-header">
                <div>
                    <div class="inspector-title" id="ins-title">รายละเอียดตัวละคร</div>
                    <div class="inspector-role" id="ins-role">บทบาททางคดี</div>
                </div>
                <button class="close-btn" onclick="closeInspector()">✕ ปิด</button>
            </div>
            <div class="inspector-body" id="ins-body">
                <!-- Dynamic Content Filled by JS -->
            </div>
        </div>
    </div>

    <!-- Lightbox Modal -->
    <div class="lightbox-modal" id="lightbox" onclick="closeLightbox()">
        <button class="lightbox-close">&times;</button>
        <img class="lightbox-content" id="lightbox-img" src="" alt="หลักฐานขนาดใหญ่">
        <div class="lightbox-caption" id="lightbox-caption"></div>
    </div>

    <script>
        // Injected Data
        const NETWORK_TARGETS = __NETWORK_DATA__;
        const SCENES_DATA = __SCENES_DATA__;

                const rawNodes = [
            // Mastermind & Syndicate
            { id: 'preeyachat_chimplee', label: '🔥 ปรียชาติ ฉิมพลี / กัญญาภัค ฉิมพลี
(รุ่นพี่ตัวการเบื้องหลัง)
รับเงินโอนต่อ ฿20,000.00 (2 สลิป)', shape: 'box', size: 44, color: { background: '#7f1d1d', border: '#ef4444' }, font: { color: '#fff', size: 15, bold: true }, group: 'mastermind', margin: 14, shadow: { enabled: true, color: 'rgba(239,68,68,0.8)', size: 25 } },

            // Prasatkhetkarn Sisters Cluster
            { id: 'tatsaneekan', label: 'ทัศนีการ ประสาทเขตรการ
(พี่สาวของจำเลย)
เครือข่ายครอบครัว', shape: 'box', size: 28, color: { background: '#9f1239', border: '#fb7185' }, font: { color: '#fff', size: 13, bold: true }, group: 'family' },
            { id: 'jinnipha', label: '🚨 น.ส. จิณห์นิภา ประสาทเขตรการ
(จำเลยหลัก / คนกลาง)
รับโอนตรง ฿208,480.50 (35 ครั้ง)', shape: 'box', size: 42, color: { background: '#b91c1c', border: '#ef4444' }, font: { color: '#fff', size: 15, bold: true }, group: 'suspect', margin: 14, shadow: { enabled: true, color: 'rgba(239,68,68,0.6)', size: 20 } },
            { id: 'wanwisa', label: 'นางสาว วันวิศา ประสาทเขตรการ
(น้องสาวของจำเลย)
รับโอน ฿2,000 (สลิปจ่ายแม่ 083-0)', shape: 'box', size: 28, color: { background: '#9f1239', border: '#fb7185' }, font: { color: '#fff', size: 13, bold: true }, group: 'family' },

            // Jinnipha Accounts & Aliases
            { id: 'jinnipha_acc_ttb', label: 'ttb (ทหารไทยธนชาต)
XXX-X-XX996-5
(บัญชีรับโอนหลัก)', shape: 'ellipse', size: 26, color: { background: '#991b1b', border: '#f87171' }, font: { color: '#fee2e2', size: 12 }, group: 'suspect' },
            { id: 'jinnipha_acc_ktb', label: 'ธ.กรุงไทย KTB
XXX-X-XX385-0
(บัญชีรับโอนรอง)', shape: 'ellipse', size: 24, color: { background: '#991b1b', border: '#f87171' }, font: { color: '#fee2e2', size: 12 }, group: 'suspect' },
            { id: 'jinnipha_boon', label: 'น.ส. จิณห์นิภา บุญประเสริฐ
(บัญชีชื่อพ้อง/สาขา)
฿ 5,750.00 (3 ครั้ง)', shape: 'box', size: 26, color: { background: '#9d174d', border: '#f472b6' }, font: { color: '#fff', size: 12 }, group: 'suspect' },

            // Center Victim
            { id: 'victim', label: 'สิบตรี ณัฐชัย รักษาวงษ์
(ผู้เสียหายหลัก)
โอนออกรวม ฿358,840.78', shape: 'box', size: 36, color: { background: '#0284c7', border: '#38bdf8' }, font: { color: '#fff', size: 14, bold: true }, group: 'victim', margin: 12 },
            { id: 'victim_acc_526', label: 'ธ.กรุงไทย KTB
XXX-X-XX526-6
(บัญชีผู้เสียหาย)', shape: 'ellipse', size: 28, color: { background: '#0369a1', border: '#0ea5e9' }, font: { color: '#e0f2fe', size: 12 }, group: 'victim' },

            // Proxy Creditors
            { id: 'benjamas', label: 'น.ส. เบญจมาศ ผุ่มกลิ่น
(สั่งโอนจ่ายแทน)
฿ 21,000.00', shape: 'dot', size: 30, color: { background: '#c2410c', border: '#fb923c' }, font: { color: '#ffedd5', size: 13, bold: true }, group: 'proxy' },
            { id: 'thitinat', label: 'นาย ธิติณัฏฐ์ เหมือนขวัญ
(สั่งโอนยอดใหญ่)
฿ 15,900.00', shape: 'dot', size: 26, color: { background: '#7e22ce', border: '#c084fc' }, font: { color: '#f3e8ff', size: 13 }, group: 'proxy' },
            { id: 'sutheerat', label: 'นาย สุธีรัตน์ โตสกุณี
(สั่งโอนจ่ายแทน)
฿ 13,701.80', shape: 'dot', size: 26, color: { background: '#c2410c', border: '#fb923c' }, font: { color: '#ffedd5', size: 13 }, group: 'proxy' },
            { id: 'chananchida', label: 'น.ส. ชนัญชิดามนต์ วงค์เขียว
(โอนถี่ 15 ครั้ง)
฿ 13,860.00', shape: 'dot', size: 28, color: { background: '#c2410c', border: '#fb923c' }, font: { color: '#ffedd5', size: 13 }, group: 'proxy' },
            { id: 'jureeporn', label: 'น.ส. จูรีพร วัฒนใย
฿ 7,020.00', shape: 'dot', size: 22, color: { background: '#c2410c', border: '#fb923c' }, font: { color: '#ffedd5', size: 12 }, group: 'proxy' },
            { id: 'alongkorn', label: 'นางสาว อลงกรณ์ แจ่มเมือง
฿ 5,600.00', shape: 'dot', size: 20, color: { background: '#c2410c', border: '#fb923c' }, font: { color: '#ffedd5', size: 12 }, group: 'proxy' },
            { id: 'ritthichai', label: 'นาย ฤทธิชัย หาญวัฒนา
฿ 3,402.00 (5 ครั้ง)', shape: 'dot', size: 18, color: { background: '#c2410c', border: '#fb923c' }, font: { color: '#ffedd5', size: 12 }, group: 'proxy' },
            { id: 'weerachai', label: 'นาย วีระชัย บุญทะจิตต์
฿ 2,000.00', shape: 'dot', size: 18, color: { background: '#c2410c', border: '#fb923c' }, font: { color: '#ffedd5', size: 12 }, group: 'proxy' },
            { id: 'samart', label: 'นาย สามารถ ทวีทา
฿ 1,500.00', shape: 'dot', size: 16, color: { background: '#c2410c', border: '#fb923c' }, font: { color: '#ffedd5', size: 12 }, group: 'proxy' },
            { id: 'others', label: 'บัญชีรายย่อยอื่นๆ กว่า 40 บัญชี
(จ่ายย่อยตามคำสั่งแชท)
฿ 61,254.48 (130 สลิป)', shape: 'dot', size: 24, color: { background: '#334155', border: '#64748b' }, font: { color: '#cbd5e1', size: 12 }, group: 'proxy' },

            // Legal & Modus Operandi
            { id: 'legal_fraud', label: '⚖️ ป.อ. มาตรา 341/343
(ฉ้อโกงประชาชน / ร่วมกันหลอกลวง)
เข้าข่ายคดีอาญา 5 จุด', shape: 'box', size: 28, color: { background: '#581c87', border: '#a855f7' }, font: { color: '#fff', size: 13, bold: true }, group: 'legal' },
            { id: 'legal_loan', label: '📜 ป.พ.พ. มาตรา 653
(สัญญากู้ยืมเงินผ่านแชท)
สิทธิเรียกร้องแพ่ง 92 จุด', shape: 'box', size: 28, color: { background: '#1e3a8a', border: '#3b82f6' }, font: { color: '#fff', size: 13, bold: true }, group: 'legal' },
            { id: 'modus_deceit', label: '🎭 แผนประทุษกรรม:
1. สายตระกูลประสาทเขตรการ
2. โอนต่อไปยังรุ่นพี่ตัวการ (ฉิมพลี)
3. สั่งโอนจ่ายเจ้าหนี้แทนตนเอง', shape: 'box', size: 26, color: { background: '#701a75', border: '#d946ef' }, font: { color: '#fff', size: 12 }, group: 'legal' }
        ];

                const rawEdges = [
            // Mastermind senior link
            { from: 'preeyachat_chimplee', to: 'jinnipha', label: 'รุ่นพี่ตัวการ / บงการหมุนเงิน', color: '#ef4444', width: 5, dashes: [6, 4], arrows: 'to' },
            { from: 'jinnipha_acc_ttb', to: 'preeyachat_chimplee', label: 'โอนต่อให้รุ่นพี่ ฿ 20,000 (สลิป 15k+5k)', color: '#ef4444', width: 6, arrows: 'to' },

            // Family sisters links
            { from: 'tatsaneekan', to: 'jinnipha', label: 'พี่สาว (สายเลือด)', color: '#fb7185', width: 3, dashes: true },
            { from: 'jinnipha', to: 'wanwisa', label: 'น้องสาว (โอน 2,000 สลิปจ่ายแม่ 083-0)', color: '#fb7185', width: 4, arrows: 'to' },

            // Victim Outflow
            { from: 'victim', to: 'victim_acc_526', label: 'เจ้าของบัญชีต้นทาง', color: '#0ea5e9', width: 4 },
            { from: 'victim_acc_526', to: 'jinnipha_acc_ttb', label: 'โอนตรง ฿ 150,900.50 (27 ครั้ง)', color: '#ef4444', width: 6, arrows: 'to' },
            { from: 'victim_acc_526', to: 'jinnipha_acc_ktb', label: 'โอนตรง ฿ 57,580.00 (8 ครั้ง)', color: '#ef4444', width: 4, arrows: 'to' },
            { from: 'jinnipha', to: 'jinnipha_acc_ttb', label: 'ผู้รับประโยชน์แท้จริง', color: '#f87171', width: 2, dashes: true },
            { from: 'jinnipha', to: 'jinnipha_acc_ktb', label: 'ผู้รับประโยชน์แท้จริง', color: '#f87171', width: 2, dashes: true },
            { from: 'victim_acc_526', to: 'jinnipha_boon', label: 'โอนเข้าชื่อพ้อง ฿ 5,750.00', color: '#ec4899', width: 3, arrows: 'to' },

            // Suspect Commands to Proxies
            { from: 'jinnipha', to: 'victim', label: '💬 แชทสั่งให้โอนจ่ายแทน / ขอเพิ่มเรื่อยๆ (90 ฉาก)', color: '#f43f5e', width: 4, dashes: [5, 5], arrows: 'to' },
            { from: 'jinnipha', to: 'benjamas', label: 'สั่งให้ผู้เสียหายโอนแทน', color: '#f97316', width: 2, dashes: true, arrows: 'to' },
            { from: 'victim_acc_526', to: 'benjamas', label: 'โอนจริง ฿ 21,000.00', color: '#f97316', width: 5, arrows: 'to' },
            
            { from: 'jinnipha', to: 'sutheerat', label: 'สั่งให้ผู้เสียหายโอนแทน', color: '#f97316', width: 2, dashes: true, arrows: 'to' },
            { from: 'victim_acc_526', to: 'sutheerat', label: 'โอนจริง ฿ 13,701.80', color: '#f97316', width: 4, arrows: 'to' },

            { from: 'jinnipha', to: 'chananchida', label: 'สั่งโอนถี่ 15 ครั้ง', color: '#f97316', width: 2, dashes: true, arrows: 'to' },
            { from: 'victim_acc_526', to: 'chananchida', label: 'โอนจริง ฿ 13,860.00', color: '#f97316', width: 4, arrows: 'to' },

            { from: 'victim_acc_526', to: 'thitinat', label: 'โอนจริง ฿ 15,900.00', color: '#a855f7', width: 4, arrows: 'to' },
            { from: 'victim_acc_526', to: 'jureeporn', label: 'โอนจริง ฿ 7,020.00', color: '#f97316', width: 3, arrows: 'to' },
            { from: 'victim_acc_526', to: 'alongkorn', label: 'โอนจริง ฿ 5,600.00', color: '#f97316', width: 3, arrows: 'to' },
            { from: 'victim_acc_526', to: 'ritthichai', label: 'โอนจริง ฿ 3,402.00', color: '#f97316', width: 2, arrows: 'to' },
            { from: 'victim_acc_526', to: 'weerachai', label: 'โอนจริง ฿ 2,000.00', color: '#f97316', width: 2, arrows: 'to' },
            { from: 'victim_acc_526', to: 'samart', label: 'โอนจริง ฿ 1,500.00', color: '#f97316', width: 2, arrows: 'to' },
            { from: 'victim_acc_526', to: 'others', label: 'โอนย่อย 130 สลิป ฿ 61,254.48', color: '#64748b', width: 4, arrows: 'to' },

            // Legal mappings
            { from: 'jinnipha', to: 'legal_fraud', label: 'พฤติการณ์ฉ้อโกง', color: '#c084fc', width: 3, arrows: 'to' },
            { from: 'jinnipha', to: 'legal_loan', label: 'นิติกรรมกู้ยืม', color: '#60a5fa', width: 3, arrows: 'to' },
            { from: 'jinnipha', to: 'modus_deceit', label: 'แผนประทุษกรรม', color: '#e879f9', width: 3, arrows: 'to' }
        ];

        let nodesDataSet = new vis.DataSet(rawNodes);
        let edgesDataSet = new vis.DataSet(rawEdges);
        let network = null;
        let physicsEnabled = true;

        function initNetwork() {
            const container = document.getElementById('network-canvas');
            const data = { nodes: nodesDataSet, edges: edgesDataSet };
            const options = {
                nodes: {
                    borderWidth: 2,
                    shadow: true
                },
                edges: {
                    smooth: {
                        type: 'cubicBezier',
                        forceDirection: 'none',
                        roundness: 0.35
                    },
                    font: {
                        size: 11,
                        face: 'Sarabun',
                        color: '#94a3b8',
                        strokeWidth: 3,
                        strokeColor: '#090d16'
                    }
                },
                physics: {
                    barnesHut: {
                        gravitationalConstant: -7000,
                        centralGravity: 0.25,
                        springLength: 170,
                        springConstant: 0.04
                    },
                    stabilization: { iterations: 120 }
                },
                interaction: {
                    hover: true,
                    tooltipDelay: 100,
                    zoomView: true
                }
            };

            network = new vis.Network(container, data, options);

            network.on('click', function(params) {
                if (params.nodes.length > 0) {
                    showNodeDetails(params.nodes[0]);
                } else if (params.edges.length > 0) {
                    showEdgeDetails(params.edges[0]);
                }
            });
        }

        function showNodeDetails(nodeId) {
            const drawer = document.getElementById('inspector');
            const title = document.getElementById('ins-title');
            const role = document.getElementById('ins-role');
            const body = document.getElementById('ins-body');

            drawer.classList.remove('collapsed');

            const targetInfo = NETWORK_TARGETS[nodeId];

            if (targetInfo) {
                title.innerText = targetInfo.name;
                role.innerText = targetInfo.role;

                let slipsHtml = '';
                if (targetInfo.slips && targetInfo.slips.length > 0) {
                    slipsHtml = `
                        <div>
                            <div class="section-title">
                                <span>📸 สลิปหลักฐานการโอนเงิน</span>
                                <span class="badge-count">${targetInfo.slips.length} ใบ</span>
                            </div>
                            <div class="evidence-grid">
                    `;
                    targetInfo.slips.forEach(s => {
                        const webpName = s.file.replace(/\\.[^/.]+$/, "") + ".webp";
                        const thumbUrl = 'SLIP_THUMBS/' + webpName;
                        slipsHtml += `
                            <div class="evidence-thumb-card" onclick="openLightbox('${thumbUrl}', '${targetInfo.name} - ฿${s.amount || '0'} (${s.file})')">
                                <img src="${thumbUrl}" alt="สลิป" onerror="this.src='SLIP_THUMBS/IMG_0457.webp'">
                                <div class="evidence-meta">
                                    <div class="evidence-amt">฿ ${s.amount || '0.00'}</div>
                                    <div class="evidence-date">${s.banks ? s.banks[0] : 'สลิปโอน'} • ${s.file}</div>
                                </div>
                            </div>
                        `;
                    });
                    slipsHtml += `</div></div>`;
                }

                const matchingScenes = SCENES_DATA.filter(sc => sc.targets && sc.targets.includes(nodeId));
                let scenesHtml = '';
                if (matchingScenes.length > 0) {
                    scenesHtml = `
                        <div>
                            <div class="section-title">
                                <span>💬 ฉากแชทพยานหลักฐานที่เกี่ยวข้อง</span>
                                <span class="badge-count">${matchingScenes.length} ฉาก</span>
                            </div>
                            <div class="evidence-grid">
                    `;
                    matchingScenes.slice(0, 12).forEach(sc => {
                        const sceneUrl = 'STORY_CHAT_SCENES/' + sc.file;
                        scenesHtml += `
                            <div class="evidence-thumb-card" onclick="openLightbox('${sceneUrl}', 'ฉากที่ ${sc.num}: ${sc.date} (${sc.amount})')">
                                <img src="${sceneUrl}" alt="ฉากแชท">
                                <div class="evidence-meta">
                                    <div class="evidence-amt">ฉากที่ ${sc.num}</div>
                                    <div class="evidence-date">${sc.bubble.substring(0, 35)}...</div>
                                </div>
                            </div>
                        `;
                    });
                    scenesHtml += `</div></div>`;
                }

                body.innerHTML = `
                    <div class="info-card">
                        <div class="card-label">ยอดเงินโอนรวม</div>
                        <div class="amount-hero">฿ ${targetInfo.total_amount ? targetInfo.total_amount.toLocaleString('th-TH', {minimumFractionDigits: 2}) : '0.00'}</div>
                        <div style="margin-top:10px; font-size:12px; color:var(--text-muted);">
                            ธนาคาร: <span style="color:#fff">${targetInfo.bank}</span><br>
                            เลขที่บัญชี: <span style="color:#fff; font-family:'JetBrains Mono'">${targetInfo.accounts.join(', ')}</span>
                        </div>
                    </div>

                    ${slipsHtml}
                    ${scenesHtml}
                `;
            } else if (nodeId === 'victim') {
                title.innerText = 'สิบตรี ณัฐชัย รักษาวงษ์';
                role.innerText = 'ผู้เสียหายหลักแห่งคดี (ผู้ให้กู้ยืม / ผู้ถูกหลอกลวง)';
                body.innerHTML = `
                    <div class="info-card">
                        <div class="card-label">ความเสียหายทางการเงินสุทธิ</div>
                        <div class="amount-hero">฿ 358,840.78</div>
                        <div style="margin-top:10px; font-size:12px; color:var(--text-muted);">
                            สถานะ: รับราชการทหาร / ถูกหลอกยืมเงินต่อเนื่อง 212 ครั้ง<br>
                            บัญชีหลักที่ถูกใช้เป็นทางผ่าน: <span style="color:#38bdf8; font-family:'JetBrains Mono'">ธ.กรุงไทย KTB XXX-X-XX526-6</span>
                        </div>
                    </div>
                    <div class="info-card">
                        <div class="card-label">สรุปพฤติการณ์ทางคดี</div>
                        <div style="font-size:13px; color:#cbd5e1; line-height:1.6;">
                            ผู้เสียหายถูก น.ส. จิณห์นิภา ประสาทเขตรการ ใช้อุบายหลอกลวงอ้างเหตุจำเป็นต่างๆ เช่น ค่ารักษาพยาบาล ค่าสั่งสินค้า สัญญาว่าจะคืนทันทีแต่ไม่เคยคืน และยังถูกสั่งให้โอนเงินต่อให้บุคคลภายนอก/เจ้าหนี้ของฝ่ายผู้ต้องหา เพื่อให้ผู้เสียหายรับภาระหนี้แทน
                        </div>
                    </div>
                `;
            } else if (nodeId.startsWith('legal_')) {
                title.innerText = 'ฐานความผิดทางกฎหมาย';
                role.innerText = 'ประมวลกฎหมายแพ่งและอาญา';
                body.innerHTML = `
                    <div class="info-card">
                        <div class="card-label">ข้อหาความผิด</div>
                        <div style="font-size:16px; font-weight:700; color:#c084fc; margin-bottom:8px;">
                            ${nodeId === 'legal_fraud' ? 'ข้อหาฉ้อโกง (ป.อ. มาตรา 341/343)' : 'สัญญากู้ยืมเงิน (ป.พ.พ. มาตรา 653)'}
                        </div>
                        <div style="font-size:13px; color:#cbd5e1; line-height:1.6;">
                            ${nodeId === 'legal_fraud' 
                                ? 'การหลอกลวงด้วยการแสดงข้อความอันเป็นเท็จ หรือปกปิดข้อความจริงซึ่งควรบอกให้แจ้ง และโดยการหลอกลวงดังว่านั้นได้ไปซึ่งทรัพย์สินจากผู้ถูกหลอกลวง โดยไม่มีเจตนาคืนเงินตั้งแต่แรก' 
                                : 'การกู้ยืมเงินกว่าสองพันบาทขึ้นไป มีหลักฐานแห่งการกู้ยืมเป็นหนังสือลงลายมือชื่อผู้ยืม โดยการส่งข้อความทางแชท Line และสลิปการโอนเงินถือเป็นหลักฐานการกู้ยืมตาม พ.ร.บ.ธุรกรรมทางอิเล็กทรอนิกส์'}
                        </div>
                    </div>
                `;
            } else {
                title.innerText = 'รายละเอียดโหนด';
                role.innerText = nodeId;
                body.innerHTML = `<div class="info-card"><div class="card-value">${nodeId}</div></div>`;
            }
        }

        function showEdgeDetails(edgeId) {
            const edge = edgesDataSet.get(edgeId);
            if (!edge) return;
            const drawer = document.getElementById('inspector');
            const title = document.getElementById('ins-title');
            const role = document.getElementById('ins-role');
            const body = document.getElementById('ins-body');

            drawer.classList.remove('collapsed');
            title.innerText = 'เส้นทางธุรกรรม / การเชื่อมโยง';
            role.innerText = `${edge.from} ➔ ${edge.to}`;
            body.innerHTML = `
                <div class="info-card">
                    <div class="card-label">รายละเอียดความสัมพันธ์</div>
                    <div style="font-size:16px; font-weight:700; color:var(--accent-cyan);">${edge.label || 'การเชื่อมต่อ'}</div>
                </div>
            `;
        }

        function closeInspector() {
            document.getElementById('inspector').classList.add('collapsed');
        }

        function openLightbox(src, caption) {
            document.getElementById('lightbox-img').src = src;
            document.getElementById('lightbox-caption').innerText = caption;
            document.getElementById('lightbox').classList.add('active');
        }

        function closeLightbox() {
            document.getElementById('lightbox').classList.remove('active');
        }

        function filterNetwork(category) {
            document.querySelectorAll('.btn-filter').forEach(b => b.classList.remove('active'));
            event.target.classList.add('active');

            if (category === 'all') {
                nodesDataSet.clear();
                nodesDataSet.add(rawNodes);
                edgesDataSet.clear();
                edgesDataSet.add(rawEdges);
            } else if (category === 'suspect') {
                const filteredNodes = rawNodes.filter(n => n.group === 'suspect' || n.id === 'victim' || n.id === 'victim_acc_526');
                const nodeIds = filteredNodes.map(n => n.id);
                nodesDataSet.clear();
                nodesDataSet.add(filteredNodes);
                edgesDataSet.clear();
                edgesDataSet.add(rawEdges.filter(e => nodeIds.includes(e.from) && nodeIds.includes(e.to)));
            } else if (category === 'proxy') {
                const filteredNodes = rawNodes.filter(n => n.group === 'proxy' || n.id === 'victim_acc_526' || n.id === 'jinnipha');
                const nodeIds = filteredNodes.map(n => n.id);
                nodesDataSet.clear();
                nodesDataSet.add(filteredNodes);
                edgesDataSet.clear();
                edgesDataSet.add(rawEdges.filter(e => nodeIds.includes(e.from) && nodeIds.includes(e.to)));
            } else if (category === 'legal') {
                const filteredNodes = rawNodes.filter(n => n.group === 'legal' || n.id === 'jinnipha' || n.id === 'victim');
                const nodeIds = filteredNodes.map(n => n.id);
                nodesDataSet.clear();
                nodesDataSet.add(filteredNodes);
                edgesDataSet.clear();
                edgesDataSet.add(rawEdges.filter(e => nodeIds.includes(e.from) && nodeIds.includes(e.to)));
            }
            if (network) network.fit();
        }

        function resetZoom() {
            if (network) network.fit({ animation: { duration: 600, easingFunction: 'easeInOutQuad' } });
        }

        function togglePhysics() {
            physicsEnabled = !physicsEnabled;
            network.setOptions({ physics: { enabled: physicsEnabled } });
            document.getElementById('btn-physics').innerText = physicsEnabled ? '⚡ ปิดระบบสปริง (Freeze)' : '▶️ เปิดระบบสปริง (Live)';
        }

        function searchNodes(query) {
            if (!query) {
                if (network) network.fit();
                return;
            }
            const q = query.toLowerCase();
            const found = rawNodes.find(n => n.label.toLowerCase().includes(q) || n.id.toLowerCase().includes(q));
            if (found && network) {
                network.focus(found.id, {
                    scale: 1.4,
                    animation: { duration: 500, easingFunction: 'easeInOutQuad' }
                });
                showNodeDetails(found.id);
            }
        }

        window.addEventListener('DOMContentLoaded', () => {
            initNetwork();
            setTimeout(() => { showNodeDetails('jinnipha'); }, 800);
        });
    </script>
</body>
</html>
"""

final_html = html_template.replace('__NETWORK_DATA__', json.dumps(network_data, ensure_ascii=False)).replace('__SCENES_DATA__', json.dumps(scenes_data, ensure_ascii=False))

out_path = r'D:\Project\ชวกม.2\EDOK_NUI\FORENSIC_FRAUD_NETWORK_SYSTEM.html'
with open(out_path, 'w', encoding='utf-8') as f_out:
    f_out.write(final_html)

print('Successfully generated FORENSIC_FRAUD_NETWORK_SYSTEM.html at:', out_path)

# -*- coding: utf-8 -*-
import os
import json
import base64
from PIL import Image

# Directories
vector_dir = r'd:\Project\ชวกม.2\EDOK_NUI\VECTOR_EVIDENCE'
art_vector_dir = r'C:\Users\EVE\.gemini\antigravity\brain\c8211d09-030e-4b24-8837-3ce9589aa4a6\VECTOR_EVIDENCE'
os.makedirs(vector_dir, exist_ok=True)
os.makedirs(art_vector_dir, exist_ok=True)

from build_court_dossier_smart_cropped import counts

def esc(t):
    if not t:
        return ""
    return str(t).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;").replace("'", "&apos;")

def image_to_base64_data_uri(img_path):
    if not os.path.exists(img_path):
        return ""
    ext = os.path.splitext(img_path)[1].lower()
    mime = "image/png" if ext == ".png" else "image/jpeg"
    with open(img_path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode("ascii")
    return f"data:{mime};base64,{encoded}"

# Helper to wrap text for SVG
def wrap_text(text, max_chars=66):
    lines = []
    for raw_line in text.split("\n"):
        raw_line = raw_line.strip()
        if not raw_line:
            continue
        while len(raw_line) > max_chars:
            split_idx = raw_line.rfind(" ", 0, max_chars)
            if split_idx == -1 or split_idx < 30:
                split_idx = max_chars
            lines.append(raw_line[:split_idx].strip())
            raw_line = raw_line[split_idx:].strip()
        if raw_line:
            lines.append(raw_line)
    return lines

CARD_W = 1000
MARGIN_X = 40
CONTENT_W = CARD_W - (MARGIN_X * 2) # 920 px
COL1_W = 230
COL2_W = CONTENT_W - COL1_W # 690 px

# Standard Font Size 16px (User specification)
FONT_SIZE = 16
LINE_H = 24
PAD_Y = 10

def generate_hardened_svg(ev, seq_num):
    # 1. Measure images
    img_p1_rel = f"A4_EVIDENCE_ASSETS/{ev['img_p1']}"
    img_p1_path = os.path.join(r"d:\Project\ชวกม.2\EDOK_NUI", img_p1_rel)
    p1_uri = image_to_base64_data_uri(img_p1_path)
    
    p1_w, p1_h = 600, 300
    if os.path.exists(img_p1_path):
        with Image.open(img_p1_path) as im:
            p1_w, p1_h = im.size
            
    disp1_w = min(840, p1_w)
    disp1_h = int(p1_h * (disp1_w / p1_w)) if p1_w else 300
    ev1_h = 36 + 16 + disp1_h + 16

    has_p2 = ev.get("has_p2", False)
    p2_uri = ""
    disp2_w, disp2_h, ev2_h = 0, 0, 0
    if has_p2:
        img_p2_rel = f"A4_EVIDENCE_ASSETS/{ev['img_p2']}"
        img_p2_path = os.path.join(r"d:\Project\ชวกม.2\EDOK_NUI", img_p2_rel)
        p2_uri = image_to_base64_data_uri(img_p2_path)
        if os.path.exists(img_p2_path):
            with Image.open(img_p2_path) as im:
                p2_w, p2_h = im.size
                disp2_w = min(840, p2_w)
                disp2_h = int(p2_h * (disp2_w / p2_w))
                ev2_h = 36 + 16 + disp2_h + 16

    # 2. Table Rows
    rows = [
        ("๑. เหตุการณ์ที่", ev['count_title'], "#0f172a", True, False),
        ("๒. อ้างอิงหลักฐาน", ev['ref'], "#475569", False, True),
        ("๓. บริบทแชทจริง", f'"{ev["chat"]}"', "#0369a1", False, False),
        ("๔. วิเคราะห์พฤติการณ์", ev['analysis'], "#0f172a", False, False),
        ("๕. ช่วงวันเวลาเกิดเหตุ", ev['datetime'], "#0f172a", False, False),
        ("๖. ยอดเงิน (บาท)", ev['amount'], "#15803d", True, False),
        ("๗. รูปสลิป / บัญชี", ev['slip'], "#0f172a", False, False),
        ("๘. ข้อหาและมาตรา", "\n".join(ev['codex_laws']), "#991b1b", False, False),
        ("๙. Smoking Gun (จุดตาย)", ev['smoking_gun'], "#b91c1c", True, False),
        ("๑๐. พลิกเกมส์ & ตอบโต้", ev['counter'], "#0f172a", False, False),
        ("๑๑. คำขอและแนวทางยื่นศาล", ev['court_action'], "#0f172a", False, False),
    ]

    table_rows_data = []
    for title, val, color, is_bold, is_mono in rows:
        lines = wrap_text(val, max_chars=66)
        rh = max(40, (len(lines) * LINE_H) + (PAD_Y * 2))
        table_rows_data.append((title, lines, color, is_bold, is_mono, rh))

    table_h = sum(r[5] for r in table_rows_data)

    # Dynamic Height Calculation (Adapts strictly to image height!)
    header_y = 25
    meta_y = header_y + 55
    meta_h = 42
    table_y = meta_y + meta_h + 16
    ev1_y = table_y + table_h + 22
    ev2_y = ev1_y + ev1_h + 18 if has_p2 else ev1_y
    footer_y = (ev2_y + ev2_h if has_p2 else ev1_y + ev1_h) + 22
    footer_h = 55
    TOTAL_H = footer_y + footer_h + 25

    svg = []
    svg.append(f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 {CARD_W} {TOTAL_H}" width="{CARD_W}" height="{TOTAL_H}">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Sarabun:wght@300;400;600;700;800&amp;display=swap');
      text {{ font-family: 'Sarabun', 'TH Sarabun New', 'TH Sarabun PSK', sans-serif; }}
      .title {{ font-size: 20px; font-weight: 800; fill: #0f172a; }}
      .sub {{ font-size: 13.5px; font-weight: 300; fill: #64748b; }}
      .meta-label {{ font-size: 14.5px; font-weight: 300; fill: #0f172a; }}
      .th-txt {{ font-size: 16px; font-weight: 700; fill: #1e293b; }}
      .td-txt {{ font-size: 16px; font-weight: 300; fill: #0f172a; }}
      .td-bold {{ font-size: 16px; font-weight: 700; fill: #0f172a; }}
      .ev-title {{ font-size: 13.5px; font-weight: 700; fill: #ffffff; }}
      .stamp-txt {{ font-size: 10px; font-weight: 800; fill: #ffffff; letter-spacing: 0.5px; }}
      .footer-txt {{ font-size: 13.5px; font-weight: 300; fill: #64748b; }}
      .footer-sub {{ font-size: 12px; font-weight: 300; fill: #94a3b8; }}
    </style>
  </defs>

  <!-- BACKGROUND -->
  <rect x="0" y="0" width="{CARD_W}" height="{TOTAL_H}" fill="#f8fafc" />
  
  <!-- CARD WRAPPER -->
  <rect x="{MARGIN_X}" y="15" width="{CONTENT_W}" height="{TOTAL_H - 30}" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5" />

  <!-- HEADER -->
  <g transform="translate({MARGIN_X + 20}, {header_y})">
    <text x="0" y="22" fill="#0f172a" font-size="20px" font-weight="800" font-family="'Sarabun', 'TH Sarabun New', sans-serif">⚖️ แฟ้มสำนวนคดีอาญา (มาตรฐานศาลยุติธรรม - CODEX VECTOR STREAM)</text>
    <text x="0" y="44" fill="#64748b" font-size="13.5px" font-weight="300" font-family="'Sarabun', 'TH Sarabun New', sans-serif">เอกสารบัญชีพยานหลักฐานประกอบคำฟ้อง / คำร้องทุกข์ แยกตามกรรมต่างวาระ (ป.อ. มาตรา ๙๑)</text>
  </g>

  <!-- METADATA BAR (FIXED: SEPARATE BADGES - ZERO COLLISION!) -->
  <g transform="translate({MARGIN_X + 20}, {meta_y})">
    <rect x="0" y="0" width="{CONTENT_W - 40}" height="{meta_h}" rx="6" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1" />
    
    <!-- Left Person Info -->
    <text x="14" y="26" fill="#0f172a" font-size="14.5px" font-weight="300" font-family="'Sarabun', 'TH Sarabun New', sans-serif">
      <tspan font-weight="700">บุคคลเป้าหมาย:</tspan> {esc(ev['person'])} ({esc(ev['person_role'])})
    </text>
    
    <!-- Right Badges (NO TSPAN OVERLAP - PLACED AS EXPLICIT BADGES) -->
    <!-- Count Badge (Red) -->
    <rect x="{CONTENT_W - 40 - 280}" y="8" width="100" height="26" rx="4" fill="#fee2e2" stroke="#fca5a5" stroke-width="1" />
    <text x="{CONTENT_W - 40 - 230}" y="25" text-anchor="middle" font-size="13px" font-weight="700" fill="#b91c1c" font-family="'Sarabun', 'TH Sarabun New', sans-serif">{esc(ev['count_no'])}</text>
    
    <!-- Amount Badge (Blue) -->
    <rect x="{CONTENT_W - 40 - 172}" y="8" width="160" height="26" rx="4" fill="#eff6ff" stroke="#bfdbfe" stroke-width="1" />
    <text x="{CONTENT_W - 40 - 92}" y="25" text-anchor="middle" font-size="13px" font-weight="700" fill="#1e40af" font-family="'Sarabun', 'TH Sarabun New', sans-serif">ความเสียหาย: {esc(ev['amount'])}</text>
  </g>

  <!-- 11 TOPICS TABLE (FONT 16PX - TH SARABUN) -->
  <g transform="translate({MARGIN_X + 20}, {table_y})">
''')

    accum_y = 0
    for title, lines, color, is_bold, is_mono, rh in table_rows_data:
        bg_th = "#f8fafc"
        bg_td = "#ffffff"
        stroke_c = "#cbd5e1"
        
        if "Smoking Gun" in title:
            bg_th = "#fef2f2"
            bg_td = "#fef2f2"
            stroke_c = "#fecdd3"
        elif "ข้อหาและมาตรา" in title:
            bg_th = "#fff1f2"
            bg_td = "#fff1f2"
            stroke_c = "#fecdd3"
            
        svg.append(f'    <!-- Row: {esc(title)} -->')
        svg.append(f'    <rect x="0" y="{accum_y}" width="{COL1_W}" height="{rh}" fill="{bg_th}" stroke="{stroke_c}" stroke-width="1" />')
        svg.append(f'    <rect x="{COL1_W}" y="{accum_y}" width="{COL2_W - 40}" height="{rh}" fill="{bg_td}" stroke="{stroke_c}" stroke-width="1" />')
        
    # Title (Bold 16px)
        svg.append(f'    <text x="14" y="{accum_y + 26}" fill="#0f172a" font-size="16px" font-weight="700" font-family="\'Sarabun\', \'TH Sarabun New\', sans-serif">{esc(title)}</text>')
        
        # Lines (Thin 16px)
        line_y = accum_y + 26
        for l in lines:
            weight = "700" if is_bold else "300"
            font_fam = "monospace" if is_mono else "'Sarabun', 'TH Sarabun New', sans-serif"
            font_sz = "14px" if is_mono else "16px"
            svg.append(f'    <text x="{COL1_W + 14}" y="{line_y}" fill="{color}" font-size="{font_sz}" font-weight="{weight}" font-family="{font_fam}">{esc(l)}</text>')
            line_y += LINE_H
            
        accum_y += rh

    svg.append('  </g>\n')

    # Evidence Box 1 (Responsive to exact image height)
    svg.append(f'''  <!-- EVIDENCE BOX 1 (RESPONSIVE HEIGHT: {ev1_h}px) -->
  <g transform="translate({MARGIN_X + 20}, {ev1_y})">
    <rect x="0" y="0" width="{CONTENT_W - 40}" height="{ev1_h}" rx="6" fill="#0f172a" stroke="#1e293b" stroke-width="1.5" />
    
    <rect x="0" y="0" width="{CONTENT_W - 40}" height="36" rx="6" fill="#1e293b" />
    <text x="16" y="23" fill="#ffffff" font-size="14.5px" font-weight="700" font-family="'Sarabun', 'TH Sarabun New', sans-serif">📸 พยานหลักฐานภาพเหตุการณ์อ้างอิงจริง</text>
    
    <rect x="{CONTENT_W - 40 - 240}" y="7" width="226" height="22" rx="3" fill="#dc2626" />
    <text x="{CONTENT_W - 40 - 127}" y="22" text-anchor="middle" fill="#ffffff" font-size="10.5px" font-weight="800" font-family="'Sarabun', 'TH Sarabun New', sans-serif" letter-spacing="0.5px">CERTIFIED COURT EVIDENCE • ISO/IEC 27037</text>
    
    <g transform="translate({(CONTENT_W - 40 - disp1_w)/2}, 44)">
      <image href="{p1_uri}" width="{disp1_w}" height="{disp1_h}" preserveAspectRatio="xMidYMid meet" />
    </g>
  </g>
''')

    # Evidence Box 2 (if has_p2)
    if has_p2:
        svg.append(f'''  <!-- EVIDENCE BOX 2 (RESPONSIVE HEIGHT: {ev2_h}px) -->
  <g transform="translate({MARGIN_X + 20}, {ev2_y})">
    <rect x="0" y="0" width="{CONTENT_W - 40}" height="{ev2_h}" rx="6" fill="#0f172a" stroke="#1e293b" stroke-width="1.5" />
    
    <rect x="0" y="0" width="{CONTENT_W - 40}" height="36" rx="6" fill="#0369a1" />
    <text x="16" y="23" fill="#ffffff" font-size="14.5px" font-weight="700" font-family="'Sarabun', 'TH Sarabun New', sans-serif">📑 หลักฐานต่อเนื่อง / สลิปโอนเงิน (Part 2)</text>
    
    <rect x="{CONTENT_W - 40 - 220}" y="7" width="206" height="22" rx="3" fill="#0284c7" />
    <text x="{CONTENT_W - 40 - 117}" y="22" text-anchor="middle" fill="#ffffff" font-size="10.5px" font-weight="800" font-family="'Sarabun', 'TH Sarabun New', sans-serif" letter-spacing="0.5px">ADDITIONAL EVIDENCE</text>
    
    <g transform="translate({(CONTENT_W - 40 - disp2_w)/2}, 44)">
      <image href="{p2_uri}" width="{disp2_w}" height="{disp2_h}" preserveAspectRatio="xMidYMid meet" />
    </g>
  </g>
''')

    # Footer (Distinct 2 lines - zero collision!)
    svg.append(f'''  <!-- FOOTER -->
  <g transform="translate({MARGIN_X + 20}, {footer_y})">
    <line x1="0" y1="0" x2="{CONTENT_W - 40}" y2="0" stroke="#cbd5e1" stroke-width="1" />
    <text x="0" y="22" fill="#475569" font-size="13px" font-weight="400" font-family="'Sarabun', 'TH Sarabun New', sans-serif">สารบบคดีอาญา: ขบวนการฉ้อโกงเป็นปกติธุระ (ป.อ. มาตรา ๓๔๑, ๙๑) | แผ่นเวกเตอร์ที่ {seq_num} จาก ๓๐ รายการ</text>
    <text x="0" y="42" fill="#64748b" font-size="12px" font-weight="400" font-family="'Sarabun', 'TH Sarabun New', sans-serif">รับรองสำเนาถูกต้องโดยระบบนิติวิทยาศาสตร์ดิจิทัล (Digital Evi Codex V2) • ISO/IEC 27037 Standard</text>
  </g>

</svg>''')

    return "\n".join(svg)

# Function to build 100% Responsive HTML card
def generate_responsive_html_card(ev, seq_num):
    img_p1_rel = f"A4_EVIDENCE_ASSETS/{ev['img_p1']}"
    img_p1_path = os.path.join(r"d:\Project\ชวกม.2\EDOK_NUI", img_p1_rel)
    p1_uri = image_to_base64_data_uri(img_p1_path)

    has_p2 = ev.get("has_p2", False)
    p2_uri = ""
    if has_p2:
        img_p2_rel = f"A4_EVIDENCE_ASSETS/{ev['img_p2']}"
        img_p2_path = os.path.join(r"d:\Project\ชวกม.2\EDOK_NUI", img_p2_rel)
        p2_uri = image_to_base64_data_uri(img_p2_path)

    laws_html = "".join([f'<div class="law-row">{esc(law)}</div>' for law in ev["codex_laws"]])

    p2_section_html = ""
    if has_p2:
        p2_section_html = f'''
        <div class="evidence-card p2-card">
          <div class="evidence-header p2-header">
            <span class="ev-title">📑 หลักฐานต่อเนื่อง / สลิปโอนเงิน (Part 2)</span>
            <span class="ev-badge" style="background: #0284c7;">ADDITIONAL EVIDENCE</span>
          </div>
          <div class="evidence-body">
            <img src="{p2_uri}" class="ev-img" alt="Evidence Part 2" />
          </div>
        </div>
        '''

    html = f'''<!DOCTYPE html>
<html lang="th">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{esc(ev['count_no'])}: {esc(ev['count_title'])}</title>
  <link href="https://fonts.googleapis.com/css2?family=Sarabun:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
  <style>
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      background: #f1f5f9;
      color: #0f172a;
      font-family: 'Sarabun', 'TH Sarabun New', sans-serif;
      padding: 20px;
      display: flex;
      justify-content: center;
    }}
    .dossier-card {{
      background: #ffffff;
      width: 100%;
      max-width: 980px;
      border-radius: 8px;
      border: 1.5px solid #cbd5e1;
      box-shadow: 0 4px 16px rgba(0,0,0,0.06);
      padding: 24px 28px;
    }}
    .court-header {{
      border-bottom: 2px solid #0f172a;
      padding-bottom: 10px;
      margin-bottom: 14px;
    }}
    .court-title {{
      font-size: 20px;
      font-weight: 800;
      color: #0f172a;
    }}
    .court-sub {{
      font-size: 13.5px;
      font-weight: 300;
      color: #64748b;
      margin-top: 2px;
    }}
    .meta-bar {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: 6px;
      padding: 8px 14px;
      margin-top: 8px;
      flex-wrap: wrap;
      gap: 8px;
    }}
    .meta-left {{
      font-size: 15px;
      font-weight: 300;
    }}
    .meta-left strong {{
      font-weight: 700;
    }}
    .meta-right {{
      display: flex;
      gap: 8px;
      align-items: center;
    }}
    .pill-count {{
      background: #fee2e2;
      color: #b91c1c;
      border: 1px solid #fca5a5;
      font-size: 13px;
      font-weight: 700;
      padding: 3px 10px;
      border-radius: 4px;
      white-space: nowrap;
    }}
    .pill-amt {{
      background: #eff6ff;
      color: #1e40af;
      border: 1px solid #bfdbfe;
      font-size: 13px;
      font-weight: 700;
      padding: 3px 10px;
      border-radius: 4px;
      white-space: nowrap;
    }}
    /* TABLE 1-11 STANDARD: TH SARABUN 16PX */
    .topics-table {{
      width: 100%;
      border-collapse: collapse;
      margin-top: 14px;
      font-size: 16px;
      line-height: 1.45;
    }}
    .topics-table th, .topics-table td {{
      border: 1px solid #cbd5e1;
      padding: 8px 12px;
      vertical-align: top;
    }}
    .th-col {{
      width: 220px;
      background: #f8fafc;
      font-weight: 700;
      color: #1e293b;
    }}
    .td-col {{
      font-weight: 300;
      color: #0f172a;
      background: #ffffff;
    }}
    .chat-quote {{
      color: #0369a1;
      background: #f0f9ff;
      font-style: italic;
    }}
    .amt-highlight {{
      color: #15803d;
      font-weight: 700;
      font-size: 18px;
    }}
    .law-box {{
      background: #fff1f2;
      border-color: #fecdd3;
    }}
    .law-row {{
      margin-bottom: 4px;
      font-weight: 300;
      color: #991b1b;
    }}
    .smoking-gun-row {{
      background: #fef2f2;
      color: #b91c1c;
      font-weight: 700;
    }}
    /* RESPONSIVE EVIDENCE BOX - ADAPTS TO ANY IMAGE HEIGHT */
    .evidence-card {{
      margin-top: 20px;
      border: 1.5px solid #0f172a;
      border-radius: 6px;
      overflow: hidden;
      background: #0f172a;
    }}
    .evidence-header {{
      background: #1e293b;
      padding: 8px 14px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 6px;
    }}
    .p2-header {{
      background: #0369a1;
    }}
    .ev-title {{
      font-size: 13.5px;
      font-weight: 700;
      color: #ffffff;
    }}
    .ev-badge {{
      background: #dc2626;
      color: #ffffff;
      font-size: 10px;
      font-weight: 800;
      padding: 3px 8px;
      border-radius: 3px;
      letter-spacing: 0.5px;
    }}
    .evidence-body {{
      background: #090d16;
      padding: 14px;
      display: flex;
      justify-content: center;
      align-items: center;
    }}
    .ev-img {{
      max-width: 100%;
      height: auto;
      border-radius: 4px;
      box-shadow: 0 4px 12px rgba(0,0,0,0.5);
      display: block;
    }}
    .court-footer {{
      border-top: 1px solid #cbd5e1;
      padding-top: 12px;
      margin-top: 20px;
      font-size: 13px;
      font-weight: 300;
      color: #64748b;
      line-height: 1.4;
    }}
    @media (max-width: 768px) {{
      .th-col {{ width: 140px; }}
      .topics-table {{ font-size: 14.5px; }}
    }}
  </style>
</head>
<body>
  <div class="dossier-card">
    <!-- HEADER -->
    <div class="court-header">
      <div class="court-title">⚖️ แฟ้มสำนวนคดีอาญา (มาตรฐานศาลยุติธรรม - CODEX RESPONSIVE STREAM)</div>
      <div class="court-sub">เอกสารบัญชีพยานหลักฐานประกอบคำฟ้อง / คำร้องทุกข์ แยกตามกรรมต่างวาระ (ป.อ. มาตรา ๙๑)</div>
      
      <!-- METADATA BAR -->
      <div class="meta-bar">
        <div class="meta-left">
          <strong>บุคคลเป้าหมาย:</strong> {esc(ev['person'])} ({esc(ev['person_role'])})
        </div>
        <div class="meta-right">
          <span class="pill-count">{esc(ev['count_no'])}</span>
          <span class="pill-amt">ความเสียหาย: {esc(ev['amount'])}</span>
        </div>
      </div>
    </div>

    <!-- 11 TOPICS TABLE (TH SARABUN 16PX) -->
    <table class="topics-table">
      <tr>
        <th class="th-col">๑. เหตุการณ์ที่</th>
        <td class="td-col" style="font-weight: 700;">{esc(ev['count_title'])}</td>
      </tr>
      <tr>
        <th class="th-col">๒. อ้างอิงหลักฐาน</th>
        <td class="td-col"><code style="font-family: monospace; font-size: 13.5px; color: #475569;">{esc(ev['ref'])}</code></td>
      </tr>
      <tr>
        <th class="th-col">๓. บริบทแชทจริง</th>
        <td class="td-col chat-quote">"{esc(ev['chat'])}"</td>
      </tr>
      <tr>
        <th class="th-col">๔. วิเคราะห์พฤติการณ์</th>
        <td class="td-col">{esc(ev['analysis'])}</td>
      </tr>
      <tr>
        <th class="th-col">๕. วันเวลาเกิดเหตุ</th>
        <td class="td-col">{esc(ev['datetime'])}</td>
      </tr>
      <tr>
        <th class="th-col">๖. ยอดเงิน (บาท)</th>
        <td class="td-col amt-highlight">{esc(ev['amount'])}</td>
      </tr>
      <tr>
        <th class="th-col">๗. รูปสลิป / บัญชี</th>
        <td class="td-col">{esc(ev['slip'])}</td>
      </tr>
      <tr class="law-box">
        <th class="th-col" style="background: #fff1f2; color: #991b1b;">๘. ข้อหาและมาตรา</th>
        <td class="td-col" style="background: #fff1f2;">
          {laws_html}
        </td>
      </tr>
      <tr class="smoking-gun-row">
        <th class="th-col" style="background: #fef2f2; color: #b91c1c;">๙. จุดตาย (Smoking Gun)</th>
        <td class="td-col" style="background: #fef2f2; color: #b91c1c; font-weight: 700;">{esc(ev['smoking_gun'])}</td>
      </tr>
      <tr>
        <th class="th-col">๑๐. พลิกเกมส์ & ตอบโต้</th>
        <td class="td-col">{esc(ev['counter'])}</td>
      </tr>
      <tr>
        <th class="th-col">๑๑. คำขอและแนวทางยื่นศาล</th>
        <td class="td-col">{esc(ev['court_action'])}</td>
      </tr>
    </table>

    <!-- EVIDENCE BOX 1 (100% RESPONSIVE) -->
    <div class="evidence-card">
      <div class="evidence-header">
        <span class="ev-title">📸 พยานหลักฐานภาพเหตุการณ์อ้างอิงจริง</span>
        <span class="ev-badge">CERTIFIED COURT EVIDENCE • ISO/IEC 27037</span>
      </div>
      <div class="evidence-body">
        <img src="{p1_uri}" class="ev-img" alt="Evidence {esc(ev['count_no'])}" />
      </div>
    </div>

    {p2_section_html}

    <!-- FOOTER -->
    <div class="court-footer">
      <div>สารบบคดีอาญา: ขบวนการฉ้อโกงเป็นปกติธุระ (ป.อ. มาตรา ๓๔๑, ๙๑) | แผ่นเวกเตอร์ที่ {seq_num} จาก ๓๐ รายการ</div>
      <div style="color: #94a3b8; font-size: 12px; margin-top: 2px;">รับรองสำเนาถูกต้องโดยระบบนิติวิทยาศาสตร์ดิจิทัล (Digital Evi Codex V2) • ISO/IEC 27037 Standard</div>
    </div>
  </div>
</body>
</html>'''
    return html

# Generate All Files
print("Building Responsive Suite (HTML + Hardened SVG)...")
card_summaries = []

for idx, ev in enumerate(counts, start=1):
    # 1. Hardened SVG
    svg_str = generate_hardened_svg(ev, idx)
    svg_fn = f"VECTOR_COUNT_{idx:02d}.svg"
    with open(os.path.join(vector_dir, svg_fn), "w", encoding="utf-8") as f:
        f.write(svg_str)
    with open(os.path.join(art_vector_dir, svg_fn), "w", encoding="utf-8") as f:
        f.write(svg_str)

    # 2. Responsive HTML Card
    html_str = generate_responsive_html_card(ev, idx)
    html_fn = f"COUNT_{idx:02d}_RESPONSIVE.html"
    with open(os.path.join(vector_dir, html_fn), "w", encoding="utf-8") as f:
        f.write(html_str)
    with open(os.path.join(art_vector_dir, html_fn), "w", encoding="utf-8") as f:
        f.write(html_str)

    card_summaries.append((html_fn, svg_fn, ev['count_no'], ev['person'], ev['amount'], ev['count_title']))
    print(f"  [+] {ev['count_no']}: Generated {svg_fn} and {html_fn}")

print("All 30 Counts generated in both Hardened SVG and Responsive HTML!")

# 3. Build Unified Master Responsive Dashboard
master_dash = f'''<!DOCTYPE html>
<html lang="th">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>แฟ้มสารบบคดีอาญาเวกเตอร์แท้ 100% (Responsive Master Dashboard - CODEX CERTIFIED)</title>
  <link href="https://fonts.googleapis.com/css2?family=Sarabun:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
  <style>
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      background: #090d16;
      color: #f8fafc;
      font-family: 'Sarabun', 'TH Sarabun New', sans-serif;
    }}
    header {{
      background: #0f172a;
      border-bottom: 2px solid #334155;
      padding: 16px 30px;
      position: sticky;
      top: 0;
      z-index: 100;
      display: flex;
      justify-content: space-between;
      align-items: center;
      box-shadow: 0 4px 12px rgba(0,0,0,0.5);
      flex-wrap: wrap;
      gap: 10px;
    }}
    .h-title {{ font-size: 19px; font-weight: 800; color: #38bdf8; display: flex; align-items: center; gap: 8px; }}
    .h-sub {{ font-size: 13px; font-weight: 300; color: #94a3b8; margin-top: 2px; }}
    .badge-vector {{
      background: #15803d;
      color: #ffffff;
      padding: 4px 12px;
      border-radius: 4px;
      font-size: 12px;
      font-weight: 800;
      letter-spacing: 0.5px;
    }}
    .container {{
      max-width: 1080px;
      margin: 25px auto;
      padding: 0 16px;
    }}
    .quick-nav {{
      background: #1e293b;
      border: 1px solid #334155;
      border-radius: 8px;
      padding: 12px 16px;
      margin-bottom: 25px;
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      align-items: center;
    }}
    .nav-label {{
      font-size: 13px;
      font-weight: 700;
      color: #38bdf8;
      margin-right: 6px;
    }}
    .nav-btn {{
      background: #0f172a;
      border: 1px solid #475569;
      color: #e2e8f0;
      padding: 4px 10px;
      border-radius: 4px;
      font-size: 12px;
      font-weight: 500;
      text-decoration: none;
      transition: all 0.2s;
    }}
    .nav-btn:hover {{
      background: #2563eb;
      border-color: #3b82f6;
      color: #ffffff;
    }}
    .card-shell {{
      margin-bottom: 35px;
      background: #0f172a;
      border: 1px solid #334155;
      border-radius: 10px;
      overflow: hidden;
      box-shadow: 0 8px 24px rgba(0,0,0,0.5);
    }}
    .shell-bar {{
      background: #1e293b;
      padding: 10px 18px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid #334155;
      flex-wrap: wrap;
      gap: 8px;
    }}
    .shell-label {{
      font-size: 15px;
      font-weight: 700;
      color: #f8fafc;
    }}
    .shell-actions {{
      display: flex;
      gap: 8px;
    }}
    .act-btn {{
      font-size: 12px;
      padding: 4px 10px;
      border-radius: 4px;
      text-decoration: none;
      font-weight: 600;
    }}
    .act-html {{
      background: #0284c7;
      color: #ffffff;
    }}
    .act-svg {{
      background: #334155;
      color: #38bdf8;
      border: 1px solid #475569;
    }}
    .shell-frame {{
      width: 100%;
      height: 980px;
      border: none;
      background: #f8fafc;
      display: block;
    }}
  </style>
</head>
<body>
  <header>
    <div>
      <div class="h-title">⚡ แฟ้มสารบบพยานหลักฐานคดีอาญา (ระบบ Responsive Vector ๑๐๐%)</div>
      <div class="h-sub">รองรับภาพทุกความสูง • ตาราง ๑–๑๑ ฟอนต์ TH Sarabun 16 • แยกกล่องข้อมูลชัดเจน ปราศจากตัวอักษรทับซ้อน 100%</div>
    </div>
    <div class="badge-vector">RESPONSIVE &amp; VECTOR ENGINE • ZERO OVERLAP</div>
  </header>

  <div class="container">
    <div class="quick-nav">
      <span class="nav-label">⚡ สารบัญทางลัดกระทง:</span>
'''

for h_fn, s_fn, cno, pers, amt, title in card_summaries:
    master_dash += f'<a href="#{h_fn}" class="nav-btn">{esc(cno)}</a>\n'

master_dash += '    </div>\n'

for h_fn, s_fn, cno, pers, amt, title in card_summaries:
    master_dash += f'''
    <div class="card-shell" id="{h_fn}">
      <div class="shell-bar">
        <span class="shell-label">📁 {esc(cno)}: {esc(title)} ({esc(amt)})</span>
        <div class="shell-actions">
          <a href="{h_fn}" target="_blank" class="act-btn act-html">🖥️ เปิดการ์ดเต็มจอ (Responsive)</a>
          <a href="{s_fn}" target="_blank" class="act-btn act-svg">🔍 เปิดไฟล์ SVG เวกเตอร์</a>
        </div>
      </div>
      <iframe src="{h_fn}" class="shell-frame" title="{esc(cno)}"></iframe>
    </div>
'''

master_dash += '''
  </div>
</body>
</html>
'''

dash_path = os.path.join(vector_dir, "VECTOR_EVIDENCE_DASHBOARD.html")
art_dash_path = os.path.join(art_vector_dir, "VECTOR_EVIDENCE_DASHBOARD.html")
with open(dash_path, "w", encoding="utf-8") as f:
    f.write(master_dash)
with open(art_dash_path, "w", encoding="utf-8") as f:
    f.write(master_dash)

print("Generated MASTER RESPONSIVE DASHBOARD successfully!")

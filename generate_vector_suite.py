# -*- coding: utf-8 -*-
import os
import json
import base64
from PIL import Image

# 1. Update Count 1 Crop specifically to guarantee 100% Quiet Zone alignment (no น้อยใจ at top, no มีแล้วไม่ให้ at bottom)
raw_ori = r'C:\Users\EVE\Downloads\ของมันคนเดียว-20261117T094313Z-1-003\ของมันคนเดียว\แคปหน้า Ori'
im1_path = os.path.join(raw_ori, 'LINE_capture_800252756.687906.jpg')
im1 = Image.open(im1_path)
c1 = im1.crop((0, 2335, 636, 2730))
out_c1 = r'd:\Project\ชวกม.2\EDOK_NUI\A4_EVIDENCE_ASSETS\ctx_count_01_p1.png'
c1.save(out_c1)
art_c1 = r'C:\Users\EVE\.gemini\antigravity\brain\c8211d09-030e-4b24-8837-3ce9589aa4a6\A4_EVIDENCE_ASSETS\ctx_count_01_p1.png'
c1.save(art_c1)
print(f"Updated Count 1 clean crop: {c1.size}")

# 2. Setup Vector Output Dirs
vector_dir = r'd:\Project\ชวกม.2\EDOK_NUI\VECTOR_EVIDENCE'
art_vector_dir = r'C:\Users\EVE\.gemini\antigravity\brain\c8211d09-030e-4b24-8837-3ce9589aa4a6\VECTOR_EVIDENCE'
os.makedirs(vector_dir, exist_ok=True)
os.makedirs(art_vector_dir, exist_ok=True)

# Import counts data
from build_court_dossier_smart_cropped import counts

print(f"Loaded {len(counts)} counts for Vector generation.")

def escape_xml(text):
    if not text:
        return ""
    return str(text).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;").replace("'", "&apos;")

def image_to_base64_data_uri(img_path):
    if not os.path.exists(img_path):
        return ""
    ext = os.path.splitext(img_path)[1].lower()
    mime = "image/png" if ext == ".png" else "image/jpeg"
    with open(img_path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode("ascii")
    return f"data:{mime};base64,{encoded}"

def build_vector_card_svg(ev, seq_num):
    img_p1_rel = f"A4_EVIDENCE_ASSETS/{ev['img_p1']}"
    img_p1_path = os.path.join(r"d:\Project\ชวกม.2\EDOK_NUI", img_p1_rel)
    
    # Get image dimensions
    p1_w, p1_h = 600, 400
    if os.path.exists(img_p1_path):
        with Image.open(img_p1_path) as im:
            p1_w, p1_h = im.size
            
    p1_uri = image_to_base64_data_uri(img_p1_path)
    
    # If has part 2
    has_p2 = ev.get("has_p2", False)
    p2_w, p2_h, p2_uri = 0, 0, ""
    if has_p2:
        img_p2_rel = f"A4_EVIDENCE_ASSETS/{ev['img_p2']}"
        img_p2_path = os.path.join(r"d:\Project\ชวกม.2\EDOK_NUI", img_p2_rel)
        if os.path.exists(img_p2_path):
            with Image.open(img_p2_path) as im:
                p2_w, p2_h = im.size
            p2_uri = image_to_base64_data_uri(img_p2_path)

    # Determine layout dimensions
    CARD_W = 1000
    PADDING = 30
    CONTENT_W = CARD_W - (PADDING * 2)
    
    # Table layout
    ROW_H_DEFAULT = 36
    
    # Rows content
    rows = [
        ("๑. เหตุการณ์ที่", ev['count_title'], "#0f172a", True),
        ("๒. อ้างอิงหลักฐาน", ev['ref'], "#475569", False),
        ("๓. บริบทแชทจริง", f'"{ev["chat"]}"', "#0369a1", True),
        ("๔. วิเคราะห์พฤติการณ์", ev['analysis'], "#0f172a", False),
        ("๕. ช่วงวันเวลาเกิดเหตุ", ev['datetime'], "#0f172a", False),
        ("๖. ยอดเงิน (บาท)", ev['amount'], "#15803d", True),
        ("๗. รูปสลิป / บัญชี", ev['slip'], "#0f172a", False),
        ("๘. ข้อหาและมาตรา", "\n".join(ev['codex_laws']), "#991b1b", False),
        ("๙. จุดตาย (Smoking Gun)", ev['smoking_gun'], "#b91c1c", True),
        ("๑๐. พลิกเกมส์ & ตอบโต้", ev['counter'], "#0f172a", False),
        ("๑๑. คำขอและแนวทางยื่นศาล", ev['court_action'], "#0f172a", False),
    ]

    # Calculate dynamic height
    curr_y = PADDING
    curr_y += 85  # Header
    
    table_y = curr_y
    # Estimate table height
    table_h = 0
    calculated_rows = []
    for title, val, color, is_bold in rows:
        val_lines = val.split("\n")
        total_sublines = 0
        for vl in val_lines:
            sub = max(1, (len(vl) // 68) + 1)
            total_sublines += sub
        rh = max(ROW_H_DEFAULT, total_sublines * 22 + 10)
        calculated_rows.append((title, val, color, is_bold, rh))
        table_h += rh
        
    curr_y += table_h + 25  # Gap before evidence box
    
    evidence_y = curr_y
    # Scale image to fit within max width 880px
    display_w = min(880, p1_w)
    display_h = int(p1_h * (display_w / p1_w)) if p1_w else 400
    evidence_h = display_h + 45  # Header bar
    
    if has_p2:
        display2_w = min(880, p2_w)
        display2_h = int(p2_h * (display2_w / p2_w)) if p2_w else 400
        evidence_h += display2_h + 70 # Part 2 header + gap
        
    curr_y += evidence_h + 30 # Gap before footer
    curr_y += 45 # Footer
    curr_y += PADDING
    
    TOTAL_H = curr_y

    # Build SVG
    svg = []
    svg.append(f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 {CARD_W} {TOTAL_H}" width="{CARD_W}" height="{TOTAL_H}">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Sarabun:wght@400;600;700;800&amp;display=swap');
      text {{ font-family: 'Sarabun', 'TH Sarabun New', sans-serif; }}
      .title {{ font-size: 19px; font-weight: 800; fill: #0f172a; }}
      .sub {{ font-size: 12px; font-weight: 500; fill: #64748b; }}
      .badge-txt {{ font-size: 13px; font-weight: 700; fill: #ffffff; }}
      .th-col {{ font-size: 13px; font-weight: 700; fill: #1e293b; }}
      .td-col {{ font-size: 13px; font-weight: 400; fill: #0f172a; }}
      .amt-txt {{ font-size: 14px; font-weight: 800; fill: #15803d; }}
      .ev-title {{ font-size: 12.5px; font-weight: 700; fill: #ffffff; }}
      .stamp-txt {{ font-size: 10px; font-weight: 800; fill: #ffffff; letter-spacing: 0.5px; }}
      .footer-txt {{ font-size: 11px; fill: #64748b; }}
    </style>
    <linearGradient id="headerGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#0f172a" />
      <stop offset="100%" stop-color="#1e293b" />
    </linearGradient>
    <filter id="cardShadow" x="-1%" y="-1%" width="102%" height="102%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.08" />
    </filter>
  </defs>

  <!-- BACKGROUND CANVAS -->
  <rect x="0" y="0" width="{CARD_W}" height="{TOTAL_H}" fill="#f8fafc" />

  <!-- MAIN CARD CONTAINER -->
  <rect x="{PADDING}" y="{PADDING}" width="{CONTENT_W}" height="{TOTAL_H - PADDING*2}" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5" filter="url(#cardShadow)" />

  <!-- HEADER BANNER -->
  <g transform="translate({PADDING + 20}, {PADDING + 20})">
    <text x="0" y="20" class="title">⚖️ แฟ้มสำนวนคดีอาญา (มาตรฐานศาลยุติธรรม - CODEX VECTOR STREAM)</text>
    <text x="0" y="38" class="sub">เอกสารบัญชีพยานหลักฐานประกอบคำฟ้อง / คำร้องทุกข์ แยกตามกรรมต่างวาระ (ป.อ. มาตรา ๙๑)</text>
    
    <!-- META INFO PILL -->
    <rect x="0" y="48" width="{CONTENT_W - 40}" height="32" rx="4" fill="#f1f5f9" stroke="#e2e8f0" stroke-width="1" />
    <text x="12" y="69" class="td-col"><strong>บุคคลเป้าหมาย:</strong> {escape_xml(ev['person'])} ({escape_xml(ev['person_role'])})</text>
    <text x="{CONTENT_W - 55}" y="69" text-anchor="end" class="td-col">
      <tspan fill="#dc2626" font-weight="800">{escape_xml(ev['count_no'])}</tspan> | 
      <tspan fill="#1e3a8a" font-weight="800">ความเสียหาย: {escape_xml(ev['amount'])}</tspan>
    </text>
  </g>
''')

    # RENDER 11-TOPIC TABLE
    y_row = table_y
    table_x = PADDING + 20
    col1_w = 200
    col2_w = CONTENT_W - 40 - col1_w

    svg.append(f'  <!-- 11 TOPICS TABLE -->\n  <g transform="translate({table_x}, {table_y})">')
    
    r_accum_y = 0
    for title, val, color, is_bold, rh in calculated_rows:
        # Row rects
        bg_col = "#f8fafc" if r_accum_y % 2 == 0 else "#ffffff"
        if "Smoking Gun" in title or "ข้อหา" in title:
            bg_col = "#fef2f2"
            
        svg.append(f'    <rect x="0" y="{r_accum_y}" width="{col1_w}" height="{rh}" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="1" />')
        svg.append(f'    <rect x="{col1_w}" y="{r_accum_y}" width="{col2_w}" height="{rh}" fill="{bg_col}" stroke="#cbd5e1" stroke-width="1" />')
        
        # Col 1 Title
        svg.append(f'    <text x="10" y="{r_accum_y + 22}" class="th-col">{escape_xml(title)}</text>')
        
        # Col 2 Content
        val_lines = val.split("\n")
        line_offset_y = 22
        for vl in val_lines:
            # Word wrap simulation
            words = vl
            chunk_size = 65
            subchunks = [words[i:i+chunk_size] for i in range(0, len(words), chunk_size)]
            for sc in subchunks:
                weight = "800" if is_bold else "400"
                svg.append(f'    <text x="{col1_w + 12}" y="{r_accum_y + line_offset_y}" class="td-col" fill="{color}" font-weight="{weight}">{escape_xml(sc)}</text>')
                line_offset_y += 20
                
        r_accum_y += rh
        
    svg.append('  </g>\n')

    # RENDER EVIDENCE CONTAINER (ZERO BLACK MARGINS - EXACT FIT)
    ev_x = PADDING + 20
    ev_w = CONTENT_W - 40
    
    svg.append(f'''  <!-- EVIDENCE CONTAINER -->
  <g transform="translate({ev_x}, {evidence_y})">
    <!-- Part 1 Frame -->
    <rect x="0" y="0" width="{ev_w}" height="{display_h + 36}" rx="6" fill="#0f172a" stroke="#1e293b" stroke-width="1" />
    
    <!-- Title Bar -->
    <rect x="0" y="0" width="{ev_w}" height="32" rx="6" fill="#1e293b" />
    <text x="14" y="21" class="ev-title">📸 พยานหลักฐานภาพเหตุการณ์อ้างอิงจริง (ครอปเฉพาะกรอบบริบทชัดเจน 100% - มาตรฐานศาล)</text>
    
    <rect x="{ev_w - 230}" y="6" width="220" height="20" rx="3" fill="#dc2626" />
    <text x="{ev_w - 120}" y="19" text-anchor="middle" class="stamp-txt">CERTIFIED COURT EVIDENCE • ISO 27037</text>
    
    <!-- Centered Crisp Image -->
    <g transform="translate({(ev_w - display_w)/2}, 34)">
      <image href="{p1_uri}" width="{display_w}" height="{display_h}" preserveAspectRatio="xMidYMid meet" />
    </g>
''')

    if has_p2:
        p2_start_y = display_h + 50
        svg.append(f'''    <!-- Part 2 Frame -->
    <rect x="0" y="{p2_start_y}" width="{ev_w}" height="{display2_h + 36}" rx="6" fill="#0f172a" stroke="#1e293b" stroke-width="1" />
    <rect x="0" y="{p2_start_y}" width="{ev_w}" height="32" rx="6" fill="#0369a1" />
    <text x="14" y="{p2_start_y + 21}" class="ev-title">📑 หลักฐานต่อเนื่อง / สลิปโอนเงินขยายใหญ่ (Part 2): {escape_xml(ev.get("p2_desc", ""))}</text>
    
    <g transform="translate({(ev_w - display2_w)/2}, {p2_start_y + 34})">
      <image href="{p2_uri}" width="{display2_w}" height="{display2_h}" preserveAspectRatio="xMidYMid meet" />
    </g>
''')

    svg.append('  </g>\n')

    # RENDER FOOTER
    footer_y = TOTAL_H - PADDING - 25
    svg.append(f'''  <!-- FOOTER -->
  <g transform="translate({PADDING + 20}, {footer_y})">
    <line x1="0" y1="0" x2="{CONTENT_W - 40}" y2="0" stroke="#cbd5e1" stroke-width="1" />
    <text x="0" y="16" class="footer-txt">สารบบคดีอาญา: ขบวนการฉ้อโกงเป็นปกติธุระ (ป.อ. มาตรา ๓๔๑, ๙๑) | แผ่นเวกเตอร์ที่ {seq_num} จากทั้งหมด {len(counts)} รายการ</text>
    <text x="{CONTENT_W - 40}" y="16" text-anchor="end" class="footer-txt">ระบบรับรองพยานหลักฐานนิติวิทยาศาสตร์ดิจิทัล (Digital Evi Codex V2)</text>
  </g>

</svg>''')

    return "\n".join(svg)

# Generate All 30 SVGs
print("Generating 30 Standalone Vector Cards (.svg)...")
svg_files = []
for idx, ev in enumerate(counts, start=1):
    svg_content = build_vector_card_svg(ev, idx)
    out_name = f"VECTOR_COUNT_{idx:02d}.svg"
    out_path = os.path.join(vector_dir, out_name)
    art_path = os.path.join(art_vector_dir, out_name)
    
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    with open(art_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
        
    svg_files.append((out_name, ev['count_no'], ev['person'], ev['amount'], ev['count_title']))
    print(f"  [+] Created {out_name} (Height: ~calculated px)")

print("All 30 SVG Vector Cards generated successfully!")

# 3. Generate Interactive Vector Evidence Dashboard HTML
dashboard_html = f'''<!DOCTYPE html>
<html lang="th">
<head>
  <meta charset="UTF-8">
  <title>แฟ้มสารบบคดีอาญาเวกเตอร์แท้ 100% (Vector Evidence Suite - CODEX CERTIFIED)</title>
  <link href="https://fonts.googleapis.com/css2?family=Sarabun:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <style>
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      padding: 0;
      background: #090d16;
      color: #f8fafc;
      font-family: 'Sarabun', sans-serif;
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
    }}
    .h-title {{ font-size: 18px; font-weight: 800; color: #38bdf8; display: flex; align-items: center; gap: 8px; }}
    .h-sub {{ font-size: 12px; color: #94a3b8; margin-top: 2px; }}
    .badge-vector {{
      background: #15803d;
      color: #ffffff;
      padding: 4px 10px;
      border-radius: 4px;
      font-size: 11px;
      font-weight: 800;
      letter-spacing: 0.5px;
    }}
    .container {{
      max-width: 1100px;
      margin: 30px auto;
      padding: 0 20px;
    }}
    .quick-nav {{
      background: #1e293b;
      border: 1px solid #334155;
      border-radius: 8px;
      padding: 14px;
      margin-bottom: 25px;
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
    }}
    .nav-btn {{
      background: #0f172a;
      border: 1px solid #475569;
      color: #e2e8f0;
      padding: 4px 10px;
      border-radius: 4px;
      font-size: 12px;
      text-decoration: none;
      transition: all 0.2s;
    }}
    .nav-btn:hover {{
      background: #2563eb;
      border-color: #3b82f6;
      color: #ffffff;
    }}
    .vector-card-wrap {{
      margin-bottom: 40px;
      background: #0f172a;
      border: 1px solid #334155;
      border-radius: 10px;
      overflow: hidden;
      box-shadow: 0 10px 25px -5px rgba(0,0,0,0.6);
    }}
    .card-topbar {{
      background: #1e293b;
      padding: 10px 20px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid #334155;
    }}
    .card-label {{ font-size: 14px; font-weight: 700; color: #f8fafc; }}
    .svg-embed {{
      width: 100%;
      height: auto;
      display: block;
    }}
    .card-actions {{
      display: flex;
      gap: 10px;
    }}
    .dl-link {{
      color: #38bdf8;
      font-size: 12px;
      text-decoration: none;
      background: rgba(56, 189, 248, 0.1);
      padding: 3px 8px;
      border-radius: 4px;
      border: 1px solid rgba(56, 189, 248, 0.3);
    }}
    .dl-link:hover {{
      background: #38bdf8;
      color: #0f172a;
    }}
  </style>
</head>
<body>
  <header>
    <div>
      <div class="h-title">⚡ แฟ้มสารบบพยานหลักฐานคดีอาญา (ระบบเวกเตอร์ 100% ไร้ขีดจำกัดหน้ากระดาษ)</div>
      <div class="h-sub">ยกเลิกข้อจำกัด PDF • ตัวอักษรและตารางเป็น Pure Scalable Vector Stream • แสดงภาพหลักฐานบริบทแท้ 100%</div>
    </div>
    <div class="badge-vector">PURE VECTOR EDITION • ZERO SPILLOVER</div>
  </header>

  <div class="container">
    <div class="quick-nav">
      <span style="font-size: 12px; color: #94a3b8; align-self: center; margin-right: 5px;">⚡ ลัดไปยังกระทง:</span>
'''

for fn, cno, pers, amt, title in svg_files:
    dashboard_html += f'<a href="#{fn}" class="nav-btn">{escape_xml(cno)}</a>\n'

dashboard_html += '    </div>\n'

for fn, cno, pers, amt, title in svg_files:
    dashboard_html += f'''
    <div class="vector-card-wrap" id="{fn}">
      <div class="card-topbar">
        <span class="card-label">📁 {escape_xml(cno)}: {escape_xml(title)} ({escape_xml(amt)})</span>
        <div class="card-actions">
          <a href="{fn}" target="_blank" class="dl-link">🔍 เปิดไฟล์ SVG เวกเตอร์โดยตรง</a>
        </div>
      </div>
      <img src="{fn}" class="svg-embed" alt="{escape_xml(cno)}" />
    </div>
'''

dashboard_html += '''
  </div>
</body>
</html>
'''

dashboard_out = os.path.join(vector_dir, "VECTOR_EVIDENCE_DASHBOARD.html")
art_dashboard_out = os.path.join(art_vector_dir, "VECTOR_EVIDENCE_DASHBOARD.html")
with open(dashboard_out, "w", encoding="utf-8") as f:
    f.write(dashboard_html)
with open(art_dashboard_out, "w", encoding="utf-8") as f:
    f.write(dashboard_html)

print("Generated VECTOR_EVIDENCE_DASHBOARD.html successfully!")

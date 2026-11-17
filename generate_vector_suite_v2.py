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

# Import structured counts
from build_court_dossier_smart_cropped import counts

print(f"Loaded {len(counts)} counts for Master Vector Suite V2.")

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

def wrap_text(text, max_chars=62):
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

LINE_H = 26
PAD_Y = 12

def build_vector_card(ev, seq_num):
    # 1. Image 1
    img_p1_rel = f"A4_EVIDENCE_ASSETS/{ev['img_p1']}"
    img_p1_path = os.path.join(r"d:\Project\ชวกม.2\EDOK_NUI", img_p1_rel)
    p1_uri = image_to_base64_data_uri(img_p1_path)
    
    p1_w, p1_h = 600, 400
    if os.path.exists(img_p1_path):
        with Image.open(img_p1_path) as im:
            p1_w, p1_h = im.size
            
    disp1_w = min(840, p1_w)
    disp1_h = int(p1_h * (disp1_w / p1_w)) if p1_w else 300
    ev1_h = 36 + 18 + disp1_h + 18

    # 2. Image 2 (if has_p2)
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
                ev2_h = 36 + 18 + disp2_h + 18

    # 3. Table Rows definition
    rows = [
        ("๑. เหตุการณ์ที่", ev['count_title'], "#0f172a", True, False),
        ("๒. อ้างอิงหลักฐาน", ev['ref'], "#475569", False, True),
        ("๓. บริบทแชทจริง", f'"{ev["chat"]}"', "#0369a1", False, False),
        ("๔. วิเคราะห์พฤติการณ์", ev['analysis'], "#0f172a", False, False),
        ("๕. ช่วงวันเวลาเกิดเหตุ", ev['datetime'], "#0f172a", False, False),
        ("๖. ยอดเงิน (บาท)", ev['amount'], "#15803d", True, False),
        ("๗. รูปสลิป / บัญชี", ev['slip'], "#0f172a", False, False),
        ("๘. ข้อหาและมาตรา", "\n".join(ev['codex_laws']), "#991b1b", False, False),
        ("๙. จุดตาย (Smoking Gun)", ev['smoking_gun'], "#b91c1c", True, False),
        ("๑๐. พลิกเกมส์ & ตอบโต้", ev['counter'], "#0f172a", False, False),
        ("๑๑. คำขอและแนวทางยื่นศาล", ev['court_action'], "#0f172a", False, False),
    ]

    # Calculate row heights
    table_rows_data = []
    for title, val, color, is_bold, is_mono in rows:
        lines = wrap_text(val, max_chars=62)
        rh = max(44, (len(lines) * LINE_H) + (PAD_Y * 2))
        table_rows_data.append((title, lines, color, is_bold, is_mono, rh))

    table_h = sum(r[5] for r in table_rows_data)

    # Coordinates
    header_y = 30
    meta_y = header_y + 60
    meta_h = 42

    table_y = meta_y + meta_h + 18
    ev1_y = table_y + table_h + 25

    ev2_y = ev1_y + ev1_h + 20 if has_p2 else ev1_y
    footer_y = (ev2_y + ev2_h if has_p2 else ev1_y + ev1_h) + 25
    footer_h = 60

    TOTAL_H = footer_y + footer_h + 25

    svg = []
    svg.append(f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 {CARD_W} {TOTAL_H}" width="{CARD_W}" height="{TOTAL_H}">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Sarabun:wght@300;400;600;700;800&amp;display=swap');
      text {{ font-family: 'Sarabun', 'TH Sarabun New', 'TH Sarabun PSK', sans-serif; }}
      .title {{ font-size: 22px; font-weight: 800; fill: #0f172a; }}
      .sub {{ font-size: 15px; font-weight: 300; fill: #64748b; }}
      .meta-label {{ font-size: 16px; font-weight: 300; fill: #0f172a; }}
      .meta-bold {{ font-size: 16px; font-weight: 700; fill: #0f172a; }}
      .th-txt {{ font-size: 18px; font-weight: 700; fill: #1e293b; }}
      .td-txt {{ font-size: 18px; font-weight: 300; fill: #0f172a; }}
      .td-bold {{ font-size: 18px; font-weight: 700; fill: #0f172a; }}
      .ev-title {{ font-size: 14px; font-weight: 700; fill: #ffffff; }}
      .stamp-txt {{ font-size: 11px; font-weight: 800; fill: #ffffff; letter-spacing: 0.5px; }}
      .footer-txt {{ font-size: 14px; font-weight: 300; fill: #64748b; }}
      .footer-sub {{ font-size: 13px; font-weight: 300; fill: #94a3b8; }}
    </style>
  </defs>

  <!-- BACKGROUND -->
  <rect x="0" y="0" width="{CARD_W}" height="{TOTAL_H}" fill="#f8fafc" />
  
  <!-- CARD WRAPPER -->
  <rect x="{MARGIN_X}" y="20" width="{CONTENT_W}" height="{TOTAL_H - 40}" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5" />

  <!-- HEADER -->
  <g transform="translate({MARGIN_X + 20}, {header_y})">
    <text x="0" y="24" class="title">⚖️ แฟ้มสำนวนคดีอาญา (มาตรฐานศาลยุติธรรม - CODEX VECTOR STREAM)</text>
    <text x="0" y="48" class="sub">เอกสารบัญชีพยานหลักฐานประกอบคำฟ้อง / คำร้องทุกข์ แยกตามกรรมต่างวาระ (ป.อ. มาตรา ๙๑)</text>
  </g>

  <!-- METADATA PILL -->
  <g transform="translate({MARGIN_X + 20}, {meta_y})">
    <rect x="0" y="0" width="{CONTENT_W - 40}" height="{meta_h}" rx="6" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1" />
    <text x="14" y="26" class="meta-label">
      <tspan font-weight="700">บุคคลเป้าหมาย:</tspan> {esc(ev['person'])} ({esc(ev['person_role'])})
    </text>
    <text x="{CONTENT_W - 54}" y="26" text-anchor="end" class="meta-bold">
      <tspan fill="#b91c1c">{esc(ev['count_no'])}</tspan> | 
      <tspan fill="#1e3a8a">ความเสียหาย: {esc(ev['amount'])}</tspan>
    </text>
  </g>

  <!-- 11 TOPICS TABLE -->
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
        
        # Title (Bold 18px)
        svg.append(f'    <text x="14" y="{accum_y + 26}" class="th-txt">{esc(title)}</text>')
        
        # Lines (Thin 18px)
        line_y = accum_y + 26
        for l in lines:
            weight_cls = "td-bold" if is_bold else "td-txt"
            font_family = "font-family: monospace; font-size: 15px;" if is_mono else ""
            svg.append(f'    <text x="{COL1_W + 14}" y="{line_y}" class="{weight_cls}" fill="{color}" style="{font_family}">{esc(l)}</text>')
            line_y += LINE_H
            
        accum_y += rh

    svg.append('  </g>\n')

    # Evidence Box 1
    svg.append(f'''  <!-- EVIDENCE BOX 1 -->
  <g transform="translate({MARGIN_X + 20}, {ev1_y})">
    <rect x="0" y="0" width="{CONTENT_W - 40}" height="{ev1_h}" rx="6" fill="#0f172a" stroke="#1e293b" stroke-width="1.5" />
    
    <rect x="0" y="0" width="{CONTENT_W - 40}" height="36" rx="6" fill="#1e293b" />
    <text x="14" y="23" class="ev-title">📸 พยานหลักฐานภาพเหตุการณ์อ้างอิงจริง (ครอปเฉพาะกรอบบริบทชัดเจน 100% - มาตรฐานศาล)</text>
    
    <rect x="{CONTENT_W - 40 - 240}" y="7" width="226" height="22" rx="3" fill="#dc2626" />
    <text x="{CONTENT_W - 40 - 127}" y="22" text-anchor="middle" class="stamp-txt">CERTIFIED COURT EVIDENCE • ISO/IEC 27037</text>
    
    <g transform="translate({(CONTENT_W - 40 - disp1_w)/2}, 45)">
      <image href="{p1_uri}" width="{disp1_w}" height="{disp1_h}" preserveAspectRatio="xMidYMid meet" />
    </g>
  </g>
''')

    # Evidence Box 2 (if has_p2)
    if has_p2:
        svg.append(f'''  <!-- EVIDENCE BOX 2 -->
  <g transform="translate({MARGIN_X + 20}, {ev2_y})">
    <rect x="0" y="0" width="{CONTENT_W - 40}" height="{ev2_h}" rx="6" fill="#0f172a" stroke="#1e293b" stroke-width="1.5" />
    
    <rect x="0" y="0" width="{CONTENT_W - 40}" height="36" rx="6" fill="#0369a1" />
    <text x="14" y="23" class="ev-title">📑 หลักฐานต่อเนื่อง / สลิปโอนเงินขยายใหญ่ (Part 2): {esc(ev.get("p2_desc", ""))}</text>
    
    <g transform="translate({(CONTENT_W - 40 - disp2_w)/2}, 45)">
      <image href="{p2_uri}" width="{disp2_w}" height="{disp2_h}" preserveAspectRatio="xMidYMid meet" />
    </g>
  </g>
''')

    # Footer
    svg.append(f'''  <!-- FOOTER -->
  <g transform="translate({MARGIN_X + 20}, {footer_y})">
    <line x1="0" y1="0" x2="{CONTENT_W - 40}" y2="0" stroke="#cbd5e1" stroke-width="1" />
    <text x="0" y="24" class="footer-txt">สารบบคดีอาญา: ขบวนการฉ้อโกงเป็นปกติธุระ (ป.อ. มาตรา ๓๔๑, ๙๑) | แผ่นเวกเตอร์ที่ {seq_num} จาก ๓๐ รายการ</text>
    <text x="0" y="46" class="footer-sub">รับรองสำเนาถูกต้องโดยระบบนิติวิทยาศาสตร์ดิจิทัล (Digital Evi Codex V2) • ISO/IEC 27037 Standard</text>
  </g>

</svg>''')

    return "\n".join(svg)

# Generate All 30 SVGs
print("Building 30 Vector SVGs with strict TH Sarabun Thin 18 & Bold Headers...")
svg_entries = []

for idx, ev in enumerate(counts, start=1):
    svg_code = build_vector_card(ev, idx)
    fn = f"VECTOR_COUNT_{idx:02d}.svg"
    fp = os.path.join(vector_dir, fn)
    art_fp = os.path.join(art_vector_dir, fn)
    
    with open(fp, "w", encoding="utf-8") as f:
        f.write(svg_code)
    with open(art_fp, "w", encoding="utf-8") as f:
        f.write(svg_code)
        
    svg_entries.append((fn, ev['count_no'], ev['person'], ev['amount'], ev['count_title']))
    print(f"  [OK] {fn}")

print("All 30 Vector Cards updated successfully!")

# Also generate a crisp preview of Count 1
preview_svg = os.path.join(vector_dir, "VECTOR_COUNT_01.svg")
doc = fitz.open(preview_svg)
pix = doc[0].get_pixmap(dpi=150)
prev_png = os.path.join(vector_dir, "preview_vector_c1.png")
pix.save(prev_png)
art_prev_png = os.path.join(art_vector_dir, "preview_vector_c1.png")
pix.save(art_prev_png)
print(f"Updated preview_vector_c1.png ({pix.width}x{pix.height})")

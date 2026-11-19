# -*- coding: utf-8 -*-
import os
import base64
from PIL import Image
import fitz

# 1. Load Count 1 data
from build_court_dossier_smart_cropped import counts
ev = counts[0]

# 2. Crop Bubble 1 ONLY from 800252756
raw_ori = r'C:\Users\EVE\Downloads\ของมันคนเดียว-20261117T094313Z-1-003\ของมันคนเดียว\แคปหน้า Ori'
im1_path = os.path.join(raw_ori, 'LINE_capture_800252756.687906.jpg')
im1 = Image.open(im1_path)
# y=2335 to 2505 (Bubble 1 ONLY, 636x170 px)
c1 = im1.crop((0, 2335, 636, 2505))
out_c1 = r'd:\Project\ชวกม.2\EDOK_NUI\A4_EVIDENCE_ASSETS\ctx_count_01_p1.png'
c1.save(out_c1)

with open(out_c1, "rb") as f:
    b64_img = base64.b64encode(f.read()).decode("ascii")
data_uri = f"data:image/png;base64,{b64_img}"

CARD_W = 1000
MARGIN_X = 40
CONTENT_W = CARD_W - (MARGIN_X * 2) # 920 px
COL1_W = 230
COL2_W = CONTENT_W - COL1_W # 690 px

# Helper for Thai word wrapping at ~65 chars
def wrap_text(text, max_chars=65):
    lines = []
    for raw_line in text.split("\n"):
        raw_line = raw_line.strip()
        if not raw_line:
            continue
        while len(raw_line) > max_chars:
            # find last space or punctuation before max_chars
            split_idx = raw_line.rfind(" ", 0, max_chars)
            if split_idx == -1 or split_idx < 30:
                split_idx = max_chars
            lines.append(raw_line[:split_idx].strip())
            raw_line = raw_line[split_idx:].strip()
        if raw_line:
            lines.append(raw_line)
    return lines

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

# Calculate table rows geometry
LINE_H = 26
PAD_Y = 12

table_rows_data = []
for title, val, color, is_bold, is_mono in rows:
    lines = wrap_text(val, max_chars=62)
    rh = max(44, (len(lines) * LINE_H) + (PAD_Y * 2))
    table_rows_data.append((title, lines, color, is_bold, is_mono, rh))

table_h = sum(r[5] for r in table_rows_data)

# Evidence image geometry
disp_w = min(840, c1.width)
disp_h = int(c1.height * (disp_w / c1.width))
ev_box_h = 36 + 20 + disp_h + 20

# Coordinates
curr_y = 30
header_y = curr_y

meta_y = header_y + 60
meta_h = 42

table_y = meta_y + meta_h + 18

ev_y = table_y + table_h + 25

footer_y = ev_y + ev_box_h + 25
footer_h = 60

TOTAL_H = footer_y + footer_h + 25

def esc(t):
    return str(t).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;").replace("'", "&apos;")

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

# Render Table
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
    
    # Title
    svg.append(f'    <text x="14" y="{accum_y + 26}" class="th-txt">{esc(title)}</text>')
    
    # Lines
    line_y = accum_y + 26
    for l in lines:
        weight_cls = "td-bold" if is_bold else "td-txt"
        font_family = "font-family: monospace; font-size: 15px;" if is_mono else ""
        svg.append(f'    <text x="{COL1_W + 14}" y="{line_y}" class="{weight_cls}" fill="{color}" style="{font_family}">{esc(l)}</text>')
        line_y += LINE_H
        
    accum_y += rh

svg.append('  </g>\n')

# Render Evidence Box
svg.append(f'''  <!-- EVIDENCE BOX -->
  <g transform="translate({MARGIN_X + 20}, {ev_y})">
    <rect x="0" y="0" width="{CONTENT_W - 40}" height="{ev_box_h}" rx="6" fill="#0f172a" stroke="#1e293b" stroke-width="1.5" />
    
    <!-- Title Bar -->
    <rect x="0" y="0" width="{CONTENT_W - 40}" height="36" rx="6" fill="#1e293b" />
    <text x="14" y="23" class="ev-title">📸 พยานหลักฐานภาพเหตุการณ์อ้างอิงจริง (ครอปเฉพาะกรอบบริบทชัดเจน 100% - มาตรฐานศาล)</text>
    
    <rect x="{CONTENT_W - 40 - 240}" y="7" width="226" height="22" rx="3" fill="#dc2626" />
    <text x="{CONTENT_W - 40 - 127}" y="22" text-anchor="middle" class="stamp-txt">CERTIFIED COURT EVIDENCE • ISO/IEC 27037</text>
    
    <!-- Evidence Image -->
    <g transform="translate({(CONTENT_W - 40 - disp_w)/2}, 46)">
      <image href="{data_uri}" width="{disp_w}" height="{disp_h}" preserveAspectRatio="xMidYMid meet" />
    </g>
  </g>
''')

# Render Footer
svg.append(f'''  <!-- FOOTER -->
  <g transform="translate({MARGIN_X + 20}, {footer_y})">
    <line x1="0" y1="0" x2="{CONTENT_W - 40}" y2="0" stroke="#cbd5e1" stroke-width="1" />
    <text x="0" y="24" class="footer-txt">สารบบคดีอาญา: ขบวนการฉ้อโกงเป็นปกติธุระ (ป.อ. มาตรา ๓๔๑, ๙๑) | แผ่นเวกเตอร์ที่ ๑ จาก ๓๐ รายการ</text>
    <text x="0" y="46" class="footer-sub">รับรองสำเนาถูกต้องโดยระบบนิติวิทยาศาสตร์ดิจิทัล (Digital Evi Codex V2) • ISO/IEC 27037 Certification Standard</text>
  </g>

</svg>''')

svg_str = "\n".join(svg)
test_svg_path = r'd:\Project\ชวกม.2\EDOK_NUI\VECTOR_EVIDENCE\test_c1_perfect.svg'
with open(test_svg_path, 'w', encoding='utf-8') as f:
    f.write(svg_str)

doc = fitz.open(test_svg_path)
pix = doc[0].get_pixmap(dpi=150)
test_png_path = r'd:\Project\ชวกม.2\EDOK_NUI\VECTOR_EVIDENCE\test_c1_perfect.png'
pix.save(test_png_path)
print(f"Generated test_c1_perfect.png successfully: {pix.width}x{pix.height}")

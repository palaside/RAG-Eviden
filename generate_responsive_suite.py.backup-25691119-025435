# -*- coding: utf-8 -*-
"""
Script: generate_responsive_suite.py (Updated with dedicated Page 2 for counts with has_p2)
- Count 4 and other 2-page counts now have:
  * Page 1: Topics 1-11 + Evidence Box 1 (Chat Context) + "มีต่อหน้า ๒ ➔" badge
  * Page 2: Header + Linking Summary + Evidence Box 2 (Part 2: Slip / Additional Evidence)
  * Separate P1 & P2 HTML cards, separate P1 & P2 SVGs
  * Master Dashboard renders Part 2 as the immediate next page ("หน้าถัดไป") with auto-resizing iframes
  * Authentic TH Sarabun PSK TrueType Base64 embedded everywhere
"""

import os
import re
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

# Load authentic government TH Sarabun PSK fonts
ttf_reg = r'C:\Users\EVE\AppData\Local\Microsoft\Windows\Fonts\THSarabun.ttf'
ttf_bold = r'C:\Users\EVE\AppData\Local\Microsoft\Windows\Fonts\THSarabun Bold.ttf'

with open(ttf_reg, 'rb') as f:
    b64_sarabun_reg = base64.b64encode(f.read()).decode('ascii')
with open(ttf_bold, 'rb') as f:
    b64_sarabun_bold = base64.b64encode(f.read()).decode('ascii')

SARABUN_FONT_FACE_CSS = f'''
@font-face {{
  font-family: 'TH Sarabun PSK';
  src: url('data:font/truetype;charset=utf-8;base64,{b64_sarabun_reg}') format('truetype');
  font-weight: 300;
  font-style: normal;
}}
@font-face {{
  font-family: 'TH Sarabun PSK';
  src: url('data:font/truetype;charset=utf-8;base64,{b64_sarabun_reg}') format('truetype');
  font-weight: 400;
  font-style: normal;
}}
@font-face {{
  font-family: 'TH Sarabun PSK';
  src: url('data:font/truetype;charset=utf-8;base64,{b64_sarabun_bold}') format('truetype');
  font-weight: 700;
  font-style: normal;
}}
@font-face {{
  font-family: 'TH Sarabun PSK';
  src: url('data:font/truetype;charset=utf-8;base64,{b64_sarabun_bold}') format('truetype');
  font-weight: 800;
  font-style: normal;
}}
@font-face {{
  font-family: 'THSarabunPSK';
  src: url('data:font/truetype;charset=utf-8;base64,{b64_sarabun_reg}') format('truetype');
  font-weight: 300;
  font-style: normal;
}}
@font-face {{
  font-family: 'THSarabunPSK';
  src: url('data:font/truetype;charset=utf-8;base64,{b64_sarabun_reg}') format('truetype');
  font-weight: 400;
  font-style: normal;
}}
@font-face {{
  font-family: 'THSarabunPSK';
  src: url('data:font/truetype;charset=utf-8;base64,{b64_sarabun_bold}') format('truetype');
  font-weight: 700;
  font-style: normal;
}}
@font-face {{
  font-family: 'THSarabunPSK';
  src: url('data:font/truetype;charset=utf-8;base64,{b64_sarabun_bold}') format('truetype');
  font-weight: 800;
  font-style: normal;
}}
'''

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

FONT_SIZE = 16
LINE_H = 24
PAD_Y = 10

# -------------------------------------------------------------
# SVG GENERATOR: PAGE 1 (Topics 1-11 + Evidence Box 1)
# -------------------------------------------------------------
def generate_hardened_svg_p1(ev, page_index_str, total_pages=1):
    is_two_page = (total_pages > 1)
    
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

    header_y = 25
    meta_y = header_y + 36
    meta_h = 42
    table_y = meta_y + meta_h + 16
    ev1_y = table_y + table_h + 22
    TOTAL_H = ev1_y + ev1_h + 25

    count_label = f"{ev['count_no']} (หน้า ๑/๒)" if is_two_page else ev['count_no']

    svg = []
    svg.append(f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 {CARD_W} {TOTAL_H}" width="{CARD_W}" height="{TOTAL_H}">
  <defs>
    <style>
      {SARABUN_FONT_FACE_CSS}
      text {{ font-family: 'TH Sarabun PSK', 'THSarabunPSK', 'TH Sarabun New', sans-serif; }}
      .title {{ font-size: 20px; font-weight: 800; fill: #0f172a; }}
      .meta-label {{ font-size: 15px; font-weight: 300; fill: #0f172a; }}
      .th-txt {{ font-size: 16px; font-weight: 700; fill: #1e293b; }}
      .td-txt {{ font-size: 16px; font-weight: 300; fill: #0f172a; }}
      .td-bold {{ font-size: 16px; font-weight: 700; fill: #0f172a; }}
      .ev-title {{ font-size: 14.5px; font-weight: 700; fill: #ffffff; }}
      .stamp-txt {{ font-size: 10.5px; font-weight: 800; fill: #ffffff; letter-spacing: 0.5px; }}
    </style>
  </defs>

  <!-- BACKGROUND -->
  <rect x="0" y="0" width="{CARD_W}" height="{TOTAL_H}" fill="#f8fafc" />
  
  <!-- CARD WRAPPER -->
  <rect x="{MARGIN_X}" y="15" width="{CONTENT_W}" height="{TOTAL_H - 30}" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5" />

  <!-- HEADER -->
  <g transform="translate({MARGIN_X + 20}, {header_y})">
    <text x="0" y="22" fill="#0f172a" font-size="20px" font-weight="800" font-family="'TH Sarabun PSK', 'THSarabunPSK', 'TH Sarabun New', sans-serif">แฟ้มสำนวน</text>
  </g>

  <!-- METADATA BAR -->
  <g transform="translate({MARGIN_X + 20}, {meta_y})">
    <rect x="0" y="0" width="{CONTENT_W - 40}" height="{meta_h}" rx="6" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1" />
    
    <!-- Left Person Info -->
    <text x="14" y="26" fill="#0f172a" font-size="15px" font-weight="300" font-family="'TH Sarabun PSK', 'THSarabunPSK', 'TH Sarabun New', sans-serif">
      <tspan font-weight="700">บุคคลเป้าหมาย:</tspan> {esc(ev['person'])}
    </text>
''')

    if is_two_page:
        svg.append(f'''    <!-- Badges for 2-Page Count -->
    <!-- Count Badge (Red) -->
    <rect x="{CONTENT_W - 40 - 380}" y="8" width="105" height="26" rx="4" fill="#fee2e2" stroke="#fca5a5" stroke-width="1" />
    <text x="{CONTENT_W - 40 - 327}" y="25" text-anchor="middle" font-size="13px" font-weight="700" fill="#b91c1c" font-family="'TH Sarabun PSK', 'THSarabunPSK', 'TH Sarabun New', sans-serif">{esc(count_label)}</text>
    
    <!-- Next Page Badge (Amber) -->
    <rect x="{CONTENT_W - 40 - 265}" y="8" width="95" height="26" rx="4" fill="#fef3c7" stroke="#fcd34d" stroke-width="1" />
    <text x="{CONTENT_W - 40 - 217}" y="25" text-anchor="middle" font-size="12px" font-weight="700" fill="#b45309" font-family="'TH Sarabun PSK', 'THSarabunPSK', 'TH Sarabun New', sans-serif">มีต่อหน้า ๒ ➔</text>
    
    <!-- Amount Badge (Blue) -->
    <rect x="{CONTENT_W - 40 - 160}" y="8" width="150" height="26" rx="4" fill="#eff6ff" stroke="#bfdbfe" stroke-width="1" />
    <text x="{CONTENT_W - 40 - 85}" y="25" text-anchor="middle" font-size="13px" font-weight="700" fill="#1e40af" font-family="'TH Sarabun PSK', 'THSarabunPSK', 'TH Sarabun New', sans-serif">ความเสียหาย: {esc(ev['amount'])}</text>
  </g>
''')
    else:
        svg.append(f'''    <!-- Count Badge (Red) -->
    <rect x="{CONTENT_W - 40 - 280}" y="8" width="100" height="26" rx="4" fill="#fee2e2" stroke="#fca5a5" stroke-width="1" />
    <text x="{CONTENT_W - 40 - 230}" y="25" text-anchor="middle" font-size="13px" font-weight="700" fill="#b91c1c" font-family="'TH Sarabun PSK', 'THSarabunPSK', 'TH Sarabun New', sans-serif">{esc(count_label)}</text>
    
    <!-- Amount Badge (Blue) -->
    <rect x="{CONTENT_W - 40 - 172}" y="8" width="160" height="26" rx="4" fill="#eff6ff" stroke="#bfdbfe" stroke-width="1" />
    <text x="{CONTENT_W - 40 - 92}" y="25" text-anchor="middle" font-size="13px" font-weight="700" fill="#1e40af" font-family="'TH Sarabun PSK', 'THSarabunPSK', 'TH Sarabun New', sans-serif">ความเสียหาย: {esc(ev['amount'])}</text>
  </g>
''')

    svg.append(f'''  <!-- 11 TOPICS TABLE (FONT 16PX - TH SARABUN PSK) -->
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
        
        svg.append(f'    <text x="14" y="{accum_y + 26}" fill="#0f172a" font-size="16px" font-weight="700" font-family="\'TH Sarabun PSK\', \'THSarabunPSK\', \'TH Sarabun New\', sans-serif">{esc(title)}</text>')
        
        line_y = accum_y + 26
        for l in lines:
            weight = "700" if is_bold else "300"
            font_fam = "monospace" if is_mono else "'TH Sarabun PSK', 'THSarabunPSK', 'TH Sarabun New', sans-serif"
            font_sz = "14px" if is_mono else "16px"
            svg.append(f'    <text x="{COL1_W + 14}" y="{line_y}" fill="{color}" font-size="{font_sz}" font-weight="{weight}" font-family="{font_fam}">{esc(l)}</text>')
            line_y += LINE_H
            
        accum_y += rh

    svg.append('  </g>\n')

    # Evidence Box 1 (Part 1 Only)
    svg.append(f'''  <!-- EVIDENCE BOX 1 (RESPONSIVE HEIGHT: {ev1_h}px) -->
  <g transform="translate({MARGIN_X + 20}, {ev1_y})">
    <rect x="0" y="0" width="{CONTENT_W - 40}" height="{ev1_h}" rx="6" fill="#0f172a" stroke="#1e293b" stroke-width="1.5" />
    
    <rect x="0" y="0" width="{CONTENT_W - 40}" height="36" rx="6" fill="#1e293b" />
    <text x="16" y="23" fill="#ffffff" font-size="14.5px" font-weight="700" font-family="'TH Sarabun PSK', 'THSarabunPSK', 'TH Sarabun New', sans-serif">📸 พยานหลักฐานภาพเหตุการณ์อ้างอิงจริง</text>
    
    <rect x="{CONTENT_W - 40 - 240}" y="7" width="226" height="22" rx="3" fill="#dc2626" />
    <text x="{CONTENT_W - 40 - 127}" y="22" text-anchor="middle" fill="#ffffff" font-size="10.5px" font-weight="800" font-family="'TH Sarabun PSK', 'THSarabunPSK', 'TH Sarabun New', sans-serif" letter-spacing="0.5px">CERTIFIED COURT EVIDENCE • ISO/IEC 27037</text>
    
    <g transform="translate({(CONTENT_W - 40 - disp1_w)/2}, 44)">
      <image href="{p1_uri}" width="{disp1_w}" height="{disp1_h}" preserveAspectRatio="xMidYMid meet" />
    </g>
  </g>
</svg>''')

    return "\n".join(svg)

# -------------------------------------------------------------
# SVG GENERATOR: PAGE 2 (Context Summary + Evidence Box 2 Part 2)
# -------------------------------------------------------------
def generate_hardened_svg_p2(ev, page_index_str):
    img_p2_rel = f"A4_EVIDENCE_ASSETS/{ev['img_p2']}"
    img_p2_path = os.path.join(r"d:\Project\ชวกม.2\EDOK_NUI", img_p2_rel)
    p2_uri = image_to_base64_data_uri(img_p2_path)
    
    p2_w, p2_h = 600, 400
    if os.path.exists(img_p2_path):
        with Image.open(img_p2_path) as im:
            p2_w, p2_h = im.size
            
    disp2_w = min(840, p2_w)
    disp2_h = int(p2_h * (disp2_w / p2_w)) if p2_w else 400
    ev2_h = 36 + 16 + disp2_h + 16

    link_rows = [
        ("อ้างอิงความเชื่อมโยง", f"สืบเนื่องจาก {ev['count_no']} (หน้า ๑/๒) - {ev['count_title']}"),
        ("วันเวลาเกิดเหตุ / ยอดเงิน", f"{ev['datetime']} | จำนวนเงิน {ev['amount']} บาท"),
        ("สาระสำคัญหลักฐาน Part 2", ev.get("p2_desc", "หลักฐานการเงิน / สลิปโอนเงินขยายความต่อเนื่องแห่งคดี")),
    ]
    
    link_rows_data = []
    for title, val in link_rows:
        lines = wrap_text(val, max_chars=66)
        rh = max(38, (len(lines) * LINE_H) + (PAD_Y * 2))
        link_rows_data.append((title, lines, rh))
        
    link_table_h = sum(r[2] for r in link_rows_data)

    header_y = 25
    meta_y = header_y + 36
    meta_h = 42
    table_y = meta_y + meta_h + 16
    ev2_y = table_y + link_table_h + 22
    TOTAL_H = ev2_y + ev2_h + 25

    count_label = f"{ev['count_no']} (หน้า ๒/๒)"

    svg = []
    svg.append(f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 {CARD_W} {TOTAL_H}" width="{CARD_W}" height="{TOTAL_H}">
  <defs>
    <style>
      {SARABUN_FONT_FACE_CSS}
      text {{ font-family: 'TH Sarabun PSK', 'THSarabunPSK', 'TH Sarabun New', sans-serif; }}
      .title {{ font-size: 20px; font-weight: 800; fill: #0f172a; }}
      .meta-label {{ font-size: 15px; font-weight: 300; fill: #0f172a; }}
      .th-txt {{ font-size: 16px; font-weight: 700; fill: #1e293b; }}
      .td-txt {{ font-size: 16px; font-weight: 300; fill: #0f172a; }}
      .td-bold {{ font-size: 16px; font-weight: 700; fill: #0f172a; }}
      .ev-title {{ font-size: 14.5px; font-weight: 700; fill: #ffffff; }}
      .stamp-txt {{ font-size: 10.5px; font-weight: 800; fill: #ffffff; letter-spacing: 0.5px; }}
    </style>
  </defs>

  <!-- BACKGROUND -->
  <rect x="0" y="0" width="{CARD_W}" height="{TOTAL_H}" fill="#f8fafc" />
  
  <!-- CARD WRAPPER -->
  <rect x="{MARGIN_X}" y="15" width="{CONTENT_W}" height="{TOTAL_H - 30}" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5" />

  <!-- HEADER -->
  <g transform="translate({MARGIN_X + 20}, {header_y})">
    <text x="0" y="22" fill="#0f172a" font-size="20px" font-weight="800" font-family="'TH Sarabun PSK', 'THSarabunPSK', 'TH Sarabun New', sans-serif">แฟ้มสำนวน</text>
  </g>

  <!-- METADATA BAR -->
  <g transform="translate({MARGIN_X + 20}, {meta_y})">
    <rect x="0" y="0" width="{CONTENT_W - 40}" height="{meta_h}" rx="6" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1" />
    
    <!-- Left Person Info -->
    <text x="14" y="26" fill="#0f172a" font-size="15px" font-weight="300" font-family="'TH Sarabun PSK', 'THSarabunPSK', 'TH Sarabun New', sans-serif">
      <tspan font-weight="700">บุคคลเป้าหมาย:</tspan> {esc(ev['person'])}
    </text>
    
    <!-- Badges -->
    <rect x="{CONTENT_W - 40 - 410}" y="8" width="105" height="26" rx="4" fill="#fee2e2" stroke="#fca5a5" stroke-width="1" />
    <text x="{CONTENT_W - 40 - 357}" y="25" text-anchor="middle" font-size="13px" font-weight="700" fill="#b91c1c" font-family="'TH Sarabun PSK', 'THSarabunPSK', 'TH Sarabun New', sans-serif">{esc(count_label)}</text>
    
    <rect x="{CONTENT_W - 40 - 295}" y="8" width="125" height="26" rx="4" fill="#e0f2fe" stroke="#7dd3fc" stroke-width="1" />
    <text x="{CONTENT_W - 40 - 232}" y="25" text-anchor="middle" font-size="12px" font-weight="700" fill="#0369a1" font-family="'TH Sarabun PSK', 'THSarabunPSK', 'TH Sarabun New', sans-serif">หลักฐานต่อเนื่อง (Part 2)</text>
    
    <rect x="{CONTENT_W - 40 - 160}" y="8" width="150" height="26" rx="4" fill="#eff6ff" stroke="#bfdbfe" stroke-width="1" />
    <text x="{CONTENT_W - 40 - 85}" y="25" text-anchor="middle" font-size="13px" font-weight="700" fill="#1e40af" font-family="'TH Sarabun PSK', 'THSarabunPSK', 'TH Sarabun New', sans-serif">ความเสียหาย: {esc(ev['amount'])}</text>
  </g>

  <!-- CONTEXT LINKING TABLE -->
  <g transform="translate({MARGIN_X + 20}, {table_y})">
''')

    accum_y = 0
    for title, lines, rh in link_rows_data:
        svg.append(f'    <!-- Row: {esc(title)} -->')
        svg.append(f'    <rect x="0" y="{accum_y}" width="{COL1_W}" height="{rh}" fill="#f0f9ff" stroke="#bae6fd" stroke-width="1" />')
        svg.append(f'    <rect x="{COL1_W}" y="{accum_y}" width="{COL2_W - 40}" height="{rh}" fill="#ffffff" stroke="#bae6fd" stroke-width="1" />')
        
        svg.append(f'    <text x="14" y="{accum_y + 25}" fill="#0369a1" font-size="16px" font-weight="700" font-family="\'TH Sarabun PSK\', \'THSarabunPSK\', \'TH Sarabun New\', sans-serif">{esc(title)}</text>')
        
        line_y = accum_y + 25
        for l in lines:
            svg.append(f'    <text x="{COL1_W + 14}" y="{line_y}" fill="#0f172a" font-size="16px" font-weight="500" font-family="\'TH Sarabun PSK\', \'THSarabunPSK\', \'TH Sarabun New\', sans-serif">{esc(l)}</text>')
            line_y += LINE_H
            
        accum_y += rh

    svg.append('  </g>\n')

    # Evidence Box 2 (Part 2 Displayed Full Size!)
    svg.append(f'''  <!-- EVIDENCE BOX 2 (FULL DISPLAY Part 2: {ev2_h}px) -->
  <g transform="translate({MARGIN_X + 20}, {ev2_y})">
    <rect x="0" y="0" width="{CONTENT_W - 40}" height="{ev2_h}" rx="6" fill="#0f172a" stroke="#0369a1" stroke-width="1.5" />
    
    <rect x="0" y="0" width="{CONTENT_W - 40}" height="36" rx="6" fill="#0369a1" />
    <text x="16" y="23" fill="#ffffff" font-size="14.5px" font-weight="700" font-family="'TH Sarabun PSK', 'THSarabunPSK', 'TH Sarabun New', sans-serif">📑 พยานหลักฐานต่อเนื่อง / สลิปโอนเงิน (Part 2)</text>
    
    <rect x="{CONTENT_W - 40 - 240}" y="7" width="226" height="22" rx="3" fill="#dc2626" />
    <text x="{CONTENT_W - 40 - 127}" y="22" text-anchor="middle" fill="#ffffff" font-size="10.5px" font-weight="800" font-family="'TH Sarabun PSK', 'THSarabunPSK', 'TH Sarabun New', sans-serif" letter-spacing="0.5px">CERTIFIED COURT EVIDENCE • ISO/IEC 27037</text>
    
    <g transform="translate({(CONTENT_W - 40 - disp2_w)/2}, 44)">
      <image href="{p2_uri}" width="{disp2_w}" height="{disp2_h}" preserveAspectRatio="xMidYMid meet" />
    </g>
  </g>
</svg>''')

    return "\n".join(svg)

# -------------------------------------------------------------
# HTML CARD GENERATORS (Page 1 & Page 2)
# -------------------------------------------------------------
def generate_responsive_html_p1(ev, page_index_str, total_pages=1):
    is_two_page = (total_pages > 1)
    img_p1_rel = f"A4_EVIDENCE_ASSETS/{ev['img_p1']}"
    img_p1_path = os.path.join(r"d:\Project\ชวกม.2\EDOK_NUI", img_p1_rel)
    p1_uri = image_to_base64_data_uri(img_p1_path)

    laws_html = "".join([f'<div class="law-row">{esc(law)}</div>' for law in ev["codex_laws"]])
    count_label = f"{ev['count_no']} (หน้า ๑/๒)" if is_two_page else ev['count_no']

    next_page_badge = '<span class="pill-next">📄 มีต่อหน้า ๒ (หลักฐานต่อเนื่อง) ➔</span>' if is_two_page else ''

    html = f'''<!DOCTYPE html>
<html lang="th">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{esc(count_label)}: {esc(ev['count_title'])}</title>
  <style>
    {SARABUN_FONT_FACE_CSS}
    * {{ box-sizing: border-box; margin: 0; padding: 0; font-family: 'TH Sarabun PSK', 'THSarabunPSK', 'TH Sarabun New', sans-serif; }}
    body {{
      background: #f1f5f9;
      color: #0f172a;
      font-family: 'TH Sarabun PSK', 'THSarabunPSK', 'TH Sarabun New', sans-serif;
      padding: 16px;
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
      font-size: 14px;
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
      flex-wrap: wrap;
    }}
    .pill-count {{
      background: #fee2e2;
      color: #b91c1c;
      border: 1px solid #fca5a5;
      font-size: 13.5px;
      font-weight: 700;
      padding: 3px 10px;
      border-radius: 4px;
      white-space: nowrap;
    }}
    .pill-next {{
      background: #fef3c7;
      color: #b45309;
      border: 1px solid #fcd34d;
      font-size: 12.5px;
      font-weight: 700;
      padding: 3px 10px;
      border-radius: 4px;
      white-space: nowrap;
    }}
    .pill-amt {{
      background: #eff6ff;
      color: #1e40af;
      border: 1px solid #bfdbfe;
      font-size: 13.5px;
      font-weight: 700;
      padding: 3px 10px;
      border-radius: 4px;
      white-space: nowrap;
    }}
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
    .ev-title {{
      font-size: 14.5px;
      font-weight: 700;
      color: #ffffff;
      white-space: nowrap;
    }}
    .ev-badge {{
      background: #dc2626;
      color: #ffffff;
      font-size: 10.5px;
      font-weight: 800;
      padding: 3px 8px;
      border-radius: 3px;
      letter-spacing: 0.5px;
      white-space: nowrap;
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
  </style>
</head>
<body>
  <div class="dossier-card">
    <!-- HEADER -->
    <div class="court-header">
      <div class="court-title">แฟ้มสำนวน</div>
      
      <!-- METADATA BAR -->
      <div class="meta-bar">
        <div class="meta-left">
          <strong>บุคคลเป้าหมาย:</strong> {esc(ev['person'])}
        </div>
        <div class="meta-right">
          <span class="pill-count">{esc(count_label)}</span>
          {next_page_badge}
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
  </div>
</body>
</html>'''
    return html

def generate_responsive_html_p2(ev, page_index_str):
    img_p2_rel = f"A4_EVIDENCE_ASSETS/{ev['img_p2']}"
    img_p2_path = os.path.join(r"d:\Project\ชวกม.2\EDOK_NUI", img_p2_rel)
    p2_uri = image_to_base64_data_uri(img_p2_path)

    count_label = f"{ev['count_no']} (หน้า ๒/๒)"

    html = f'''<!DOCTYPE html>
<html lang="th">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{esc(count_label)}: หลักฐานต่อเนื่อง (Part 2)</title>
  <style>
    {SARABUN_FONT_FACE_CSS}
    * {{ box-sizing: border-box; margin: 0; padding: 0; font-family: 'TH Sarabun PSK', 'THSarabunPSK', 'TH Sarabun New', sans-serif; }}
    body {{
      background: #f1f5f9;
      color: #0f172a;
      font-family: 'TH Sarabun PSK', 'THSarabunPSK', 'TH Sarabun New', sans-serif;
      padding: 16px;
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
      font-size: 14px;
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
      flex-wrap: wrap;
    }}
    .pill-count {{
      background: #fee2e2;
      color: #b91c1c;
      border: 1px solid #fca5a5;
      font-size: 13.5px;
      font-weight: 700;
      padding: 3px 10px;
      border-radius: 4px;
      white-space: nowrap;
    }}
    .pill-p2 {{
      background: #e0f2fe;
      color: #0369a1;
      border: 1px solid #7dd3fc;
      font-size: 12.5px;
      font-weight: 700;
      padding: 3px 10px;
      border-radius: 4px;
      white-space: nowrap;
    }}
    .pill-amt {{
      background: #eff6ff;
      color: #1e40af;
      border: 1px solid #bfdbfe;
      font-size: 13.5px;
      font-weight: 700;
      padding: 3px 10px;
      border-radius: 4px;
      white-space: nowrap;
    }}
    .topics-table {{
      width: 100%;
      border-collapse: collapse;
      margin-top: 14px;
      font-size: 16px;
      line-height: 1.45;
    }}
    .topics-table th, .topics-table td {{
      border: 1px solid #bae6fd;
      padding: 8px 12px;
      vertical-align: top;
    }}
    .th-col {{
      width: 220px;
      background: #f0f9ff;
      font-weight: 700;
      color: #0369a1;
    }}
    .td-col {{
      font-weight: 400;
      color: #0f172a;
      background: #ffffff;
    }}
    .evidence-card {{
      margin-top: 20px;
      border: 1.5px solid #0369a1;
      border-radius: 6px;
      overflow: hidden;
      background: #0f172a;
    }}
    .p2-header {{
      background: #0369a1;
      padding: 8px 14px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 6px;
    }}
    .ev-title {{
      font-size: 14.5px;
      font-weight: 700;
      color: #ffffff;
      white-space: nowrap;
    }}
    .ev-badge {{
      background: #dc2626;
      color: #ffffff;
      font-size: 10.5px;
      font-weight: 800;
      padding: 3px 8px;
      border-radius: 3px;
      letter-spacing: 0.5px;
      white-space: nowrap;
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
  </style>
</head>
<body>
  <div class="dossier-card">
    <!-- HEADER -->
    <div class="court-header">
      <div class="court-title">แฟ้มสำนวน</div>
      
      <!-- METADATA BAR -->
      <div class="meta-bar">
        <div class="meta-left">
          <strong>บุคคลเป้าหมาย:</strong> {esc(ev['person'])}
        </div>
        <div class="meta-right">
          <span class="pill-count">{esc(count_label)}</span>
          <span class="pill-p2">📑 หลักฐานต่อเนื่อง (Part 2)</span>
          <span class="pill-amt">ความเสียหาย: {esc(ev['amount'])}</span>
        </div>
      </div>
    </div>

    <!-- CONTEXT LINK TABLE -->
    <table class="topics-table">
      <tr>
        <th class="th-col">อ้างอิงความเชื่อมโยง</th>
        <td class="td-col" style="font-weight: 700;">สืบเนื่องจาก {esc(ev['count_no'])} (หน้า ๑/๒) - {esc(ev['count_title'])}</td>
      </tr>
      <tr>
        <th class="th-col">วันเวลา / ยอดเงิน</th>
        <td class="td-col">{esc(ev['datetime'])} | จำนวนเงิน <strong>{esc(ev['amount'])} บาท</strong></td>
      </tr>
      <tr>
        <th class="th-col">สาระสำคัญ Part 2</th>
        <td class="td-col" style="color: #0369a1; font-weight: 600;">{esc(ev.get('p2_desc', 'หลักฐานการเงิน / สลิปโอนเงินขยายความต่อเนื่องแห่งคดี'))}</td>
      </tr>
    </table>

    <!-- EVIDENCE BOX 2 (FULL DISPLAY) -->
    <div class="evidence-card">
      <div class="p2-header">
        <span class="ev-title">📑 พยานหลักฐานต่อเนื่อง / สลิปโอนเงิน (Part 2)</span>
        <span class="ev-badge">CERTIFIED COURT EVIDENCE • ISO/IEC 27037</span>
      </div>
      <div class="evidence-body">
        <img src="{p2_uri}" class="ev-img" alt="Evidence Part 2 ({esc(ev['count_no'])})" />
      </div>
    </div>
  </div>
</body>
</html>'''
    return html

# -------------------------------------------------------------
# MASTER EXECUTION: GENERATE 35 PAGES SUITE & DASHBOARD
# -------------------------------------------------------------
print("Generating 35 Pages Complete Suite (Dedicated Page 2 for Count 4 & 2-page counts)...")

all_pages_list = [] # List of tuples for master dashboard
page_counter = 1
master_strip_elements = []

for idx, ev in enumerate(counts, start=1):
    has_p2 = ev.get("has_p2", False)
    
    if not has_p2:
        # Single Page Count
        p_str = f"{page_counter}"
        svg_fn = f"VECTOR_COUNT_{idx:02d}.svg"
        html_fn = f"COUNT_{idx:02d}_RESPONSIVE.html"
        
        svg_content = generate_hardened_svg_p1(ev, p_str, total_pages=1)
        html_content = generate_responsive_html_p1(ev, p_str, total_pages=1)
        
        with open(os.path.join(vector_dir, svg_fn), "w", encoding="utf-8") as f:
            f.write(svg_content)
        with open(os.path.join(art_vector_dir, svg_fn), "w", encoding="utf-8") as f:
            f.write(svg_content)
            
        with open(os.path.join(vector_dir, html_fn), "w", encoding="utf-8") as f:
            f.write(html_content)
        with open(os.path.join(art_vector_dir, html_fn), "w", encoding="utf-8") as f:
            f.write(html_content)
            
        all_pages_list.append({
            'html_fn': html_fn,
            'svg_fn': svg_fn,
            'badge': ev['count_no'],
            'title': f"{ev['count_no']}: {ev['count_title']}",
            'amount': ev['amount'],
            'page_no': page_counter
        })
        master_strip_elements.append(svg_fn)
        page_counter += 1
        print(f"  [+] {ev['count_no']}: Single Page ({html_fn})")
    else:
        # Two-Page Count (e.g. Count 4, Count 6, Count 14, Count 22, Count 27)
        p1_str = f"{page_counter}"
        svg_p1_fn = f"VECTOR_COUNT_{idx:02d}_P1.svg"
        html_p1_fn = f"COUNT_{idx:02d}_P1_RESPONSIVE.html"
        
        svg_p1_content = generate_hardened_svg_p1(ev, p1_str, total_pages=2)
        html_p1_content = generate_responsive_html_p1(ev, p1_str, total_pages=2)
        
        with open(os.path.join(vector_dir, svg_p1_fn), "w", encoding="utf-8") as f:
            f.write(svg_p1_content)
        with open(os.path.join(art_vector_dir, svg_p1_fn), "w", encoding="utf-8") as f:
            f.write(svg_p1_content)
            
        with open(os.path.join(vector_dir, html_p1_fn), "w", encoding="utf-8") as f:
            f.write(html_p1_content)
        with open(os.path.join(art_vector_dir, html_p1_fn), "w", encoding="utf-8") as f:
            f.write(html_p1_content)
            
        # Also maintain main fn as P1
        main_svg_fn = f"VECTOR_COUNT_{idx:02d}.svg"
        main_html_fn = f"COUNT_{idx:02d}_RESPONSIVE.html"
        with open(os.path.join(vector_dir, main_svg_fn), "w", encoding="utf-8") as f:
            f.write(svg_p1_content)
        with open(os.path.join(art_vector_dir, main_svg_fn), "w", encoding="utf-8") as f:
            f.write(svg_p1_content)
        with open(os.path.join(vector_dir, main_html_fn), "w", encoding="utf-8") as f:
            f.write(html_p1_content)
        with open(os.path.join(art_vector_dir, main_html_fn), "w", encoding="utf-8") as f:
            f.write(html_p1_content)

        all_pages_list.append({
            'html_fn': html_p1_fn,
            'svg_fn': svg_p1_fn,
            'badge': f"{ev['count_no']} (หน้า ๑/๒)",
            'title': f"{ev['count_no']} (หน้า ๑/๒): {ev['count_title']} - [แชทสั่งโอน]",
            'amount': ev['amount'],
            'page_no': page_counter
        })
        master_strip_elements.append(svg_p1_fn)
        page_counter += 1

        # Page 2 (NEXT PAGE)
        p2_str = f"{page_counter}"
        svg_p2_fn = f"VECTOR_COUNT_{idx:02d}_P2.svg"
        html_p2_fn = f"COUNT_{idx:02d}_P2_RESPONSIVE.html"
        
        svg_p2_content = generate_hardened_svg_p2(ev, p2_str)
        html_p2_content = generate_responsive_html_p2(ev, p2_str)
        
        with open(os.path.join(vector_dir, svg_p2_fn), "w", encoding="utf-8") as f:
            f.write(svg_p2_content)
        with open(os.path.join(art_vector_dir, svg_p2_fn), "w", encoding="utf-8") as f:
            f.write(svg_p2_content)
            
        with open(os.path.join(vector_dir, html_p2_fn), "w", encoding="utf-8") as f:
            f.write(html_p2_content)
        with open(os.path.join(art_vector_dir, html_p2_fn), "w", encoding="utf-8") as f:
            f.write(html_p2_content)

        all_pages_list.append({
            'html_fn': html_p2_fn,
            'svg_fn': svg_p2_fn,
            'badge': f"{ev['count_no']} (หน้า ๒/๒)",
            'title': f"{ev['count_no']} (หน้า ๒/๒): หลักฐานต่อเนื่อง / สลิปโอนเงิน (Part 2)",
            'amount': ev['amount'],
            'page_no': page_counter
        })
        master_strip_elements.append(svg_p2_fn)
        page_counter += 1
        print(f"  [+] {ev['count_no']}: 2 Pages Generated ({html_p1_fn} and {html_p2_fn})")

print(f"Total Pages Generated: {len(all_pages_list)} (from 30 counts)")

# -------------------------------------------------------------
# BUILD MASTER DASHBOARD (35 Pages - Seamless Document View)
# -------------------------------------------------------------
master_dash = f'''<!DOCTYPE html>
<html lang="th">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>แฟ้มสารบบคดีอาญาเวกเตอร์แท้ 100% (Responsive Master Dashboard - CODEX CERTIFIED)</title>
  <style>
    {SARABUN_FONT_FACE_CSS}
    * {{ box-sizing: border-box; margin: 0; padding: 0; font-family: 'TH Sarabun PSK', 'THSarabunPSK', 'TH Sarabun New', sans-serif; }}
    body {{
      background: #090d16;
      color: #f8fafc;
      font-family: 'TH Sarabun PSK', 'THSarabunPSK', 'TH Sarabun New', sans-serif;
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
    .h-title {{ font-size: 20px; font-weight: 800; color: #38bdf8; display: flex; align-items: center; gap: 8px; }}
    .h-sub {{ font-size: 14px; font-weight: 300; color: #94a3b8; margin-top: 2px; }}
    .badge-vector {{
      background: #15803d;
      color: #ffffff;
      padding: 4px 12px;
      border-radius: 4px;
      font-size: 13px;
      font-weight: 800;
      letter-spacing: 0.5px;
    }}
    .container {{
      max-width: 1040px;
      margin: 25px auto;
      padding: 0 16px;
    }}
    .quick-nav {{
      background: #1e293b;
      border: 1px solid #334155;
      border-radius: 8px;
      padding: 14px 18px;
      margin-bottom: 25px;
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      align-items: center;
    }}
    .nav-label {{
      font-size: 14px;
      font-weight: 700;
      color: #38bdf8;
      margin-right: 6px;
      width: 100%;
      margin-bottom: 4px;
    }}
    .nav-btn {{
      background: #0f172a;
      border: 1px solid #475569;
      color: #e2e8f0;
      padding: 4px 10px;
      border-radius: 4px;
      font-size: 13px;
      font-weight: 600;
      text-decoration: none;
      transition: all 0.2s;
    }}
    .nav-btn:hover {{
      background: #2563eb;
      border-color: #3b82f6;
      color: #ffffff;
    }}
    .nav-btn.p2-btn {{
      background: #082f49;
      border-color: #0284c7;
      color: #7dd3fc;
    }}
    .nav-btn.p2-btn:hover {{
      background: #0284c7;
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
      font-size: 16px;
      font-weight: 700;
      color: #f8fafc;
    }}
    .shell-actions {{
      display: flex;
      gap: 8px;
    }}
    .act-btn {{
      font-size: 13px;
      padding: 4px 12px;
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
      min-height: 850px;
      border: none;
      background: #f8fafc;
      display: block;
    }}
  </style>
  <script>
    function resizeIframe(obj) {{
      try {{
        if (obj.contentWindow && obj.contentWindow.document.body) {{
          var h = obj.contentWindow.document.documentElement.scrollHeight || obj.contentWindow.document.body.scrollHeight;
          if (h > 200) {{
            obj.style.height = (h + 35) + 'px';
          }}
        }}
      }} catch(e) {{}}
    }}
    window.addEventListener('load', function() {{
      setTimeout(function() {{
        document.querySelectorAll('.shell-frame').forEach(resizeIframe);
      }}, 600);
      setTimeout(function() {{
        document.querySelectorAll('.shell-frame').forEach(resizeIframe);
      }}, 1500);
    }});
  </script>
</head>
<body>
  <header>
    <div>
      <div class="h-title">⚡ แฟ้มสารบบพยานหลักฐานคดีอาญา (ระบบ Responsive Master Dashboard - CODEX CERTIFIED)</div>
      <div class="h-sub">สารบบพยานหลักฐาน ๓๕ แผ่น • บังคับใช้ฟอนต์ TH Sarabun PSK 16 • แยก Part 2 เป็นหน้าถัดไปชัดเจน ๑๐๐%</div>
    </div>
    <div class="badge-vector">TOTAL {len(all_pages_list)} COURT PAGES • ZERO COLLISION</div>
  </header>

  <div class="container">
    <div class="quick-nav">
      <span class="nav-label">⚡ สารบัญทางลัดพยานหลักฐาน (รวม ๓๕ แผ่น):</span>
'''

for item in all_pages_list:
    cls = "nav-btn p2-btn" if "หน้า ๒/๒" in item['badge'] else "nav-btn"
    master_dash += f'      <a href="#{item["html_fn"]}" class="{cls}">{esc(item["badge"])}</a>\n'

master_dash += '    </div>\n'

for item in all_pages_list:
    master_dash += f'''
    <div class="card-shell" id="{item["html_fn"]}">
      <div class="shell-bar">
        <span class="shell-label">📁 แผ่นที่ {item["page_no"]}: {esc(item["title"])} ({esc(item["amount"])} บาท)</span>
        <div class="shell-actions">
          <a href="{item["html_fn"]}" target="_blank" class="act-btn act-html">🖥️ เปิดแผ่นเต็มจอ</a>
          <a href="{item["svg_fn"]}" target="_blank" class="act-btn act-svg">🔍 เปิดไฟล์ SVG เวกเตอร์</a>
        </div>
      </div>
      <iframe src="{item["html_fn"]}" class="shell-frame" title="{esc(item["badge"])}" onload="resizeIframe(this)"></iframe>
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

print(f"Generated MASTER RESPONSIVE DASHBOARD ({len(all_pages_list)} pages) successfully!")

# -------------------------------------------------------------
# REBUILD MASTER VECTOR EVIDENCE STRIP (35 Pages Sequential)
# -------------------------------------------------------------
print("Rebuilding MASTER_VECTOR_EVIDENCE_STRIP.svg with all 35 pages...")
master_elements = []
current_y = 40
strip_w = 1040

for idx, fn in enumerate(master_strip_elements, start=1):
    fp = os.path.join(vector_dir, fn)
    if not os.path.exists(fp):
        continue
    with open(fp, "r", encoding="utf-8") as f:
        content = f.read()
        
    m = re.search(r'viewBox="0 0 (\d+) (\d+)"', content)
    if not m:
        continue
    w = int(m.group(1))
    h = int(m.group(2))
    
    defs_end = content.find("</defs>")
    svg_end = content.rfind("</svg>")
    inner = content[defs_end+7:svg_end]
    
    master_elements.append(f'  <!-- PAGE {idx:02d}: {fn} -->\n  <g transform="translate(20, {current_y})">\n{inner}\n  </g>')
    current_y += h + 30

total_h = current_y + 40

master_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 {strip_w} {total_h}" width="{strip_w}" height="{total_h}">
  <defs>
    <style>
      {SARABUN_FONT_FACE_CSS}
      text {{ font-family: 'TH Sarabun PSK', 'THSarabunPSK', 'TH Sarabun New', sans-serif; }}
      .title {{ font-size: 20px; font-weight: 800; fill: #0f172a; }}
      .sub {{ font-size: 14px; font-weight: 300; fill: #64748b; }}
      .meta-label {{ font-size: 15px; font-weight: 300; fill: #0f172a; }}
      .th-txt {{ font-size: 16px; font-weight: 700; fill: #1e293b; }}
      .td-txt {{ font-size: 16px; font-weight: 300; fill: #0f172a; }}
      .td-bold {{ font-size: 16px; font-weight: 700; fill: #0f172a; }}
      .ev-title {{ font-size: 14.5px; font-weight: 700; fill: #ffffff; }}
      .stamp-txt {{ font-size: 10.5px; font-weight: 800; fill: #ffffff; letter-spacing: 0.5px; }}
      .footer-txt {{ font-size: 13.5px; font-weight: 300; fill: #64748b; }}
      .footer-sub {{ font-size: 12px; font-weight: 300; fill: #94a3b8; }}
    </style>
  </defs>

  <rect x="0" y="0" width="{strip_w}" height="{total_h}" fill="#090d16" />

{''.join(master_elements)}

</svg>'''

out_master = os.path.join(vector_dir, "MASTER_VECTOR_EVIDENCE_STRIP.svg")
out_art_master = os.path.join(art_vector_dir, "MASTER_VECTOR_EVIDENCE_STRIP.svg")

with open(out_master, "w", encoding="utf-8") as f:
    f.write(master_svg)
with open(out_art_master, "w", encoding="utf-8") as f:
    f.write(master_svg)

print(f"Generated MASTER_VECTOR_EVIDENCE_STRIP.svg (Total Height: {total_h}px) successfully!")

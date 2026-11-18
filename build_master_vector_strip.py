# -*- coding: utf-8 -*-
import os
import re
import base64

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

vector_dir = r'd:\Project\ชวกม.2\EDOK_NUI\VECTOR_EVIDENCE'
art_vector_dir = r'C:\Users\EVE\.gemini\antigravity\brain\c8211d09-030e-4b24-8837-3ce9589aa4a6\VECTOR_EVIDENCE'

# Collect all 30 SVGs
svg_files = [f"VECTOR_COUNT_{i:02d}.svg" for i in range(1, 31)]

master_elements = []
current_y = 40
strip_w = 1040

for idx, fn in enumerate(svg_files, start=1):
    fp = os.path.join(vector_dir, fn)
    if not os.path.exists(fp):
        continue
    with open(fp, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Extract viewBox
    m = re.search(r'viewBox="0 0 (\d+) (\d+)"', content)
    if not m:
        continue
    w = int(m.group(1))
    h = int(m.group(2))
    
    # Extract inner body (between <defs>...</defs> and </svg>)
    # Find </defs>
    defs_end = content.find("</defs>")
    svg_end = content.rfind("</svg>")
    inner = content[defs_end+7:svg_end]
    
    # Wrap in a group translated to current_y
    master_elements.append(f'  <!-- COUNT {idx:02d} -->\n  <g transform="translate(20, {current_y})">\n{inner}\n  </g>')
    current_y += h + 30 # gap between cards

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

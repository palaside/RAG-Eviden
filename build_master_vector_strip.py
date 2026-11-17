# -*- coding: utf-8 -*-
import os
import re

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

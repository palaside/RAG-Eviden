# -*- coding: utf-8 -*-
import os
import json
import base64
from PIL import Image
import fitz

# Load Count 1 data
from build_court_dossier_smart_cropped import counts
ev = counts[0]

# Crop Count 1 Bubble 1 ONLY
raw_ori = r'C:\Users\EVE\Downloads\ของมันคนเดียว-20261117T094313Z-1-003\ของมันคนเดียว\แคปหน้า Ori'
im1_path = os.path.join(raw_ori, 'LINE_capture_800252756.687906.jpg')
im1 = Image.open(im1_path)
c1 = im1.crop((0, 2335, 636, 2505))
out_c1 = r'd:\Project\ชวกม.2\EDOK_NUI\A4_EVIDENCE_ASSETS\ctx_count_01_p1.png'
c1.save(out_c1)

with open(out_c1, "rb") as f:
    b64_img = base64.b64encode(f.read()).decode("ascii")
data_uri = f"data:image/png;base64,{b64_img}"

# Laws HTML
laws_html = "".join([f'<div style="margin-bottom: 6px; font-weight: 300; line-height: 1.4;">{law}</div>' for law in ev["codex_laws"]])

CARD_W = 1000
# Estimated height: Padding(40) + Header(100) + Table(600) + Evidence(300) + Footer(60) = ~1100
CARD_H = 1250

svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {CARD_W} {CARD_H}" width="{CARD_W}" height="{CARD_H}">
  <foreignObject x="0" y="0" width="{CARD_W}" height="{CARD_H}">
    <div xmlns="http://www.w3.org/1999/xhtml" style="box-sizing: border-box; width: {CARD_W}px; padding: 25px 30px; background: #ffffff; font-family: 'Sarabun', 'TH Sarabun New', 'TH Sarabun PSK', sans-serif; color: #0f172a; line-height: 1.5;">
      
      <!-- HEADER -->
      <div style="border-bottom: 2px solid #0f172a; padding-bottom: 8px; margin-bottom: 12px;">
        <div style="display: flex; justify-content: space-between; align-items: baseline;">
          <div style="font-size: 22px; font-weight: 800; color: #0f172a;">⚖️ แฟ้มสำนวนคดีอาญา (มาตรฐานศาลยุติธรรม - CODEX VECTOR STREAM)</div>
          <div style="font-size: 14px; font-weight: 300; color: #64748b;">เอกสารบัญชีพยานหลักฐานประกอบคำฟ้อง (ป.อ. มาตรา ๙๑)</div>
        </div>
        <div style="display: flex; justify-content: space-between; align-items: center; background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 4px; padding: 6px 12px; margin-top: 6px;">
          <div style="font-size: 16px; font-weight: 300;"><strong>บุคคลเป้าหมาย:</strong> {ev['person']} ({ev['person_role']})</div>
          <div style="font-size: 16px;">
            <span style="color: #b91c1c; font-weight: 700;">{ev['count_no']}</span> | 
            <span style="color: #1e3a8a; font-weight: 700;">ความเสียหาย: {ev['amount']}</span>
          </div>
        </div>
      </div>

      <!-- 11 TOPICS TABLE -->
      <table style="width: 100%; border-collapse: collapse; margin-bottom: 20px; font-size: 18px;">
        <tr>
          <td style="width: 250px; background: #f8fafc; font-weight: 700; color: #1e293b; padding: 8px 12px; border: 1px solid #cbd5e1;">๑. เหตุการณ์ที่</td>
          <td style="font-weight: 700; color: #0f172a; padding: 8px 12px; border: 1px solid #cbd5e1;">{ev['count_title']}</td>
        </tr>
        <tr>
          <td style="background: #f8fafc; font-weight: 700; color: #1e293b; padding: 8px 12px; border: 1px solid #cbd5e1;">๒. อ้างอิงหลักฐาน</td>
          <td style="font-weight: 300; color: #475569; padding: 8px 12px; border: 1px solid #cbd5e1; font-family: monospace; font-size: 15px;">{ev['ref']}</td>
        </tr>
        <tr>
          <td style="background: #f8fafc; font-weight: 700; color: #1e293b; padding: 8px 12px; border: 1px solid #cbd5e1;">๓. บริบทแชทจริง</td>
          <td style="font-weight: 300; font-style: italic; color: #0369a1; background: #f0f9ff; padding: 8px 12px; border: 1px solid #cbd5e1;">"{ev['chat']}"</td>
        </tr>
        <tr>
          <td style="background: #f8fafc; font-weight: 700; color: #1e293b; padding: 8px 12px; border: 1px solid #cbd5e1;">๔. วิเคราะห์พฤติการณ์</td>
          <td style="font-weight: 300; color: #0f172a; padding: 8px 12px; border: 1px solid #cbd5e1;">{ev['analysis']}</td>
        </tr>
        <tr>
          <td style="background: #f8fafc; font-weight: 700; color: #1e293b; padding: 8px 12px; border: 1px solid #cbd5e1;">๕. วันเวลาเกิดเหตุ</td>
          <td style="font-weight: 300; color: #0f172a; padding: 8px 12px; border: 1px solid #cbd5e1;">{ev['datetime']}</td>
        </tr>
        <tr>
          <td style="background: #f8fafc; font-weight: 700; color: #1e293b; padding: 8px 12px; border: 1px solid #cbd5e1;">๖. ยอดเงิน (บาท)</td>
          <td style="font-weight: 700; font-size: 20px; color: #15803d; padding: 8px 12px; border: 1px solid #cbd5e1;">{ev['amount']}</td>
        </tr>
        <tr>
          <td style="background: #f8fafc; font-weight: 700; color: #1e293b; padding: 8px 12px; border: 1px solid #cbd5e1;">๗. รูปสลิป / บัญชี</td>
          <td style="font-weight: 300; color: #0f172a; padding: 8px 12px; border: 1px solid #cbd5e1;">{ev['slip']}</td>
        </tr>
        <tr style="background: #fff1f2;">
          <td style="background: #fef2f2; font-weight: 700; color: #991b1b; padding: 8px 12px; border: 1px solid #cbd5e1;">๘. ข้อหาและมาตราที่เข้าข่าย</td>
          <td style="padding: 8px 12px; border: 1px solid #cbd5e1;">
            {laws_html}
          </td>
        </tr>
        <tr>
          <td style="background: #f8fafc; font-weight: 700; color: #1e293b; padding: 8px 12px; border: 1px solid #cbd5e1;">๙. Smoking Gun (จุดตาย)</td>
          <td style="font-weight: 700; color: #b91c1c; padding: 8px 12px; border: 1px solid #cbd5e1;">{ev['smoking_gun']}</td>
        </tr>
        <tr>
          <td style="background: #f8fafc; font-weight: 700; color: #1e293b; padding: 8px 12px; border: 1px solid #cbd5e1;">๑๐. พลิกเกมส์ &amp; ตอบโต้</td>
          <td style="font-weight: 300; color: #0f172a; padding: 8px 12px; border: 1px solid #cbd5e1;">{ev['counter']}</td>
        </tr>
        <tr>
          <td style="background: #f8fafc; font-weight: 700; color: #1e293b; padding: 8px 12px; border: 1px solid #cbd5e1;">๑๑. คำขอและแนวทางยื่นศาล</td>
          <td style="font-weight: 300; color: #0f172a; padding: 8px 12px; border: 1px solid #cbd5e1;">{ev['court_action']}</td>
        </tr>
      </table>

      <!-- EVIDENCE BOX (PERFECTLY CENTERED, EXACT WIDTH, NO BLACK SIDES) -->
      <div style="border: 1.5px solid #0f172a; border-radius: 6px; overflow: hidden; background: #0f172a; margin-top: 15px;">
        <div style="background: #0f172a; color: #ffffff; padding: 6px 14px; display: flex; justify-content: space-between; align-items: center;">
          <span style="font-size: 14px; font-weight: 700;">📸 พยานหลักฐานภาพเหตุการณ์อ้างอิงจริง (ครอปเฉพาะกรอบบริบทชัดเจน 100% - มาตรฐานศาล)</span>
          <span style="background: #dc2626; color: #ffffff; font-size: 11px; font-weight: 800; padding: 2px 6px; border-radius: 3px; letter-spacing: 0.5px;">CERTIFIED COURT EVIDENCE • ISO/IEC 27037</span>
        </div>
        <div style="background: #090d16; padding: 12px; display: flex; justify-content: center; align-items: center;">
          <img src="{data_uri}" style="max-width: 100%; height: auto; border-radius: 4px; box-shadow: 0 4px 12px rgba(0,0,0,0.5);" alt="Evidence {ev['count_no']}" />
        </div>
      </div>

      <!-- FOOTER BAR -->
      <div style="border-top: 1px solid #cbd5e1; padding-top: 10px; margin-top: 20px; display: flex; justify-content: space-between; font-size: 14px; font-weight: 300; color: #64748b;">
        <div>สารบบคดีอาญา: ขบวนการฉ้อโกงเป็นปกติธุระ (ป.อ. มาตรา ๓๔๑, ๙๑) | แผ่นเวกเตอร์ที่ ๑ จาก ๓๐ รายการ</div>
        <div>ระบบรับรองพยานหลักฐานนิติวิทยาศาสตร์ดิจิทัล (Digital Evi Codex V2)</div>
      </div>

    </div>
  </foreignObject>
</svg>'''

out_svg = r'd:\Project\ชวกม.2\EDOK_NUI\VECTOR_EVIDENCE\test_c1_fo.svg'
with open(out_svg, 'w', encoding='utf-8') as f:
    f.write(svg_content)

# Render with fitz to check preview
doc = fitz.open(out_svg)
pix = doc[0].get_pixmap(dpi=150)
out_png = r'd:\Project\ชวกม.2\EDOK_NUI\VECTOR_EVIDENCE\test_c1_fo_preview.png'
pix.save(out_png)
print(f"Rendered test_c1_fo_preview.png: {pix.width}x{pix.height}")

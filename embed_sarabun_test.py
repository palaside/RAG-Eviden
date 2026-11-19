# -*- coding: utf-8 -*-
import os
import base64
import fitz

ttf_reg = r'C:\Users\EVE\AppData\Local\Microsoft\Windows\Fonts\THSarabun.ttf'
ttf_bold = r'C:\Users\EVE\AppData\Local\Microsoft\Windows\Fonts\THSarabun Bold.ttf'

with open(ttf_reg, 'rb') as f:
    b64_reg = base64.b64encode(f.read()).decode('ascii')
with open(ttf_bold, 'rb') as f:
    b64_bold = base64.b64encode(f.read()).decode('ascii')

svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 200" width="800" height="200">
  <defs>
    <style>
      @font-face {{
        font-family: 'TH Sarabun PSK';
        src: url('data:font/truetype;charset=utf-8;base64,{b64_reg}') format('truetype');
        font-weight: 400;
        font-style: normal;
      }}
      @font-face {{
        font-family: 'TH Sarabun PSK';
        src: url('data:font/truetype;charset=utf-8;base64,{b64_bold}') format('truetype');
        font-weight: 700;
        font-style: normal;
      }}
      @font-face {{
        font-family: 'THSarabunPSK';
        src: url('data:font/truetype;charset=utf-8;base64,{b64_reg}') format('truetype');
        font-weight: 400;
        font-style: normal;
      }}
      @font-face {{
        font-family: 'THSarabunPSK';
        src: url('data:font/truetype;charset=utf-8;base64,{b64_bold}') format('truetype');
        font-weight: 700;
        font-style: normal;
      }}
    </style>
  </defs>
  <rect width="800" height="200" fill="#ffffff"/>
  <text x="20" y="60" font-family="'TH Sarabun PSK', 'THSarabunPSK'" font-size="28px" font-weight="700" fill="#000000">ทดสอบฟอนต์ TH Sarabun PSK ตัวหนา (Court Standard 100%)</text>
  <text x="20" y="110" font-family="'TH Sarabun PSK', 'THSarabunPSK'" font-size="20px" font-weight="400" fill="#333333">ทดสอบฟอนต์ TH Sarabun PSK ตัวปกติ ๑๒๓๔๕๖๗๘๙๐ ขอยืมเงิน 2,000 บาท ค่าครีมและแฟนอับสัญญาณ</text>
</svg>'''

with open('test_sarabun.svg', 'w', encoding='utf-8') as f:
    f.write(svg_content)

doc = fitz.open('test_sarabun.svg')
page = doc[0]
pix = page.get_pixmap(dpi=150)
pix.save(r'C:\Users\EVE\.gemini\antigravity\brain\c8211d09-030e-4b24-8837-3ce9589aa4a6\test_sarabun_render.png')
print('test_sarabun_render.png generated successfully!')

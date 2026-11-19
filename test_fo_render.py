# -*- coding: utf-8 -*-
import fitz

svg_test = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 800" width="1000" height="800">
  <foreignObject x="0" y="0" width="1000" height="800">
    <div xmlns="http://www.w3.org/1999/xhtml" style="font-family: 'Sarabun', sans-serif; font-size: 18px; font-weight: 300; padding: 20px; background: #ffffff;">
      <h2 style="font-weight: 700; margin: 0 0 15px 0;">ทดสอบหัวข้อตัวหนา TH Sarabun 18</h2>
      <table style="width: 100%; border-collapse: collapse; border: 1px solid #cbd5e1;">
        <tr>
          <td style="border: 1px solid #cbd5e1; padding: 8px 12px; font-weight: 700; width: 250px; background: #f1f5f9;">๑. เหตุการณ์ที่</td>
          <td style="border: 1px solid #cbd5e1; padding: 8px 12px; font-weight: 300;">กรรมที่ ๑ (ขอยืมเงิน 2,000 บาท)</td>
        </tr>
      </table>
    </div>
  </foreignObject>
</svg>'''

with open(r'd:\Project\ชวกม.2\test_fo.svg', 'w', encoding='utf-8') as f:
    f.write(svg_test)

try:
    doc = fitz.open(r'd:\Project\ชวกม.2\test_fo.svg')
    pix = doc[0].get_pixmap()
    pix.save(r'd:\Project\ชวกม.2\test_fo.png')
    print("PyMuPDF successfully rendered foreignObject SVG!")
except Exception as e:
    print("PyMuPDF note:", e)

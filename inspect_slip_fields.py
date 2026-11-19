# -*- coding: utf-8 -*-
import os
import re
from PIL import Image
import pytesseract

slip_dir = r'C:\Users\EVE\Downloads\ของมันคนเดียว-20261117T094313Z-1-003\ของมันคนเดียว\สนทนาแนบสลิป'
files = sorted([f for f in os.listdir(slip_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg'))])

print(f"Total files in สนทนาแนบสลิป: {len(files)}")

def inspect_slip(fp):
    with Image.open(fp) as im:
        txt = pytesseract.image_to_string(im, lang='tha+eng')
        return txt

samples = [0, 5, 10, 15, 20, 25, 30, 40, 50, 60]
for idx in samples:
    if idx < len(files):
        fn = files[idx]
        fp = os.path.join(slip_dir, fn)
        txt = inspect_slip(fp)
        print("="*60)
        print(f"FILE #{idx}: {fn}")
        for l in txt.splitlines():
            if any(k in l for k in ['โอน', 'สำเร็จ', 'อ้างอิง', 'บาท', 'ไปยัง', 'จาก', 'XXX', 'นาย', 'นาง', 'น.ส.', 'จิณห์', 'ธนาคาร', 'กรุง', 'กสิกร', 'ไทยพาณิชย์', 'พร้อมเพย์', 'บันทึก', 'Ref', 'date', '2568', '2025']):
                print("  MATCH:", l.strip())

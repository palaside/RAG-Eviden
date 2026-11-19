# -*- coding: utf-8 -*-
import os
import re
from PIL import Image
import pytesseract

slip_dir = r'C:\Users\EVE\Downloads\ของมันคนเดียว-20261117T094313Z-1-003\ของมันคนเดียว\สนทนาแนบสลิป'
files = [f for f in os.listdir(slip_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg'))][:10]

print("Testing slip OCR on 5 sample files...")

for fn in files[:5]:
    fp = os.path.join(slip_dir, fn)
    with Image.open(fp) as im:
        txt = pytesseract.image_to_string(im, lang='tha+eng')
        print("="*50)
        print("FILE:", fn)
        print("--- EXTRACTED TEXT ---")
        lines = [l.strip() for l in txt.splitlines() if l.strip()]
        for l in lines[:15]:
            print("  ", l)

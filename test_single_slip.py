# -*- coding: utf-8 -*-
import os
import re
from PIL import Image
import pytesseract

fp = r'C:\Users\EVE\Downloads\ของมันคนเดียว-20261117T094313Z-1-003\ของมันคนเดียว\สนทนาแนบสลิป\03.2.68_IMG_6085.PNG'
im = Image.open(fp)

# Let's inspect the full OCR output line by line
txt = pytesseract.image_to_string(im, lang='tha+eng')
lines = [l.strip() for l in txt.splitlines() if l.strip()]

print("FULL OCR LINES:")
for i, l in enumerate(lines):
    print(f"[{i:02d}] {l}")

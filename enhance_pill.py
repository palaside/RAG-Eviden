# -*- coding: utf-8 -*-
from PIL import Image, ImageOps, ImageEnhance
import pytesseract

im = Image.open('detected_pill_node001.png')
gray = im.convert('L')
inv = ImageOps.invert(gray)
enhancer = ImageEnhance.Contrast(inv)
contrasted = enhancer.enhance(3.0)
scaled = contrasted.resize((contrasted.width * 3, contrasted.height * 3), Image.Resampling.LANCZOS)
scaled.save('detected_pill_node001_prep.png')

txt = pytesseract.image_to_string(scaled, lang='tha+eng', config='--psm 7')
print("Enhanced Pill OCR:", txt.strip())

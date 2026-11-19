# -*- coding: utf-8 -*-
import pytesseract
from PIL import Image
import re

im = Image.open('EDOK_NUI/SSOT_STREAM_ASSETS/node_001.jpg')
# Crop top 400px to see the date pill
top_crop = im.crop((0, 0, im.width, min(400, im.height)))
txt = pytesseract.image_to_string(top_crop, lang='tha+eng')
print("Top crop OCR text:")
print(txt)

# Test with PSM 6 or 11
txt_psm6 = pytesseract.image_to_string(top_crop, lang='tha+eng', config='--psm 6')
print("Top crop PSM 6:")
print(txt_psm6)

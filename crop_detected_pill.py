# -*- coding: utf-8 -*-
from PIL import Image
import pytesseract

im = Image.open('EDOK_NUI/SSOT_STREAM_ASSETS/node_001.jpg')
# Crop around (427, 113)
crop_pill = im.crop((427, 113, 427 + 181, 113 + 42))
crop_pill.save('detected_pill_node001.png')

txt = pytesseract.image_to_string(crop_pill, lang='tha+eng', config='--psm 7')
print("Pill OCR from node_001.jpg:", txt.strip())

# -*- coding: utf-8 -*-
import pytesseract
from PIL import Image
import os

img_path = 'EDOK_NUI/SSOT_STREAM_ASSETS/node_001.jpg'
if os.path.exists(img_path):
    im = Image.open(img_path)
    print("Image loaded:", im.size)
    try:
        txt = pytesseract.image_to_string(im, lang='tha+eng')
        print("Tesseract Thai+Eng success!")
        print("Text snippet:", txt[:300])
    except Exception as e:
        print("Error with tha+eng:", e)
        txt = pytesseract.image_to_string(im, lang='eng')
        print("Eng OCR:", txt[:300])

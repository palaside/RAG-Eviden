# -*- coding: utf-8 -*-
import pytesseract
from PIL import Image, ImageEnhance, ImageOps

media_p = r'C:/Users/EVE/.gemini/antigravity/brain/c8211d09-030e-4b24-8837-3ce9589aa4a6/.user_uploaded/media_1795035913928_3189cf63.png'
im = Image.open(media_p)
print("Pill image size:", im.size)

gray = im.convert('L')
inv = ImageOps.invert(gray)
enhancer = ImageEnhance.Contrast(inv)
contrasted = enhancer.enhance(3.0)
scaled = contrasted.resize((contrasted.width * 3, contrasted.height * 3), Image.Resampling.LANCZOS)
scaled.save('test_pill_prep2.png')

txt = pytesseract.image_to_string(scaled, lang='tha+eng', config='--psm 7')
print("Processed Pill 2 OCR:", txt.strip())

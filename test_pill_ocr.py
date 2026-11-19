# -*- coding: utf-8 -*-
import pytesseract
from PIL import Image, ImageEnhance, ImageOps

media_p = r'C:/Users/EVE/.gemini/antigravity/brain/c8211d09-030e-4b24-8837-3ce9589aa4a6/.user_uploaded/media_1795036777323_42d3d722.png'
im = Image.open(media_p)

# Preprocessing: convert to grayscale, invert (white text on dark -> dark text on white), enhance contrast
gray = im.convert('L')
inv = ImageOps.invert(gray)
enhancer = ImageEnhance.Contrast(inv)
contrasted = enhancer.enhance(2.5)

# Scale up 2x
scaled = contrasted.resize((contrasted.width * 2, contrasted.height * 2), Image.Resampling.LANCZOS)
scaled.save('test_pill_prep.png')

txt = pytesseract.image_to_string(scaled, lang='tha+eng', config='--psm 7')
print("Processed Pill OCR:", txt.strip())

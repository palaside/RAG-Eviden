# -*- coding: utf-8 -*-
import os
from PIL import Image
import pytesseract

raw_ori = r'C:\Users\EVE\Downloads\ของมันคนเดียว-20261117T094313Z-1-003\ของมันคนเดียว\แคปหน้า Ori'
raw_root = r'C:\Users\EVE\Downloads\ของมันคนเดียว-20261117T094313Z-1-003\ของมันคนเดียว'

# Let's inspect Count 1 carefully
im1 = Image.open(os.path.join(raw_ori, 'LINE_capture_800252756.687906.jpg'))
# We want to crop from right above "เค้าสั่งครีมไปไง เงินมันขาด2000" to right below "คืนให้"
# Let's test crop y=2300 to y=2730
c1 = im1.crop((0, 2300, 636, 2730))
t1 = pytesseract.image_to_string(c1, lang='tha+eng')
print("=== Count 1 Crop Text ===")
print(t1.strip())

# Also let's inspect Count 1 Part 2 (if needed, or if Count 1 doesn't need Part 2 because Part 1 already has 100% of the crime!)
# Wait! In Count 1, what was Part 2?
# Part 2 was "เค้าได้ก็ค่ำๆ แค่ทักไปยืมมัน ค่ำๆ แล้วครีมเค้าก็ต้องโอนให้เค้าปิดงาน"
# If y=2300 to y=2730 has BOTH the cream 2000 AND the repayment promise, then Count 1 fits completely in ONE single clean crop!

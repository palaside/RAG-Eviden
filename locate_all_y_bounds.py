# -*- coding: utf-8 -*-
import os
import json
from PIL import Image

ori_dir = r'C:\Users\EVE\Downloads\ของมันคนเดียว-20261117T094313Z-1-003\ของมันคนเดียว\แคปหน้า Ori'
root_dir = r'C:\Users\EVE\Downloads\ของมันคนเดียว-20261117T094313Z-1-003\ของมันคนเดียว'

with open(r'd:\Project\ชวกม.2\EDOK_NUI\REAL_IMAGE_OCR_WORDS.json', 'r', encoding='utf-8') as f:
    ocr_data = json.load(f)

# Helper to inspect words around a search term
def inspect_image_words(img_name, search_terms):
    words = ocr_data.get(img_name, {}).get('words', [])
    print(f"=== {img_name} ===")
    matches = []
    for w in words:
        if any(term in w['text'] for term in search_terms):
            matches.append((w['top'], w['left'], w['text']))
    matches.sort(key=lambda x: x[0])
    for top, left, txt in matches:
        print(f"  y={top}, x={left}: {txt}")

print("Checking Counts...")
inspect_image_words('LINE_capture_800252756.687906.jpg', ['ครีม', '2000', '13:54', 'ปิดงาน'])
inspect_image_words('LINE_capture_800252921.297142.jpg', ['3000', '50000', 'ทุ่ม'])
inspect_image_words('LINE_capture_800253182.934029.jpg', ['500', 'ยืม'])
inspect_image_words('LINE_capture_800253185.789705.jpg', ['หอม', 'เหล็ก', '4000', '2000'])
inspect_image_words('LINE_capture_800253252.988857.jpg', ['สองแสน', '90,000', '2000', 'บ่น'])
inspect_image_words('LINE_capture_800253550.895289.jpg', ['7,000', '7000', 'พัทยา', '19:33', '19:36'])
inspect_image_words('LINE_capture_800253553.588898.jpg', ['8000', '3000', '2000', '4100', '2500', '5500', '20000'])
inspect_image_words('LINE_capture_800254134.610661.jpg', ['23,700', '23700', '15000', '15,000', 'แม็ก', '2000'])
inspect_image_words('LINE_capture_800255060.737309.jpg', ['5000', '5,000', '25000', '25,000', '15000', '15,000'])
inspect_image_words('LINE_capture_800256213.882803.jpg', ['35000', '35,000', '5000', '5,000', '6000', '6,000', '4000', '4,000'])

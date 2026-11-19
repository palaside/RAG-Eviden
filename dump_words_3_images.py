# -*- coding: utf-8 -*-
import json

with open(r'd:\Project\ชวกม.2\EDOK_NUI\REAL_IMAGE_OCR_WORDS.json', 'r', encoding='utf-8') as f:
    ocr_data = json.load(f)

for img in ['LINE_capture_800254134.610661.jpg', 'LINE_capture_800255060.737309.jpg', 'LINE_capture_800256213.882803.jpg']:
    words = ocr_data[img]['words']
    print(f"=== {img} (total words {len(words)}) ===")
    for w in words:
        # print words that have length > 2
        if len(w['text']) >= 3:
            print(f"  y={w['top']}, x={w['left']}: {w['text']}")

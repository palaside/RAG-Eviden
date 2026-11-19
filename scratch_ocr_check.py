import json

with open(r'd:\Project\ชวกม.2\EDOK_NUI\REAL_IMAGE_OCR_WORDS.json', 'r', encoding='utf-8') as f:
    ocr_data = json.load(f)

for img in ['LINE_capture_800253550.895289.jpg', 'LINE_capture_800254134.610661.jpg', 'LINE_capture_800255060.737309.jpg', 'LINE_capture_800256213.882803.jpg']:
    words = ocr_data[img]['words']
    print(f'=== {img} ===')
    digits = [w for w in words if any(c.isdigit() for c in w['text'])]
    for w in digits[:20]:
        print(f"  y={w['top']}, x={w['left']}: {w['text']}")

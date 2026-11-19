import json

with open('EDOK_NUI/REAL_IMAGE_OCR_WORDS.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for fn in ['LINE_capture_800253550.895289.jpg', 'LINE_capture_800254134.610661.jpg', 'LINE_capture_800255060.737309.jpg', 'LINE_capture_800256213.882803.jpg']:
    print(f"=== {fn} ===")
    words = data[fn]['words']
    for w in words:
        txt = w['text']
        # print words that contain numbers or thai loan words
        if any(c.isdigit() for c in txt) or any(k in txt for k in ['กู้', 'ยืม', 'โอน', 'พัทยา', 'เคลียร์', 'ด่วน', 'น้อง', 'ขาด', 'ดอก']):
            print(f"  y={w['top']}: {txt}")

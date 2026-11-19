import json

with open('EDOK_NUI/REAL_IMAGE_OCR_WORDS.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for fn, info in data.items():
    print(f"=== {fn} ===")
    words = info['words']
    for w in words:
        txt = w['text']
        if any(k in txt for k in ['2000', '3000', '4000', '500', '5000', '7000', '8000', '1000', '15000', '20000', '25000', '35000', 'ครีม', 'หอม', 'เหล็ก', 'สองแสน', '90,000', 'ว่างงาน', 'แม๊ก', 'สบายใจ']):
            print(f"  y={w['top']}: {txt}")

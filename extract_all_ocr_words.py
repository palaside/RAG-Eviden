import pytesseract
from PIL import Image
import os

dl_root = r'C:\Users\EVE\Downloads\ของมันคนเดียว-20261117T094313Z-1-003\ของมันคนเดียว\แคปหน้า Ori'

image_files = [
    'LINE_capture_800252756.687906.jpg',
    'LINE_capture_800252921.297142.jpg',
    'LINE_capture_800253182.934029.jpg',
    'LINE_capture_800253185.789705.jpg',
    'LINE_capture_800253252.988857.jpg',
    'LINE_capture_800253550.895289.jpg',
    'LINE_capture_800253553.588898.jpg',
    'LINE_capture_800254134.610661.jpg',
    'LINE_capture_800255060.737309.jpg',
    'LINE_capture_800256213.882803.jpg'
]

results = {}

for fn in image_files:
    fp = os.path.join(dl_root, fn)
    im = Image.open(fp)
    data = pytesseract.image_to_data(im, lang='tha+eng', output_type=pytesseract.Output.DICT)
    
    found = []
    for i, t in enumerate(data['text']):
        txt = t.strip()
        if txt:
            found.append({
                'top': data['top'][i],
                'left': data['left'][i],
                'w': data['width'][i],
                'h': data['height'][i],
                'text': txt
            })
    results[fn] = {
        'size': im.size,
        'words': found
    }
    print(f"{fn} ({im.size}): {len(found)} words extracted.")

import json
with open('EDOK_NUI/REAL_IMAGE_OCR_WORDS.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print("Saved OCR coordinates to EDOK_NUI/REAL_IMAGE_OCR_WORDS.json")

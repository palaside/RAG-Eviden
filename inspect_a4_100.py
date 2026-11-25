import cv2
import pytesseract
import json

path = r'D:\Project\Digital Evi - Codex\For Test\Done\A4_IMG_ (100).PNG'
img = cv2.imread(path)
crop = img[990:2400, 660:1820]

data = pytesseract.image_to_data(crop, lang='tha+eng', output_type=pytesseract.Output.DICT)
n_boxes = len(data['text'])
results = []
for i in range(n_boxes):
    txt = data['text'][i].strip()
    if txt:
        results.append({
            'y': data['top'][i],
            'x': data['left'][i],
            'w': data['width'][i],
            'h': data['height'][i],
            'conf': data['conf'][i],
            'text': txt
        })

print(f"Total words found: {len(results)}")
for r in results:
    print(f"y={r['y']:4d}, x={r['x']:4d}, w={r['w']:4d}, h={r['h']:4d}, conf={r['conf']:2d}: {r['text']}")

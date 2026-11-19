import pytesseract
from PIL import Image
import os

dl_root = r'C:\Users\EVE\Downloads\ของมันคนเดียว-20261117T094313Z-1-003\ของมันคนเดียว\แคปหน้า Ori'
img_path = os.path.join(dl_root, 'LINE_capture_800253185.789705.jpg')

# Let's test image_to_data with thai+eng
try:
    data = pytesseract.image_to_data(Image.open(img_path), lang='tha+eng', output_type=pytesseract.Output.DICT)
    print("pytesseract works!")
    matches = []
    for i, w in enumerate(data['text']):
        if 'ถอดเหล็ก' in w or '4000' in w or 'น้ำหอม' in w or 'น้าหอม' in w:
            print(f"Found word: '{w}' at y={data['top'][i]}, h={data['height'][i]}")
            matches.append((w, data['top'][i]))
    print(f"Total words: {len(data['text'])}, matches: {len(matches)}")
except Exception as e:
    print("pytesseract error:", e)

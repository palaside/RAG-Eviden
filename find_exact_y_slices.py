import os
from PIL import Image
import pytesseract

dl_root = r'C:\Users\EVE\Downloads\ของมันคนเดียว-20261117T094313Z-1-003\ของมันคนเดียว\แคปหน้า Ori'

def search_text_y(img_fn, search_terms):
    fp = os.path.join(dl_root, img_fn)
    im = Image.open(fp)
    data = pytesseract.image_to_data(im, lang='tha+eng', output_type=pytesseract.Output.DICT)
    
    matches = []
    for i, t in enumerate(data['text']):
        txt = t.strip()
        if any(term in txt for term in search_terms):
            matches.append((data['top'][i], txt))
    return matches

print("1. LINE_capture_800252756.687906.jpg (ครีม, 2000):")
print(search_text_y('LINE_capture_800252756.687906.jpg', ['2000', 'ครีม', 'ปิดงาน', '13:54']))

print("2. LINE_capture_800252921.297142.jpg (3000, 50000, 1ทุ่ม):")
print(search_text_y('LINE_capture_800252921.297142.jpg', ['3000', '3,000', '50000', '50,000', '1ทุ่ม', 'ทุ่ม']))

print("3. LINE_capture_800253182.934029.jpg (500):")
print(search_text_y('LINE_capture_800253182.934029.jpg', ['500', 'ยืม']))

print("4. LINE_capture_800253185.789705.jpg (2000, น้ำหอม, ถอดเหล็ก, 4000):")
print(search_text_y('LINE_capture_800253185.789705.jpg', ['2000', '4000', 'เหล็ก', 'หอม', 'แก้ว', 'สำนักงาน', 'สํานักงาน']))

print("5. LINE_capture_800253252.988857.jpg (สองแสน, 90,000):")
print(search_text_y('LINE_capture_800253252.988857.jpg', ['2000', 'สองแสน', '90,000', '90000', 'บ่น', 'พี่สาว']))

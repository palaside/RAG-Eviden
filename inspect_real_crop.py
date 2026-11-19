from PIL import Image
import os

dl_root = r'C:\Users\EVE\Downloads\ของมันคนเดียว-20261117T094313Z-1-003\ของมันคนเดียว\แคปหน้า Ori'
img_path = os.path.join(dl_root, 'LINE_capture_800253185.789705.jpg')

im = Image.open(img_path)
print(f"Original size: {im.size}")

# Crop around y=4320
crop1 = im.crop((0, 4100, im.width, 4650))
out_test = r'd:\Project\ชวกม.2\EDOK_NUI\crop_test_thod_lek.png'
crop1.save(out_test)
print(f"Saved test crop: {crop1.size}")

# Also let's check what words are in data between y=2000 and y=5000
import pytesseract
data = pytesseract.image_to_data(im, lang='tha+eng', output_type=pytesseract.Output.DICT)

lines = []
for i, txt in enumerate(data['text']):
    t = txt.strip()
    if t:
        lines.append((data['top'][i], data['left'][i], t))

lines.sort(key=lambda x: x[0])
print(f"Total non-empty text boxes: {len(lines)}")
for top, left, txt in lines:
    if any(k in txt for k in ['2000', '4000', 'หอม', 'แก้ว', 'ร้าน', 'วาง']):
        print(f"  y={top}, x={left}: {txt}")

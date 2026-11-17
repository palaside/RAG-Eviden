import pytesseract
from PIL import Image

img_path = r'C:\Users\EVE\Downloads\ของมันคนเดียว-20261117T094313Z-1-003\ของมันคนเดียว\แคปหน้า Ori\LINE_capture_800256213.882803.jpg'
im = Image.open(img_path)
data = pytesseract.image_to_data(im, lang='tha+eng', output_type=pytesseract.Output.DICT)

for i in range(len(data['text'])):
    txt = data['text'][i].strip()
    if any(k in txt for k in ['ประสาก', 'เขตร', 'วันวิศา', 'แม่', 'ทัศ']):
        x, y, w, h = data['left'][i], data['top'][i], data['width'][i], data['height'][i]
        print(f'Match: "{txt}" at box ({x}, {y}, {w}, {h})')
        crop_box = (0, max(0, y - 60), im.width, min(im.height, y + h + 80))
        crop_im = im.crop(crop_box)
        crop_path = f'D:/Project/ชวกม.2/EDOK_NUI/crop_target_{i}.png'
        crop_im.save(crop_path)
        print('Saved box crop to:', crop_path)

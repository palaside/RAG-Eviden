import pytesseract
from PIL import Image

im = Image.open(r'C:\Users\EVE\Downloads\ของมันคนเดียว-20261117T094313Z-1-003\ของมันคนเดียว\แคปหน้า Ori\LINE_capture_800252756.687906.jpg')
data = pytesseract.image_to_data(im, lang='tha+eng', output_type=pytesseract.Output.DICT)

for i in range(len(data['text'])):
    t = data['text'][i].strip()
    if any(k in t for k in ['2000', 'ครีม', 'น้อยใจ', 'เค้าสั่ง']):
        top = data['top'][i]
        h = data['height'][i]
        left = data['left'][i]
        w = data['width'][i]
        print(f"{t}: top={top}, bottom={top+h}, left={left}, w={w}")

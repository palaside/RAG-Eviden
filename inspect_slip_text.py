import pytesseract
from PIL import Image
import os

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
os.environ["TESSDATA_PREFIX"] = r"D:\Models\tessdata"

BASE_DIR = r"C:\Users\EVE\Downloads\ของมันคนเดียว-20261117T094313Z-1-003\ของมันคนเดียว"

for f in ["IMG_0481.JPG", "IMG_0497.JPG"]:
    im = Image.open(os.path.join(BASE_DIR, f))
    txt = pytesseract.image_to_string(im, lang="tha+eng")
    print(f"=== {f} ===")
    print(txt)

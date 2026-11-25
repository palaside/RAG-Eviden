import os
import pytesseract
from PIL import Image

tessdata_dir = r"D:\Project\Digital Evi - Codex"
os.environ["TESSDATA_PREFIX"] = tessdata_dir
rec_crop = Image.open(r"C:\Users\EVE\AppData\Local\Temp\receiver_exact.png")

for psm in [6, 7, 8, 11]:
    try:
        txt = pytesseract.image_to_string(rec_crop, lang="tha+eng", config=f'--tessdata-dir "{tessdata_dir}" --psm {psm}').strip()
        print(f"PSM {psm}: {txt}")
    except Exception as e:
        print(f"PSM {psm} error: {e}")

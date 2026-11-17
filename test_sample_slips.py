import os
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
os.environ["TESSDATA_PREFIX"] = r"D:\Models\tessdata"

BASE_DIR = r"C:\Users\EVE\Downloads\ของมันคนเดียว-20261117T094313Z-1-003\ของมันคนเดียว"

# Test 5 images from root and 5 from 'สนทนาแนบสลิป'
test_samples = []
for f in os.listdir(BASE_DIR):
    if f.lower().endswith(('.jpg', '.png')) and os.path.isfile(os.path.join(BASE_DIR, f)):
        test_samples.append(os.path.join(BASE_DIR, f))
        if len(test_samples) >= 5:
            break

slip_folder = os.path.join(BASE_DIR, "สนทนาแนบสลิป")
if os.path.exists(slip_folder):
    for f in os.listdir(slip_folder):
        if f.lower().endswith(('.jpg', '.png')):
            test_samples.append(os.path.join(slip_folder, f))
            if len(test_samples) >= 10:
                break

print(f"Testing {len(test_samples)} sample images for slip content...")

for p in test_samples:
    try:
        im = Image.open(p)
        text = pytesseract.image_to_string(im, lang="tha+eng", config="--psm 6")
        # Check if text contains typical slip keywords
        is_slip = any(kw in text for kw in ["โอนเงินสำเร็จ", "จำนวนเงิน", "จาก", "ไปยัง", "ไปยังบัญชี", "ธนาคาร", "กรุงไทย", "กสิกร", "ไทยพาณิชย์", "พร้อมเพย์", "Ref", "เลขที่รายการ"])
        print(f"\nFile: {os.path.basename(p)} ({im.size}) -> Is Slip: {is_slip}")
        # Print snippet
        lines = [l.strip() for l in text.split("\n") if l.strip()]
        for l in lines[:6]:
            print(f"   | {l}")
    except Exception as e:
        print(f"Error reading {p}: {e}")

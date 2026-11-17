import os
import re
import pytesseract
from PIL import Image
from concurrent.futures import ThreadPoolExecutor

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
os.environ["TESSDATA_PREFIX"] = r"D:\Models\tessdata"

BASE_DIR = r"C:\Users\EVE\Downloads\ของมันคนเดียว-20261117T094313Z-1-003\ของมันคนเดียว"
files = [os.path.join(BASE_DIR, f) for f in os.listdir(BASE_DIR) if f.upper().startswith("IMG_") and f.lower().endswith(('.jpg', '.png', '.jpeg'))]

print(f"Total root IMG_ files: {len(files)}")

def process_file(fpath):
    fname = os.path.basename(fpath)
    try:
        im = Image.open(fpath)
        # Resize if huge
        if im.width > 1200 or im.height > 1600:
            im.thumbnail((1200, 1600), Image.Resampling.LANCZOS)
        text = pytesseract.image_to_string(im, lang="tha+eng", config="--psm 6")
        
        # Check if slip
        is_transfer = any(w in text for w in ["โอนเงินสำเร็จ", "จ่ายบิลสำเร็จ", "จำนวนเงิน", "รหัสอ้างอิง", "Ref."])
        
        # Find amounts
        amounts = re.findall(r"(\d{1,3}(?:,\d{3})*\.\d{2})", text)
        
        # Find banks
        banks = []
        for b in ["กรุงไทย", "กสิกรไทย", "ไทยพาณิชย์", "ทหารไทยธนชาต", "พร้อมเพย์", "ออมสิน", "กรุงศรี", "ttb", "SCB", "KBANK", "KTB"]:
            if b in text:
                banks.append(b)
                
        # Find recipient
        # Usually lines after 'ไปยัง' or 'เข้าบัญชี' or names like 'น.ส.', 'นาง', 'นาย', 'จิณห์นิภา'
        lines = [l.strip() for l in text.split("\n") if l.strip()]
        
        to_name = None
        for i, l in enumerate(lines):
            if any(k in l for k in ["ไปยัง", "ผู้รับเงิน", "เข้าบัญชี", "To"]):
                if i + 1 < len(lines):
                    to_name = lines[i+1]
                elif i + 2 < len(lines):
                    to_name = lines[i+2]
                break
                
        # Also look for 'จิณห์นิภา'
        jinnipha_match = any("จิณห์" in l or "จิณ" in l or "นิภา" in l for l in lines)
        
        return {
            "file": fname,
            "is_transfer": is_transfer,
            "banks": list(set(banks)),
            "amounts": amounts,
            "to_name": to_name,
            "has_jinnipha": jinnipha_match,
            "raw_text": text[:300]
        }
    except Exception as e:
        return {"file": fname, "error": str(e)}

# Process first 30 files as a fast batch
with ThreadPoolExecutor(max_workers=6) as executor:
    results = list(executor.map(process_file, files[:30]))

slips = [r for r in results if r.get("is_transfer", False)]
print(f"Scanned 30 files, found {len(slips)} transfer slips.\n")

for s in slips[:10]:
    print(f"File: {s['file']}")
    print(f"  Banks: {s['banks']}, Amounts: {s['amounts']}, Has Jinnipha: {s['has_jinnipha']}")
    print(f"  To Candidate: {s['to_name']}")
    print("-" * 50)

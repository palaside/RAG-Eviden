import os
import re
import json
import pytesseract
from PIL import Image
from concurrent.futures import ThreadPoolExecutor

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
os.environ["TESSDATA_PREFIX"] = r"D:\Models\tessdata"

BASE_DIR = r"C:\Users\EVE\Downloads\ของมันคนเดียว-20261117T094313Z-1-003\ของมันคนเดียว"
files = [os.path.join(BASE_DIR, f) for f in os.listdir(BASE_DIR) if f.upper().startswith("IMG_") and f.lower().endswith(('.jpg', '.png', '.jpeg'))]

print(f"Total root slip files to scan: {len(files)}")

def parse_slip_ocr(fpath):
    fname = os.path.basename(fpath)
    try:
        im = Image.open(fpath)
        if im.width > 1200 or im.height > 1600:
            im.thumbnail((1200, 1600), Image.Resampling.LANCZOS)
        text = pytesseract.image_to_string(im, lang="tha+eng")
        
        # Check if transfer slip
        if not any(w in text for w in ["โอนเงินสําเร็จ", "โอนเงินสำเร็จ", "จ่ายบิลสําเร็จ", "จ่ายบิลสำเร็จ", "รหัสอ้างอิง", "Ref"]):
            return None
            
        lines = [l.strip() for l in text.split("\n") if l.strip()]
        
        # Extract Date / Time
        date_time = None
        for l in lines:
            if any(m in l for m in ["ม.ค.", "ก.พ.", "มี.ค.", "เม.ย.", "พ.ค.", "มิ.ย.", "ก.ค.", "ส.ค.", "ก.ย.", "ต.ค.", "พ.ย.", "ธ.ค."]):
                if any(c.isdigit() for c in l):
                    date_time = l
                    break
                    
        # Extract Amount
        amount = None
        amt_matches = re.findall(r"(\d{1,3}(?:,\d{3})*\.\d{2})", text)
        for a in amt_matches:
            if a != "0.00":
                amount = a
                break
                
        # Extract Reference ID
        ref_id = None
        for l in lines:
            m = re.search(r"(?:รหัสอ้างอิง|Ref|Reference)[:\s]*([A-Za-z0-9]+)", l, re.IGNORECASE)
            if m:
                ref_id = m.group(1)
                break
                
        # Extract Accounts & Banks & Names
        # Thai slips list Payer first, then Recipient
        # E.g.
        # [Payer Name]
        # [Payer Acc]
        # [Payer Bank]
        # [Recipient Name]
        # [Recipient Acc]
        # [Recipient Bank]
        
        # Look for accounts (e.g. xxx-x-xx558-9 or 123-4-56789-0)
        acc_matches = re.findall(r"([xX\d]{3,4}[-\s]?[xX\d]{1,2}[-\s]?[xX\d]{4,6}[-\s]?[\dxX])", text)
        
        # Recipient Name candidate
        # Look for names with นาย, นาง, น.ส., หรือ น.ส. จิณห์นิภา
        names = []
        for l in lines:
            # Clean noise
            if any(title in l for title in ["นาย ", "นาง ", "น.ส. ", "น.ส.", "นางสาว ", "จิณห์นิภา", "จิณนิภา"]):
                # exclude payer if it's Natthachai
                if not any(n in l for n in ["ณัฐชัย", "รักษาวงษ์"]):
                    names.append(l)
                    
        recipient_name = names[0] if names else None
        
        # Fallback recipient detection if name has no title
        if not recipient_name:
            for i, l in enumerate(lines):
                if any(w in l for w in ["ไปยัง", "เข้าบัญชี", "ผู้รับ"]):
                    if i + 1 < len(lines):
                        candidate = lines[i+1]
                        if not any(k in candidate for k in ["ธนาคาร", "xxx", "XXX", "บาท", "ค่าธรรมเนียม"]):
                            recipient_name = candidate
                    break
                    
        # Destination Bank
        dest_bank = None
        bank_keywords = [
            ("ttb", "ttb (ทหารไทยธนชาต)"),
            ("ทหารไทย", "ttb (ทหารไทยธนชาต)"),
            ("กรุงไทย", "ธนาคารกรุงไทย (KTB)"),
            ("KTB", "ธนาคารกรุงไทย (KTB)"),
            ("กสิกร", "ธนาคารกสิกรไทย (KBANK)"),
            ("KBANK", "ธนาคารกสิกรไทย (KBANK)"),
            ("ไทยพาณิชย์", "ธนาคารไทยพาณิชย์ (SCB)"),
            ("SCB", "ธนาคารไทยพาณิชย์ (SCB)"),
            ("กรุงเทพ", "ธนาคารกรุงเทพ (BBL)"),
            ("BBL", "ธนาคารกรุงเทพ (BBL)"),
            ("พร้อมเพย์", "พร้อมเพย์ (PromptPay)"),
            ("ออมสิน", "ธนาคารออมสิน (GSB)"),
            ("กรุงศรี", "ธนาคารกรุงศรีอยุธยา (BAY)")
        ]
        
        # Check which banks appear after recipient name or in text
        matched_banks = []
        for kw, full_b in bank_keywords:
            if kw in text:
                matched_banks.append(full_b)
                
        recipient_acc = acc_matches[-1] if len(acc_matches) >= 2 else (acc_matches[0] if acc_matches else None)
        
        return {
            "file": fname,
            "date_time": date_time,
            "amount": amount,
            "recipient_name": recipient_name,
            "recipient_account": recipient_acc,
            "banks": list(set(matched_banks)),
            "ref_id": ref_id,
            "raw_snippet": "\n".join(lines[:12])
        }
    except Exception as e:
        return None

print("Scanning all 288 files with 8 threads...")
with ThreadPoolExecutor(max_workers=8) as executor:
    all_results = list(executor.map(parse_slip_ocr, files))

slips = [r for r in all_results if r is not None]
print(f"\nScan completed! Found {len(slips)} valid transaction slips out of 288 files.")

# Save raw slip json
with open(r"d:\Project\ชวกม.2\all_scanned_slips.json", "w", encoding="utf-8") as f:
    json.dump(slips, f, ensure_ascii=False, indent=2)

# Group by recipient name / account
recipients_map = {}
for s in slips:
    name = s["recipient_name"] or "ไม่ระบุชื่อชัดเจน (ตรวจจับตามเลขบัญชี)"
    # Standardize Jinnipha
    if any(k in name for k in ["จิณห์นิภา", "จิณนิภา", "ประสาทเขตรการ", "จิณ"]):
        key = "น.ส. จิณห์นิภา ประสาทเขตรการ"
    else:
        key = name
        
    if key not in recipients_map:
        recipients_map[key] = {
            "name": key,
            "accounts": set(),
            "banks": set(),
            "transactions": [],
            "total_amount": 0.0,
            "files": []
        }
        
    if s["recipient_account"]:
        recipients_map[key]["accounts"].add(s["recipient_account"])
    for b in s["banks"]:
        recipients_map[key]["banks"].add(b)
        
    amt_val = 0.0
    if s["amount"]:
        try:
            amt_val = float(s["amount"].replace(",", ""))
            recipients_map[key]["total_amount"] += amt_val
        except Exception:
            pass
            
    recipients_map[key]["transactions"].append({
        "file": s["file"],
        "date_time": s["date_time"],
        "amount": s["amount"],
        "ref_id": s["ref_id"]
    })
    recipients_map[key]["files"].append(s["file"])

print(f"\n--- RECIPIENT NETWORK ANALYSIS ({len(recipients_map)} distinct beneficiaries detected) ---")
for r_name, data in recipients_map.items():
    print(f"\n👤 ผู้รับโอน: {r_name}")
    print(f"   จำนวนรายการโอน: {len(data['transactions'])} ครั้ง")
    print(f"   ยอดเงินรวม: {data['total_amount']:,.2f} บาท")
    print(f"   เลขที่บัญชี: {list(data['accounts'])}")
    print(f"   ธนาคาร: {list(data['banks'])}")
    print(f"   ตัวอย่างไฟล์: {data['files'][:3]}")

import json
import re

with open('new_folders_evidence.json', 'r', encoding='utf-8') as f:
    nfe = json.load(f)

print(f"Loaded {len(nfe)} items from new_folders_evidence.json")

results = []
for i, item in enumerate(nfe):
    fn = item['file']
    txt = item['snippet']
    
    # Amount detection
    # Common format in slips: 3,000.00 or 2,000.00
    amounts = re.findall(r'(\d{1,3}(?:,\d{3})*\.\d{2})', txt)
    # Filter out fee 0.00
    valid_amounts = [a for a in amounts if a != '0.00']
    
    # Date detection
    date_matches = re.findall(r'(\d{1,2}\s*(?:ม\.ค\.|ก\.พ\.|มี\.ค\.|เม\.ย\.|พ\.ค\.|มิ\.ย\.|ก\.ค\.|ส\.ค\.|ก\.ย\.|ต\.ค\.|พ\.ย\.|ธ\.ค\.|กย|ตค|พย|ธค|มค|กพ)\s*\.?\s*\d{2,4}(?:,\s*\d{1,2}:\d{2}\s*น\.)?)', txt)
    
    # Also look at folder date in filename (e.g. 01.9.68_IMG_6288.PNG)
    fn_date = re.search(r'(\d{2}\.\d{1,2}\.\d{2})', fn)
    date_str = date_matches[0] if date_matches else (fn_date.group(1) if fn_date else "ไม่ระบุ")

    # Recipient detection
    recipient = "ไม่ระบุ"
    if "จิณห์นิภา" in txt or "จินห์นิภา" in txt or "996-5" in txt:
        recipient = "น.ส. จิณห์นิภา ประสาทเขตต์การ"
    elif "ปรียาฉัตร" in txt or "ชิมพลี" in txt:
        recipient = "น.ส. ปรียาฉัตร ชิมพลี (พี่แมว)"
    elif "วรรณวิสา" in txt:
        recipient = "น.ส. วรรณวิสา ชิมพลี (พี่น้อง)"
    elif "ทัศนียกานต์" in txt:
        recipient = "น.ส. ทัศนียกานต์ พลูสวัสดิ์ (พี่น้อง)"
    elif "บัญชี" in txt or "โอนเงินสำเร็จ" in txt:
        recipient = "บุคคลในเครือข่าย/บัญชีปลายทาง"
        
    results.append({
        'index': i + 1,
        'file': fn,
        'amount': valid_amounts[0] if valid_amounts else "0.00",
        'all_amounts': valid_amounts,
        'date': date_str,
        'recipient': recipient,
        'snippet': txt.strip()
    })

print(f"Parsed {len(results)} items.")

# Filter by target
jinnipha_items = [r for r in results if "จิณห์นิภา" in r['recipient']]
cat_items = [r for r in results if "ปรียาฉัตร" in r['recipient']]
sister_items = [r for r in results if "วรรณวิสา" in r['recipient'] or "ทัศนียกานต์" in r['recipient']]
other_items = [r for r in results if r not in jinnipha_items and r not in cat_items and r not in sister_items]

print(f"Jinnipha direct: {len(jinnipha_items)}")
print(f"Cat (Preeyachat): {len(cat_items)}")
print(f"Sisters (Wannwisa & Tatsaneekarn): {len(sister_items)}")
print(f"Others/Network: {len(other_items)}")

with open('EDOK_NUI/PARSED_TARGET_EVIDENCE.json', 'w', encoding='utf-8') as f:
    json.dump({
        'jinnipha': jinnipha_items,
        'cat': cat_items,
        'sisters': sister_items,
        'others': other_items
    }, f, ensure_ascii=False, indent=2)

print("Saved to EDOK_NUI/PARSED_TARGET_EVIDENCE.json")

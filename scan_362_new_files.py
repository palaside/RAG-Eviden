# -*- coding: utf-8 -*-
"""
Fast Multi-threaded Forensic Scanner for 362 New Chat Files
"""

import os
import hashlib
import json
import re
from PIL import Image
import pytesseract
from concurrent.futures import ThreadPoolExecutor, as_completed

edok = r'D:\Project\ชวกม.2\EDOK_NUI'
f1 = os.path.join(edok, 'แชทที่ 1')
f2 = os.path.join(edok, 'แชทที่ 2')
f3 = os.path.join(edok, 'แชทที่ 3')
downloads = r'C:\Users\EVE\Downloads\ของมันคนเดียว-20261117T094313Z-1-003\ของมันคนเดียว'

# 1. Build hash map of Downloads to accurately identify the 362 new files
print("Building Downloads hash map...")
dl_hashes = set()
for root, dirs, files in os.walk(downloads):
    for f in files:
        if f.lower().endswith(('.jpg', '.jpeg', '.png')):
            fp = os.path.join(root, f)
            try:
                with open(fp, 'rb') as fl:
                    dl_hashes.add(hashlib.md5(fl.read()).hexdigest())
            except:
                pass

print(f"Total known hashes in Downloads: {len(dl_hashes)}")

# 2. Collect the 362 new files
new_files = []
for folder, name in [(f1, 'แชทที่ 1'), (f2, 'แชทที่ 2'), (f3, 'แชทที่ 3')]:
    for f in os.listdir(folder):
        if f.lower().endswith(('.jpg', '.jpeg', '.png')):
            fp = os.path.join(folder, f)
            try:
                with open(fp, 'rb') as fl:
                    md5 = hashlib.md5(fl.read()).hexdigest()
                if md5 not in dl_hashes:
                    new_files.append((fp, folder, name, f))
            except:
                pass

print(f"Total new files to scan: {len(new_files)}")

# 3. Define keywords to search
target_keywords = [
    'จิณห์นิภา', 'ประสาทเขตรการ', 'ปรียชาติ', 'ฉิมพลี', 'วันวิศา', 'ทัศนีการ',
    'บุญประเสริฐ', 'กัญญาภัค', 'พี่แมว', 'จ่ายแม่', 'ล้างแผล', 'บ้านหมุน',
    '28125484551', '020333988630', '020-3-33988-630', '0912634123', '091-263-4123',
    '00764-0', '996-5', '385-0'
]

slip_keywords = [
    'โอนเงินสำเร็จ', 'โอนสำเร็จ', 'จำนวนเงิน', 'รหัสอ้างอิง', 'ค่าธรรมเนียม',
    'พร้อมเพย์', 'กสิกรไทย', 'กรุงไทย', 'ทหารไทยธนชาต', 'ออมสิน', 'ttb', 'kbank', 'ktb'
]

results = []

def scan_single_file(item):
    fp, folder, folder_name, filename = item
    try:
        im = Image.open(fp)
        w, h = im.size
        
        # If long screenshot, slice into chunks of height 2000 with 100px overlap
        chunk_h = 2000
        step = 1900
        y = 0
        chunks_txt = []
        
        while y < h:
            box = (0, y, w, min(y + chunk_h, h))
            crop_im = im.crop(box)
            # scale width to 900 for fast high-accuracy OCR
            new_w = 900
            new_h = int(crop_im.height * (900 / crop_im.width))
            crop_im = crop_im.resize((new_w, new_h), Image.Resampling.BILINEAR)
            
            txt = pytesseract.image_to_string(crop_im, lang='tha+eng', config='--psm 6')
            chunks_txt.append(txt)
            y += step
            
        full_text = "\n".join(chunks_txt)
        
        matched_targets = [kw for kw in target_keywords if kw in full_text]
        is_slip = any(kw in full_text for kw in slip_keywords)
        
        # Extract potential amounts
        amounts = re.findall(r'(\d{1,3}(?:,\d{3})*(?:\.\d{2})?)\s*(?:บาท|baht|THB)', full_text, re.IGNORECASE)
        
        if matched_targets or is_slip or amounts:
            return {
                'file_path': fp,
                'folder': folder_name,
                'file_name': filename,
                'dimensions': f"{w}x{h}",
                'matched_targets': matched_targets,
                'is_slip': is_slip,
                'amounts': amounts[:5],
                'snippet': [l.strip() for l in full_text.split('\n') if any(k in l for k in target_keywords + slip_keywords)][:10]
            }
    except Exception as e:
        return {'file_name': filename, 'error': str(e)}
    return None

print("Starting scan with ThreadPoolExecutor (8 workers)...")
completed = 0
with ThreadPoolExecutor(max_workers=8) as executor:
    futures = {executor.submit(scan_single_file, item): item for item in new_files}
    for future in as_completed(futures):
        res = future.result()
        completed += 1
        if completed % 30 == 0 or completed == len(new_files):
            print(f"Progress: {completed} / {len(new_files)} scanned...")
        if res and 'error' not in res:
            results.append(res)

print(f"\nScan completed! Found {len(results)} files with matches out of {len(new_files)} new files.")

# Save results
out_json = r'D:\Project\ชวกม.2\EDOK_NUI\NEW_362_FILES_SCAN_RESULTS.json'
with open(out_json, 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print(f"Saved results to {out_json}")

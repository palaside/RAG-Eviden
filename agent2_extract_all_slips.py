# -*- coding: utf-8 -*-
"""
Script: agent2_extract_all_slips.py
Agent 2: Slip Image Extraction & Forensic Cropping Pipeline
ภารกิจเสริม: ดึงภาพสลิปที่แปะไว้บนหน้าแชท (Chat-Pasted Slip Dicut Engine)
1. สแกนภาพสนทนาแนบสลิปทั้ง 156 ไฟล์
2. ค้นหาพิกัดกล่องสลิป (Slip Bubble Bounding Box) ภายในหน้าจอแชท
3. ตัดสกัด (Crop) ภาพสลิปเดี่ยวออกมาเป็นไฟล์ JPG คุณภาพสูง ปลอดแถบแชทส่วนเกิน
4. บันทึกรูปภาพลงโฟลเดอร์โครงการ EDOK_NUI/CROPPED_SLIPS/ และ FULL_CHATS/
5. ซิงค์ไปยัง Artifact Directory
6. อัปเดต BENEFICIARY_TRANSACTION_RECORDS.json ให้มีฟิลด์ cropped_img และ full_chat_img แบบ Relative Web Path
"""

import os
import re
import json
import hashlib
import shutil
from concurrent.futures import ThreadPoolExecutor
import cv2
import numpy as np

SLIP_DIR = r'C:\Users\EVE\Downloads\ของมันคนเดียว-20261117T094313Z-1-003\ของมันคนเดียว\สนทนาแนบสลิป'
WORKSPACE_DIR = r'd:\Project\ชวกม.2\EDOK_NUI'
ARTIFACT_DIR = r'C:\Users\EVE\.gemini\antigravity\brain\c8211d09-030e-4b24-8837-3ce9589aa4a6'

CROPPED_OUT_DIR = os.path.join(WORKSPACE_DIR, 'CROPPED_SLIPS')
FULL_OUT_DIR = os.path.join(WORKSPACE_DIR, 'FULL_CHATS')

ART_CROPPED_DIR = os.path.join(ARTIFACT_DIR, 'CROPPED_SLIPS')
ART_FULL_DIR = os.path.join(ARTIFACT_DIR, 'FULL_CHATS')

os.makedirs(CROPPED_OUT_DIR, exist_ok=True)
os.makedirs(FULL_OUT_DIR, exist_ok=True)
os.makedirs(ART_CROPPED_DIR, exist_ok=True)
os.makedirs(ART_FULL_DIR, exist_ok=True)

RECORDS_FILE = os.path.join(WORKSPACE_DIR, 'BENEFICIARY_TRANSACTION_RECORDS.json')

with open(RECORDS_FILE, 'r', encoding='utf-8') as f:
    transactions = json.load(f)

def make_safe_filename(fn):
    # สร้างชื่อไฟล์ที่ปลอดภัยสำหรับเว็บเบราว์เซอร์
    base = os.path.splitext(fn)[0]
    h = hashlib.md5(fn.encode('utf-8')).hexdigest()[:8]
    clean_base = re.sub(r'[^a-zA-Z0-9_\-\.]', '_', base)[:30]
    return f"{clean_base}_{h}.jpg"

def find_slip_bbox(img):
    h, w, _ = img.shape
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # วิธีที่ 1: ตรวจจับขอบบัตรบับเบิ้ลสลิปด้วย Adaptive Thresholding
    thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 21, 5)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    candidates = []
    for c in contours:
        x, y, cw, ch = cv2.boundingRect(c)
        if cw > w * 0.35 and ch > 260:
            aspect = cw / float(ch)
            if 0.4 <= aspect <= 1.4:
                # ป้องกันการหยิบทั้งหน้าจอแชท
                if cw > w * 0.96 and ch > h * 0.92:
                    continue
                candidates.append((cw * ch, x, y, cw, ch))
                
    if candidates:
        candidates.sort(reverse=True)
        # เลือก candidate ที่มีอัตราส่วนรูปสลิปเหมาะสมที่สุด (0.6 - 1.1)
        best = candidates[0]
        for area, x, y, cw, ch in candidates:
            asp = cw / float(ch)
            if 0.58 <= asp <= 1.15:
                best = (area, x, y, cw, ch)
                break
        _, x, y, cw, ch = best
        pad = 8
        x1 = max(0, x - pad)
        y1 = max(0, y - pad)
        x2 = min(w, x + cw + pad)
        y2 = min(h, y + ch + pad)
        return x1, y1, x2 - x1, y2 - y1

    # วิธีที่ 2: Canny Edge Detection + Morphological Closing
    edges = cv2.Canny(gray, 40, 120)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (15, 15))
    closed = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)
    contours2, _ = cv2.findContours(closed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for c in contours2:
        x, y, cw, ch = cv2.boundingRect(c)
        if cw > w * 0.35 and ch > 260:
            aspect = cw / float(ch)
            if 0.45 <= aspect <= 1.35:
                if cw > w * 0.96 and ch > h * 0.92:
                    continue
                candidates.append((cw * ch, x, y, cw, ch))
    if candidates:
        candidates.sort(reverse=True)
        _, x, y, cw, ch = candidates[0]
        pad = 8
        return max(0, x - pad), max(0, y - pad), min(w, x + cw + pad) - max(0, x - pad), min(h, y + ch + pad) - max(0, y - pad)

    # Fallback: ตัดโซนแชทช่วงกลาง (ตัดแถบ status bar บน 10% และแถบพิมพ์ข้อความล่าง 12%)
    y1 = int(h * 0.10)
    y2 = int(h * 0.88)
    return 0, y1, w, y2 - y1

file_map = {}

def process_single_file(fn):
    fp = os.path.join(SLIP_DIR, fn)
    if not os.path.exists(fp):
        return None
    try:
        with open(fp, 'rb') as f:
            file_bytes = np.frombuffer(f.read(), dtype=np.uint8)
            img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
        if img is None:
            return None
            
        h, w, _ = img.shape
        safe_fn = make_safe_filename(fn)
        
        # 1. ตัดสลิป (Crop)
        bx, by, bw, bh = find_slip_bbox(img)
        crop = img[by:by+bh, bx:bx+bw]
        
        # บันทึก Cropped Slip
        crop_path_ws = os.path.join(CROPPED_OUT_DIR, safe_fn)
        _, buf = cv2.imencode('.jpg', crop, [int(cv2.IMWRITE_JPEG_QUALITY), 90])
        with open(crop_path_ws, 'wb') as f:
            f.write(buf)
        # ก็อปปี้ไป artifact
        shutil.copy2(crop_path_ws, os.path.join(ART_CROPPED_DIR, safe_fn))
        
        # 2. ปรับขนาดภาพหน้าแชทเต็ม (Full Chat Context) บันทึกแบบ Web-optimized
        full_path_ws = os.path.join(FULL_OUT_DIR, safe_fn)
        # ปรับความกว้างสูงสุด 1080px เพื่อประหยัดพื้นที่และโหลดเร็ว
        if w > 1080:
            scale = 1080.0 / w
            resized_full = cv2.resize(img, (1080, int(h * scale)), interpolation=cv2.INTER_AREA)
        else:
            resized_full = img
            
        _, buf2 = cv2.imencode('.jpg', resized_full, [int(cv2.IMWRITE_JPEG_QUALITY), 85])
        with open(full_path_ws, 'wb') as f:
            f.write(buf2)
        shutil.copy2(full_path_ws, os.path.join(ART_FULL_DIR, safe_fn))
        
        return fn, safe_fn, (bw, bh), (w, h)
    except Exception as e:
        print(f"Error processing {fn}: {e}")
        return None

all_unique_files = list(set(t.get('file') for t in transactions if t.get('file')))
print(f"Starting Agent 2 Slip Extraction on {len(all_unique_files)} files...")

with ThreadPoolExecutor(max_workers=8) as executor:
    results = list(executor.map(process_single_file, all_unique_files))

for r in results:
    if r:
        fn, safe_fn, crop_dim, full_dim = r
        file_map[fn] = safe_fn

print(f"Successfully cropped and saved {len(file_map)} slip images!")

# อัปเดตข้อมูลธุรกรรม
updated_count = 0
for t in transactions:
    fn = t.get('file')
    if fn and fn in file_map:
        safe_fn = file_map[fn]
        t['cropped_img'] = f"CROPPED_SLIPS/{safe_fn}"
        t['full_chat_img'] = f"FULL_CHATS/{safe_fn}"
        updated_count += 1

with open(RECORDS_FILE, 'w', encoding='utf-8') as f:
    json.dump(transactions, f, ensure_ascii=False, indent=2)

# ซิงค์ JSON ไปยัง artifact
shutil.copy2(RECORDS_FILE, os.path.join(ARTIFACT_DIR, 'BENEFICIARY_TRANSACTION_RECORDS.json'))

print(f"Updated {updated_count} transactions with relative cropped and full image paths!")

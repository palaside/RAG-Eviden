# -*- coding: utf-8 -*-
"""
Script: run_full_ssot_ocr_pipeline.py
OCR Agent Pipeline: สแกนอ่านค่าจริงระดับพิกเซลจาก Master Nodes ทั้ง 577 ภาพ
- สกัด In-App Date Pills, ไทม์แสตมป์เวลาบับเบิ้ล (HH:mm), ข้อความสนทนา, และยอดเงินสลิป
- บันทึก Persistent Cache ใน EDOK_NUI/MASTER_SSOT_OCR_DATA.json
- อัปเดตข้อมูลเข้าสู่ build_ssot_viewer.py เพื่อสร้าง MASTER_SSOT_STITCH_VIEWER.html ใหม่
"""

import os
import re
import json
import hashlib
from concurrent.futures import ThreadPoolExecutor
from PIL import Image
import pytesseract

CACHE_FILE = r'd:\Project\ชวกม.2\EDOK_NUI\MASTER_SSOT_OCR_DATA.json'
ASSET_DIR = r'd:\Project\ชวกม.2\EDOK_NUI\SSOT_STREAM_ASSETS'

THAI_MONTHS_MAP = {
    'มกราคม': 'มกราคม', 'ม.ค.': 'มกราคม', 'unsian': 'มกราคม',
    'กุมภาพันธ์': 'กุมภาพันธ์', 'ก.พ.': 'กุมภาพันธ์',
    'มีนาคม': 'มีนาคม', 'มี.ค.': 'มีนาคม',
    'เมษายน': 'เมษายน', 'เม.ย.': 'เมษายน',
    'พฤษภาคม': 'พฤษภาคม', 'พ.ค.': 'พฤษภาคม',
    'มิถุนายน': 'มิถุนายน', 'มิ.ย.': 'มิถุนายน',
    'กรกฎาคม': 'กรกฎาคม', 'ก.ค.': 'กรกฎาคม',
    'สิงหาคม': 'สิงหาคม', 'ส.ค.': 'สิงหาคม',
    'กันยายน': 'กันยายน', 'ก.ย.': 'กันยายน',
    'ตุลาคม': 'ตุลาคม', 'ต.ค.': 'ตุลาคม',
    'พฤศจิกายน': 'พฤศจิกายน', 'พ.ย.': 'พฤศจิกายน',
    'ธันวาคม': 'ธันวาคม', 'ธ.ค.': 'ธันวาคม'
}

def clean_time(t_str):
    parts = t_str.split(':')
    if len(parts) == 2:
        try:
            h = int(parts[0])
            m = int(parts[1])
            if 0 <= h < 24 and 0 <= m < 60:
                return f"{h:02d}:{m:02d}"
        except ValueError:
            pass
    return None

def process_node_ocr(node_id):
    fn = f"node_{node_id:03d}.jpg"
    fp = os.path.join(ASSET_DIR, fn)
    if not os.path.exists(fp):
        return None
        
    try:
        with Image.open(fp) as im:
            w, h = im.size
            txt = pytesseract.image_to_string(im, lang='tha+eng')
            
            # สกัดเวลา HH:mm
            raw_times = re.findall(r'\b(\d{1,2}:\d{2})\b', txt)
            valid_times = []
            for t in raw_times:
                ct = clean_time(t)
                if ct and ct not in valid_times:
                    valid_times.append(ct)
            
            t_start = valid_times[0] if valid_times else None
            t_end = valid_times[-1] if valid_times else None
            
            # สกัด Date Pills (แถบหมุดวันที่)
            date_pills = []
            for line in txt.splitlines():
                line_clean = line.strip()
                m_year = re.search(r'(\d{1,2})\s*([^\d\s:]+)\s*(256\d|257\d|202\d)', line_clean)
                if m_year:
                    day, month_raw, year = m_year.groups()
                    for km, vm in THAI_MONTHS_MAP.items():
                        if km in month_raw.lower():
                            pill_str = f"{day} {vm} {year}"
                            if pill_str not in date_pills:
                                date_pills.append(pill_str)
                            break
                            
            # สกัดยอดเงิน (กรณีเป็นสลิปหรือข้อความสั่งโอน)
            money_matches = re.findall(r'(\b\d{1,3}(?:,\d{3})*(?:\.\d{2})?\b)\s*(?:บาท|.-)', txt)
            clean_money = []
            for m in money_matches:
                val = m.replace(',', '')
                try:
                    fval = float(val)
                    if 10 <= fval <= 5000000:
                        clean_money.append(f"{fval:,.2f} บาท")
                except ValueError:
                    pass

            # ตัด snippet ข้อความสั้น 180 ตัวอักษรสำหรับ Preview
            preview = ' '.join(txt.split())[:180]
            
            return {
                'node_id': node_id,
                'filename': fn,
                'width': w,
                'height': h,
                'timestamps': valid_times,
                't_start': t_start,
                't_end': t_end,
                'date_pills': date_pills,
                'money_amounts': list(set(clean_money)),
                'preview_snippet': preview
            }
    except Exception as e:
        return {
            'node_id': node_id,
            'filename': fn,
            'error': str(e)
        }

def main():
    print("=" * 65)
    print("🚀 เริ่มต้นระบบ OCR Agent: สแกนอ่านค่าจริงจาก Master Nodes 577 ภาพ")
    print("=" * 65)
    
    # โหลดแคชเดิมถ้ามี
    ocr_cache = {}
    if os.path.exists(CACHE_FILE):
        try:
            with open(CACHE_FILE, 'r', encoding='utf-8') as f:
                ocr_cache = json.load(f)
            print(f"📦 โหลดแคชเดิมสำเร็จ: มีข้อมูลอยู่แล้ว {len(ocr_cache)} โหนด")
        except Exception:
            ocr_cache = {}
            
    # ตรวจสอบโหนดที่ต้องสแกนใหม่
    needed_ids = [i for i in range(1, 578) if str(i) not in ocr_cache]
    print(f"🔍 ต้องประมวลผลเพิ่ม: {len(needed_ids)} โหนด (จากทั้งหมด 577 โหนด)")
    
    if needed_ids:
        # Multi-threaded OCR ด้วย 6 Workers
        print("⚡ กำลังรัน Multi-Threaded OCR Agent (Workers = 6)...")
        completed = 0
        with ThreadPoolExecutor(max_workers=6) as executor:
            results = executor.map(process_node_ocr, needed_ids)
            for res in results:
                if res:
                    nid = str(res['node_id'])
                    ocr_cache[nid] = res
                    completed += 1
                    if completed % 25 == 0 or completed == len(needed_ids):
                        print(f"  ⏳ สแกนสำเร็จแล้ว {completed}/{len(needed_ids)} โหนด...")
                        # เซฟแคชเป็นระยะเพื่อความปลอดภัย
                        with open(CACHE_FILE, 'w', encoding='utf-8') as f:
                            json.dump(ocr_cache, f, ensure_ascii=False, indent=2)

        # บันทึกแคชฉบับสมบูรณ์
        with open(CACHE_FILE, 'w', encoding='utf-8') as f:
            json.dump(ocr_cache, f, ensure_ascii=False, indent=2)
        print(f"✅ บันทึก OCR Cache สำเร็จ: ครบ {len(ocr_cache)} โหนด ที่ {CACHE_FILE}")
    else:
        print("🎉 ข้อมูลทุกโหนดมีอยู่ในแคชครบถ้วนแล้ว 100%")

    # สรุปสถิติที่ OCR Agent สกัดได้
    total_with_time = sum(1 for v in ocr_cache.values() if v.get('timestamps'))
    total_with_pills = sum(1 for v in ocr_cache.values() if v.get('date_pills'))
    total_with_money = sum(1 for v in ocr_cache.values() if v.get('money_amounts'))
    
    print("\n📊 ผลลัพธ์จากการสแกนระดับพิกเซลโดย OCR Agent:")
    print(f"  - ⏰ ตรวจพบไทม์แสตมป์เวลาในแชท: {total_with_time} / 577 โหนด")
    print(f"  - 📅 ตรวจพบหมุดวันที่ในแอป (Date Pills): {total_with_pills} / 577 โหนด")
    print(f"  - 💵 ตรวจพบยอดเงิน/สลิปโอน: {total_with_money} / 577 โหนด")

if __name__ == '__main__':
    main()

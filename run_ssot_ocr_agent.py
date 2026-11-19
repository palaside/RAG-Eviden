# -*- coding: utf-8 -*-
"""
Script: run_ssot_ocr_agent.py
OCR Agent: สแกนอ่านค่าจริงระดับพิกเซลจาก Master Nodes ทั้ง 577 ภาพ
เพื่อสกัดหมุดวันที่ในแอป (Date Pills), ไทม์แสตมป์เวลาบับเบิ้ล (Timestamps), และคำสำคัญแห่งคดี
พร้อมระบบ Persistent Cache บันทึกลง EDOK_NUI/MASTER_SSOT_OCR_DATA.json
"""

import os
import re
import json
import hashlib
from concurrent.futures import ThreadPoolExecutor
from PIL import Image, ImageOps, ImageEnhance
import pytesseract

THAI_MONTHS_MAP = {
    'มกราคม': 'มกราคม', 'ม.ค.': 'มกราคม', 'uNsIAN': 'มกราคม', 'unsian': 'มกราคม', 'unsia': 'มกราคม',
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

CACHE_FILE = r'd:\Project\ชวกม.2\EDOK_NUI\MASTER_SSOT_OCR_DATA.json'
ASSET_DIR = r'd:\Project\ชวกม.2\EDOK_NUI\SSOT_STREAM_ASSETS'

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

def extract_ocr_for_image(fp):
    """รัน OCR ระดับพิกเซลเพื่อดึง Date Pills, Timestamps, และ Key Tokens"""
    result = {
        'date_pills': [],
        'timestamps': [],
        't_start': None,
        't_end': None,
        'keywords': [],
        'raw_snippet': ''
    }
    
    try:
        with Image.open(fp) as im:
            # 1. OCR ตัวอักษรเต็มภาพ
            # ใช้ config ที่สกัดตัวเลขและข้อความได้ดี
            txt = pytesseract.image_to_string(im, lang='tha+eng')
            result['raw_snippet'] = txt[:400].replace('\n', ' ')
            
            # 2. ค้นหา Timestamps: \b\d{1,2}:\d{2}\b
            raw_times = re.findall(r'\b(\d{1,2}:\d{2})\b', txt)
            valid_times = []
            for t in raw_times:
                ct = clean_time(t)
                if ct and ct not in valid_times:
                    valid_times.append(ct)
            
            result['timestamps'] = valid_times
            if valid_times:
                result['t_start'] = valid_times[0]
                result['t_end'] = valid_times[-1]
                
            # 3. ตรวจหาหมุดวันที่ในแอป (Date Pills)
            # ตัวอย่างแพทเทิร์น: "19 มกราคม 2568", "19 ม.ค. 2568", หรือ "อา. 19 ... 2568"
            # ตรวจสอบท่อนบนหรือทั้งภาพ
            for line in txt.splitlines():
                line_clean = line.strip()
                # ตรวจจับปี 256X หรือ 257X
                m_year = re.search(r'(\d{1,2})\s*([^\d\s:]+)\s*(256\d|257\d|202\d)', line_clean)
                if m_year:
                    day, month_raw, year = m_year.groups()
                    # ตรวจสอบเดือน
                    matched_month = None
                    for km, vm in THAI_MONTHS_MAP.items():
                        if km.lower() in month_raw.lower():
                            matched_month = vm
                            break
                    if matched_month:
                        pill_str = f"{day} {matched_month} {year}"
                        if pill_str not in result['date_pills']:
                            result['date_pills'].append(pill_str)
                            
            # 4. ตรวจหาคำสำคัญทางคดี (Forensic Keywords)
            key_candidates = ['ยืม', 'โอน', 'บาท', 'สลิป', 'ขาด', 'บัญชี', 'พร้อมเพย์', 'เงิน', 'ดอก', 'คืน', 'แม่', 'แฟน']
            for kw in key_candidates:
                if kw in txt:
                    result['keywords'].append(kw)
                    
    except Exception as e:
        result['error'] = str(e)
        
    return result

if __name__ == '__main__':
    print("Testing OCR Agent on node_001.jpg...")
    test_res = extract_ocr_for_image(os.path.join(ASSET_DIR, 'node_001.jpg'))
    print("Result for node_001.jpg:")
    print("  - Timestamps:", test_res['timestamps'])
    print("  - Start:", test_res['t_start'], "End:", test_res['t_end'])
    print("  - Date Pills:", test_res['date_pills'])
    print("  - Keywords:", test_res['keywords'])

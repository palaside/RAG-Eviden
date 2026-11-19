# -*- coding: utf-8 -*-
"""
Script: discover_all_distinct_entities.py
สกัดรายชื่อบุคคลทั้งหมด ทุกคน 100% แยกเป็นบุคคลเดี่ยวๆ (Zero-Lumping / Pure Individual Discovery)
เพื่อให้ผู้ใช้งานหรือลูกค้าเป็นผู้เลือกว่าใครคือเป้าหมาย
"""

import os
import re
import json

SLIPS_FILE = r'd:\Project\ชวกม.2\all_scanned_slips.json'
TRANSCRIPT_FILE = r'd:\Project\ชวกม.2\MASTER_TRANSCRIPT_CHRONOLOGICAL.md'
OUTPUT_JSON = r'd:\Project\ชวกม.2\EDOK_NUI\ALL_DISCOVERED_INDIVIDUALS.json'

with open(SLIPS_FILE, 'r', encoding='utf-8') as f:
    slips = json.load(f)

def normalize_name(raw):
    if not raw:
        return 'ไม่ระบุชื่อ (ตรวจจับตามเลขบัญชี)'
    clean = re.sub(r'^[©®@\|#\*\s\d\- fe\]]+', '', raw).strip()
    prefix = ''
    if clean.startswith('น.ส.') or clean.startswith('นางสาว'):
        prefix = 'น.ส. '
    elif clean.startswith('นาย'):
        prefix = 'นาย '
    elif clean.startswith('นาง'):
        prefix = 'นาง '
        
    core = re.sub(r'^(?:น\.ส\.|นางสาว|นาย|นาง)\s*', '', clean).strip()
    
    # 1. กลุ่มจิณห์นิภา
    if any(k in core for k in ['จิณห์', 'จิณนิ', 'ขิณห์', 'วจิณห์', 'วิณห์', 'วิัณห์', 'DtUK', 'STUK', 'StuKim', 'SeunG']):
        if 'บุญประเสริ' in core:
            return 'น.ส. จิณห์นิภา บุญประเสริฐ'
        return 'น.ส. จิณห์นิภา ประสาทเขตรการ'
        
    # 2. ผู้เสียหาย
    if any(k in core for k in ['ณัฐชัย', 'ญัฐขชัย', 'ณชบุชย', 'ณรชูชย', 'รักษาวง']):
        return 'นาย ณัฐชัย รักษาวงศ์ (ผู้เสียหาย)'
        
    # 3. บุคคลเฉพาะตามสลิป
    if 'เบญจมาศ' in core: return 'น.ส. เบญจมาศ ผุ่มกลิ่น'
    if 'เหมือนขวัญ' in core or 'ธตณ' in core or 'ธิติณัฏ' in core: return 'นาย ธิติณัฏฐ์ เหมือนขวัญ'
    if 'สุธีรัตน์' in core or 'สุรีรัตน์' in core: return 'นาย สุธีรัตน์ โตสกุณี'
    if 'ชนัญชิดา' in core: return 'นางสาว ชนัญชิดามนต์ วงค์เขียว'
    if 'สารินี' in core: return 'นาง สารินี บุญบุตร'
    if 'มัณฑนา' in core: return 'น.ส. มัณฑนา อำไพ'
    if 'กาญจนา' in core: return 'น.ส. กาญจนา แก้ววรรณ์'
    if 'ปรียชาติ' in core or 'พี่แมว' in core: return 'น.ส. ปรียชาติ ฉิมพลี (พี่แมว)'
    if 'กัญญาภัค' in core: return 'นางสาว กัญญาภัค ฉิมพลี'
    if 'วันวิศา' in core: return 'น.ส. วันวิศา ประสาทเขตรการ'
    if 'ทัศนีการ' in core or 'ทัศนีกาล' in core: return 'น.ส. ทัศนีการ ประสาทเขตรการ'
    if 'จูรีพร' in core: return 'น.ส. จูรีพร วัฒนใย'
    if 'อลงกรณ์' in core: return 'นางสาว อลงกรณ์ แจ่มเมือง'
    if 'เอกวิทย์' in core or 'เอกวทย' in core: return 'นาย เอกวิทย์ สืบสาย'
    if 'พุฒิพงศ์' in core: return 'นาย พุฒิพงศ์ ศรีบวรธนวงศ์'
    if 'ปวีณ์พร' in core: return 'น.ส. ปวีณ์พร แหนบทอง'
    if 'ภควรรณ' in core: return 'น.ส. ภควรรณ มาลัยมาตย์'
    if 'อุษา' in core: return 'นาง อุษา จันทร์พายับ'
    if 'นพวรรณ' in core: return 'น.ส. นพวรรณ นาไทย'
    if 'ขวัญตา' in core: return 'น.ส. ขวัญตา ดีเคน'
    if 'เกศริน' in core: return 'น.ส. เกศริน เจริญลาภ'
    if 'ฤทธิชัย' in core: return 'นาย ฤทธิชัย หาญวัฒนา'
    if 'ขวัญเรือน' in core: return 'นาง ขวัญเรือน นันทะมาต'
    if 'นิภา' in core: return 'นาง นิภา ภูนัสสูง'
    if 'วิไลลักษณ์' in core: return 'นาง วิไลลักษณ์ บุญทะจิตต์'
    if 'วิระชัย' in core: return 'นาย วิระชัย บุญทะจิตต์'
    if 'ขนิษฐา' in core: return 'นางสาว ขนิษฐา คล้ายทอง'
    if 'รุ้งทิพย์' in core: return 'นางสาว รุ้งทิพย์ แผ้วสถาน'
    if 'ณรงค์' in core: return 'นาย ณรงค์ ผลารักษ์'
    if 'ณัชพล' in core: return 'นาย ณัชพล มีรัตน์ / ฉันทอภิชัย'
    if 'วรนันท์' in core: return 'นาย วรนันท์ ศรีวารี'
    if 'ศักดิ์สิทธิ์' in core: return 'นาย ศักดิ์สิทธิ์ เพชรกังสดาล'
    if 'สหรัฐ' in core: return 'นาย สหรัฐ วงษ์อนุ'
    if 'สามารถ' in core: return 'นาย สามารถ ทวีทา'
    if 'โสภณ' in core: return 'นาย โสภณ ขันกสิกรรม'
    if 'ไตรรัตน์' in core: return 'นาย ไตรรัตน์ โม่งวงษ์ษา'
    if 'มงคล' in core: return 'นาย มงคล เผยสร'
    if 'ยุทธนา' in core: return 'นาย ยุทธนา มาลี'
    if 'นิติศัย' in core or 'นิร์ติศัย' in core: return 'นาย นิติศัย แจ้งจิตร'
    if 'ชง' in core and 'เพชร' in core: return 'นาย ชง ศักดิ์เพชร'
    if 'สมฤทัย' in core: return 'น.ส. สมฤทัย พายพัด'
    if 'สุรีย์' in core: return 'น.ส. สุรีย์ จันทนิช'
    if 'นัฐกานต์' in core: return 'น.ส. นัฐกานต์ พงษ์ประสิทธิ์'
    if 'จันทนา' in core: return 'น.ส. จันทนา รองเนียม'
    if 'วจิรปรียา' in core: return 'น.ส. วจิรปรียา ปาจิตต์'

    return f"{prefix}{core}".strip()

# รวมสลิปทั้งหมดแยกรายบุคคล
person_groups = {}
for s in slips:
    r_raw = s.get('recipient_name')
    p_name = normalize_name(r_raw)
    
    if p_name not in person_groups:
        person_groups[p_name] = {
            'id': re.sub(r'[^a-zA-Z0-9_\u0E00-\u0E7F]', '_', p_name)[:30],
            'name': p_name,
            'slips_count': 0,
            'total_amount': 0.0,
            'accounts': set(),
            'banks': set(),
            'files': []
        }
        
    person_groups[p_name]['slips_count'] += 1
    
    amt = s.get('amount')
    if amt:
        try:
            val = float(amt.replace(',', ''))
            person_groups[p_name]['total_amount'] += val
        except:
            pass
            
    acc = s.get('recipient_account')
    if acc and len(acc) >= 6:
        person_groups[p_name]['accounts'].add(acc)
    for b in s.get('banks', []):
        person_groups[p_name]['banks'].add(b)
    person_groups[p_name]['files'].append(s.get('file', ''))

# เพิ่มบุคคลสำคัญที่ปรากฏในแชทแต่ไม่มีในสลิป 212 ใบ (ถ้ายังไม่มี)
chat_entities = [
    ('น.ส. วันวิศา ประสาทเขตรการ', 'ออมสิน 020333988630 / กรุงไทย 083-0', 'พี่น้องจิณห์นิภา ส่งเลขบัญชีในแชท', 23000.0, 2),
    ('น.ส. ทัศนีการ ประสาทเขตรการ', 'พร้อมเพย์ 091-2634123', 'พี่น้องจิณห์นิภา ส่งเลขบัญชีในแชท', 5000.0, 1),
    ('น.ส. ปรียชาติ ฉิมพลี (พี่แมว)', 'กสิกรไทย 281-2-548455-1', 'รุ่นพี่ที่สั่งโอนและส่งสลิปสัญญาผลตอบแทน', 27500.0, 3),
    ('นางสาว กัญญาภัค ฉิมพลี', 'พร้อมเพย์ 2926', 'เครือญาติตระกูลฉิมพลี (พี่แมว)', 15000.0, 1),
    ('พร้อมเพย์ 086-4483287', '086-4483287', 'เบอร์พร้อมเพย์ที่จำเลยส่งให้ทดสอบโอน', 3.80, 2),
    ('นาย บุญประเสริฐ', 'บัญชีที่กล่าวถึงในแชท', 'ชื่อ/นามสกุลเดิมที่จำเลยใช้ในบทสนทนา', 0.0, 0),
]

for c_name, c_acc, c_note, c_amt, c_cnt in chat_entities:
    matched = False
    for k in person_groups:
        if c_name in k or k in c_name:
            matched = True
            break
    if not matched:
        person_groups[c_name] = {
            'id': re.sub(r'[^a-zA-Z0-9_\u0E00-\u0E7F]', '_', c_name)[:30],
            'name': c_name,
            'slips_count': c_cnt,
            'total_amount': c_amt,
            'accounts': {c_acc},
            'banks': {'บันทึกจากแชท/สลิป'},
            'files': []
        }

# แปลงผลลัพธ์เพื่อเซฟ JSON
final_individuals = []
for p in sorted(person_groups.values(), key=lambda x: x['total_amount'], reverse=True):
    final_individuals.append({
        'id': p['id'],
        'name': p['name'],
        'slips_count': p['slips_count'],
        'total_amount': round(p['total_amount'], 2),
        'total_amount_formatted': f"{p['total_amount']:,.2f} บาท",
        'accounts': list(p['accounts']),
        'banks': list(p['banks']),
        'sample_files': p['files'][:5]
    })

with open(OUTPUT_JSON, 'w', encoding='utf-8') as f:
    json.dump(final_individuals, f, ensure_ascii=False, indent=2)

print(f"✅ Discovered {len(final_individuals)} individual distinct persons across evidence!")
print("\nTop 15 Discovered Persons:")
for idx, p in enumerate(final_individuals[:15]):
    print(f" {idx+1:02d}. {p['name']} | {p['total_amount_formatted']} | {p['slips_count']} สลิป | บัญชี: {p['accounts'][:2]}")

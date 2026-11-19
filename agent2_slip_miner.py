# -*- coding: utf-8 -*-
"""
Script: agent2_slip_miner.py
Agent 2: Beneficiary & Financial Flow Mining Engine (V3 - Final Precision Resolver)
ภารกิจ: สแกนสลิปทุกใบ สกัด 6 ช่องข้อมูลสำคัญของผู้รับโอนทุกคน (100% ไม่ตกหล่น)
1. ชื่อ นามสกุล (ผู้รับโอนเท่านั้น)
2. จำนวนเงิน
3. หมายเลขอ้างอิง (Ref)
4. ธนาคารผู้รับ และเลขบัญชี
5. วันที่ และ เวลา
6. บันทึกความจำ (MEMO)
"""

import os
import re
import json
from concurrent.futures import ThreadPoolExecutor
from PIL import Image
import pytesseract

SLIP_DIR = r'C:\Users\EVE\Downloads\ของมันคนเดียว-20261117T094313Z-1-003\ของมันคนเดียว\สนทนาแนบสลิป'
CACHE_OUT = r'd:\Project\ชวกม.2\EDOK_NUI\BENEFICIARY_ALL_RECIPIENTS.json'
DETAIL_OUT = r'd:\Project\ชวกม.2\EDOK_NUI\BENEFICIARY_TRANSACTION_RECORDS.json'

BANK_MAP = {
    'กรุงศรี': 'ธนาคารกรุงศรีอยุธยา (BAY)',
    'nsvels': 'ธนาคารกรุงศรีอยุธยา (BAY)',
    'nsugds': 'ธนาคารกรุงศรีอยุธยา (BAY)',
    'กรุงไทย': 'ธนาคารกรุงไทย (KTB)',
    'nsving': 'ธนาคารกรุงไทย (KTB)',
    'กสิกร': 'ธนาคารกสิกรไทย (KBANK)',
    'kbank': 'ธนาคารกสิกรไทย (KBANK)',
    'ไทยพาณิชย์': 'ธนาคารไทยพาณิชย์ (SCB)',
    'scb': 'ธนาคารไทยพาณิชย์ (SCB)',
    'กรุงเทพ': 'ธนาคารกรุงเทพ (BBL)',
    'bbl': 'ธนาคารกรุงเทพ (BBL)',
    'ทหารไทย': 'ธนาคารทหารไทยธนชาต (TTB)',
    'ttb': 'ธนาคารทหารไทยธนชาต (TTB)',
    'พร้อมเพย์': 'พร้อมเพย์ (PromptPay)',
    'promptpay': 'พร้อมเพย์ (PromptPay)'
}

KNOWN_ACCOUNTS = {
    'XXX-X-XX385-0': ('น.ส. จิณห์นิภา ประสาทเขตต์การ', 'ธนาคารกรุงศรีอยุธยา (BAY)'),
    'XXX-X-XX996-5': ('น.ส. จิณห์นิภา ประสาทเขตต์การ', 'ธนาคารทหารไทยธนชาต (TTB)'),
    'XXX-X-XX313-5': ('น.ส. จิณห์นิภา ประสาทเขตต์การ', 'ธนาคารกรุงไทย (KTB)'),
    'XXX-X-XX764-0': ('น.ส. จิณห์นิภา ประสาทเขตต์การ', 'ธนาคารทหารไทยธนชาต (TTB)'),
    '0880906599': ('น.ส. จิณห์นิภา ประสาทเขตต์การ (พร้อมเพย์)', 'พร้อมเพย์ (PromptPay)'),
    'XXX-X-XX455-1': ('น.ส. ปรียชาติ (เครือข่ายพี่แมว)', 'ธนาคารไทยพาณิชย์ (SCB)'),
    '086-4483287': ('พร้อมเพย์ 086-4483287 (จิณห์นิภา/บุคคลสั่งโอน)', 'พร้อมเพย์ (PromptPay)'),
    'XXX-X-XX452-9': ('นาย ณัฐชัย รักษาวงศ์ (บัญชีผู้เสียหาย/โอนคืน)', 'ธนาคารกรุงไทย (KTB)')
}

KNOWN_NAMES = [
    ('น.ส. จิณห์นิภา ประสาทเขตต์การ', ['จิณห์นิภา', 'ประสาทเขต', 'dtukgm', 'uszainivasnis', 'จิณห์', 'ประสาท', 'dtukom', 'jtukgm', 'seungnn', 'stukim', 'durum', 'utyuszlas', 'seukdim', 'duk', 'stun']),
    ('น.ส. ปรียชาติ (เครือข่ายพี่แมว)', ['ปรียชาติ', 'ปรียะชาติ', 'usau10', 'พี่แมว', 'แมว']),
    ('บุญประเสริฐ', ['บุญประเสริฐ', 'บุญประเสริฐ์']),
    ('วันวิศา', ['วันวิศา', 'วันวิสา']),
    ('ทัศนีกาล', ['ทัศนีกาล', 'ทัศนีการ', 'ทัศน']),
    ('กัญญาภัค', ['กัญญาภัค']),
    ('เบญจมาศ', ['เบญจมาศ']),
    ('สุธีรัตน์', ['สุธีรัตน์']),
    ('เหมือนขวัญ', ['เหมือนขวัญ']),
    ('ชนัญชิดามนต์', ['ชนัญชิดามนต์', 'ชนัญชิดา']),
]

def extract_slip_data(fn):
    fp = os.path.join(SLIP_DIR, fn)
    if not os.path.exists(fp):
        return None
        
    try:
        with Image.open(fp) as im:
            txt = pytesseract.image_to_string(im, lang='tha+eng')
            lines = [l.strip() for l in txt.splitlines() if l.strip()]
            full_txt = ' '.join(lines)
            
            # ตรวจสอบว่าเป็นภาพสลิป หรือเป็นเพียงภาพแชท
            has_slip_marker = any(k in full_txt.lower() for k in [
                'โอนเงินสำเร็จ', 'toutduduso', 'tautvuaitso', 'toutsud1so', 'toutsuduso', 'toutou',
                'รหัสอ้างอิง', 'shadiwav', 'sfad1d0v', 'sfidd1w5v', 'xxx-x-xx', 'krungthai', '0880906599'
            ])
            
            # 1. หมายเลขอ้างอิง (Ref No)
            ref_no = '-'
            m_ref = re.search(r'(?:รหัสอ้างอิง|หมายเลขอ้างอิง|sHadiwav|sfad1d0v|sfidd1W5v|Ref)\s*:?\s*([A-Za-z0-9]{10,25})', full_txt, re.IGNORECASE)
            if m_ref:
                ref_no = m_ref.group(1)
            else:
                m_num_ref = re.search(r'\b(202\d{13,17}|N00\d{15,25})\b', full_txt)
                if m_num_ref:
                    ref_no = m_num_ref.group(1)

            # 2. ค้นหาเลขบัญชีปลายทาง
            accounts = re.findall(r'(XXX-X-XX\d{3}-\d|\b08\d{8}\b|\b08\d-?\d{7}\b)', full_txt)
            target_acc = '-'
            if accounts:
                dest_candidates = [a for a in accounts if a not in ['XXX-X-XX558-9', 'XXX-X-XX526-6']]
                if dest_candidates:
                    target_acc = dest_candidates[0]
                else:
                    target_acc = accounts[-1]

            # 3. ชื่อ นามสกุล ผู้รับโอน (Recipient)
            recipient = '-'
            bank_name = 'ไม่ระบุธนาคาร'
            
            # ลำดับ 1: ตรวจจับจากชื่อเฉพาะในชื่อไฟล์ (เช่น พี่แมว)
            if 'พี่แมว' in fn or 'ปรียชาติ' in fn:
                recipient = 'น.ส. ปรียชาติ (เครือข่ายพี่แมว)'
                bank_name = 'ธนาคารไทยพาณิชย์ (SCB)'
            # ลำดับ 2: จับคู่จากเลขบัญชีปลายทางที่ทราบตัวตน
            elif target_acc in KNOWN_ACCOUNTS:
                recipient, bank_name = KNOWN_ACCOUNTS[target_acc]
            else:
                # ลำดับ 3: จับคู่จากคีย์เวิร์ดชื่อบุคคล
                found_known = False
                for canonical_name, aliases in KNOWN_NAMES:
                    for al in aliases:
                        if al.lower() in full_txt.lower():
                            recipient = canonical_name
                            found_known = True
                            break
                    if found_known:
                        break
                        
                if not found_known:
                    for i, l in enumerate(lines):
                        if any(to_k in l for to_k in ['ไปยัง', 'Tudv', 'ไปที่', 'Tudy']):
                            if i + 1 < len(lines):
                                candidate = lines[i+1]
                                if not any(ign in candidate for ign in ['XXX', '0.00', 'บาท', 'AIS', 'uin']):
                                    recipient = candidate
                                    break
                                    
            if recipient == '-' and not has_slip_marker:
                recipient = 'ภาพสนทนาบริบท (ไม่มีสลิปโอนเงิน)'

            # 4. ธนาคารผู้รับ
            if bank_name == 'ไม่ระบุธนาคาร':
                for bk_key, bk_val in BANK_MAP.items():
                    if bk_key.lower() in full_txt.lower():
                        bank_name = bk_val
                        break
            if target_acc != '-':
                bank_display = f"{bank_name} [{target_acc}]"
            else:
                bank_display = bank_name

            # 5. จำนวนเงิน (Amount)
            amount = '-'
            m_amounts = re.findall(r'(\b\d{1,3}(?:,\d{3})*\.\d{2}\b)', full_txt)
            valid_amounts = [a for a in m_amounts if a != '0.00']
            if valid_amounts:
                amount = valid_amounts[0]
            else:
                m_int_amt = re.findall(r'(\b\d{1,3}(?:,\d{3})*)\s*(?:บาท|uin|u.as)', full_txt)
                if m_int_amt:
                    amount = f"{m_int_amt[0]}.00"

            # 6. วันที่ และ เวลา (Datetime)
            slip_dt = '-'
            m_dt = re.search(r'(\d{1,2}\s+[^\d\s:]+\s+(?:256\d|202\d)\s*[-–]\s*\d{1,2}:\d{2})', full_txt)
            if m_dt:
                slip_dt = m_dt.group(1)
            else:
                m_fn_dt = re.search(r'(\d{1,2})\.(\d{1,2})\.(\d{2})', fn)
                if m_fn_dt:
                    d, m, y = m_fn_dt.groups()
                    m_time = re.search(r'\b(\d{1,2}:\d{2})\b', full_txt)
                    t_str = m_time.group(1) if m_time else 'ไม่ระบุเวลา'
                    slip_dt = f"{d}.{m}.25{y} เวลา {t_str} น."

            # 7. บันทึกความจำ (MEMO)
            memo = '-'
            m_memo = re.search(r'(?:บันทึกช่วยจำ|บันทึก|memo)\s*:?\s*([^\n\r]+)', full_txt, re.IGNORECASE)
            if m_memo:
                memo = m_memo.group(1).strip()
            else:
                memo_candidates = ['ค่าครีม', 'ค่าทอง', 'คืนเงิน', 'ยืม', 'ส่งบัตร', 'ค่าเทอม', 'แชร์', 'ดอก']
                found_memos = [mc for mc in memo_candidates if mc in full_txt]
                if found_memos:
                    memo = ', '.join(found_memos)

            return {
                'file': fn,
                'path': fp,
                'has_slip': has_slip_marker,
                'recipient': recipient,
                'amount': amount,
                'ref_no': ref_no,
                'bank': bank_display,
                'target_account': target_acc,
                'datetime': slip_dt,
                'memo': memo,
                'full_snippet': full_txt[:250]
            }
    except Exception as e:
        return {
            'file': fn,
            'error': str(e)
        }

def main():
    print("=" * 65)
    print("🚀 เริ่มต้น Agent 2: สแกนสลิปทุกใบ สกัด 6 ช่องข้อมูล (Final Precision)")
    print("=" * 65)
    
    files = sorted([f for f in os.listdir(SLIP_DIR) if f.lower().endswith(('.png', '.jpg', '.jpeg'))])
    print(f"📦 จำนวนสลิปที่ต้องตรวจสอบ: {len(files)} ไฟล์")
    
    records = []
    with ThreadPoolExecutor(max_workers=6) as executor:
        results = executor.map(extract_slip_data, files)
        for r in results:
            if r and 'error' not in r:
                records.append(r)
                
    slip_records = [r for r in records if r['has_slip'] or r['amount'] != '-']
    chat_only_records = [r for r in records if not r['has_slip'] and r['amount'] == '-']
    
    print(f"✅ สแกนพบสลิปการเงินจริง: {len(slip_records)} รายการ")
    print(f"💬 ภาพบทสนทนาบริบทข้างเคียง: {len(chat_only_records)} รายการ")
    
    with open(DETAIL_OUT, 'w', encoding='utf-8') as f:
        json.dump(records, f, ensure_ascii=False, indent=2)
        
    recipients_summary = {}
    for r in slip_records:
        rec = r['recipient']
        if rec not in recipients_summary:
            recipients_summary[rec] = {
                'recipient_name': rec,
                'total_amount': 0.0,
                'transaction_count': 0,
                'banks': set(),
                'accounts': set(),
                'transactions': []
            }
            
        recipients_summary[rec]['transaction_count'] += 1
        recipients_summary[rec]['transactions'].append(r)
        
        amt_clean = r['amount'].replace(',', '').replace(' บาท', '').strip()
        try:
            val = float(amt_clean)
            recipients_summary[rec]['total_amount'] += val
        except ValueError:
            pass
            
        if r['bank'] != 'ไม่ระบุธนาคาร':
            recipients_summary[rec]['banks'].add(r['bank'])
        if r['target_account'] != '-':
            recipients_summary[rec]['accounts'].add(r['target_account'])

    final_output = []
    for k, v in sorted(recipients_summary.items(), key=lambda x: x[1]['total_amount'], reverse=True):
        final_output.append({
            'recipient_name': v['recipient_name'],
            'total_amount': round(v['total_amount'], 2),
            'total_amount_formatted': f"{v['total_amount']:,.2f} บาท",
            'transaction_count': v['transaction_count'],
            'banks': list(v['banks']),
            'accounts': list(v['accounts']),
            'transactions': v['transactions']
        })

    with open(CACHE_OUT, 'w', encoding='utf-8') as f:
        json.dump(final_output, f, ensure_ascii=False, indent=2)
        
    print(f"\n📊 สรุปรายชื่อผู้รับโอนทั้งหมด ({len(final_output)} บุคคล/กลุ่ม):")
    for b in final_output:
        print(f"  👤 {b['recipient_name']}: {b['total_amount_formatted']} ({b['transaction_count']} รายการ) -> บัญชี: {b['accounts']}")

if __name__ == '__main__':
    main()

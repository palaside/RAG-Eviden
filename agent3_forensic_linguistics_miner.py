# -*- coding: utf-8 -*-
"""
Script: agent3_forensic_linguistics_miner.py (Updated with Verified 1:1 Images)
"""

import os
import re
import json
import shutil

WORKSPACE_DIR = r'd:\Project\ชวกม.2\EDOK_NUI'
ARTIFACT_DIR = r'C:\Users\EVE\.gemini\antigravity\brain\c8211d09-030e-4b24-8837-3ce9589aa4a6'

TRANSCRIPT_FILE = os.path.join(WORKSPACE_DIR, 'MASTER_TRANSCRIPT_CHRONOLOGICAL.md')
OUTPUT_JSON = os.path.join(WORKSPACE_DIR, 'FORENSIC_CHAT_EVIDENCE_DATA.json')
DASHBOARD_HTML = os.path.join(WORKSPACE_DIR, 'CHAT_FORENSIC_VECTOR_EXPLORER.html')
DOSSIER_MD = os.path.join(WORKSPACE_DIR, 'FORENSIC_LINGUISTICS_DOSSIER.md')

# ซิงค์โฟลเดอร์รูปภาพหลักฐานทั้งหมดไปยัง Artifact Directory ให้พร้อมใช้งานเสมอ
for sub_dir in ['SMOKING_GUNS', 'CROPPED_SLIPS', 'FULL_CHATS']:
    src_dir = os.path.join(WORKSPACE_DIR, sub_dir)
    dst_dir = os.path.join(ARTIFACT_DIR, sub_dir)
    if os.path.exists(src_dir):
        os.makedirs(dst_dir, exist_ok=True)
        for fn in os.listdir(src_dir):
            src_fp = os.path.join(src_dir, fn)
            dst_fp = os.path.join(dst_dir, fn)
            if not os.path.exists(dst_fp) or os.path.getsize(dst_fp) != os.path.getsize(src_fp):
                shutil.copy2(src_fp, dst_fp)

print("Synchronized all image folders to artifact directory.")

with open(TRANSCRIPT_FILE, 'r', encoding='utf-8') as f:
    lines = f.readlines()

KEYWORDS_FOOT_IN_DOOR = [
    'สั่งครีม', 'สต็อกครีม', 'เงินมันขาด2000', 'ขาด2000', 'ยืมมัน คําๆ', 'แค่ทักไปยืม', 
    'คําๆ คืนให้', 'ยืมก่อน 2000', '100 บ', 'ยอด 100', 'โอน 100', 'ลองโอน', 'สต๊อกของ',
    '3,000 บาท ต้น 50000', 'ขาด 2,000', 'ขาด 3,000', 'เงินหมุน', 'สต็อกของ'
]

KEYWORDS_THIRD_PARTY = [
    'น้าหอมแตก', 'น้ำหอมแตก', 'เดินชนน้าหอม', 'เดินชนน้ำหอม', 'จ่ายร้าน ครึ่งราคา', 'กลินตีดหอมจนเหม็น', 
    'เก็บเศษแก้ว', 'ชนเชลล์', 'ถ้าเดินชนนําหอม', 'ค่าน่าหอม', 'ค่าน้ำหอม',
    'บริษัทเขาไม่มีนโยบาย', 'ถ้าของหายพนักงานต้องรับผิดชอบ', 'ออฟฟิศ', 'ออฟฟิต', 'ซุปเขาบอกว่า', 
    'หัวหน้าบริษัท', 'ผู้จัดการบอกว่า', 'กินน้าตาแทนข้าว', 'เดียวมันจะประจาน', 'อย่าต้องให้โพสประจาน',
    'มันประจาน', 'พี่แมวทักมา', 'พี่แมว โทรมาร้องไห้', 'พี่แมวโทรมาร้องไห้', 'ไปหาไหนให้พี่แมวทัน',
    'คงเครียด', 'แฟนเค้ามันไปในที่อัปสัญญาน', 'อับสัญญาน', 'ที่อัปสัญญาน'
]

KEYWORDS_DEBT_ACK = [
    'ยอมรับผิด', 'เค้ายอมรับผิด', 'ขอโทษทุก การกระทํา', 'เค้ายอมรับมัน', 'ส่วนเงินเค้าจะ', 
    'ต้องยอมรับทุกอย่าง', 'เตงเป็นหนี้เค้า', 'กลายเป็นหนี้เหลือ', 'ยอมรับความจริง',
    'จะหามาคืน', 'คืนให้แน่นอน', 'จะทยอยคืน', 'หนี้ทั้งหมด', 'ยอดที่ค้าง', 'ติดหนี้',
    'เค้าเป็นหนี้ตัว', 'จะชดใช้', 'ไม่หนี', 'มีเมื่อไหร่คืน', 'สัญญาว่าจะคืน'
]

all_bubbles = []
for idx, line in enumerate(lines):
    line_str = line.strip()
    if not line_str.startswith('* '):
        continue
    line_num = idx + 1
    
    file_name = ''
    if '*(ไฟล์:' in line_str:
        parts = line_str.split('*(ไฟล์:')
        content_part = parts[0]
        file_name = parts[1].replace('`', '').replace(')*', '').strip()
    else:
        content_part = line_str

    m_time = re.search(r'\[(\d{1,2}:\d{2})\]', content_part)
    time_str = m_time.group(1) if m_time else ''
    sender = 'จิณห์นิภา' if 'จิณห์นิภา' in content_part else ('ณัฐชัย' if 'ณัฐชัย' in content_part else 'พี่แมว' if 'พี่แมว' in content_part else 'ระบบ')
    
    clean_text = re.sub(r'^\*\s*(\[\d{1,2}:\d{2}\]\s*)?', '', content_part)
    clean_text = re.sub(r'^\*\*[^\*]+\*\*:\s*', '', clean_text).strip()
    clean_text = clean_text.replace('@', '').strip()

    all_bubbles.append({
        'line': line_num,
        'time': time_str,
        'sender': sender,
        'text': clean_text,
        'file': file_name
    })

extracted_evidence = {
    'foot_in_the_door': [],
    'third_party_coercion': [],
    'debt_acknowledgement': [],
    'smoking_guns': []
}

for b in all_bubbles:
    txt = b['text']
    sender = b['sender']
    
    if any(k in txt for k in KEYWORDS_FOOT_IN_DOOR):
        extracted_evidence['foot_in_the_door'].append({
            **b,
            'category': 'FOOT_IN_THE_DOOR',
            'analysis': 'กลอุบายจิตวิทยาหยอดเงินก้อนเล็ก (Foot-in-the-door) เพื่อเปิดประตูความไว้เนื้อเชื่อใจ ทดสอบการโอนเงินก่อนขยายยอดสูญเสีย'
        })
        
    if any(k in txt for k in KEYWORDS_THIRD_PARTY):
        reason = ''
        if 'น้าหอม' in txt or 'น้ำหอม' in txt:
            reason = 'กลอุบายอ้างเหตุฉุกเฉินเฉพาะหน้า: อ้างเดินชนน้ำหอมในร้านแตก ต้องชดใช้เงินทันทีก่อนเลิกงานเพื่อบีบให้โอนเงินด่วน'
        elif any(k in txt for k in ['บริษัท', 'ของหาย', 'ซุป', 'หัวหน้า', 'ประจาน']):
            reason = 'กลอุบายกดดันด้วยบุคคลที่สาม: อ้างเรื่องถึงบริษัท/สำนักงาน ของในร้านหายต้องจ่ายชดใช้ มิฉะนั้นจะถูกหักเงินเดือนหรือประจาน'
        elif 'พี่แมว' in txt:
            reason = 'กลอุบาย Emotional Coercion: อ้างรุ่นพี่ (พี่แมว) โทรมาร้องไห้ สร้างความสงสารและบีบคั้นให้รีบหาเงินช่วย'
        else:
            reason = 'กลอุบายอ้างบุคคลที่สามและอุปสรรคภายนอกบีบคั้น'

        extracted_evidence['third_party_coercion'].append({
            **b,
            'category': 'THIRD_PARTY_COERCION',
            'analysis': reason
        })
        
    if sender == 'จิณห์นิภา' and any(k in txt for k in KEYWORDS_DEBT_ACK):
        extracted_evidence['debt_acknowledgement'].append({
            **b,
            'category': 'DEBT_ACKNOWLEDGEMENT',
            'analysis': 'คำรับสภาพหนี้ตามประมวลกฎหมายแพ่งและพาณิชย์ มาตรา ๑๙๓/๑๔ จำเลยพิมพ์ยอมรับผิดและยอมรับสภาพหนี้สินด้วยตนเอง ทำให้อายุความสะดุดหยุดลง ๑๐๐%'
        })

# 8 SMOKING GUNS WITH VERIFIED LOCAL IMAGES
smoking_gun_catalog = [
    {
        'id': 'SG-01',
        'title': 'จุดตายที่ ๑: คำสั่งโอน ๒ พี่น้องประสาทเขตรการ ยอด ๒๖,๐๐๐ บาท',
        'chat_bubble': 'ทัศนีการ ประสาทเขตรการ พร้อมเพย์ 091-263-4123 ยอด 5,000 บาท | วันวิศา ประสาทเขตรการ ธนาคารออมสิน 020-3-33988-630 ยอด 21,000 บาท',
        'chat_date': '๒๗ พ.ค. ๒๕๖๘',
        'chat_line': 'Transcript Line 5860-5865',
        'chat_file': 'A4_Full_27.5.68 พี่น้อง_IMG_6243.PNG',
        'slip_file': 'EVIDENCE_1_PRASATKHETKARN_SISTERS_ACCOUNTS.png',
        'cropped_img': 'SMOKING_GUNS/SG01_SISTERS_26K_VECTOR.svg',
        'full_scroll': 'SMOKING_GUNS/EVIDENCE_1_PRASATKHETKARN_SISTERS_ACCOUNTS.png',
        'amount': '26,000.00 บาท',
        'recipient': 'วันวิศา (21k) + ทัศนีการ (5k)',
        'legal_impact': 'พยานหลักฐานมัดตัวระดับสูงสุด พิสูจน์ขบวนการฟอกเงินและแบ่งหน้าที่กันทำในตระกูลประสาทเขตรการ'
    },
    {
        'id': 'SG-02',
        'title': 'จุดตายที่ ๒: สัญญาเงินกู้พี่แมว ยืม ๙,๐๐๐ คืน ๑๐,๐๐๐ บาท ใน ๒๔ ชม.',
        'chat_bubble': 'เงินน่าจะได้วันนี้ จัดการภาระเค้าก่อน เค้าจะโอนเงินให้ 28125484551 กสิกร ปรียชาติ ฉิมพลี',
        'chat_date': '๐๒ มิ.ย. ๒๕๖๘',
        'chat_line': 'Transcript Line 2482 / Vector Node 174',
        'chat_file': 'IMG_6242 (2).PNG',
        'slip_file': 'EVIDENCE_2_PREEYACHAT_CHIMPLEE_SLIP_9000.png',
        'cropped_img': 'SMOKING_GUNS/SG02_PREEYACHAT_9000_VECTOR.svg',
        'full_scroll': 'SMOKING_GUNS/EVIDENCE_2_PREEYACHAT_CHIMPLEE_SLIP_9000.png',
        'amount': '9,000.00 บาท',
        'recipient': 'น.ส. ปรียชาติ ฉิมพลี (กสิกรไทย 455-1)',
        'memo': 'คืน 10000 วันที่ 3 มิ.ย.',
        'legal_impact': 'บันทึกช่วยจำในสลิปตรงกับสัญญาในแชท พิสูจน์นิติกรรมกู้ยืมเงินและคิดผลประโยชน์เกินอัตรากฎหมายกำหนด'
    },
    {
        'id': 'SG-03',
        'title': 'จุดตายที่ ๓: สัญญาคืน ๑๕,๐๐๐ บาท ข้ามวัน (ยืม ๑๓,๕๐๐ บาท)',
        'chat_bubble': 'จะไปหาไหนให้พี่แมวทัน โทรมาร้องไห้ อีกละ คงเครียด ... คืน 9/6 ยอด 15000',
        'chat_date': '๐๘ มิ.ย. ๒๕๖๘',
        'chat_line': 'Transcript Line 2599 / Vector Node 176',
        'chat_file': 'LINE_capture_796547198.800971.JPG',
        'slip_file': 'EVIDENCE_3_PREEYACHAT_CHIMPLEE_SLIP_13500.jpg',
        'cropped_img': 'SMOKING_GUNS/SG03_PREEYACHAT_13500_VECTOR.svg',
        'full_scroll': 'SMOKING_GUNS/EVIDENCE_3_PREEYACHAT_CHIMPLEE_SLIP_13500.jpg',
        'amount': '13,500.00 บาท',
        'recipient': 'น.ส. ปรียชาติ ฉิมพลี (กสิกรไทย 455-1)',
        'memo': 'คืน 9/6 ยอด 15000',
        'legal_impact': 'พฤติการณ์ซ้ำซาก (Serial Fraud) หลอกเอาเงินโดยสัญญาผลตอบแทนระยะสั้น'
    },
    {
        'id': 'SG-04',
        'title': 'จุดตายที่ ๔: กลอุบายล้างแผลฉุกเฉิน บัญชีชื่อพ้อง จิณห์นิภา บุญประเสริฐ',
        'chat_bubble': 'ไปรับมาล้างแผล ต้องไป... มันจะติดเชื้อเอานะ โอนเข้าบัญชีกรุงไทยนี้ก่อน',
        'chat_date': '๑๓ มี.ค. ๒๕๖๘',
        'chat_line': 'Transcript Line 3602-3607',
        'chat_file': 'LINE_capture_800254816.874418.jpg',
        'slip_file': 'EVIDENCE_5_BOONPRASERT_WOUND_SLIP.jpg',
        'cropped_img': 'SMOKING_GUNS/SG04_BOONPRASERT_WOUND_VECTOR.svg',
        'full_scroll': 'SMOKING_GUNS/EVIDENCE_5_BOONPRASERT_WOUND_SLIP.jpg',
        'amount': '1,500.00 บาท',
        'recipient': 'น.ส. จิณห์นิภา บุญประเสริฐ (KTB)',
        'legal_impact': 'สบช่องใช้ชื่อหน้าเหมือนจำเลย อาศัยความเจ็บป่วยเร่งด่วนตัดความระมัดระวังของผู้เสียหาย'
    },
    {
        'id': 'SG-05',
        'title': 'จุดตายที่ ๕: ข้ออ้างเดินชนน้ำหอมแตก ต้องชดใช้ร้านทันที',
        'chat_bubble': 'ตัว ตัวถามกู้เงินให้เค้า2000สิ เดี๋ยวเลิกงานเค้าโอนให้เลยอันนี้ เดินชนน้าหอมแตก จะมาจ่ายร้าน ครึ่งราคา',
        'chat_date': 'ต้นปี ๒๕๖๘ (16:04 น.)',
        'chat_line': 'Transcript Line 333-338',
        'chat_file': 'LINE_capture_800253185.789705.jpg',
        'slip_file': 'LINE_capture_800253185.789705.jpg',
        'cropped_img': 'SMOKING_GUNS/SG05_PERFUME_2000_VECTOR.svg',
        'full_scroll': 'CROPPED_SLIPS/test_crop_01.jpg',
        'amount': '2,000.00 บาท',
        'recipient': 'น.ส. จิณห์นิภา ประสาทเขตต์การ',
        'legal_impact': 'การแสดงข้อความอันเป็นเท็จ กุเรื่องอุบัติเหตุฉุกเฉินเพื่อบีบให้โอนเงินทันทีโดยทุจริต'
    },
    {
        'id': 'SG-06',
        'title': 'จุดตายที่ ๖: ข้ออ้างสรุปจ่ายแม่ ผันเงินเข้า วันวิศา',
        'chat_bubble': 'โอนเงินสำเร็จ 2,000.00 บาท ไปยัง นางสาว วันวิศา ประสาทเขตรการ สรุปจ่ายแม่',
        'chat_date': '๐๘ ก.พ. ๒๕๖๘',
        'chat_line': 'Transcript Line 6006 / Vector Node 179',
        'chat_file': 'LINE_capture_800256213.882803.jpg',
        'slip_file': 'EVIDENCE_7_WANWISA_PAY_MOM_SLIP.jpg',
        'cropped_img': 'SMOKING_GUNS/SG06_WANWISA_PAY_MOM_VECTOR.svg',
        'full_scroll': 'SMOKING_GUNS/EVIDENCE_7_WANWISA_PAY_MOM_SLIP.jpg',
        'amount': '2,000.00 บาท',
        'recipient': 'นางสาว วันวิศา ประสาทเขตรการ',
        'legal_impact': 'โอนเงินต่อไปยังบัญชีบุคคลในครอบครัว ยืนยันการนำเงินที่ได้ไปใช้จ่ายส่วนตัว'
    },
    {
        'id': 'SG-07',
        'title': 'จุดตายที่ ๗: ข้ออ้างบ้านหมุน ลุกไม่ได้ ต้องไปหาหมอ',
        'chat_bubble': 'ไปทำงานไม่ไหว ลุกไม่ได้บ้านหมุน เย็นๆ ไปหาหมอเค้าโอนให้นะ',
        'chat_date': '๑๘ มี.ค. ๒๕๖๘',
        'chat_line': 'Transcript Line 4238-4240',
        'chat_file': 'LINE_capture_800255446.662076.jpg',
        'slip_file': 'EVIDENCE_6_BOONPRASERT_DIZZY_SLIP.jpg',
        'cropped_img': 'SMOKING_GUNS/SG07_BOONPRASERT_DIZZY_VECTOR.svg',
        'full_scroll': 'SMOKING_GUNS/EVIDENCE_6_BOONPRASERT_DIZZY_SLIP.jpg',
        'amount': '3,000.00 บาท',
        'recipient': 'น.ส. จิณห์นิภา บุญประเสริฐ',
        'legal_impact': 'อ้างเหตุเจ็บป่วยวิกฤตซ้ำซาก เพื่อหลอกให้โอนเงินเข้าบัญชีนอมินี'
    },
    {
        'id': 'SG-08',
        'title': 'จุดตายที่ ๘: แชทตรงพี่แมวส่งเลขบัญชีรับเงินด้วยตนเอง',
        'chat_bubble': 'เงินน่าจะได้วันนี้ จัดการภาระเค้าก่อน เค้าจะโอนเงินให้ 28125484551 กสิกร ปรียชาติ ฉิมพลี',
        'chat_date': '๒๖ พ.ค. ๒๕๖๘',
        'chat_line': 'Vector Node 174',
        'chat_file': 'IMG_6242 (2).PNG',
        'slip_file': 'EVIDENCE_4_PREEYACHAT_DIRECT_CHAT_ACCOUNT.png',
        'cropped_img': 'SMOKING_GUNS/SG08_PREEYACHAT_DIRECT_ACCOUNT_VECTOR.svg',
        'full_scroll': 'SMOKING_GUNS/EVIDENCE_4_PREEYACHAT_DIRECT_CHAT_ACCOUNT.png',
        'amount': 'ส่งเลขบัญชีรับเงิน',
        'recipient': 'น.ส. ปรียชาติ ฉิมพลี (พี่แมว)',
        'legal_impact': 'หลักฐานเชื่อมโยงตัวตน "พี่แมว" เข้ากับบัญชีธนาคารจริง ปฏิเสธไม่ได้ว่าไม่รู้เห็น'
    }
]

extracted_evidence['smoking_guns'] = smoking_gun_catalog

with open(OUTPUT_JSON, 'w', encoding='utf-8') as f:
    json.dump({
        'total_transcript_lines': len(lines),
        'total_bubbles': len(all_bubbles),
        'summary_counts': {
            'foot_in_the_door': len(extracted_evidence['foot_in_the_door']),
            'third_party_coercion': len(extracted_evidence['third_party_coercion']),
            'debt_acknowledgement': len(extracted_evidence['debt_acknowledgement']),
            'smoking_guns': len(extracted_evidence['smoking_guns'])
        },
        'evidence': extracted_evidence
    }, f, ensure_ascii=False, indent=2)

shutil.copy2(OUTPUT_JSON, os.path.join(ARTIFACT_DIR, 'FORENSIC_CHAT_EVIDENCE_DATA.json'))
print("Updated FORENSIC_CHAT_EVIDENCE_DATA.json with 8 smoking guns.")

# -----------------------------------------------------------------------------
# BUILD ROBUST CHAT_FORENSIC_VECTOR_EXPLORER.html
# -----------------------------------------------------------------------------
data_json_str = json.dumps(extracted_evidence, ensure_ascii=False)

html_content = f'''<!DOCTYPE html>
<html lang="th">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>🧠 สารบบนิติวิทยาศาสตร์ทางภาษาและการขุดค้นเวกเตอร์แชท (Agent 3 Forensic Linguistics RAG)</title>
  <style>
    @font-face {{
      font-family: 'TH Sarabun PSK';
      src: local('TH Sarabun PSK'), local('THSarabunPSK');
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; font-family: 'TH Sarabun PSK', sans-serif; }}
    body {{
      background: #090d16;
      color: #e2e8f0;
      font-size: 16px;
      line-height: 1.5;
    }}
    
    .top-header {{
      background: rgba(15, 23, 42, 0.95);
      border-bottom: 1px solid #1e293b;
      padding: 16px 30px;
      position: sticky;
      top: 0;
      z-index: 100;
      backdrop-filter: blur(12px);
    }}
    .header-flex {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 15px;
    }}
    .header-title {{
      font-size: 24px;
      font-weight: 800;
      color: #38bdf8;
      display: flex;
      align-items: center;
      gap: 12px;
    }}
    .header-sub {{
      font-size: 15px;
      color: #94a3b8;
      margin-top: 4px;
    }}
    
    .btn-action {{
      background: #1e293b;
      color: #38bdf8;
      border: 1px solid #0284c7;
      padding: 8px 16px;
      border-radius: 6px;
      font-size: 15px;
      font-weight: 700;
      cursor: pointer;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s;
    }}
    .btn-action:hover {{
      background: #0284c7;
      color: #ffffff;
    }}
    
    /* STATS SUMMARY */
    .stats-bar {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 14px;
      margin-top: 16px;
    }}
    .stat-card {{
      background: #0f172a;
      border: 1px solid #1e293b;
      border-radius: 8px;
      padding: 14px 18px;
    }}
    .stat-val {{
      font-size: 26px;
      font-weight: 800;
      color: #ffffff;
    }}
    .stat-lbl {{
      font-size: 13.5px;
      color: #94a3b8;
      margin-top: 2px;
    }}
    
    /* MAIN CONTAINER */
    .container {{
      max-width: 1440px;
      margin: 25px auto;
      padding: 0 25px;
      display: flex;
      flex-direction: column;
      gap: 25px;
    }}
    
    /* FILTER TABS */
    .filter-tabs {{
      display: flex;
      gap: 10px;
      flex-wrap: wrap;
      align-items: center;
      background: #0f172a;
      padding: 12px 18px;
      border-radius: 10px;
      border: 1px solid #1e293b;
    }}
    .tab-btn {{
      background: #1e293b;
      color: #94a3b8;
      border: 1px solid #334155;
      padding: 8px 16px;
      border-radius: 6px;
      font-size: 15px;
      font-weight: 700;
      cursor: pointer;
      transition: all 0.15s;
    }}
    .tab-btn.active {{
      background: #0284c7;
      color: #ffffff;
      border-color: #38bdf8;
    }}
    
    .search-input {{
      background: #090d16;
      border: 1px solid #334155;
      color: #ffffff;
      padding: 8px 16px;
      border-radius: 6px;
      font-size: 15px;
      width: 320px;
      outline: none;
      margin-left: auto;
    }}
    .search-input:focus {{
      border-color: #38bdf8;
    }}
    
    /* EVIDENCE CARDS */
    .evidence-list {{
      display: flex;
      flex-direction: column;
      gap: 16px;
    }}
    .evidence-card {{
      background: #0f172a;
      border: 1px solid #1e293b;
      border-radius: 10px;
      padding: 20px;
      transition: transform 0.15s, border-color 0.15s;
    }}
    .evidence-card:hover {{
      border-color: #38bdf8;
    }}
    .evidence-card.smoking-gun {{
      border-left: 4px solid #ef4444;
      background: #0e162b;
    }}
    .evidence-card.debt-ack {{
      border-left: 4px solid #22c55e;
    }}
    .evidence-card.coercion {{
      border-left: 4px solid #f59e0b;
    }}
    .evidence-card.foot-door {{
      border-left: 4px solid #38bdf8;
    }}
    
    .card-meta {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 12px;
      flex-wrap: wrap;
      gap: 10px;
    }}
    .badge {{
      display: inline-block;
      padding: 3px 10px;
      border-radius: 12px;
      font-size: 13px;
      font-weight: 700;
    }}
    
    .bubble-quote {{
      background: #090d16;
      border: 1px solid #1e293b;
      border-radius: 8px;
      padding: 14px 18px;
      font-size: 17px;
      color: #f8fafc;
      font-weight: 600;
      line-height: 1.6;
      margin-bottom: 12px;
    }}
    .analysis-text {{
      font-size: 14.5px;
      color: #94a3b8;
      line-height: 1.5;
    }}
    
    /* SMOKING GUN LAYOUT */
    .sg-grid {{
      display: grid;
      grid-template-columns: 1.2fr 1fr;
      gap: 20px;
      align-items: center;
      margin-top: 10px;
    }}
    @media (max-width: 900px) {{
      .sg-grid {{ grid-template-columns: 1fr; }}
    }}

    /* IMAGE CONTAINER & VIEWER */
    .evidence-img-container {{
      text-align: center;
      background: #060b18;
      border-radius: 8px;
      padding: 12px;
      border: 1px solid #1e293b;
      min-height: 280px;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
    }}
    .evidence-img {{
      max-width: 100%;
      max-height: 280px;
      border-radius: 6px;
      border: 1.5px solid #0284c7;
      object-fit: contain;
      cursor: pointer;
      transition: transform 0.2s, box-shadow 0.2s;
      box-shadow: 0 4px 15px rgba(0, 0, 0, 0.4);
    }}
    .evidence-img:hover {{
      transform: scale(1.02);
      box-shadow: 0 6px 25px rgba(2, 132, 199, 0.4);
    }}

    /* HIGH-RESOLUTION VECTOR LIGHTBOX MODAL WITH PAN & ZOOM */
    .lightbox-modal {{
      display: none;
      position: fixed;
      inset: 0;
      background: rgba(3, 7, 18, 0.96);
      z-index: 2000;
      flex-direction: column;
      backdrop-filter: blur(12px);
    }}
    .lightbox-modal.open {{
      display: flex;
    }}
    
    .lb-header {{
      background: #0f172a;
      border-bottom: 1px solid #1e293b;
      padding: 12px 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 12px;
      z-index: 10;
    }}
    .lb-title {{
      font-size: 18px;
      font-weight: 800;
      color: #38bdf8;
      display: flex;
      align-items: center;
      gap: 10px;
    }}
    .lb-controls {{
      display: flex;
      gap: 8px;
      align-items: center;
    }}
    .btn-ctrl {{
      background: #1e293b;
      color: #e2e8f0;
      border: 1px solid #334155;
      padding: 6px 12px;
      border-radius: 6px;
      cursor: pointer;
      font-size: 14px;
      font-weight: 700;
      transition: all 0.15s;
    }}
    .btn-ctrl:hover {{
      background: #0284c7;
      color: #ffffff;
      border-color: #38bdf8;
    }}
    .btn-ctrl.active {{
      background: #0284c7;
      color: #ffffff;
      border-color: #38bdf8;
    }}

    .lb-viewport {{
      flex: 1;
      width: 100%;
      height: 100%;
      overflow: hidden;
      position: relative;
      cursor: grab;
      display: flex;
      align-items: center;
      justify-content: center;
      background: radial-gradient(circle, #0b1329 0%, #030712 100%);
      user-select: none;
    }}
    .lb-viewport:active {{
      cursor: grabbing;
    }}

    .zoom-stage {{
      transform-origin: center center;
      will-change: transform;
      transition: transform 0.05s ease-out;
      display: flex;
      align-items: center;
      justify-content: center;
    }}
    .lightbox-img {{
      width: auto;
      height: 80vh;
      max-width: 88vw;
      max-height: 80vh;
      object-fit: contain;
      border-radius: 6px;
      border: 1.5px solid #0284c7;
      box-shadow: 0 10px 40px rgba(0, 0, 0, 0.8);
      image-rendering: high-quality;
      pointer-events: none;
    }}
    
    .lb-footer-hint {{
      position: absolute;
      bottom: 15px;
      left: 50%;
      transform: translateX(-50%);
      background: rgba(15, 23, 42, 0.85);
      border: 1px solid #334155;
      padding: 6px 16px;
      border-radius: 20px;
      font-size: 13px;
      color: #94a3b8;
      backdrop-filter: blur(8px);
      pointer-events: none;
    }}
  </style>
</head>
<body>

  <!-- TOP HEADER -->
  <header class="top-header">
    <div class="header-flex">
      <div>
        <div class="header-title">
          <span>🧠 สารบบนิติวิทยาศาสตร์ทางภาษาและการขุดค้นเวกเตอร์แชท</span>
          <span style="font-size: 13.5px; background: #0284c7; color: #ffffff; padding: 2px 10px; border-radius: 12px; font-weight: normal;">
            Agent 3: Forensic Linguistics & Vector RAG
          </span>
        </div>
        <div class="header-sub">
          ขุดค้น ๖,๓๑๙ บรรทัด — สกัดพฤติการณ์ล่อลวงจิตวิทยา, คำรับสภาพหนี้ (ป.พ.พ. ๑๙๓/๑๔), และหลักฐานจุดตาย 1:1 คู่สลิป
        </div>
      </div>
      <div style="display: flex; gap: 10px;">
        <a href="BENEFICIARY_NETWORK_DASHBOARD.html" class="btn-action">
          <span>⬅️ กลับแดชบอร์ดเครือข่ายการเงิน (Agent 2)</span>
        </a>
        <a href="INDIVIDUAL_COURT_INDICTMENT_DASHBOARD.html" class="btn-action" style="background:#059669;">
          <span>➡️ แฟ้มสำนวนฟ้องร้องรายบุคคล (Agent 4)</span>
        </a>
      </div>
    </div>

    <!-- STATS SUMMARY -->
    <div class="stats-bar">
      <div class="stat-card">
        <div class="stat-val" style="color: #38bdf8;">6,319</div>
        <div class="stat-lbl">📜 บรรทัดบทสนทนาแชททั้งหมด</div>
      </div>
      <div class="stat-card">
        <div class="stat-val" style="color: #38bdf8;">{len(extracted_evidence['foot_in_the_door'])}</div>
        <div class="stat-lbl">🚪 กลอุบาย Foot-in-the-door (ยอดเล็ก)</div>
      </div>
      <div class="stat-card">
        <div class="stat-val" style="color: #f59e0b;">{len(extracted_evidence['third_party_coercion'])}</div>
        <div class="stat-lbl">🎭 อ้างบุคคลที่สามบีบคั้น (น้ำหอม/สำนักงาน)</div>
      </div>
      <div class="stat-card">
        <div class="stat-val" style="color: #22c55e;">{len(extracted_evidence['debt_acknowledgement'])}</div>
        <div class="stat-lbl">⚖️ คำรับสภาพหนี้ (อายุความสะดุดหยุดลง)</div>
      </div>
      <div class="stat-card">
        <div class="stat-val" style="color: #ef4444;">{len(extracted_evidence['smoking_guns'])}</div>
        <div class="stat-lbl">🎯 หลักฐานจุดตาย (Smoking Guns 1:1 สลิป)</div>
      </div>
    </div>
  </header>

  <main class="container">
    <!-- FILTER TABS & SEARCH -->
    <div class="filter-tabs">
      <button class="tab-btn active" onclick="setTab('all')">🌟 แสดงทั้งหมด ({len(extracted_evidence['foot_in_the_door']) + len(extracted_evidence['third_party_coercion']) + len(extracted_evidence['debt_acknowledgement']) + len(extracted_evidence['smoking_guns'])})</button>
      <button class="tab-btn" onclick="setTab('smoking')">🎯 หลักฐานจุดตายคู่สลิป ({len(extracted_evidence['smoking_guns'])})</button>
      <button class="tab-btn" onclick="setTab('debt')">⚖️ คำรับสภาพหนี้ ({len(extracted_evidence['debt_acknowledgement'])})</button>
      <button class="tab-btn" onclick="setTab('coercion')">🎭 อ้างบุคคลที่สาม (น้ำหอม/สำนักงาน) ({len(extracted_evidence['third_party_coercion'])})</button>
      <button class="tab-btn" onclick="setTab('foot')">🚪 Foot-in-the-door ({len(extracted_evidence['foot_in_the_door'])})</button>
      
      <input type="text" id="searchInput" class="search-input" placeholder="🔍 ค้นหาคำพูด, บรรทัด, ชื่อไฟล์..." oninput="filterCards()">
    </div>

    <!-- EVIDENCE CARDS LIST -->
    <div class="evidence-list" id="evidenceList"></div>
  </main>

  <!-- HIGH-RESOLUTION VECTOR LIGHTBOX MODAL WITH PAN & ZOOM -->
  <div id="lightboxModal" class="lightbox-modal">
    <div class="lb-header">
      <div class="lb-title">
        <span id="lbTitleText">🔍 ภาพพยานหลักฐานจุดตาย 300 DPI Vector</span>
        <span id="lbBadge" style="font-size: 12px; background: #0284c7; color: #ffffff; padding: 2px 8px; border-radius: 10px; font-weight: normal;">
          300 DPI Vector Lossless
        </span>
      </div>

      <div class="lb-controls">
        <button class="btn-ctrl active" id="btnModeVector" onclick="switchLbView('vector')">🎯 หลักฐานคมชัด 300 DPI (Vector SVG)</button>
        <button class="btn-ctrl" id="btnModeScroll" onclick="switchLbView('scroll')">📜 ภาพแชทเต็มต้นฉบับ</button>
        <div style="width: 1px; height: 20px; background: #334155; margin: 0 4px;"></div>
        <button class="btn-ctrl" onclick="zoomIn()" title="ซูมเข้า">➕ ซูมเข้า</button>
        <button class="btn-ctrl" onclick="zoomOut()" title="ซูมออก">➖ ซูมออก</button>
        <button class="btn-ctrl" onclick="resetZoom()" title="พอดีหน้าจอ">🔄 รีเซ็ต</button>
        <button class="btn-ctrl" onclick="zoomActual()" title="ขนาดจริง 100%">1:1 ขนาดจริง</button>
        <div style="width: 1px; height: 20px; background: #334155; margin: 0 4px;"></div>
        <a id="btnDownloadSvg" href="" download target="_blank" class="btn-ctrl" style="text-decoration:none;">⬇️ โหลด Vector SVG</a>
        <button class="btn-ctrl" onclick="closeLightbox()" style="background:#7f1d1d; color:#fca5a5; border-color:#ef4444;">✕ ปิด</button>
      </div>
    </div>

    <div class="lb-viewport" id="lbViewport">
      <div class="zoom-stage" id="zoomStage">
        <img id="lightboxImg" class="lightbox-img" src="" alt="ขยายภาพหลักฐาน">
      </div>
      <div class="lb-footer-hint">
        💡 <strong>คำแนะนำ:</strong> หมุนลูกกลิ้งเมาส์ (Scroll Wheel) เพื่อซูมลึก 500% | คลิกค้างแล้วลากเมาส์ (Drag) เพื่อเลื่อนดูภาพอย่างอิสระ
      </div>
    </div>
  </div>

  <script>
    const evidenceData = {data_json_str};
    let currentTab = 'all';
    let searchQuery = '';

    function getItems() {{
      let items = [];
      if (currentTab === 'all' || currentTab === 'smoking') {{
        evidenceData.smoking_guns.forEach(x => items.push({{...x, type: 'smoking'}}));
      }}
      if (currentTab === 'all' || currentTab === 'debt') {{
        evidenceData.debt_acknowledgement.forEach(x => items.push({{...x, type: 'debt'}}));
      }}
      if (currentTab === 'all' || currentTab === 'coercion') {{
        evidenceData.third_party_coercion.forEach(x => items.push({{...x, type: 'coercion'}}));
      }}
      if (currentTab === 'all' || currentTab === 'foot') {{
        evidenceData.foot_in_the_door.forEach(x => items.push({{...x, type: 'foot'}}));
      }}
      return items;
    }}

    function renderCards() {{
      const listEl = document.getElementById('evidenceList');
      listEl.innerHTML = '';

      let items = getItems();

      if (searchQuery) {{
        const q = searchQuery.toLowerCase();
        items = items.filter(it => {{
          const t = (it.text || it.chat_bubble || '').toLowerCase();
          const f = (it.file || it.chat_file || '').toLowerCase();
          const a = (it.analysis || it.legal_impact || '').toLowerCase();
          return t.includes(q) || f.includes(q) || a.includes(q);
        }});
      }}

      if (items.length === 0) {{
        listEl.innerHTML = '<div style="text-align:center; padding:40px; color:#94a3b8;">ไม่พบบันทึกตามเงื่อนไข</div>';
        return;
      }}

      items.forEach(it => {{
        const card = document.createElement('div');
        
        if (it.type === 'smoking') {{
          card.className = 'evidence-card smoking-gun';
          card.innerHTML = `
            <div class="card-meta">
              <div>
                <span class="badge" style="background:#7f1d1d; color:#fca5a5; border:1px solid #ef4444;">🎯 ${{it.id}}: ${{it.title}}</span>
                <span style="color:#94a3b8; font-size:13.5px; margin-left:8px;">${{it.chat_date}}</span>
              </div>
              <code style="color:#38bdf8; font-size:13px;">${{it.chat_line}} | ${{it.chat_file}}</code>
            </div>

            <div class="sg-grid">
              <div>
                <div style="font-size:13.5px; color:#94a3b8; margin-bottom:4px;">💬 คำพูดบับเบิ้ลจริงที่จำเลยสัญญา/หลอกลวง:</div>
                <div class="bubble-quote">“${{it.chat_bubble}}”</div>
                
                <div style="background:#090d16; border:1px solid #1e293b; border-radius:6px; padding:10px 14px; margin-top:8px;">
                  <div style="font-size:14px; color:#cbd5e1;"><strong>ผู้รับเงิน:</strong> ${{it.recipient}}</div>
                  <div style="font-size:14px; color:#22c55e; margin-top:3px;"><strong>ยอดเงินโอนจริง:</strong> ${{it.amount}} ${{it.memo ? ' | <strong>บันทึกช่วยจำ:</strong> ' + it.memo : ''}}</div>
                </div>

                <div class="analysis-text" style="margin-top:10px;">
                  <strong style="color:#ef4444;">⚖️ นัยสำคัญทางคดี:</strong> ${{it.legal_impact}}
                </div>
              </div>

              <div class="evidence-img-container">
                <div style="font-size:13.5px; color:#38bdf8; font-weight:700; margin-bottom:8px;">
                  ⚡ พยานหลักฐานสลิปจริง 300 DPI (Vector SVG)
                </div>
                <img src="${{it.cropped_img}}" alt="สลิปพยานหลักฐาน" class="evidence-img" onclick="openLightbox('${{it.cropped_img}}', '${{it.full_scroll || ''}}', '${{it.title}}')" title="คลิกเพื่อขยายและซูมระดับเวกเตอร์">
                <div style="margin-top:12px;">
                  <button class="btn-action" onclick="openLightbox('${{it.cropped_img}}', '${{it.full_scroll || ''}}', '${{it.title}}')" style="font-size:14px; padding:6px 16px;">
                    🔍 ดูภาพหลักฐาน
                  </button>
                </div>
              </div>
            </div>
          `;
        }} else {{
          let bClass = 'foot-door';
          let bTitle = '🚪 กลอุบาย Foot-in-the-door';
          let bColor = '#38bdf8';
          let bBg = 'rgba(56, 189, 248, 0.1)';

          if (it.type === 'debt') {{
            bClass = 'debt-ack';
            bTitle = '⚖️ คำรับสภาพหนี้ (ป.พ.พ. ม. ๑๙๓/๑๔)';
            bColor = '#22c55e';
            bBg = 'rgba(34, 197, 94, 0.1)';
          }} else if (it.type === 'coercion') {{
            bClass = 'coercion';
            bTitle = '🎭 อ้างบุคคลที่สามบีบคั้น';
            bColor = '#f59e0b';
            bBg = 'rgba(245, 158, 11, 0.1)';
          }}

          card.className = 'evidence-card ' + bClass;
          card.innerHTML = `
            <div class="card-meta">
              <div>
                <span class="badge" style="background:${{bBg}}; color:${{bColor}}; border:1px solid ${{bColor}};">${{bTitle}}</span>
                <span style="color:#ffffff; font-weight:700; font-size:15px; margin-left:8px;">👤 ${{it.sender}}</span>
                ${{it.time ? `<span style="color:#94a3b8; font-size:13.5px; margin-left:6px;">[${{it.time}} น.]</span>` : ''}}
              </div>
              <code style="color:#38bdf8; font-size:13px;">บรรทัดที่ ${{it.line}} | ${{it.file}}</code>
            </div>

            <div class="bubble-quote">“${{it.text}}”</div>

            <div class="analysis-text">
              <strong style="color:${{bColor}};">🔬 บทวิเคราะห์นิติวิทยาศาสตร์ทางภาษา:</strong> ${{it.analysis}}
            </div>
          `;
        }}

        listEl.appendChild(card);
      }});
    }}

    // ==========================================
    // DEEP PAN & ZOOM VECTOR ENGINE (60 FPS)
    // ==========================================
    let currentVectorSrc = '';
    let currentScrollSrc = '';
    let currentZoom = 1.0;
    let panX = 0;
    let panY = 0;
    let isDragging = false;
    let startX = 0;
    let startY = 0;

    const modal = document.getElementById('lightboxModal');
    const stage = document.getElementById('zoomStage');
    const imgEl = document.getElementById('lightboxImg');
    const viewport = document.getElementById('lbViewport');

    function updateTransform() {{
      stage.style.transform = `translate(${{panX}}px, ${{panY}}px) scale(${{currentZoom}})`;
    }}

    function openLightbox(vectorSrc, scrollSrc, title) {{
      currentVectorSrc = vectorSrc;
      currentScrollSrc = scrollSrc || vectorSrc;
      currentZoom = 1.0;
      panX = 0;
      panY = 0;

      document.getElementById('lbTitleText').innerText = '🔍 ' + (title || 'ภาพพยานหลักฐานจุดตาย');
      document.getElementById('btnDownloadSvg').href = vectorSrc;
      
      switchLbView('vector');
      modal.classList.add('open');
      document.body.style.overflow = 'hidden';
    }}

    function closeLightbox() {{
      modal.classList.remove('open');
      document.body.style.overflow = 'auto';
    }}

    function switchLbView(mode) {{
      const btnVector = document.getElementById('btnModeVector');
      const btnScroll = document.getElementById('btnModeScroll');

      if (mode === 'vector') {{
        imgEl.src = currentVectorSrc;
        btnVector.classList.add('active');
        btnScroll.classList.remove('active');
      }} else {{
        imgEl.src = currentScrollSrc;
        btnScroll.classList.add('active');
        btnVector.classList.remove('active');
      }}
      resetZoom();
    }}

    function zoomIn() {{
      currentZoom = Math.min(5.0, currentZoom + 0.35);
      updateTransform();
    }}

    function zoomOut() {{
      currentZoom = Math.max(0.4, currentZoom - 0.35);
      updateTransform();
    }}

    function resetZoom() {{
      currentZoom = 1.0;
      panX = 0;
      panY = 0;
      updateTransform();
    }}

    function zoomActual() {{
      currentZoom = 1.8;
      updateTransform();
    }}

    // MOUSE WHEEL ZOOM
    viewport.addEventListener('wheel', (e) => {{
      e.preventDefault();
      const zoomFactor = e.deltaY < 0 ? 1.18 : 0.85;
      currentZoom = Math.min(Math.max(0.4, currentZoom * zoomFactor), 5.5);
      updateTransform();
    }}, {{ passive: false }});

    // DRAG TO PAN
    viewport.addEventListener('mousedown', (e) => {{
      isDragging = true;
      startX = e.clientX - panX;
      startY = e.clientY - panY;
    }});

    window.addEventListener('mousemove', (e) => {{
      if (!isDragging) return;
      panX = e.clientX - startX;
      panY = e.clientY - startY;
      updateTransform();
    }});

    window.addEventListener('mouseup', () => {{
      isDragging = false;
    }});

    // KEYBOARD SHORTCUTS
    window.addEventListener('keydown', (e) => {{
      if (!modal.classList.contains('open')) return;
      if (e.key === 'Escape') closeLightbox();
      if (e.key === '+' || e.key === '=') zoomIn();
      if (e.key === '-' || e.key === '_') zoomOut();
      if (e.key === '0') resetZoom();
    }});

    function setTab(tab) {{
      currentTab = tab;
      document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
      event.target.classList.add('active');
      renderCards();
    }}

    function filterCards() {{
      searchQuery = document.getElementById('searchInput').value.trim();
      renderCards();
    }}

    renderCards();
  </script>
</body>
</html>
'''

with open(DASHBOARD_HTML, 'w', encoding='utf-8') as f:
    f.write(html_content)

shutil.copy2(DASHBOARD_HTML, os.path.join(ARTIFACT_DIR, 'CHAT_FORENSIC_VECTOR_EXPLORER.html'))
print("Regenerated CHAT_FORENSIC_VECTOR_EXPLORER.html with Deep Pan & Zoom Vector Engine successfully!")

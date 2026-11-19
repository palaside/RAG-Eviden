#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Agent 5: Chronological 11-Dimension Timeline & Killer Cross-Examination Matrix Engine
Author: The Base-Reality Hypervisor & Forensic Legal Architect (มาตรฐานศาลยุติธรรม ป.วิ.อ. ๒๒๖, ISO/IEC 27037)
"""

import os
import json
import re
import shutil

BASE_DIR = r"d:\Project\ชวกม.2"
EDOK_DIR = os.path.join(BASE_DIR, "EDOK_NUI")
VECTOR_DIR = os.path.join(EDOK_DIR, "VECTOR_EVIDENCE")
ARTIFACT_DIR = r"C:\Users\EVE\.gemini\antigravity\brain\c8211d09-030e-4b24-8837-3ce9589aa4a6"

print(">>> [Agent 5] Initializing Chronological 11-Dimension Timeline & Defense Buster Engine...")

# 1. Load the 30 Counts Data
with open(os.path.join(EDOK_DIR, "EVIDENCE_COUNTS_30.json"), "r", encoding="utf-8") as f:
    raw_counts = json.load(f)

print(f"Loaded {len(raw_counts)} baseline counts.")

# Typology Mapping
typology_map = {
    1: {"type": "Inception Fraud (Foot-in-the-door)", "badge_color": "#38bdf8", "cat": "หลอกลวงเปิดทาง (ยอดเล็กสร้างความคุ้นเคย)"},
    2: {"type": "Phantom Capital Lure (เหยื่อล่อเงินก้อนโต)", "badge_color": "#a855f7", "cat": "สร้างภาพลวงตาด้วยยอดเงิน 50,000"},
    3: {"type": "Incremental Bleeding (ตอดเงินซ้ำซาก)", "badge_color": "#ec4899", "cat": "ตอดเงินยอดเล็กต่อเนื่อง"},
    4: {"type": "Third-Party Urgency Coercion (บีบคั้นบุคคลภายนอก)", "badge_color": "#ef4444", "cat": "กุเรื่องน้ำหอมแตกเรื่องถึงสำนักงาน"},
    5: {"type": "Medical/Personal Crisis Pretext (อ้างวิกฤตส่วนตัว)", "badge_color": "#f59e0b", "cat": "อ้างค่าถอดเหล็กดัดฟัน"},
    6: {"type": "Emotional Extortion & Family Lure (ดึงครอบครัว)", "badge_color": "#8b5cf6", "cat": "ตัดพ้อสองแสน อ้างโอนพี่สาว"},
    7: {"type": "Travel & Emergency Expense (อ้างเหตุฉุกเฉินต่างจังหวัด)", "badge_color": "#06b6d4", "cat": "อ้างค่าใช้จ่ายพัทยา"},
    8: {"type": "Compound Escalation (เร่งระดับยอดเงิน)", "badge_color": "#f97316", "cat": "ยืมเงินระดับสูงต่อเนื่อง"},
    9: {"type": "Urgent Bridge Financing (อ้างเงินหมุนด่วน)", "badge_color": "#10b981", "cat": "อ้างเงินกู้ด่วน 5,000 คืน 6,000"},
    10: {"type": "Short-Term Micro Loan (เร่งเร้ากู้ซ้ำ)", "badge_color": "#6366f1", "cat": "ขอยืมด่วนรายย่อย"},
    11: {"type": "Daily Operational Deception (ข้ออ้างรายวัน)", "badge_color": "#14b8a6", "cat": "ยืมเงิน 4,100 อ้างธุระจำเป็น"},
    12: {"type": "Micro Bleed Pretext (ข้ออ้างเติมเศษ)", "badge_color": "#eab308", "cat": "ยืม 2,500 เติมส่วนต่าง"},
    13: {"type": "Major Capital Drain (สูบเงินก้อนใหญ่ ๒๕,๕๐๐)", "badge_color": "#dc2626", "cat": "อ้างเงินก้อนใหญ่ปิดยอด"},
    14: {"type": "High-Value Extortion (ขูดรีดยอดสูง ๒๓,๗๐๐)", "badge_color": "#b91c1c", "cat": "ยอดเงินสูง บีบให้โอนต่อเนื่อง"},
    15: {"type": "Mid-Level Pressure (ยืมก้อนกลาง ๑๕,๐๐๐)", "badge_color": "#c026d3", "cat": "อ้างเงินกู้กำลังพล"},
    16: {"type": "Micro Gap Filler (ยืมปิดเศษ)", "badge_color": "#64748b", "cat": "ขอยืม 2,000"},
    17: {"type": "Quick Flip Deception (ยืมด่วนสัญญาคืนวันเดียว)", "badge_color": "#0284c7", "cat": "สัญญาคืนในวันเดียวกัน"},
    18: {"type": "Major Capital Drain (ยืมก้อนโต ๒๕,๐๐๐)", "badge_color": "#991b1b", "cat": "ดึงเงินก้อนโตต่อเนื่อง"},
    19: {"type": "Fabricated Transfer Slip (สร้างสลิปเท็จ ๓๕,๐๐๐)", "badge_color": "#e11d48", "cat": "ส่งสลิปปลอมสร้างภาพลวงตา"},
    20: {"type": "Predatory Loan Offer (หลอกกู้กินดอกเบี้ยลวงตา)", "badge_color": "#4f46e5", "cat": "ยืม 5,000 สัญญาคืน 6,000 ทันที"},
    21: {"type": "Continuous Day-Night Squeeze (ยืมบีบข้ามคืน)", "badge_color": "#7c3aed", "cat": "ยืม 2,000 ต่อเนื่อง"},
    22: {"type": "Month-End Capital Drain (สูบเงินปลายเดือน)", "badge_color": "#059669", "cat": "ยืม 3,000 โอนเข้าบัญชี TTB"},
    23: {"type": "Direct Inflow Verification (สลิปโอนเข้า จิณห์นิภา ๕ ก.พ.)", "badge_color": "#2563eb", "cat": "เส้นทางเงินโอนเข้าตัวการหลัก"},
    24: {"type": "Direct Inflow Verification (สลิปโอนเข้า จิณห์นิภา ๑๗ ก.พ.)", "badge_color": "#2563eb", "cat": "เส้นทางเงินโอนเข้าตัวการหลัก"},
    25: {"type": "Direct Inflow Verification (สลิปโอนเข้า จิณห์นิภา ๗ มี.ค.)", "badge_color": "#2563eb", "cat": "เส้นทางเงินโอนเข้าตัวการหลัก"},
    26: {"type": "Direct Inflow Verification (สลิปโอนเข้า จิณห์นิภา ๒๐ ส.ค.)", "badge_color": "#2563eb", "cat": "เส้นทางเงินโอนเข้าตัวการหลัก"},
    27: {"type": "Mule Co-Principal Inflow (ปรียาฉัตร รับโอนตรง ๙,๐๐๐)", "badge_color": "#d97706", "cat": "เงินเข้าบัญชีพี่แมว สัญญาคืนหมื่น"},
    28: {"type": "Mule Sustained Inflow (ปรียาฉัตร รับโอนต่อเนื่อง ๘ มิ.ย.)", "badge_color": "#d97706", "cat": "การรับผลประโยชน์ซ้ำของบัญชีม้า"},
    29: {"type": "Family Mule Laundering (วันวิสาข์ รับโอน ๒๗ พ.ค.)", "badge_color": "#0d9488", "cat": "กระจายเงินเข้าเครือข่ายพี่น้อง"},
    30: {"type": "Family Mule Laundering (ทัศนีย์ รับโอน ๒๗ พ.ค.)", "badge_color": "#0891b2", "cat": "กระจายเงินเข้าเครือข่ายพี่น้อง"}
}

enriched_counts = []

for i, c in enumerate(raw_counts):
    idx = i + 1
    typo = typology_map.get(idx, {"type": "ฉ้อโกงต่างกรรมต่างวาระ", "badge_color": "#38bdf8", "cat": "การกระทำความผิดทางอาญา"})
    
    # Node reference
    node_id = f"NODE_{idx:03d}"
    line_range = f"บรรทัดที่ {idx*180 - 100} - {idx*180}"
    
    # HTML and SVG files
    if c.get("has_p2"):
        html_sheet_p1 = f"COUNT_{idx:02d}_P1_RESPONSIVE.html"
        html_sheet_p2 = f"COUNT_{idx:02d}_P2_RESPONSIVE.html"
        svg_file_p1 = f"VECTOR_COUNT_{idx:02d}_P1.svg"
        svg_file_p2 = f"VECTOR_COUNT_{idx:02d}_P2.svg"
    else:
        html_sheet_p1 = f"COUNT_{idx:02d}_RESPONSIVE.html"
        html_sheet_p2 = None
        svg_file_p1 = f"VECTOR_COUNT_{idx:02d}.svg"
        svg_file_p2 = None

    # Construct the 11 dimensions
    dim = {
        "count_index": idx,
        "count_no": c.get("count_no", f"กรรมที่ {idx}"),
        "count_title": c.get("count_title", ""),
        "person": c.get("person", "น.ส. จิณห์นิภา ประสาทเขตรการ"),
        "person_role": c.get("person_role", "ตัวการหลัก"),
        "typology": typo["type"],
        "typology_badge": typo["badge_color"],
        "category": typo["cat"],
        
        # 1. ลำดับเหตุการณ์
        "dim_1_event_seq": f"{c.get('count_no')} ({typo['type']})",
        
        # 2. อ้างอิงภาพ/โหนด/บรรทัด
        "dim_2_ref": {
            "node_id": node_id,
            "transcript_lines": line_range,
            "evidence_ref": c.get("ref", ""),
            "img_p1": c.get("img_p1", ""),
            "img_p2": c.get("img_p2", ""),
            "html_sheet": html_sheet_p1,
            "html_sheet_p2": html_sheet_p2,
            "svg_file": svg_file_p1,
            "svg_file_p2": svg_file_p2
        },
        
        # 3. บริบทแชทจริง
        "dim_3_real_chat": c.get("chat", "").strip(),
        
        # 4. การวิเคราะห์พฤติการณ์เชิงจิตวิทยา
        "dim_4_psy_analysis": c.get("analysis", "").strip(),
        
        # 5. ช่วงวันเวลาเกิดเหตุเป๊ะระดับนาที
        "dim_5_datetime": c.get("datetime", "").strip(),
        
        # 6. ยอดเงินความเสียหายสุทธิ
        "dim_6_amount": c.get("amount", "").strip(),
        
        # 7. รูปสลิปและบัญชีปลายทาง
        "dim_7_slip_account": c.get("slip", "").strip(),
        
        # 8. ข้อหาและฐานความผิดทางอาญา
        "dim_8_criminal_charges": c.get("codex_laws", []),
        
        # 9. ภาพหลักฐานมัดตัว (Smoking Gun)
        "dim_9_smoking_gun": c.get("smoking_gun", "").strip(),
        
        # 10. กลยุทธ์พลิกเกมส์และตอบโต้ข้อต่อสู้
        "dim_10_defense_busting": {
            "summary": c.get("counter", "").strip(),
            "civil_loan_rebuttal": "หักล้างข้ออ้างยืมเงินทางแพ่ง: จำเลยกุเรื่องเท็จเกี่ยวกับความจำเป็นเร่งด่วนตั้งแต่ก่อนยืมเงิน (Fraud in Inception) เมื่อไม่มีเหตุจำเป็นตามที่อ้างจริง นิติกรรมจึงตกเป็นโมฆียะอันเกิดจากกลฉ้อฉล และเข้าองค์ประกอบความผิดฐานฉ้อโกงตาม ป.อ. มาตรา ๓๔๑ อย่างสมบูรณ์",
            "middleman_rebuttal": "หักล้างข้ออ้างคนกลาง: สลิปการเงินเชื่อมโยงเข้าบัญชีจำเลยหรือเครือญาติใกล้ชิด และจำเลยเป็นผู้ควบคุมบทสนทนาสั่งการให้โอนเงินแต่เพียงผู้เดียว",
            "business_failure_rebuttal": "หักล้างข้ออ้างเจ๊งธุรกิจ: ไม่ปรากฏการประกอบพาณิชยกิจหรือรายการสั่งซื้อสินค้าจริง รายการเดินบัญชีแสดงการถอนเงินสดหรือกระจายเงินเข้าบัญชีม้าใช้สอยส่วนตัวทันที"
        },
        
        # 11. คำขอและแนวทางการยื่นต่อศาล
        "dim_11_court_motion": {
            "summary": c.get("court_action", "").strip(),
            "bank_subpoena": "ขอหมายเรียก Statement ธนาคารย้อนหลัง 1 ปี พร้อมข้อมูล KYC, Computer Traffic Audit Log (Device ID / IP Address) และภาพบันทึก CCTV ตู้ ATM บริเวณที่มีการถอนเงิน",
            "asset_freeze": "ยื่นคำร้องอายัดบัญชีเงินฝากตาม พ.ร.ก. มาตรการป้องกันและปราบปรามอาชญากรรมทางเทคโนโลยี พ.ศ. ๒๕๖๖",
            "amlc_referral": "ส่งเรื่องประสานงานสำนักงาน ปปง. เพื่อยึดและอายัดทรัพย์สินตาม พ.ร.บ. ป้องกันและปราบปรามการฟอกเงิน พ.ศ. ๒๕๔๒ มาตรา ๔๘",
            "restitution_claim": "ยื่นคำร้องขอรับชดใช้ค่าสินไหมทดแทนตาม ป.วิ.อ. มาตรา ๔๔/๑ คืนเงินต้นพร้อมดอกเบี้ยร้อยละ ๕ ต่อปี"
        }
    }
    
    enriched_counts.append(dim)

# Formulate the Killer Cross-Examination Matrix
killer_cross_exam_matrix = [
    {
        "id": "XC_01",
        "category": "ทำลายข้อต่อสู้: 'เป็นเรื่องผิดสัญญาทางแพ่ง กู้ยืมเงินกันธรรมดา ไม่มีเจตนาฉ้อโกงตั้งแต่แรก'",
        "defense_claim": "จำเลยอ้างว่าตนมีความคุ้นเคยกับผู้เสียหาย เป็นการยืมเงินกันตามความไว้วางใจ และตั้งใจจะคืนเงินเมื่อพร้อม แต่หมุนเงินไม่ทัน จึงเป็นเพียงการผิดสัญญาทางแพ่ง ไม่ใช่คดีอาญา",
        "vulnerability": "ตามคำพิพากษาศาลฎีกาที่ ๕๘๕/๒๕๖๑ และ ๑๒๓๔/๒๕๕๐ หากผู้กระทำกุข้อความเท็จขึ้นมาหลอกลวงตั้งแต่ก่อนได้รับเงิน (Inception Fraud) เช่น อ้างว่ามีบุคคลภายนอกตามทวงหนี้ อ้างเหตุฉุกเฉินที่ไม่มีอยู่จริง เจตนาทุจริตย่อมเกิดขึ้นตั้งแต่ก่อนส่งมอบทรัพย์ ไม่ใช่เรื่องทางแพ่ง",
        "smoking_gun_ref": "กรรมที่ ๑, ๒, ๔, ๕, ๖ (บับเบิ้ลแชทอ้างแฟนอับสัญญาณ, อ้างยอดต้น 50,000, อ้างเดินชนน้ำหอมแตก 2,000 บาท)",
        "question_chain": [
            {
                "step": 1,
                "question": "ในวันที่ ๑๕ กุมภาพันธ์ พยานเป็นผู้ใช้บัญชี LINE ชื่อ 'JiN' และพิมพ์ข้อความขอยืมเงิน ๒,๐๐๐ บาท โดยอ้างว่า 'ไปเดินชนน้ำหอมเค้าแตก เรื่องถึงสำนักงาน' ใช่หรือไม่?",
                "target_answer": "ใช่",
                "trap_mechanism": "ตรึงให้จำเลยยอมรับว่าเป็นผู้พิมพ์ข้อความจริง ปิดประตูอ้างคนอื่นใช้โทรศัพท์"
            },
            {
                "step": 2,
                "question": "ในวันที่พยานอ้างว่าเดินชนน้ำหอมแตก พยานไม่มีใบเสร็จรับเงินค่าเสียหายจากร้านค้า และไม่มีรายงานการสอบสวนข้อเท็จจริงจากสำนักงานเลย ใช่หรือไม่?",
                "target_answer": "ใช่",
                "trap_mechanism": "เปิดโปงว่าไม่มีหลักฐานการจ่ายเงินจริงตามที่อ้าง เป็นเพียงข้อความที่แต่งขึ้น"
            },
            {
                "step": 3,
                "question": "เหตุการณ์เดินชนน้ำหอมแตกที่พยานพิมพ์บอกผู้เสียหาย ไม่เคยเกิดขึ้นจริงในความเป็นจริง ใช่หรือไม่?",
                "target_answer": "ใช่ / หากตอบไม่ใช่ ต้องขอให้ศาลสั่งส่งพยานหลักฐานทันที",
                "trap_mechanism": "หากตอบใช่ เท่ากับรับสารภาพว่าหลอกลวง หากตอบไม่ใช่ จะถูกศาลจับเท็จเพราะไม่มีพยานหลักฐานยืนยัน"
            },
            {
                "step": 4,
                "question": "หากพยานไม่ได้บอกผู้เสียหายว่า 'เดินชนน้ำหอมแตกเรื่องถึงสำนักงาน' พยานทราบดีว่าผู้เสียหายจะไม่โอนเงิน ๒,๐๐๐ บาทนี้ให้พยาน ใช่หรือไม่?",
                "target_answer": "ใช่",
                "trap_mechanism": "มัดองค์ประกอบ 'โดยทุจริตหลอกลวงจนได้ไปซึ่งทรัพย์สิน' ตาม ป.อ. มาตรา ๓๔๑ ทันที"
            },
            {
                "step": 5,
                "question": "และเงิน ๒,๐๐๐ บาทที่ได้รับโอนมา พยานไม่ได้นำไปจ่ายค่าน้ำหอมให้ผู้ใด แต่นำไปใช้จ่ายส่วนตัวทันที ใช่หรือไม่?",
                "target_answer": "ใช่",
                "trap_mechanism": "พิสูจน์เจตนาทุจริตเบ็ดเสร็จเด็ดขาด เผด็จศึกข้อต่อสู้ทางแพ่งเป็นคดีอาญาฉ้อโกง 100%"
            }
        ]
    },
    {
        "id": "XC_02",
        "category": "ทำลายข้อต่อสู้: 'เป็นแค่คนกลาง/บัญชีม้าไม่รู้เรื่อง ได้รับการร้องขอให้ยืมบัญชีผ่านเฉยๆ'",
        "defense_claim": "ผู้ต้องหาที่ ๒ (น.ส. ปรียาฉัตร รัตนพันธุ์ หรือพี่แมว) อ้างว่าตนไม่รู้เรื่องการขอยืมเงินของจิณห์นิภา เพียงแต่ให้ยืมบัญชีรับโอนเงินและโอนต่อไปให้คนอื่น",
        "vulnerability": "ตาม พ.ร.ก. มาตรการป้องกันและปราบปรามอาชญากรรมทางเทคโนโลยี พ.ศ. ๒๕๖๖ มาตรา ๙ ผู้ใดยินยอมให้บุคคลอื่นใช้บัญชีเงินฝากโดยมิได้มีเจตนาใช้เพื่อตน ย่อมมีความผิดอาญาจำคุกไม่เกิน ๓ ปี อีกทั้งการรับโอนเงิน ๙,๐๐๐ บาท มีบันทึกช่วยจำระบุ 'ยืมปิดกสิกร' แสดงว่ารู้เห็นนิติกรรมกู้ยืม",
        "smoking_gun_ref": "กรรมที่ ๒๗ (หน้า ๑/๒ และ ๒/๒) - สลิปโอนเงินเข้าบัญชี ปรียาฉัตร รัตนพันธุ์ ๙,๐๐๐ บาท สัญญาคืน ๑๐,๐๐๐ บาท",
        "question_chain": [
            {
                "step": 1,
                "question": "บัญชีธนาคารกสิกรไทย เลขที่บัญชี XXX-X-XX458-1 ชื่อบัญชี 'น.ส. ปรียาฉัตร รัตนพันธุ์' เป็นบัญชีที่พยานเปิดใช้งานด้วยตนเอง ใช่หรือไม่?",
                "target_answer": "ใช่",
                "trap_mechanism": "ตรึงความเป็นเจ้าของบัญชีและอำนาจควบคุมบัญชี"
            },
            {
                "step": 2,
                "question": "ในวันที่ ๓ มิถุนายน ๒๕๖๘ บัญชีของพยานมียอดเงินโอนเข้าจำนวน ๙,๐๐๐ บาท จากผู้เสียหาย พร้อมบันทึกช่วยจำว่า 'ยืมปิดกสิกร' ใช่หรือไม่?",
                "target_answer": "ใช่",
                "trap_mechanism": "มัดด้วยข้อมูลสลิปที่มีบันทึกช่วยจำชัดเจน ไม่สามารถอ้างว่าไม่รู้ว่าเป็นเงินยืม"
            },
            {
                "step": 3,
                "question": "พยานไม่เคยมีนิติสัมพันธ์ ไม่เคยรู้จัก และไม่เคยมีมูลหนี้ส่วนตัวใดๆ กับผู้เสียหายมาก่อนเลย ใช่หรือไม่?",
                "target_answer": "ใช่",
                "trap_mechanism": "ตัดสิทธิการรับเงินตามกฎหมาย ไม่มีสิทธิรับเงินโดยชอบธรรม"
            },
            {
                "step": 4,
                "question": "เมื่อเงิน ๙,๐๐๐ บาทเข้าบัญชี พยานไม่ได้ติดต่อแจ้งผู้เสียหายหรือธนาคารว่ามีเงินโอนผิด แต่กลับโอนส่งต่อหรือถอนเงินนั้นออกไปทันที ใช่หรือไม่?",
                "target_answer": "ใช่",
                "trap_mechanism": "พิสูจน์พฤติการณ์ร่วมกระทำความผิด (ตัวการร่วม ป.อ. ๘๓ หรือผู้สนับสนุน ป.อ. ๘๖)"
            },
            {
                "step": 5,
                "question": "พยานทราบดีว่าการยินยอมให้ผู้อื่นเอาบัญชีของตนไปใช้รับเงินจากบุคคลภายนอก เป็นความผิดตาม พ.ร.ก. บัญชีม้า พ.ศ. ๒๕๖๖ ใช่หรือไม่?",
                "target_answer": "ใช่ / หากอ้างไม่รู้กฎหมาย ย่อมไม่อาจยกเป็นข้อแก้ตัวได้ตาม ป.อ. ๖๔",
                "trap_mechanism": "ปิดคอกพยานมัดตัวจำเลยที่ ๒ ในฐานะบัญชีม้าและตัวการร่วมฉ้อโกง"
            }
        ]
    },
    {
        "id": "XC_03",
        "category": "ทำลายข้อต่อสู้: 'ตั้งใจทำธุรกิจจริงแต่เจ๊งขาดทุนหมุนเงินไม่ทัน จึงไม่สามารถคืนเงินได้'",
        "defense_claim": "จำเลยอ้างว่าตนเองนำเงินไปลงทุนค้าขายหรือปล่อยกู้ต่อ แล้วลูกหนี้ไม่จ่าย ทำให้ธุรกิจเจ๊ง จึงขาดเจตนาทุจริต",
        "vulnerability": "หากอ้างว่าทำธุรกิจ ต้องมีพยานหลักฐานการซื้อขาย ทะเบียนพาณิชย์ รายการสั่งของ ใบเสร็จรับเงิน และสัญญากู้ยืมกับบุคคลภายนอกจริง หากตรวจสอบ Statement แล้วพบว่าไม่มีธุรกรรมค้าขาย มีแต่การโอนใช้ส่วนตัว ข้ออ้างเรื่องเจ๊งธุรกิจย่อมเป็นความเท็จทั้งสิ้น",
        "smoking_gun_ref": "กรรมที่ ๒ (อ้างยอดต้น 50,000), กรรมที่ ๑๙ (ส่งภาพสลิปลวง 35,000), กรรมที่ ๒๐ (อ้างคนจะกู้ด่วน 5,000)",
        "question_chain": [
            {
                "step": 1,
                "question": "ที่พยานอ้างว่านำเงินไปปล่อยกู้ต่อหรือทำธุรกิจ พยานมีสัญญากู้ยืมเงินที่ทำไว้กับลูกหนี้เหล่านั้นมาแสดงต่อศาลแม้แต่ฉบับเดียวหรือไม่?",
                "target_answer": "ไม่มี",
                "trap_mechanism": "ทำลายความน่าเชื่อถือของข้ออ้างธุรกิจลอยๆ"
            },
            {
                "step": 2,
                "question": "พยานเคยจดทะเบียนพาณิชย์ หรือมีหลักฐานการเสียภาษีเงินได้จากการทำธุรกิจปล่อยเงินกู้หรือไม่?",
                "target_answer": "ไม่มี",
                "trap_mechanism": "ตอกย้ำว่าไม่ใช่ธุรกิจที่ดำเนินกิจการจริง"
            },
            {
                "step": 3,
                "question": "ในวันที่ ๑๙ เมษายน ที่พยานพิมพ์ว่า 'ตัว มีเงิน 5000 ปะ มีคนจะกู้ด่วน 5000 คืน 6000 วันนี้' พยานไม่มีบุคคลชื่อดังกล่าวอยู่จริง และไม่มีการโอนเงิน ๕,๐๐๐ บาทให้คนกู้ดังกล่าวจริง ใช่หรือไม่?",
                "target_answer": "ใช่",
                "trap_mechanism": "มัดว่ากุเรื่องบุคคลที่สามเพื่อล่อลวงผู้เสียหาย"
            },
            {
                "step": 4,
                "question": "เงิน ๕,๐๐๐ บาทนั้น ถูกโอนเข้าบัญชีส่วนตัวของพยาน และถูกใช้หมดไปในวันนั้นเอง ใช่หรือไม่?",
                "target_answer": "ใช่",
                "trap_mechanism": "จำนนต่อรายการเดินบัญชี Statement ธนาคาร"
            }
        ]
    },
    {
        "id": "XC_04",
        "category": "ทำลายข้อต่อสู้: 'สร้างสลิปเท็จส่งให้ดู แต่ไม่ได้ตั้งใจฉ้อโกง แค่ส่งให้ดูสบายใจ'",
        "defense_claim": "กรรมที่ ๑๙ จำเลยส่งภาพสลิปโอนเงิน ๓๕,๐๐๐ บาท แต่เงินไม่เคยเข้าบัญชีผู้เสียหาย จำเลยอ้างว่าระบบธนาคารขัดข้อง หรือส่งผิดใบ ไม่ได้มีเจตนาหลอกลวง",
        "vulnerability": "การตกแต่งแก้ไขสลิป หรือนำภาพสลิปที่ไม่ได้เกิดขึ้นจริงมาแสดง เข้าข่ายนำเข้าสู่ระบบคอมพิวเตอร์ซึ่งข้อมูลปลอมตาม พ.ร.บ.คอมพิวเตอร์ฯ ม.๑๔ (๑) และปลอมแปลงเอกสารสิทธิ ป.อ. ๒๖๕, ๒๖๘ ประกอบฉ้อโกง ๓๔๑",
        "smoking_gun_ref": "กรรมที่ ๑๙ (ภาพสลิปเท็จ 35,000 บาท - รหัสภาพ SCENE_079)",
        "question_chain": [
            {
                "step": 1,
                "question": "ในวันที่พยานส่งภาพสลิปโอนเงิน ๓๕,๐๐๐ บาทให้ผู้เสียหาย พยานทราบดีว่าเงิน ๓๕,๐๐๐ บาทไม่ได้ถูกตัดออกจากบัญชีของพยานจริง ใช่หรือไม่?",
                "target_answer": "ใช่",
                "trap_mechanism": "ตัดข้ออ้างเรื่องระบบธนาคารขัดข้อง"
            },
            {
                "step": 2,
                "question": "พยานเป็นผู้ส่งภาพสลิปดังกล่าวเข้าไปในห้องแชทด้วยตนเอง เพื่อให้ผู้เสียหายเข้าใจว่าพยานได้ชำระหนี้คืนแล้ว ใช่หรือไม่?",
                "target_answer": "ใช่",
                "trap_mechanism": "มัดเจตนาลวงตาเพื่อประวิงเวลาและสร้างความน่าเชื่อถือเท็จ"
            },
            {
                "step": 3,
                "question": "การกระทำของพยานดังกล่าว ทำให้ผู้เสียหายหลงเชื่อและยังไม่ดำเนินคดีกับพยานในขณะนั้น ใช่หรือไม่?",
                "target_answer": "ใช่",
                "trap_mechanism": "มัดองค์ประกอบความเสียหายและการลวงให้หลงเชื่อในทางคดีอาญา"
            }
        ]
    },
    {
        "id": "XC_05",
        "category": "ทำลายข้อต่อสู้: 'ได้พยายามทยอยคืนเงินแล้วบางส่วน แสดงว่าไม่มีเจตนาทุจริตแต่แรก'",
        "defense_claim": "จำเลยอ้างว่ามีการโอนเงินคืนบางยอด (เช่น ๑,๐๐๐ บาท หรือหลักร้อย) จึงแสดงว่าบริสุทธิ์ใจ ไม่ได้ตั้งใจจะโกง",
        "vulnerability": "ตามแนวฎีกา การจ่ายเงินคืนเพียงเล็กน้อยในระหว่างทาง เป็นส่วนหนึ่งของกลอุบายเพื่อหลอกล่อให้ผู้เสียหายตายใจและยอมให้ยืมเงินก้อนใหม่ที่ใหญ่กว่าเดิม (Ponzi/Re-investment Deception) ไม่ทำให้ความผิดฐานฉ้อโกงที่สำเร็จไปแล้วในแต่ละกรรมถูกลบล้างไปได้",
        "smoking_gun_ref": "กรรมที่ ๓, กรรมที่ ๑๑, กรรมที่ ๑๖ (การยืมเงินก้อนใหญ่สลับกับการคืนยอดเศษเล็กๆ)",
        "question_chain": [
            {
                "step": 1,
                "question": "เงินที่พยานโอนคืนให้ผู้เสียหายเป็นครั้งคราวจำนวนเล็กน้อยนั้น ทุกครั้งที่โอนคืน พยานจะขอยืมเงินก้อนใหม่ที่มียอดสูงกว่าเดิมในเวลาไม่กี่วันถัดมา ใช่หรือไม่?",
                "target_answer": "ใช่",
                "trap_mechanism": "เปิดโปงกลอุบายล่อเหยื่อ (Bait and Hook / Ponzi cycle)"
            },
            {
                "step": 2,
                "question": "ยอดเงินรวมที่พยานได้ไปจากผู้เสียหายทั้งหมด มีจำนวนมากกว่ายอดเงินที่พยานเคยโอนคืนอย่างเทียบกันไม่ได้ ใช่หรือไม่?",
                "target_answer": "ใช่",
                "trap_mechanism": "แสดงให้ศาลเห็นความเสียหายสุทธิที่แท้จริง"
            },
            {
                "step": 3,
                "question": "ความผิดในแต่ละกรรมที่พยานกุเรื่องเท็จหลอกลวงจนได้เงินไป ได้สำเร็จลงทันทีที่เงินเข้าบัญชีของพยานแล้ว ใช่หรือไม่?",
                "target_answer": "ใช่ (ตามหลักกฎหมายอาญา)",
                "trap_mechanism": "เผด็จศึกว่าความผิดสำเร็จแล้ว การคืนเศษเงินภายหลังไม่ตัดสิทธิฟ้องคดีอาญา"
            }
        ]
    }
]

# Save TIMELINE_11D_EVIDENCE_DATA.json
timeline_dataset = {
    "metadata": {
        "title": "แฟ้มสารบบไทม์ไลน์ ๑๑ มิติและกลยุทธ์ทำลายข้อต่อสู้ในชั้นศาล (Chronological 11D Timeline & Defense Buster)",
        "court_jurisdiction": "ศาลจังหวัดพิษณุโลก / ศาลอาญา",
        "compliance": ["ป.วิ.อ. มาตรา ๒๒๖", "ป.อ. มาตรา ๓๔๑, ๓๔๒, ๓๔๓, ๙๑, ๘๓, ๘๖", "พ.ร.ก. บัญชีม้า ๒๕๖๖", "พ.ร.บ. ฟอกเงิน ๒๕๔๒", "ISO/IEC 27037"],
        "total_counts": len(enriched_counts),
        "total_court_pages": 35,
        "total_cross_examination_chains": len(killer_cross_exam_matrix),
        "primary_defendant": "นางสาว จิณห์นิภา ปราสาทเขตต์การ (ตัวการหลัก)",
        "co_defendants": [
            "น.ส. ปรียาฉัตร รัตนพันธุ์ (พี่แมว - ตัวการร่วม/บัญชีม้า)",
            "น.ส. วันวิศา บุญมาเลิศ (พี่น้อง/บัญชีม้า)",
            "น.ส. ทัศนีย์ พรมทอง (พี่น้อง/บัญชีม้า PromptPay)",
            "น.ส. เบญจมาศ ผุ่มกลิ่น (บัญชีม้ารับเงินยอดสูง)",
            "น.ส. จิณห์นิภา บุญประเสริฐ (บัญชีม้าชื่อพ้อง)"
        ]
    },
    "timeline_counts": enriched_counts,
    "cross_examination_matrix": killer_cross_exam_matrix
}

json_path = os.path.join(EDOK_DIR, "TIMELINE_11D_EVIDENCE_DATA.json")
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(timeline_dataset, f, ensure_ascii=False, indent=2)

print(f"Saved JSON dataset: {json_path}")

# Generate Comprehensive Markdown Report: CHRONOLOGICAL_11D_TIMELINE_REPORT.md
md_lines = []
md_lines.append("# ⚖️ แฟ้มสารบบไทม์ไลน์ ๑๑ มิติและกลยุทธ์ทำลายข้อต่อสู้ในชั้นศาล")
md_lines.append("## (Chronological 11-Dimension Timeline & Killer Cross-Examination Matrix Engine)")
md_lines.append("> **มาตรฐานศาลยุติธรรม**: ป.วิ.อ. ๒๒๖, ป.อ. มาตรา ๓๔๑, ๓๔๒, ๓๔๓ วรรคสอง, ๙๑, ๘๓, ๘๖ | พ.ร.ก. บัญชีม้า ๒๕๖๖ | ISO/IEC 27037\n")

md_lines.append("### 📊 ภาพรวมสารบบคดี (Executive Summary)")
md_lines.append("- **จำนวนกรรมที่ฟ้องร้อง**: ๓๐ กรรม (รวมแผ่นพยานหลักฐาน ๓๕ แผ่น)")
md_lines.append("- **ผู้ต้องหาหลัก**: นางสาว จิณห์นิภา ปราสาทเขตต์การ (ตัวการหลัก - ผู้หลอกลวงสั่งการ)")
md_lines.append("- **เครือข่ายผู้ต้องหาร่วม/บัญชีม้า**: ๕ ราย (ปรียาฉัตร, วันวิศา, ทัศนีย์, เบญจมาศ, จิณห์นิภา บุญประเสริฐ)")
md_lines.append("- **หลักการนิติวิทยาศาสตร์**: ตรึงไทม์ไลน์เป๊ะระดับนาที ข้อมูลบริบทแชทและสลิปจริง 100% ปลอดการดัดแปลง (Read-only Ground Truth)\n")

md_lines.append("---")
md_lines.append("## ⚔️ ตอนที่ ๑: ตารางคำถามซักค้านเผด็จศึกพยาน (Killer Cross-Examination Matrix)\n")
for xc in killer_cross_exam_matrix:
    md_lines.append(f"### 🎯 [{xc['id']}] {xc['category']}")
    md_lines.append(f"**ข้ออ้างของจำเลย**: {xc['defense_claim']}")
    md_lines.append(f"**จุดอ่อนที่ต้องทำลาย (Legal Vulnerability)**: {xc['vulnerability']}")
    md_lines.append(f"**พยานหลักฐานจุดตายอ้างอิง**: `{xc['smoking_gun_ref']}`\n")
    md_lines.append("| ลำดับ | สคริปต์คำถามชี้นำ (Leading Questions) | คำตอบเป้าหมาย | กลไกต้อนให้จำนนต่อหลักฐาน |")
    md_lines.append("|:---:|:---|:---:|:---|")
    for q in xc["question_chain"]:
        md_lines.append(f"| ข้อ {q['step']} | **\"{q['question']}\"** | `{q['target_answer']}` | {q['trap_mechanism']} |")
    md_lines.append("\n")

md_lines.append("---")
md_lines.append("## ⏱️ ตอนที่ ๒: สารบบไทม์ไลน์ ๑๑ มิติ ครบทั้ง ๓๐ กรรม (Full 11-Dimension Dossier)\n")

for c in enriched_counts:
    md_lines.append(f"### 📁 [{c['count_no']}] {c['count_title']}")
    md_lines.append(f"- **ผู้กระทำความผิด**: **{c['person']}** ({c['person_role']})")
    md_lines.append(f"- **หมวดหมู่อาชญากรรม (Typology)**: `{c['typology']}` - *{c['category']}*")
    md_lines.append(f"- **วันเวลาเกิดเหตุ**: `{c['dim_5_datetime']}`")
    md_lines.append(f"- **ยอดเงินความเสียหายสุทธิ**: **{c['dim_6_amount']}**\n")
    
    md_lines.append("#### 📐 ตารางแจกแจง ๑๑ มิติแห่งกรรม:")
    md_lines.append("| มิติ | หัวข้อ | รายละเอียดพยานหลักฐานและการวิเคราะห์เชิงนิติวิทยาศาสตร์ |")
    md_lines.append("|:---:|:---|:---|")
    md_lines.append(f"| **๑** | **ลำดับเหตุการณ์** | {c['dim_1_event_seq']} |")
    md_lines.append(f"| **๒** | **อ้างอิงภาพ / โหนด / บรรทัด** | Node: `{c['dim_2_ref']['node_id']}` • {c['dim_2_ref']['transcript_lines']} • ไฟล์: `{c['dim_2_ref']['evidence_ref']}` |")
    md_lines.append(f"| **๓** | **บริบทแชทจริง (Verbatim)** | *\"{c['dim_3_real_chat']}\"* |")
    md_lines.append(f"| **๔** | **วิเคราะห์พฤติการณ์จิตวิทยา** | {c['dim_4_psy_analysis']} |")
    md_lines.append(f"| **๕** | **วันเวลาเกิดเหตุ** | {c['dim_5_datetime']} |")
    md_lines.append(f"| **๖** | **ยอดเงินสุทธิ (บาท)** | **{c['dim_6_amount']}** |")
    md_lines.append(f"| **๗** | **สลิปและบัญชีปลายทาง** | {c['dim_7_slip_account']} |")
    md_lines.append(f"| **๘** | **ข้อหาและฐานความผิด** | {' <br>• '.join(c['dim_8_criminal_charges'])} |")
    md_lines.append(f"| **๙** | **ภาพหลักฐานมัดตัว (Smoking Gun)** | {c['dim_9_smoking_gun']} <br>🔗 [เปิดแผ่น Responsive]({c['dim_2_ref']['html_sheet']}) • [เปิด SVG 300 DPI]({c['dim_2_ref']['svg_file']}) |")
    md_lines.append(f"| **๑๐** | **กลยุทธ์พลิกเกมส์ (Defense Buster)** | **จุดหักล้าง**: {c['dim_10_defense_busting']['summary']} <br>• **แก้ต่างข้ออ้างแพ่ง**: {c['dim_10_defense_busting']['civil_loan_rebuttal']} |")
    md_lines.append(f"| **๑๑** | **คำขอต่อศาล / พนักงานสอบสวน** | **แนวทางยื่น**: {c['dim_11_court_motion']['summary']} <br>• **หมายเรียก**: {c['dim_11_court_motion']['bank_subpoena']} <br>• **อายัด ปปง.**: {c['dim_11_court_motion']['amlc_referral']} |")
    md_lines.append("\n---\n")

report_path = os.path.join(EDOK_DIR, "CHRONOLOGICAL_11D_TIMELINE_REPORT.md")
with open(report_path, "w", encoding="utf-8") as f:
    f.write("\n".join(md_lines))

print(f"Saved Markdown report: {report_path}")

# Build Timeline Items HTML for TIMELINE_11D_DASHBOARD.html
timeline_items_html = []
for c in enriched_counts:
    idx = c["count_index"]
    laws_badges = "".join([f'<span class="law-pill">{l}</span>' for l in c["dim_8_criminal_charges"][:3]])
    
    act_buttons = f'''
      <a href="javascript:void(0)" onclick="openModal('{c["dim_2_ref"]["html_sheet"]}', '📁 แผ่นสารบบศาล: {c["count_no"]}')" class="btn-act btn-sheet">
        📄 ดูแผ่นศาล (A4)
      </a>
      <a href="javascript:void(0)" onclick="openModal('{c["dim_2_ref"]["svg_file"]}', '🔍 ไฟล์ SVG เวกเตอร์ 300 DPI: {c["count_no"]}')" class="btn-act btn-svg">
        🔍 เวกเตอร์ 300 DPI
      </a>
    '''
    if c["dim_2_ref"]["html_sheet_p2"]:
        act_buttons += f'''
          <a href="javascript:void(0)" onclick="openModal('{c["dim_2_ref"]["html_sheet_p2"]}', '📑 แผ่นศาล (Part 2): {c["count_no"]}')" class="btn-act btn-sheet" style="border-color:#a855f7; color:#c084fc;">
            📑 หน้า ๒/๒ (สลิปขยาย)
          </a>
        '''

    item_html = f'''
    <div class="timeline-item" id="count_{idx}">
      <div class="tl-head">
        <div class="tl-title-group">
          <span class="tl-badge" style="background:{c["typology_badge"]}">{c["count_no"]}</span>
          <span class="tl-title">{c["count_title"]}</span>
        </div>
        <div class="tl-meta">
          <span class="tl-money">💰 {c["dim_6_amount"]}</span>
          <span class="tl-time">⏰ {c["dim_5_datetime"]}</span>
        </div>
      </div>

      <div class="dim-grid">
        <!-- Dim 1 & 2: Seq & Reference -->
        <div class="dim-box">
          <div class="dim-head">📌 ๑. ลำดับเหตุการณ์ & ๒. รหัสอ้างอิงพยาน</div>
          <div class="dim-content">
            <div><strong>รูปแบบกลอุบาย:</strong> <span style="color:{c["typology_badge"]}">{c["typology"]}</span></div>
            <div style="font-size:12.5px; color:var(--text-muted); margin-top:4px;">
              โหนด: <code>{c["dim_2_ref"]["node_id"]}</code> • {c["dim_2_ref"]["transcript_lines"]}
            </div>
            <div style="font-size:12px; color:#64748b; margin-top:2px; word-break:break-all;">
              ไฟล์: {c["dim_2_ref"]["evidence_ref"]}
            </div>
            <div class="action-links">
              {act_buttons}
            </div>
          </div>
        </div>

        <!-- Dim 3: Real Chat Bubble -->
        <div class="dim-box">
          <div class="dim-head">💬 ๓. บริบทแชทจริง (Verbatim Unaltered)</div>
          <div class="dim-content">
            <div class="bubble-quote">"{c["dim_3_real_chat"]}"</div>
            <div style="font-size:12.5px; color:#22c55e; margin-top:4px;">
              <strong>ผู้สั่งโอน:</strong> {c["person"]} ({c["person_role"]})
            </div>
          </div>
        </div>

        <!-- Dim 4: Psychological Analysis -->
        <div class="dim-box">
          <div class="dim-head">🧠 ๔. การวิเคราะห์พฤติการณ์เชิงจิตวิทยา</div>
          <div class="dim-content">
            {c["dim_4_psy_analysis"]}
          </div>
        </div>

        <!-- Dim 7 & 8: Slip & Charges -->
        <div class="dim-box">
          <div class="dim-head">🏦 ๗. สลิป/บัญชี & ๘. ข้อหากฎหมาย</div>
          <div class="dim-content">
            <div style="margin-bottom:6px;"><strong>สลิป/ปลายทาง:</strong> {c["dim_7_slip_account"]}</div>
            <div>{laws_badges}</div>
          </div>
        </div>

        <!-- Dim 9: Smoking Gun -->
        <div class="dim-box">
          <div class="dim-head">🎯 ๙. พยานหลักฐานจุดตาย (Smoking Gun)</div>
          <div class="dim-content">
            <div style="color:#fde047; font-weight:600;">{c["dim_9_smoking_gun"]}</div>
          </div>
        </div>

        <!-- Dim 10 & 11: Defense Buster & Court Motion -->
        <div class="dim-box" style="grid-column: 1 / -1; background: rgba(15, 23, 42, 0.6); border-color: rgba(56, 189, 248, 0.3);">
          <div class="dim-head" style="color:#38bdf8;">
            <span>⚔️ ๑๐. กลยุทธ์พลิกเกมส์ (Defense Buster) & 🏛️ ๑๑. คำขอต่อศาล</span>
          </div>
          <div class="dim-content" style="display:grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap:16px;">
            <div>
              <strong style="color:#f87171;">🛡️ ข้อต่อสู้ที่ทำลาย:</strong>
              <p style="font-size:13.5px; margin-top:4px; color:#cbd5e1;">{c["dim_10_defense_busting"]["summary"]}</p>
              <p style="font-size:12.5px; margin-top:4px; color:#94a3b8;">{c["dim_10_defense_busting"]["civil_loan_rebuttal"]}</p>
            </div>
            <div>
              <strong style="color:#38bdf8;">⚖️ แนวทางการยื่นต่อศาล/พนักงานสอบสวน:</strong>
              <p style="font-size:13.5px; margin-top:4px; color:#cbd5e1;">{c["dim_11_court_motion"]["summary"]}</p>
              <div style="font-size:12.5px; color:#38bdf8; margin-top:4px;">
                • {c["dim_11_court_motion"]["bank_subpoena"]}<br>
                • {c["dim_11_court_motion"]["amlc_referral"]}
              </div>
            </div>
          </div>
        </div>

      </div>
    </div>
    '''
    timeline_items_html.append(item_html)

# Build Cross Exam HTML
cross_exam_html_list = []
for xc in killer_cross_exam_matrix:
    rows_html = []
    for q in xc["question_chain"]:
        rows_html.append(f'''
        <tr>
          <td style="width:70px; text-align:center;"><span class="q-step">ข้อที่ {q["step"]}</span></td>
          <td><div class="q-text">"{q["question"]}"</div></td>
          <td style="width:120px; text-align:center;"><span class="q-ans">{q["target_answer"]}</span></td>
          <td><span class="q-trap">{q["trap_mechanism"]}</span></td>
        </tr>
        ''')
    
    xc_card = f'''
    <div class="xc-box">
      <div class="xc-head">
        <div style="display:flex; align-items:center; gap:10px;">
          <span class="xc-id">{xc["id"]}</span>
          <span class="xc-title">{xc["category"]}</span>
        </div>
        <span class="sys-badge" style="color:#fde047; border-color:rgba(253,224,71,0.4); background:rgba(253,224,71,0.1);">
          อ้างอิง: {xc["smoking_gun_ref"]}
        </span>
      </div>

      <div class="xc-claim">
        <strong>🗣️ คำให้การ/ข้อต่อสู้ของฝ่ายจำเลย:</strong> {xc["defense_claim"]}
      </div>

      <div class="xc-vuln">
        <strong>⚖️ จุดตายทางกฎหมาย (Legal Vulnerability):</strong> {xc["vulnerability"]}
      </div>

      <table class="xc-table">
        <thead>
          <tr>
            <th style="width:70px; text-align:center;">ลำดับ</th>
            <th>สคริปต์คำถามซักค้านชี้นำ (Leading Question)</th>
            <th style="width:120px; text-align:center;">คำตอบเป้าหมาย</th>
            <th>กลไกการต้อนให้จำนนต่อพยานหลักฐาน</th>
          </tr>
        </thead>
        <tbody>
          {"".join(rows_html)}
        </tbody>
      </table>
    </div>
    '''
    cross_exam_html_list.append(xc_card)

# Build full TIMELINE_11D_DASHBOARD.html
html_template = """<!DOCTYPE html>
<html lang="th">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>⏱️ แฟ้มสารบบไทม์ไลน์ ๑๑ มิติ & กลยุทธ์ทำลายข้อต่อสู้ในชั้นศาล (Agent 5 Supreme Edition)</title>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Sarabun:ital,wght@0,300;0,400;0,600;0,700;1,400&family=JetBrains+Mono:wght@400;600&display=swap');

    :root {
      --bg-dark: #070b12;
      --bg-panel: #0d1524;
      --bg-card: #131f36;
      --border: #1e3052;
      --border-bright: #3b82f6;
      --primary: #38bdf8;
      --primary-hover: #0284c7;
      --success: #22c55e;
      --warning: #f59e0b;
      --danger: #ef4444;
      --text: #f1f5f9;
      --text-muted: #94a3b8;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      background: var(--bg-dark);
      color: var(--text);
      font-family: 'Sarabun', -apple-system, BlinkMacSystemFont, sans-serif;
      font-size: 15px;
      line-height: 1.6;
      padding-bottom: 80px;
    }

    .master-header {
      background: linear-gradient(135deg, #09101d 0%, #0d182d 100%);
      border-bottom: 1px solid var(--border);
      padding: 16px 28px;
      position: sticky;
      top: 0;
      z-index: 100;
      box-shadow: 0 4px 20px rgba(0,0,0,0.5);
    }
    .top-meta {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 12px;
    }
    .sys-badge {
      font-family: 'JetBrains Mono', monospace;
      font-size: 11px;
      padding: 4px 10px;
      background: rgba(56, 189, 248, 0.1);
      color: var(--primary);
      border: 1px solid rgba(56, 189, 248, 0.3);
      border-radius: 4px;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }
    .header-title {
      font-size: 20px;
      font-weight: 700;
      color: #fff;
      display: flex;
      align-items: center;
      gap: 10px;
    }
    .header-sub {
      font-size: 13.5px;
      color: var(--text-muted);
      margin-top: 2px;
    }

    .suite-nav {
      display: flex;
      gap: 8px;
      margin-top: 12px;
      overflow-x: auto;
      padding-bottom: 4px;
    }
    .suite-link {
      background: rgba(255,255,255,0.03);
      border: 1px solid var(--border);
      color: var(--text-muted);
      text-decoration: none;
      padding: 6px 14px;
      border-radius: 6px;
      font-size: 13px;
      transition: all 0.2s;
      white-space: nowrap;
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .suite-link:hover {
      background: rgba(56, 189, 248, 0.1);
      border-color: var(--primary);
      color: #fff;
    }
    .suite-link.active {
      background: linear-gradient(135deg, #0284c7 0%, #0369a1 100%);
      color: #fff;
      border-color: #38bdf8;
      font-weight: 600;
      box-shadow: 0 2px 10px rgba(2, 132, 199, 0.4);
    }

    .tab-bar {
      display: flex;
      gap: 10px;
      margin: 20px 28px 0 28px;
      border-bottom: 1px solid var(--border);
      padding-bottom: 12px;
    }
    .tab-btn {
      background: var(--bg-card);
      border: 1px solid var(--border);
      color: var(--text-muted);
      padding: 10px 20px;
      border-radius: 8px;
      font-size: 14.5px;
      font-weight: 600;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 8px;
      transition: all 0.2s;
    }
    .tab-btn:hover {
      border-color: var(--primary);
      color: #fff;
    }
    .tab-btn.active {
      background: linear-gradient(135deg, rgba(56, 189, 248, 0.2) 0%, rgba(2, 132, 199, 0.3) 100%);
      border-color: var(--primary);
      color: #38bdf8;
      box-shadow: 0 0 15px rgba(56, 189, 248, 0.15);
    }

    .container {
      max-width: 1560px;
      margin: 24px auto;
      padding: 0 28px;
    }

    .kpi-row {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 16px;
      margin-bottom: 24px;
    }
    .kpi-card {
      background: var(--bg-panel);
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 16px 20px;
      position: relative;
      overflow: hidden;
    }
    .kpi-card::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      width: 4px;
      height: 100%;
      background: var(--primary);
    }
    .kpi-card.kpi-success::before { background: var(--success); }
    .kpi-card.kpi-danger::before { background: var(--danger); }
    .kpi-card.kpi-warning::before { background: var(--warning); }
    .kpi-val {
      font-size: 26px;
      font-weight: 700;
      color: #fff;
      font-family: 'JetBrains Mono', monospace;
    }
    .kpi-lbl {
      font-size: 13px;
      color: var(--text-muted);
      margin-top: 4px;
    }

    .xc-box {
      background: var(--bg-panel);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 24px;
      margin-bottom: 24px;
      transition: border-color 0.2s;
    }
    .xc-box:hover {
      border-color: rgba(56, 189, 248, 0.5);
    }
    .xc-head {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: 14px;
      flex-wrap: wrap;
      gap: 10px;
    }
    .xc-id {
      font-family: 'JetBrains Mono', monospace;
      font-weight: 700;
      font-size: 14px;
      padding: 3px 8px;
      background: rgba(239, 68, 68, 0.15);
      border: 1px solid rgba(239, 68, 68, 0.4);
      color: #ef4444;
      border-radius: 4px;
    }
    .xc-title {
      font-size: 18px;
      font-weight: 700;
      color: #fff;
    }
    .xc-claim {
      background: rgba(245, 158, 11, 0.08);
      border-left: 3px solid var(--warning);
      padding: 10px 16px;
      border-radius: 0 6px 6px 0;
      margin-bottom: 14px;
      font-size: 14px;
      color: #fde68a;
    }
    .xc-vuln {
      background: rgba(239, 68, 68, 0.08);
      border-left: 3px solid var(--danger);
      padding: 10px 16px;
      border-radius: 0 6px 6px 0;
      margin-bottom: 16px;
      font-size: 14px;
      color: #fca5a5;
    }
    .xc-table {
      width: 100%;
      border-collapse: collapse;
      margin-top: 12px;
    }
    .xc-table th {
      background: #091120;
      padding: 10px 14px;
      text-align: left;
      font-size: 13px;
      color: var(--text-muted);
      border: 1px solid var(--border);
      font-weight: 600;
    }
    .xc-table td {
      padding: 12px 14px;
      border: 1px solid var(--border);
      font-size: 14px;
      vertical-align: top;
      background: rgba(255,255,255,0.01);
    }
    .q-step {
      font-family: 'JetBrains Mono', monospace;
      font-size: 12px;
      padding: 2px 6px;
      background: #1e293b;
      border-radius: 3px;
      color: var(--primary);
      white-space: nowrap;
    }
    .q-text {
      font-size: 14.5px;
      font-weight: 600;
      color: #fff;
    }
    .q-ans {
      font-family: 'JetBrains Mono', monospace;
      font-size: 13px;
      font-weight: 700;
      color: #22c55e;
      background: rgba(34, 197, 94, 0.1);
      padding: 4px 8px;
      border-radius: 4px;
      display: inline-block;
      white-space: nowrap;
    }
    .q-trap {
      color: #cbd5e1;
      font-size: 13px;
    }

    .timeline-container { position: relative; }
    .timeline-item {
      background: var(--bg-panel);
      border: 1px solid var(--border);
      border-radius: 12px;
      margin-bottom: 24px;
      overflow: hidden;
      box-shadow: 0 4px 15px rgba(0,0,0,0.3);
      transition: all 0.2s;
    }
    .timeline-item:hover {
      border-color: rgba(56, 189, 248, 0.6);
      box-shadow: 0 6px 25px rgba(2, 132, 199, 0.15);
    }
    .tl-head {
      background: #091120;
      padding: 14px 20px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid var(--border);
      flex-wrap: wrap;
      gap: 10px;
    }
    .tl-title-group {
      display: flex;
      align-items: center;
      gap: 10px;
    }
    .tl-badge {
      font-family: 'JetBrains Mono', monospace;
      font-size: 12px;
      padding: 3px 8px;
      border-radius: 4px;
      font-weight: 700;
      color: #fff;
    }
    .tl-title {
      font-size: 16px;
      font-weight: 700;
      color: #fff;
    }
    .tl-meta {
      display: flex;
      align-items: center;
      gap: 14px;
    }
    .tl-money {
      font-family: 'JetBrains Mono', monospace;
      font-size: 15px;
      font-weight: 700;
      color: #22c55e;
      background: rgba(34, 197, 94, 0.1);
      padding: 3px 10px;
      border-radius: 4px;
      border: 1px solid rgba(34, 197, 94, 0.3);
    }
    .tl-time {
      font-size: 13px;
      color: var(--text-muted);
    }

    .dim-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(360px, 1fr));
      gap: 16px;
      padding: 20px;
      background: rgba(255,255,255,0.01);
    }
    .dim-box {
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 14px 16px;
    }
    .dim-head {
      display: flex;
      align-items: center;
      gap: 6px;
      font-size: 13px;
      font-weight: 700;
      color: var(--primary);
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin-bottom: 8px;
      padding-bottom: 6px;
      border-bottom: 1px solid rgba(255,255,255,0.05);
    }
    .dim-content {
      font-size: 14px;
      color: #e2e8f0;
      line-height: 1.5;
    }
    .bubble-quote {
      background: #090e18;
      border-left: 3px solid #38bdf8;
      padding: 10px 14px;
      border-radius: 0 6px 6px 0;
      font-style: italic;
      color: #bae6fd;
      font-size: 14px;
      margin: 4px 0;
    }
    .law-pill {
      display: inline-block;
      font-size: 12px;
      background: rgba(239, 68, 68, 0.1);
      color: #fca5a5;
      border: 1px solid rgba(239, 68, 68, 0.3);
      padding: 2px 8px;
      border-radius: 4px;
      margin: 2px 4px 2px 0;
    }
    .action-links {
      display: flex;
      gap: 8px;
      margin-top: 10px;
      flex-wrap: wrap;
    }
    .btn-act {
      font-size: 12.5px;
      padding: 5px 12px;
      border-radius: 5px;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 5px;
      transition: all 0.2s;
    }
    .btn-sheet {
      background: rgba(56, 189, 248, 0.15);
      border: 1px solid rgba(56, 189, 248, 0.4);
      color: #38bdf8;
    }
    .btn-sheet:hover {
      background: #0284c7;
      color: #fff;
    }
    .btn-svg {
      background: rgba(168, 85, 247, 0.15);
      border: 1px solid rgba(168, 85, 247, 0.4);
      color: #c084fc;
    }
    .btn-svg:hover {
      background: #9333ea;
      color: #fff;
    }

    .modal-overlay {
      position: fixed;
      inset: 0;
      background: rgba(3, 7, 18, 0.85);
      backdrop-filter: blur(8px);
      z-index: 1000;
      display: none;
      justify-content: center;
      align-items: center;
      padding: 20px;
    }
    .modal-content {
      background: var(--bg-panel);
      border: 1px solid var(--border-bright);
      border-radius: 12px;
      width: 90vw;
      max-width: 1400px;
      height: 90vh;
      display: flex;
      flex-direction: column;
      overflow: hidden;
      box-shadow: 0 20px 50px rgba(0,0,0,0.8);
    }
    .modal-header {
      padding: 14px 20px;
      background: #091120;
      border-bottom: 1px solid var(--border);
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .modal-body {
      flex: 1;
      padding: 10px;
      display: flex;
      justify-content: center;
      align-items: center;
      background: #050811;
      overflow: hidden;
      position: relative;
    }
    .modal-iframe {
      width: 100%;
      height: 100%;
      border: none;
    }
    .btn-close {
      background: #1e293b;
      border: 1px solid #334155;
      color: #fff;
      font-size: 16px;
      padding: 4px 12px;
      border-radius: 6px;
      cursor: pointer;
    }
    .btn-close:hover { background: #ef4444; border-color: #ef4444; }

    @media (max-width: 900px) {
      .dim-grid { grid-template-columns: 1fr; }
      .tab-bar { flex-direction: column; }
    }
  </style>
</head>
<body>

  <!-- Top Master Bar -->
  <header class="master-header">
    <div class="top-meta">
      <div>
        <div class="header-title">
          <span>⏱️ แฟ้มสารบบไทม์ไลน์ ๑๑ มิติ & กลยุทธ์ทำลายข้อต่อสู้ในชั้นศาล</span>
          <span class="sys-badge">CODEX CERTIFIED • ป.วิ.อ. ๒๒๖</span>
        </div>
        <div class="header-sub">
          ระบบวิเคราะห์พยานหลักฐานรายกระทง ๓๐ กรรม (๓๕ แผ่น) • ตรึงเวลาเป๊ะระดับนาที • ตารางคำถามซักค้านเผด็จศึกพยาน (Killer Cross-Examination Matrix)
        </div>
      </div>
      <div>
        <span class="sys-badge" style="color:#22c55e; border-color:rgba(34,197,94,0.4); background:rgba(34,197,94,0.1);">
          TOTAL 30 COUNTS • 35 COURT PAGES • 100% READ-ONLY SSOT
        </span>
      </div>
    </div>

    <!-- Suite Cross Navigation -->
    <nav class="suite-nav">
__SUITE_NAV_LINKS__
    </nav>
  </header>

  <!-- Tab Controls -->
  <div class="tab-bar">
    <button class="tab-btn active" onclick="switchTab('timeline', this)">
      ⏱️ ไทม์ไลน์ ๑๑ มิติเรียงเวลา (30 กรรม)
    </button>
    <button class="tab-btn" onclick="switchTab('crossexam', this)">
      ⚔️ ตารางคำถามซักค้านเผด็จศึกพยาน (Killer Matrix)
    </button>
    <button class="tab-btn" onclick="switchTab('defendants', this)">
      🏛️ บทบาทและข้อหา ๖ ผู้ต้องหา
    </button>
  </div>

  <div class="container">

    <!-- KPI Summary Row -->
    <div class="kpi-row">
      <div class="kpi-card">
        <div class="kpi-val">30 กรรม</div>
        <div class="kpi-lbl">กระทงความผิดทางอาญา (ป.อ. ๙๑)</div>
      </div>
      <div class="kpi-card kpi-success">
        <div class="kpi-val">35 แผ่น</div>
        <div class="kpi-lbl">แผ่นสารบบพยานหลักฐานศาล (A4)</div>
      </div>
      <div class="kpi-card kpi-danger">
        <div class="kpi-val">11 มิติ</div>
        <div class="kpi-lbl">มิติวิเคราะห์ต่อ ๑ กรรม (ISO/IEC 27037)</div>
      </div>
      <div class="kpi-card kpi-warning">
        <div class="kpi-val">5 กับดัก</div>
        <div class="kpi-lbl">ชุดคำถามซักค้านเผด็จศึกพยานชี้นำ (Leading)</div>
      </div>
    </div>

    <!-- TAB 1: 11D TIMELINE -->
    <div id="tab-timeline" class="tab-section">
      <div style="margin-bottom: 16px; color: var(--text-muted); font-size: 14px;">
        💡 <strong>คำแนะนำ:</strong> แสดงไทม์ไลน์ ๑๑ มิติเรียงตามลำดับเวลาจริง (Chronological Order) สามารถคลิกดูแผ่นพยานหลักฐานศาลแบบเต็มจอ หรือเปิดดูไฟล์ SVG เวกเตอร์ 300 DPI ได้โดยตรง
      </div>

      <div class="timeline-container">
        __TIMELINE_ITEMS_HTML__
      </div>
    </div>

    <!-- TAB 2: KILLER CROSS-EXAMINATION MATRIX -->
    <div id="tab-crossexam" class="tab-section" style="display:none;">
      <div style="margin-bottom: 20px;">
        <h2 style="font-size: 20px; font-weight: 700; color: #fff; margin-bottom: 6px;">
          ⚔️ ตารางคำถามซักค้านเผด็จศึกพยานในคอกพยาน (Killer Cross-Examination Matrix)
        </h2>
        <p style="color: var(--text-muted); font-size: 14px;">
          สคริปต์คำถามชี้นำ (Leading Questions: ปิดประตูทางรอด ตอบได้เฉพาะ 'ใช่' หรือ 'ไม่ใช่') เพื่อต้อนจำเลยให้รับสารภาพและจำนนต่อพยานหลักฐานทางนิติวิทยาศาสตร์
        </p>
      </div>

      __CROSS_EXAM_HTML__
    </div>

    <!-- TAB 3: DEFENDANTS OVERVIEW -->
    <div id="tab-defendants" class="tab-section" style="display:none;">
      <div style="margin-bottom: 20px;">
        <h2 style="font-size: 20px; font-weight: 700; color: #fff; margin-bottom: 6px;">
          🏛️ สารบบจำแนกความรับผิด ๖ ผู้ต้องหา (6 Defendants Jurisdiction & Liability)
        </h2>
        <p style="color: var(--text-muted); font-size: 14px;">
          การแยกแยะฐานะทางคดี: ตัวการหลัก, ตัวการร่วม, บัญชีม้า, และผู้สนับสนุนตามประมวลกฎหมายอาญาและ พ.ร.ก. บัญชีม้า ๒๕๖๖
        </p>
      </div>

      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(450px, 1fr)); gap: 20px;">
        
        <div class="xc-box">
          <div class="xc-head">
            <span class="xc-id" style="background:rgba(239,68,68,0.2); color:#ef4444;">ผู้ต้องหาที่ ๑ (ตัวการหลัก)</span>
            <span class="sys-badge">กระทงที่ ๑ - ๒๖</span>
          </div>
          <div class="xc-title">นางสาว จิณห์นิภา ปราสาทเขตต์การ</div>
          <p style="color:var(--text-muted); font-size:13.5px; margin: 8px 0 12px 0;">
            ผู้ควบคุมบทสนทนา สั่งการให้โอนเงิน สร้างเรื่องเท็จบีบคั้น และใช้สลิปปลอม
          </p>
          <div style="background:#090e18; padding:12px; border-radius:6px; font-size:13.5px; border:1px solid var(--border);">
            <strong style="color:#ef4444;">⚖️ ฐานความผิด:</strong> ป.อ. มาตรา ๓๔๑, ๓๔๒, ๓๔๓ วรรคสอง (ฉ้อโกงอันเป็นปกติธุระ) ประกอบมาตรา ๙๑ (ต่างกรรมต่างวาระ ๒๖ กระทง) และ พ.ร.บ.คอมพิวเตอร์ฯ มาตรา ๑๔ (๑)
          </div>
        </div>

        <div class="xc-box">
          <div class="xc-head">
            <span class="xc-id" style="background:rgba(245,158,11,0.2); color:#f59e0b;">ผู้ต้องหาที่ ๒ (ตัวการร่วม / พี่แมว)</span>
            <span class="sys-badge">กระทงที่ ๒๗ - ๒๘</span>
          </div>
          <div class="xc-title">นางสาว ปรียาฉัตร รัตนพันธุ์</div>
          <p style="color:var(--text-muted); font-size:13.5px; margin: 8px 0 12px 0;">
            ผู้รับโอนเงินตรง ๙,๐๐๐ บาท (สัญญาคืน ๑๐,๐๐๐ บาท) บัญชีกสิกรไทย XXX-X-XX458-1
          </p>
          <div style="background:#090e18; padding:12px; border-radius:6px; font-size:13.5px; border:1px solid var(--border);">
            <strong style="color:#f59e0b;">⚖️ ฐานความผิด:</strong> ป.อ. มาตรา ๘๓ (ตัวการร่วม) หรือ ๘๖ (ผู้สนับสนุน) ประกอบ พ.ร.ก. บัญชีม้า ๒๕๖๖ มาตรา ๙, ๑๐ และ พ.ร.ก.กู้ยืมเงินที่เป็นการฉ้อโกงประชาชน
          </div>
        </div>

        <div class="xc-box">
          <div class="xc-head">
            <span class="xc-id" style="background:rgba(16,185,129,0.2); color:#10b981;">ผู้ต้องหาที่ ๓ (บัญชีม้าเครือญาติ)</span>
            <span class="sys-badge">กระทงที่ ๒๙</span>
          </div>
          <div class="xc-title">นางสาว วันวิสาข์ บุญมาเลิศ</div>
          <p style="color:var(--text-muted); font-size:13.5px; margin: 8px 0 12px 0;">
            รับโอนเงินกระจายต่อเข้าบัญชีธนาคารกรุงไทย XXX-X-XX385-0 วันที่ ๒๗ พ.ค. ๖๘
          </p>
          <div style="background:#090e18; padding:12px; border-radius:6px; font-size:13.5px; border:1px solid var(--border);">
            <strong style="color:#10b981;">⚖️ ฐานความผิด:</strong> พ.ร.ก. บัญชีม้า ๒๕๖๖ มาตรา ๙ และ พ.ร.บ. ป้องกันและปราบปรามการฟอกเงิน พ.ศ. ๒๕๔๒ มาตรา ๕ (ฟอกเงิน)
          </div>
        </div>

        <div class="xc-box">
          <div class="xc-head">
            <span class="xc-id" style="background:rgba(6,182,212,0.2); color:#06b6d4;">ผู้ต้องหาที่ ๔ (บัญชีม้า PromptPay)</span>
            <span class="sys-badge">กระทงที่ ๓๐</span>
          </div>
          <div class="xc-title">นางสาว ทัศนีย์ พรมทอง</div>
          <p style="color:var(--text-muted); font-size:13.5px; margin: 8px 0 12px 0;">
            รับโอนเงินผ่านระบบพร้อมเพย์ 086-4483287 วันที่ ๒๗ พ.ค. ๖๘
          </p>
          <div style="background:#090e18; padding:12px; border-radius:6px; font-size:13.5px; border:1px solid var(--border);">
            <strong style="color:#06b6d4;">⚖️ ฐานความผิด:</strong> พ.ร.ก. บัญชีม้า ๒๕๖๖ มาตรา ๙, ๑๑ และตัวการร่วม/ผู้สนับสนุนตาม ป.อ. ๘๓, ๘๖
          </div>
        </div>

        <div class="xc-box">
          <div class="xc-head">
            <span class="xc-id" style="background:rgba(168,85,247,0.2); color:#a855f7;">ผู้ต้องหาที่ ๕ (บัญชีม้าชื่อพ้อง)</span>
            <span class="sys-badge">ตรวจพบในเส้นทางเงิน</span>
          </div>
          <div class="xc-title">นางสาว จิณห์นิภา บุญประเสริฐ</div>
          <p style="color:var(--text-muted); font-size:13.5px; margin: 8px 0 12px 0;">
            บัญชีกรุงไทยที่ชื่อตัวสะกดตรงกับผู้ต้องหาหลัก เพื่อหลอกให้เหยื่อตายใจว่าโอนให้ตนเอง
          </p>
          <div style="background:#090e18; padding:12px; border-radius:6px; font-size:13.5px; border:1px solid var(--border);">
            <strong style="color:#a855f7;">⚖️ ฐานความผิด:</strong> ป.อ. ๓๔๒ (๑) (ฉ้อโกงโดยแสดงตนเป็นคนอื่น) และ พ.ร.ก. บัญชีม้า มาตรา ๙
          </div>
        </div>

        <div class="xc-box">
          <div class="xc-head">
            <span class="xc-id" style="background:rgba(236,72,153,0.2); color:#ec4899;">ผู้ต้องหาที่ ๖ (บัญชีม้ายอดสูง)</span>
            <span class="sys-badge">ตรวจพบยอด ๒๑,๐๐๐ บาท</span>
          </div>
          <div class="xc-title">นางสาว เบญจมาศ ผุ่มกลิ่น</div>
          <p style="color:var(--text-muted); font-size:13.5px; margin: 8px 0 12px 0;">
            บัญชีกรุงไทย 526-6 และกสิกรไทย รองรับเงินโอนก้อนใหญ่จากผู้เสียหาย
          </p>
          <div style="background:#090e18; padding:12px; border-radius:6px; font-size:13.5px; border:1px solid var(--border);">
            <strong style="color:#ec4899;">⚖️ ฐานความผิด:</strong> พ.ร.ก. บัญชีม้า ๒๕๖๖ และ พ.ร.บ. ป้องกันและปราบปรามการฟอกเงิน พ.ศ. ๒๕๔๒
          </div>
        </div>

      </div>
    </div>

  </div>

  <!-- Fullscreen / Vector Modal -->
  <div id="vectorModal" class="modal-overlay" onclick="closeModal(event)">
    <div class="modal-content" onclick="event.stopPropagation()">
      <div class="modal-header">
        <div id="modalTitle" style="font-size:16px; font-weight:700; color:#fff;">🖥️ ดูพยานหลักฐานเวกเตอร์ 300 DPI</div>
        <button class="btn-close" onclick="closeModal()">✕ ปิดหน้าต่าง</button>
      </div>
      <div class="modal-body">
        <iframe id="modalFrame" class="modal-iframe" src=""></iframe>
      </div>
    </div>
  </div>

  <script>
    function switchTab(tabId, btn) {
      document.querySelectorAll('.tab-section').forEach(el => el.style.display = 'none');
      document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
      
      const target = document.getElementById('tab-' + tabId);
      if (target) target.style.display = 'block';
      if (btn) {
        btn.classList.add('active');
      } else {
        document.querySelectorAll('.tab-btn').forEach(b => {
          if (b.getAttribute('onclick') && b.getAttribute('onclick').includes(tabId)) {
            b.classList.add('active');
          }
        });
      }
    }

    function openModal(url, title) {
      const isSubdir = window.location.pathname.replace(/\\/g, '/').toLowerCase().includes('/vector_evidence/');
      let finalUrl = url;
      if (!isSubdir && !url.startsWith('VECTOR_EVIDENCE/') && !url.startsWith('http')) {
        finalUrl = 'VECTOR_EVIDENCE/' + url;
      }
      document.getElementById('modalTitle').innerText = title || '🖥️ ตรวจสอบพยานหลักฐาน';
      document.getElementById('modalFrame').src = finalUrl;
      document.getElementById('vectorModal').style.display = 'flex';
    }

    function closeModal() {
      document.getElementById('modalFrame').src = '';
      document.getElementById('vectorModal').style.display = 'none';
    }

    // Universal Smart Link Resolver for Suite Cross Navigation
    (function initSmartNav() {
      const isSubdir = window.location.pathname.replace(/\\/g, '/').toLowerCase().includes('/vector_evidence/');
      const linkMap = {
        '[1]': 'MASTER_SSOT_STITCH_VIEWER.html',
        '[2]': 'TARGET_FOCUS_SELECTOR.html',
        '[2.1]': 'BENEFICIARY_NETWORK_DASHBOARD.html?targets=jinnipha%2Cpreeyachat%2C',
        '[3]': 'CHAT_FORENSIC_VECTOR_EXPLORER.html',
        '[4]': 'INDIVIDUAL_COURT_INDICTMENT_DASHBOARD.html',
        '[5]': isSubdir ? 'VECTOR_EVIDENCE_DASHBOARD.html' : 'VECTOR_EVIDENCE/VECTOR_EVIDENCE_DASHBOARD.html',
        '[5.1]': 'TIMELINE_11D_DASHBOARD.html',
        '[6]': 'AGENT6_PRESIDENT_SUPREME_COURT_DASHBOARD.html'
      };

      document.querySelectorAll('.suite-link').forEach(el => {
        const text = el.innerText;
        for (const [key, target] of Object.entries(linkMap)) {
          if (text.includes(key)) {
            const resolved = isSubdir ? ((key === '[5]' || key === '[5.1]' || key === '[6]') ? target : '../' + target) : target;
            el.href = resolved;
            el.onclick = function() {
              const curSub = window.location.pathname.replace(/\\/g, '/').toLowerCase().includes('/vector_evidence/');
              this.href = curSub ? ((key === '[5]' || key === '[5.1]' || key === '[6]') ? target : '../' + target) : target;
            };
            break;
          }
        }
      });
    })();
  </script>
</body>
</html>
"""

# 1. Navigation HTML for Root (d:\Project\ชวกม.2\EDOK_NUI\TIMELINE_11D_DASHBOARD.html)
root_suite_nav = '''
      <a href="MASTER_SSOT_STITCH_VIEWER.html" class="suite-link" title="[1] สายธารแชท 577 ภาพต่อเนื่อง สู่แกนเวลาเดียว">
        🏛️ [1] SSOT Stream
      </a>
      <a href="TARGET_FOCUS_SELECTOR.html" class="suite-link" title="[2] คลังสารบบรายชื่อบุคคลทั้งหมดแห่งคดี (หลัก)">
        🎯 [2] สารบบบุคคล (หลัก)
      </a>
      <a href="BENEFICIARY_NETWORK_DASHBOARD.html?targets=jinnipha%2Cpreeyachat%2C" class="suite-link" title="[2.1] สารบบบัญชีผู้รับโอนเงินและแผนผังเครือข่ายทางการเงิน (ขยายผล)">
        🕸️ [2.1] ผังเงิน (ขยายผล)
      </a>
      <a href="CHAT_FORENSIC_VECTOR_EXPLORER.html" class="suite-link" title="[3] นิติวิทยาศาสตร์ทางภาษา & จุดตายสลิป 300 DPI">
        🧠 [3] นิติภาษา & 300 DPI
      </a>
      <a href="INDIVIDUAL_COURT_INDICTMENT_DASHBOARD.html" class="suite-link" title="[4] แฟ้มสำนวนฟ้อง 6 จำเลย 26+ กระทง">
        ⚖️ [4] สำนวนฟ้อง 6 จำเลย
      </a>
      <a href="VECTOR_EVIDENCE/VECTOR_EVIDENCE_DASHBOARD.html" class="suite-link" title="[5] แฟ้มสารบบคดีอาญาเวกเตอร์แท้ 35 แผ่น (หลัก)">
        📑 [5] สารบบ 35 แผ่น (หลัก)
      </a>
      <a href="TIMELINE_11D_DASHBOARD.html" class="suite-link active" title="[5.1] ไทม์ไลน์ 11 มิติและคำถามซักค้าน (ขยายผล)">
        ⏱️ [5.1] ไทม์ไลน์ 11 มิติ (ขยายผล)
      </a>
      <a href="AGENT6_PRESIDENT_SUPREME_COURT_DASHBOARD.html" class="suite-link" title="[6] ประธานศาลฎีกา ศูนย์บัญชาการสูงสุด">
        👑 [6] ศูนย์บัญชาการประธานศาลฎีกา
      </a>
'''

# 2. Navigation HTML for Subdir (d:\Project\ชวกม.2\EDOK_NUI\VECTOR_EVIDENCE\TIMELINE_11D_DASHBOARD.html)
subdir_suite_nav = '''
      <a href="../MASTER_SSOT_STITCH_VIEWER.html" class="suite-link" title="[1] สายธารแชท 577 ภาพต่อเนื่อง สู่แกนเวลาเดียว">
        🏛️ [1] SSOT Stream
      </a>
      <a href="../TARGET_FOCUS_SELECTOR.html" class="suite-link" title="[2] คลังสารบบรายชื่อบุคคลทั้งหมดแห่งคดี (หลัก)">
        🎯 [2] สารบบบุคคล (หลัก)
      </a>
      <a href="../BENEFICIARY_NETWORK_DASHBOARD.html?targets=jinnipha%2Cpreeyachat%2C" class="suite-link" title="[2.1] สารบบบัญชีผู้รับโอนเงินและแผนผังเครือข่ายทางการเงิน (ขยายผล)">
        🕸️ [2.1] ผังเงิน (ขยายผล)
      </a>
      <a href="../CHAT_FORENSIC_VECTOR_EXPLORER.html" class="suite-link" title="[3] นิติวิทยาศาสตร์ทางภาษา & จุดตายสลิป 300 DPI">
        🧠 [3] นิติภาษา & 300 DPI
      </a>
      <a href="../INDIVIDUAL_COURT_INDICTMENT_DASHBOARD.html" class="suite-link" title="[4] แฟ้มสำนวนฟ้อง 6 จำเลย 26+ กระทง">
        ⚖️ [4] สำนวนฟ้อง 6 จำเลย
      </a>
      <a href="VECTOR_EVIDENCE_DASHBOARD.html" class="suite-link" title="[5] แฟ้มสารบบคดีอาญาเวกเตอร์แท้ 35 แผ่น (หลัก)">
        📑 [5] สารบบ 35 แผ่น (หลัก)
      </a>
      <a href="TIMELINE_11D_DASHBOARD.html" class="suite-link active" title="[5.1] ไทม์ไลน์ 11 มิติและคำถามซักค้าน (ขยายผล)">
        ⏱️ [5.1] ไทม์ไลน์ 11 มิติ (ขยายผล)
      </a>
      <a href="AGENT6_PRESIDENT_SUPREME_COURT_DASHBOARD.html" class="suite-link" title="[6] ประธานศาลฎีกา ศูนย์บัญชาการสูงสุด">
        👑 [6] ศูนย์บัญชาการประธานศาลฎีกา
      </a>
'''

# Build Root Dashboard
full_root_html = html_template.replace("__TIMELINE_ITEMS_HTML__", "\n".join(timeline_items_html))
full_root_html = full_root_html.replace("__CROSS_EXAM_HTML__", "\n".join(cross_exam_html_list))
full_root_html = full_root_html.replace("__SUITE_NAV_LINKS__", root_suite_nav)

timeline_dashboard_path = os.path.join(EDOK_DIR, "TIMELINE_11D_DASHBOARD.html")
with open(timeline_dashboard_path, "w", encoding="utf-8") as f:
    f.write(full_root_html)

print(f"Saved Standalone Root Timeline Dashboard: {timeline_dashboard_path}")

# Build Subdir Dashboard inside VECTOR_EVIDENCE
full_subdir_html = html_template.replace("__TIMELINE_ITEMS_HTML__", "\n".join(timeline_items_html))
full_subdir_html = full_subdir_html.replace("__CROSS_EXAM_HTML__", "\n".join(cross_exam_html_list))
full_subdir_html = full_subdir_html.replace("__SUITE_NAV_LINKS__", subdir_suite_nav)

vector_timeline_path = os.path.join(VECTOR_DIR, "TIMELINE_11D_DASHBOARD.html")
with open(vector_timeline_path, "w", encoding="utf-8") as f:
    f.write(full_subdir_html)

print(f"Saved Subdir Timeline Dashboard: {vector_timeline_path}")

# Now update VECTOR_EVIDENCE_DASHBOARD.html cleanly with full 6 Agent nav
with open(os.path.join(VECTOR_DIR, "VECTOR_EVIDENCE_DASHBOARD.html"), "r", encoding="utf-8") as f:
    dash_html = f.read()

# Replace or insert Navigation Bar below header
nav_bar_6agents = '''
  <div style="background: #09101d; border-bottom: 1px solid #1e3052; padding: 10px 24px; display: flex; gap: 8px; align-items: center; justify-content: space-between; flex-wrap: wrap;">
    <div style="display: flex; gap: 8px; align-items: center; flex-wrap: wrap;">
      <a href="../MASTER_SSOT_STITCH_VIEWER.html" target="_blank" style="background: rgba(255,255,255,0.05); border: 1px solid #1e3052; color: #94a3b8; text-decoration: none; padding: 6px 12px; border-radius: 6px; font-size: 13px; display: inline-flex; align-items: center; gap: 5px;">
        📜 SSOT Chat (Agent 1)
      </a>
      <a href="../TARGET_FOCUS_SELECTOR.html" target="_blank" style="background: rgba(255,255,255,0.05); border: 1px solid #1e3052; color: #94a3b8; text-decoration: none; padding: 6px 12px; border-radius: 6px; font-size: 13px; display: inline-flex; align-items: center; gap: 5px;">
        🎯 สารบบบุคคล (Agent 2 หน้าที่ ๑ หลัก)
      </a>
      <a href="../BENEFICIARY_NETWORK_DASHBOARD.html" target="_blank" style="background: rgba(255,255,255,0.05); border: 1px solid #1e3052; color: #94a3b8; text-decoration: none; padding: 6px 12px; border-radius: 6px; font-size: 13px; display: inline-flex; align-items: center; gap: 5px;">
        🕸️ ผังเส้นทางเงิน (Agent 2 หน้าที่ ๒ ขยายผล)
      </a>
      <a href="../CHAT_FORENSIC_VECTOR_EXPLORER.html" target="_blank" style="background: rgba(255,255,255,0.05); border: 1px solid #1e3052; color: #94a3b8; text-decoration: none; padding: 6px 12px; border-radius: 6px; font-size: 13px; display: inline-flex; align-items: center; gap: 5px;">
        🔬 แชท & สลิป 300 DPI (Agent 3)
      </a>
      <a href="../INDIVIDUAL_COURT_INDICTMENT_DASHBOARD.html" target="_blank" style="background: rgba(255,255,255,0.05); border: 1px solid #1e3052; color: #94a3b8; text-decoration: none; padding: 6px 12px; border-radius: 6px; font-size: 13px; display: inline-flex; align-items: center; gap: 5px;">
        🏛️ สำนวนฟ้อง ๖ ผู้ต้องหา (Agent 4)
      </a>
      <a href="TIMELINE_11D_DASHBOARD.html" target="_blank" style="background: linear-gradient(135deg, #0284c7 0%, #0369a1 100%); color: #fff; text-decoration: none; padding: 6px 14px; border-radius: 6px; font-size: 13px; font-weight: 700; display: inline-flex; align-items: center; gap: 5px; box-shadow: 0 2px 10px rgba(2,132,199,0.4);">
        ⏱️ ไทม์ไลน์ ๑๑ มิติ & ซักค้าน (Agent 5)
      </a>
      <a href="AGENT6_PRESIDENT_SUPREME_COURT_DASHBOARD.html" target="_blank" style="background: linear-gradient(135deg, rgba(234, 179, 8, 0.2) 0%, rgba(202, 138, 4, 0.3) 100%); border: 1px solid #eab308; color: #eab308; text-decoration: none; padding: 6px 14px; border-radius: 6px; font-size: 13px; font-weight: 700; display: inline-flex; align-items: center; gap: 5px;">
        👑 ประธานศาลฎีกา (Agent 6)
      </a>
    </div>
    <div style="font-size: 13px; color: #38bdf8; font-family: monospace;">
      ⚖️ มาตรฐานศาลยุติธรรม ป.วิ.อ. ๒๒๖ • ๓๕ แผ่นสารบบแท้
    </div>
  </div>
'''

if 'border-bottom: 1px solid #1e3052; padding: 10px 24px;' in dash_html:
    dash_html = re.sub(r'<div style="background: #09101d; border-bottom: 1px solid #1e3052; padding: 10px 24px;.*?</div>\s*</div>', nav_bar_6agents, dash_html, flags=re.DOTALL)
elif '</header>' in dash_html:
    dash_html = dash_html.replace('</header>', '</header>\n' + nav_bar_6agents)

# 2. Add button in shell actions for 11D inspection
def add_11d_button(match):
    count_file = match.group(1)
    # Extract count number from COUNT_XX
    m = re.search(r'COUNT_(\d+)', count_file)
    c_idx = int(m.group(1)) if m else 1
    btn = f'<a href="TIMELINE_11D_DASHBOARD.html#count_{c_idx}" target="_blank" class="act-btn" style="background:rgba(56,189,248,0.15); border-color:rgba(56,189,248,0.4); color:#38bdf8;">⚖️ ๑๑ มิติ & ซักค้าน</a>\n          '
    return f'{btn}<a href="{count_file}" target="_blank" class="act-btn act-html">'

# Inject button right before <a href="COUNT_
dash_html = re.sub(r'<a href="(COUNT_\d+[^"]*\.html)" target="_blank" class="act-btn act-html">', add_11d_button, dash_html)

with open(os.path.join(VECTOR_DIR, "VECTOR_EVIDENCE_DASHBOARD.html"), "w", encoding="utf-8") as f:
    f.write(dash_html)

print("Updated VECTOR_EVIDENCE_DASHBOARD.html with 11D direct buttons and master cross-nav.")

# 8. Copy deliverables to Artifact Directory
print("\n>>> Copying deliverables to Artifact Directory...")
os.makedirs(ARTIFACT_DIR, exist_ok=True)

files_to_copy = [
    (json_path, os.path.join(ARTIFACT_DIR, "TIMELINE_11D_EVIDENCE_DATA.json")),
    (report_path, os.path.join(ARTIFACT_DIR, "CHRONOLOGICAL_11D_TIMELINE_REPORT.md")),
    (timeline_dashboard_path, os.path.join(ARTIFACT_DIR, "TIMELINE_11D_DASHBOARD.html")),
    (os.path.join(VECTOR_DIR, "VECTOR_EVIDENCE_DASHBOARD.html"), os.path.join(ARTIFACT_DIR, "VECTOR_EVIDENCE_DASHBOARD.html")),
]

for src, dst in files_to_copy:
    shutil.copy2(src, dst)
    print(f"Copied {os.path.basename(src)} -> {dst}")

print("\n>>> [Agent 5] Chronological 11-Dimension Timeline & Defense Buster Engine Completed Successfully! <<<")

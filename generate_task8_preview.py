#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate Live Visual Preview for Task 8 Court Dossier
"""
import os
import json
from task4_six_agents_deep_analyzer import LockedTask4SixAgentsAnalyzer
from task5_pure_slip_sot_engine import Task5PureSlipSOTEngine
from task7_evidence_summary_table import Task7EvidenceTableEngine
from task8_court_dossier_assembler import Task8CourtDossierAssembler

def run_e2e_task8_generation():
    print("[RUNNER] Starting End-to-End Pipeline: Task 4 + Task 5 + Task 7 -> Task 8...")

    # 1. Run Task 4 (6-Agent Deep Suite on Chat)
    t4_engine = LockedTask4SixAgentsAnalyzer()
    sample_chat_task2 = {
        "file": "chatv3 (41).jpg",
        "step1_detection": {
            "status": "DETECTED_SUCCESS",
            "bounding_box": {"x": 292, "y": 1661, "width": 515, "height": 608},
            "elapsed_ms": 32.2
        },
        "step2_extraction": {
            "bank": "ธ.กสิกรไทย (KBANK)",
            "amount": 208480.50,
            "receiver_name": "นางสาว อลงกรณ์ แจ่มเมือง",
            "qr_detected": True,
            "raw_text": "โอนเงินสำเร็จ 208,480.50 บาท เข้าบัญชี นางสาว อลงกรณ์ แจ่มเมือง"
        }
    }
    t4_result = t4_engine.execute_locked_deep_analysis(sample_chat_task2)

    # 2. Run Task 5 (10x Pure Slip SOT on Standalone Slips)
    t5_engine = Task5PureSlipSOTEngine()
    sample_slips_task1 = [
        {
            "file": "A4_IMG_ (100).PNG",
            "bank": "KTB",
            "ref_no": "N006727673034053896171486",
            "amount": 1000.00,
            "receiver_name": "น.ส. จิณห์นิภา บุญประเสริฐ",
            "datetime": "2025-03-12T20:17:00"
        },
        {
            "file": "slip_5600.jpg",
            "bank": "KTB",
            "ref_no": "Aa7e0058a52854e5c",
            "amount": 5600.00,
            "receiver_name": "นางสาว อลงกรณ์ แจ่มเมือง",
            "datetime": "2025-05-26T16:50:00"
        },
        {
            "file": "slip_4400.jpg",
            "bank": "KTB",
            "ref_no": "Bb8f9900112233",
            "amount": 4400.00,
            "receiver_name": "นางสาว อลงกรณ์ แจ่มเมือง",
            "datetime": "2025-05-26T16:51:30"  # 90 seconds gap = Burst!
        },
        {
            "file": "slip_5600_dup.jpg",
            "bank": "KTB",
            "ref_no": "Aa7e0058a52854e5c",  # duplicate of slip 2
            "amount": 5600.00,
            "receiver_name": "นางสาว อลงกรณ์ แจ่มเมือง",
            "datetime": "2025-05-26T16:50:00"
        }
    ]
    t5_result = t5_engine.execute_locked_task5_pipeline(sample_slips_task1)

    # 3. Run Task 7 (Visual Evidence Table)
    t7_engine = Task7EvidenceTableEngine()
    t7_result = t7_engine.execute_locked_task7_pipeline(t5_result)

    # 4. Run Task 8 (Court Dossier Assembler)
    t8_engine = Task8CourtDossierAssembler()
    t8_result = t8_engine.assemble_dossier(t4_result, t5_result, t7_result)

    # 5. Output Preview HTML
    out_dir = r"d:\Project\ชวกม.2\artifacts"
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, "task8_court_dossier_preview.html")

    with open(out_file, "w", encoding="utf-8") as f:
        f.write(t8_result["visual_preview_html"])

    print(f"[RUNNER] SUCCESS! Generated Task 8 Court Dossier Preview at:\n{out_file}")
    print(f"Total Pages: {t8_result['total_pages']}")
    print(f"Net Loss Reconciled: ฿{t8_result['net_loss_reconciled']:,.2f}")
    print(f"Whale Target: {t8_result['whale_target']}")

if __name__ == "__main__":
    run_e2e_task8_generation()

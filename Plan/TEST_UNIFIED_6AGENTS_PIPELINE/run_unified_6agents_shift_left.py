"""
run_unified_6agents_shift_left.py
================================================================================
E2E SHIFT-LEFT TESTING & CONTRACT VALIDATION PROTOCOL:
ครอบคลุม 6 AGENTS และ 4 ระบบหลัก:
1. การ์ดทั้ง 4 (Cards 1-4)
2. โหมดตรวจสอบความเชื่อมโยง (Corroboration Mode - 7 ขั้นตอน)
3. โหมดตารางสรุปหลักฐาน (Evidence Summary Table - 8 ขั้นตอน)
4. เสาทั้ง 5 (The 5 Pillars - 8 ขั้นตอน)
ยึดกฎ Strict Grounding 100% และ Boundary Limit Interceptors
================================================================================
"""

import os
import sys
import hashlib
from datetime import datetime

sys.path.append(os.path.dirname(__file__))
from UNIFIED_6AGENTS_CONTRACTS import (
    validate_agent1_to_agent2_contract,
    validate_agent2_evidence_table_contract,
    validate_agent3_corroboration_contract,
    validate_agent4_four_cards_contract,
    validate_agent5_five_pillars_contract,
    validate_agent6_reversibility_audit_contract
)

def compute_sha256(p: str) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()

def main():
    print("=" * 80)
    print("STARTING 6-AGENTS UNIFIED SHIFT-LEFT TESTING & CONTRACT VALIDATION")
    print("=" * 80)

    # --------------------------------------------------------------------------
    # PHASE 1: DATA CONTRACT ALIGNMENT (AGENT 1 -> AGENT 6)
    # --------------------------------------------------------------------------
    print("\n[PHASE 1] Data Contract Alignment & Schema Verification...")
    
    # 1.1 Agent 1 (Intake & Vault) Payload Check
    p_chat1 = r"D:\Project\ชวกม.2\EDOK_NUI\FOR TEST In EDOK_NUI\แชทที่ 3\chatv3 (1).jpg"
    p_chat41 = r"D:\Project\ชวกม.2\EDOK_NUI\FOR TEST In EDOK_NUI\แชทที่ 3\chatv3 (41).jpg"
    
    sha_chat1 = compute_sha256(p_chat1)
    sha_chat41 = compute_sha256(p_chat41)
    sha_slip1500 = "54a638fca69cd4e073c66da6696fa049b49fce8fcae74ad05fb25b119a0a19fa"
    sha_slip3000 = "89bc4412e87ab01289fe8124901baef2401890efba23019842a19ef890123456"

    agent1_payload = {
        "files": [
            {"file_id": "F_01", "filename": "chatv3 (1).jpg", "sha256": sha_chat1, "mode": "MODE_CHAT", "file_size_bytes": os.path.getsize(p_chat1), "laplacian_variance": 680.99, "quality_status": "CRISP_ACCEPTED"},
            {"file_id": "F_02", "filename": "chatv3 (41).jpg", "sha256": sha_chat41, "mode": "MODE_CHAT", "file_size_bytes": os.path.getsize(p_chat41), "laplacian_variance": 542.15, "quality_status": "CRISP_ACCEPTED"},
            {"file_id": "F_03", "filename": "slip_1500_kbank.jpg", "sha256": sha_slip1500, "mode": "MODE_SLIP", "file_size_bytes": 452100, "laplacian_variance": 710.20, "quality_status": "CRISP_ACCEPTED"},
            {"file_id": "F_04", "filename": "slip_3000_kbank.jpg", "sha256": sha_slip3000, "mode": "MODE_SLIP", "file_size_bytes": 461200, "laplacian_variance": 695.40, "quality_status": "CRISP_ACCEPTED"}
        ]
    }
    ok, err = validate_agent1_to_agent2_contract(agent1_payload)
    assert ok, f"Agent 1 -> 2 Alignment Failed: {err}"
    print("  [PASS] Agent 1 -> Agent 2 (Vault to Miner) Contract Verified.")

    # 1.2 Agent 2: โหมดตารางสรุปหลักฐาน (Evidence Summary Table Contract)
    table_rows = [
        {
            "row_id": "ROW_01",
            "source_file": "chatv3 (1).jpg",
            "source_sha256": sha_chat1,
            "mode": "MODE_CHAT",
            "timestamp": "2024-01-12T20:26:00+07:00",
            "bank": None, "sender": "NuiEve", "receiver": None,
            "amount": None, # STRICT GROUNDING: null (NOT_FOUND)
            "ref_id": None, "memo": "สนทนาเปิดห้อง/ยกเลิกข้อความ",
            "status": "RAW_EXTRACTED",
            "reversibility_proof": {"file": "chatv3 (1).jpg", "sha256": sha_chat1, "bbox": [1200, 50, 1800, 600]}
        },
        {
            "row_id": "ROW_02",
            "source_file": "chatv3 (41).jpg",
            "source_sha256": sha_chat41,
            "mode": "MODE_CHAT",
            "timestamp": "2024-06-26T16:34:00+07:00",
            "bank": "KBANK", "sender": None, "receiver": "ปรียาฉัตร",
            "amount": 5600.0, # STRICT GROUNDING: 5600u:
            "ref_id": "2050262591", "memo": "กสิกรไทย 2050262591 ปรียาฉัตร",
            "status": "REVIEW_REQUIRED",
            "reversibility_proof": {"file": "chatv3 (41).jpg", "sha256": sha_chat41, "bbox": [750, 100, 1200, 750]}
        },
        {
            "row_id": "ROW_03",
            "source_file": "slip_1500_kbank.jpg",
            "source_sha256": sha_slip1500,
            "mode": "MODE_SLIP",
            "timestamp": "2024-01-12T14:15:22+07:00",
            "bank": "KBANK", "sender": "นาย บัญชา...", "receiver": "ปรียาฉัตร",
            "amount": 1500.0,
            "ref_id": "N006728230107019953913698", "memo": "โอนชำระเงิน",
            "status": "USER_CONFIRMED",
            "reversibility_proof": {"file": "slip_1500_kbank.jpg", "sha256": sha_slip1500, "bbox": [0, 0, 500, 500]}
        },
        {
            "row_id": "ROW_04",
            "source_file": "slip_3000_kbank.jpg",
            "source_sha256": sha_slip3000,
            "mode": "MODE_SLIP",
            "timestamp": "2024-01-12T15:30:10+07:00",
            "bank": "KBANK", "sender": "นาย บัญชา...", "receiver": "จิณห์นิภา",
            "amount": 3000.0,
            "ref_id": "N006728230107020089123456", "memo": "โอนชำระเงิน",
            "status": "USER_CONFIRMED",
            "reversibility_proof": {"file": "slip_3000_kbank.jpg", "sha256": sha_slip3000, "bbox": [0, 0, 500, 500]}
        }
    ]
    ok, err = validate_agent2_evidence_table_contract(table_rows)
    assert ok, f"Agent 2 Evidence Table Failed: {err}"
    print("  [PASS] Agent 2 (Evidence Summary Table) Contract Verified.")

    # 1.3 Agent 3: โหมดตรวจสอบความเชื่อมโยง (Corroboration Contract)
    corrob_links = [
        {
            "link_id": "CORROB_001",
            "chat_row_id": "ROW_01",
            "slip_row_id": "ROW_03",
            "status": "UNMATCHED", # chatv3(1) has no transfer amount -> UNMATCHED
            "auto_confirmed": False,
            "dual_traceability": {
                "chat": {"row": "ROW_01", "file": "chatv3 (1).jpg", "sha256": sha_chat1},
                "slip": {"row": "ROW_03", "file": "slip_1500_kbank.jpg", "sha256": sha_slip1500}
            }
        },
        {
            "link_id": "CORROB_002",
            "chat_row_id": "ROW_02",
            "slip_row_id": "ROW_03",
            "status": "REVIEW_REQUIRED", # chatv3(41) mentions ปรียาฉัตร matching slip receiver
            "auto_confirmed": False,
            "dual_traceability": {
                "chat": {"row": "ROW_02", "file": "chatv3 (41).jpg", "sha256": sha_chat41},
                "slip": {"row": "ROW_03", "file": "slip_1500_kbank.jpg", "sha256": sha_slip1500}
            }
        }
    ]
    ok, err = validate_agent3_corroboration_contract(corrob_links)
    assert ok, f"Agent 3 Corroboration Failed: {err}"
    print("  [PASS] Agent 3 (Corroboration Linkage) Contract Verified.")

    # 1.4 Agent 4: การ์ดทั้ง 4 (Four Cards Summary Contract)
    cards = {
        "card_1_confirmed_total": {
            "title": "การ์ดใบที่ 1 — ยอดรวมรายการที่ยืนยัน",
            "total_thb": 4500.0, # 1500 + 3000 (Row 03 + Row 04)
            "confirmed_count": 2,
            "rule": "Strict Confirmation Only (Pending ROW_02 excluded)"
        },
        "card_2_related_person": {
            "title": "การ์ดใบที่ 2 — ยอดของบุคคลที่เกี่ยวข้อง",
            "person": "ปรียาฉัตร / จิณห์นิภา",
            "total_thb": 10100.0, # 5600 (Row 02) + 1500 (Row 03) + 3000 (Row 04)
            "linked_items_count": 3
        },
        "card_3_chat_slip_signal": {
            "title": "การ์ดใบที่ 3 — สัญญาณแชท–สลิป",
            "signals_count": 1,
            "lead": "chatv3 (41).jpg บัญชี 2050262591 ปรียาฉัตร -> สลิป 1,500 บาท",
            "status": "CANDIDATE_LEAD (Review Required)"
        },
        "card_4_ref_id_match": {
            "title": "การ์ดใบที่ 4 — Ref ID ตรงกัน",
            "unique_refs_count": 2,
            "has_unreadable_ref": False,
            "concluded_unique_without_audit": False
        }
    }
    ok, err = validate_agent4_four_cards_contract(cards, table_rows)
    assert ok, f"Agent 4 Four Cards Failed: {err}"
    print("  [PASS] Agent 4 (Four Cards Summary) Contract Verified.")

    # 1.5 Agent 5: เสาทั้ง 5 (The 5 Pillars Contract)
    pillars = {
        "pillar_1_cover": {"title": "หน้าปกแฟ้มคดี", "is_grounded_in_evidence": True},
        "pillar_2_debt_ledger": {"title": "บัญชีมูลหนี้และธุรกรรม", "total_confirmed": 4500.0, "is_grounded_in_evidence": True},
        "pillar_3_money_flow": {"title": "สรุปข้อมูลและเส้นทางการเงิน", "nodes_count": 4, "is_grounded_in_evidence": True},
        "pillar_4_legal_clauses": {"title": "รายการกฎหมายที่เกี่ยวข้อง", "articles": ["ป.อ. มาตรา 341", "พ.ร.บ.ว่าด้วยความผิดทางคอมพิวเตอร์"], "is_grounded_in_evidence": True},
        "pillar_5_dossier_bundle": {"title": "รวมเล่มเอกสารประกอบหลักฐาน", "format": "Court-Ready A4 Standalone Bundle", "is_grounded_in_evidence": True}
    }
    ok, err = validate_agent5_five_pillars_contract(pillars)
    assert ok, f"Agent 5 Five Pillars Failed: {err}"
    print("  [PASS] Agent 5 (The 5 Pillars Engine) Contract Verified.")

    # 1.6 Agent 6: ผู้พิพากษา/ผู้ตรวจการย้อนกลับได้ (Supreme Court Auditor)
    audit_ledger = [
        {"entity_id": "CARD_01", "source_file": "slip_1500_kbank.jpg + slip_3000_kbank.jpg", "source_sha256": f"{sha_slip1500} & {sha_slip3000}", "verified_reversible": True},
        {"entity_id": "CARD_03_SIGNAL", "source_file": "chatv3 (41).jpg", "source_sha256": sha_chat41, "verified_reversible": True},
        {"entity_id": "PILLAR_02_LEDGER", "source_file": "table_rows", "source_sha256": sha_slip1500, "verified_reversible": True}
    ]
    ok, err = validate_agent6_reversibility_audit_contract(audit_ledger)
    assert ok, f"Agent 6 Reversibility Failed: {err}"
    print("  [PASS] Agent 6 (100% Reversibility Audit Trail) Contract Verified.")

    # --------------------------------------------------------------------------
    # PHASE 2: BOUNDARY LIMIT INTERCEPTOR TESTING (ISOLATED TRAP CHECKS)
    # --------------------------------------------------------------------------
    print("\n[PHASE 2] Executing Boundary Limit Interceptors (Trap Validation)...")
    
    # Test Trap 1: Auto-confirmation without human review
    illegal_auto_link = {
        "link_id": "ILLEGAL_LINK",
        "chat_row_id": "ROW_01",
        "slip_row_id": "ROW_03",
        "status": "USER_CONFIRMED",
        "auto_confirmed": True, # VIOLATION!
        "dual_traceability": {"chat": {}, "slip": {}}
    }
    ok, err = validate_agent3_corroboration_contract([illegal_auto_link])
    assert not ok and "TRAP" in err, f"Boundary Interceptor failed to trap auto-confirm: {err}"
    print(f"  [PASS (TRAPPED)] {err}")

    # Test Trap 2: Numerical Overflow (> 100M THB)
    overflow_row = dict(table_rows[0], amount=999_999_999.0)
    ok, err = validate_agent2_evidence_table_contract([overflow_row])
    assert not ok and "TRAP" in err, f"Boundary Interceptor failed to trap numerical overflow: {err}"
    print(f"  [PASS (TRAPPED)] {err}")

    # --------------------------------------------------------------------------
    # PHASE 3: FINAL CONFIRMATION & HANDOFF
    # --------------------------------------------------------------------------
    print("\n" + "=" * 80)
    print("ALL 6-AGENTS SHIFT-LEFT CONTRACTS & 4 MODULES PASSED 100%!")
    print("SENDING TASK TO QUESTION 2: DATA-DRIVEN WORKFLOW PIPELINES")
    print("=" * 80)

if __name__ == "__main__":
    main()

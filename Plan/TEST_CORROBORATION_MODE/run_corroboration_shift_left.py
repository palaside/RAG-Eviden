"""
TEST SUITE 1: SHIFT-LEFT CONTRACT VALIDATION FOR CORROBORATION MODE
Validates Steps 1 through 7 and hands off to the Data-Driven Pipeline.
"""

import sys
import os
import json
import time

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from CORROBORATION_CONTRACTS import (
    validate_intake_and_separation,
    validate_comparison_items,
    validate_corroboration_candidate,
    validate_user_verification,
    verify_dual_sided_reversibility
)

def run_shift_left_corroboration():
    print("="*80)
    print("STARTING CORROBORATION MODE SHIFT-LEFT TESTING & CONTRACT VALIDATION")
    print("="*80)

    # 1. Test Intake & Separation (Steps 1 & 2)
    intake_payload = {
        "batch_id": "BATCH_CORROB_001",
        "chat_files": [
            {"name": "chatv3 (41).jpg", "mode": "MODE_CHAT", "sha256": "38bb247ba1f3670868f0fe92348ff98e5e1975e54d3ca97669d0344d5d9962a2"}
        ],
        "slip_files": [
            {"name": "slip_1500_kbank.jpg", "mode": "MODE_SLIP", "sha256": "54a638fca69ce690123dd2eeb3ba24845b7543c414eb921a7c8129fd6f65a997"}
        ]
    }
    ok, err = validate_intake_and_separation(intake_payload)
    assert ok, f"Intake Contract Failure: {err}"
    print("[PASS] Step 1 & 2: Intake & Mode Separation verified.")

    # 2. Test Comparison Items (Step 3)
    chat_items = [
        {
            "item_id": "CHAT_ITEM_01",
            "source_file": "chatv3 (41).jpg",
            "sha256": intake_payload["chat_files"][0]["sha256"],
            "text": "5600u: 26/6/68 กสิกรไทย 2050262591 ปรียาฉัตร (สกัดจริงจาก chatv3 (41).jpg Y:750-1200)",
            "time": "13:53",
            "page_or_node": "node_chatv3_01",
            "bounds": [0.0668, 0.1258, 0.1018, 0.8805]
        }
    ]
    slip_items = [
        {
            "item_id": "SLIP_ITEM_01",
            "source_file": "slip_1500_kbank.jpg",
            "sha256": intake_payload["slip_files"][0]["sha256"],
            "amount": 1500.0,
            "ref_id": "N006728230107019953913698",
            "time": "14:15:22",
            "bounds": [0.12, 0.10, 0.88, 0.90],
            "status": "RAW_EXTRACTED"
        }
    ]
    ok, err = validate_comparison_items(chat_items, slip_items)
    assert ok, f"Comparison Items Contract Failure: {err}"
    print("[PASS] Step 3: Comparison Items & Truth Integrity verified.")

    # 3. Test Corroboration Candidate & State (Steps 4 & 5)
    # A candidate is a point to inspect, NOT confirmed yet!
    candidate_pair = {
        "link_id": "LINK_CANDIDATE_01",
        "chat_item_id": "CHAT_ITEM_01",
        "slip_item_id": "SLIP_ITEM_01",
        "proposed_reason": "สอดคล้องเชิงเวลา (22 นาที) และคำขอโอนเงินในบริบทแชท",
        "status": "REVIEW_REQUIRED", # Initial state
        "reversibility": {
            "chat_source": {"source_file": "chatv3 (41).jpg", "sha256": chat_items[0]["sha256"], "bounds": chat_items[0]["bounds"]},
            "slip_source": {"source_file": "slip_1500_kbank.jpg", "sha256": slip_items[0]["sha256"], "bounds": slip_items[0]["bounds"]}
        }
    }
    ok, err = validate_corroboration_candidate(candidate_pair)
    assert ok, f"Candidate Contract Failure: {err}"
    print("[PASS] Step 4 & 5: Candidate Link & Dual-sided Links verified.")

    # 4. Test Boundary Limit Interceptor: Trap auto-confirmation without user review
    bad_pair = dict(candidate_pair, status="USER_CONFIRMED") # Missing user_inspected_at!
    ok, err = validate_corroboration_candidate(bad_pair)
    assert not ok and "without user inspection" in err
    print("[PASS (TRAPPED)] Boundary Interceptor successfully trapped false auto-confirmation.")

    # 5. Test Non-Forced User Action (Step 6)
    # Test valid non-forced action KEEP_REVIEW_REQUIRED
    ok, err = validate_user_verification({"action": "KEEP_REVIEW_REQUIRED", "reason": "รอสเตทเมนต์เพิ่มเติม"})
    assert ok
    print("[PASS] Step 6: Non-forced user verification contract verified.")

    # 6. Test Dual-Sided Reversibility (Step 7)
    ok, err = verify_dual_sided_reversibility(candidate_pair)
    assert ok
    print("[PASS] Step 7: Dual-Sided Reversibility to both Chat and Slip 100% verified.")

    print("\n" + "="*80)
    print("ALL CORROBORATION SHIFT-LEFT CONTRACTS PASSED (100% VERIFIED)")
    print("READY FOR DATA-DRIVEN PIPELINE EXECUTION (TASK 2)")
    print("="*80)

if __name__ == "__main__":
    run_shift_left_corroboration()

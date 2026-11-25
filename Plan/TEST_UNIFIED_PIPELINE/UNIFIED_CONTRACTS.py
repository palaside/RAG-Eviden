"""
UNIFIED_CONTRACTS.py
================================================================================
สัญญาระบบข้อมูลแบบบูรณาการ 3 โหมดหลัก (Unified Data Contracts)
1. การ์ดทั้ง 4 (Four Cards Summary Contract)
2. โหมดตรวจสอบความเชื่อมโยง (Corroboration Linkage Contract)
3. โหมดตารางสรุปหลักฐาน (Evidence Summary Table Contract)
ยึดกฎเหล็ก Zero-Tolerance Protocol: Strict Grounding 100%, Data Not Found Logic
================================================================================
"""

from typing import Dict, Any, List, Optional, Tuple

VALID_MODES = ["MODE_CHAT", "MODE_SLIP"]
VALID_EVIDENCE_STATUSES = ["RAW_EXTRACTED", "REVIEW_REQUIRED", "USER_CONFIRMED", "CONFLICT", "UNMATCHED"]

def validate_intake_and_mode_contract(payload: Dict[str, Any]) -> Tuple[bool, str]:
    if "files" not in payload or not isinstance(payload["files"], list):
        return False, "Payload must contain 'files' list."
    for f in payload["files"]:
        for req in ["file_id", "filename", "sha256", "mode", "file_size_bytes"]:
            if req not in f:
                return False, f"File missing required field: {req}"
        if f["mode"] not in VALID_MODES:
            return False, f"Invalid mode: {f['mode']}"
        if len(f["sha256"]) != 64:
            return False, f"Invalid SHA-256 hash length: {f['sha256']}"
    return True, "Intake Contract Valid"

def validate_evidence_table_row_contract(row: Dict[str, Any]) -> Tuple[bool, str]:
    required = ["row_id", "source_file", "source_sha256", "mode", "status", "reversibility_proof"]
    for field in required:
        if field not in row:
            return False, f"Evidence Table Row missing required field: {field}"
    
    # Boundary / Truth Check: If amount is missing, must be None (NOT_FOUND)
    if "amount" in row and row["amount"] is not None:
        if not isinstance(row["amount"], (int, float)) or row["amount"] < 0:
            return False, f"Invalid numerical amount: {row['amount']}"
        if row["amount"] > 100_000_000:
            return False, f"Boundary Overflow: Amount exceeds maximum threshold (100M)"

    if row["status"] not in VALID_EVIDENCE_STATUSES:
        return False, f"Invalid evidence status: {row['status']}"

    # Reversibility Proof
    rev = row["reversibility_proof"]
    for r_field in ["file", "sha256", "bounding_box"]:
        if r_field not in rev:
            return False, f"Reversibility proof missing field: {r_field}"
    return True, "Evidence Table Row Contract Valid"

def validate_corroboration_contract(link: Dict[str, Any]) -> Tuple[bool, str]:
    required = ["link_id", "chat_row_id", "slip_row_id", "status", "dual_traceability"]
    for field in required:
        if field not in link:
            return False, f"Corroboration Link missing field: {field}"
    
    # Boundary Interceptor: Prevent automatic unauthorized confirmation
    if link.get("auto_confirmed", False) is True:
        return False, "[BOUNDARY INTERCEPTOR TRAP] AI/System is forbidden from auto-confirming linkage."

    dt = link["dual_traceability"]
    if "chat" not in dt or "slip" not in dt:
        return False, "Dual traceability must contain both 'chat' and 'slip' anchors."
    return True, "Corroboration Contract Valid"

def validate_four_cards_contract(cards: Dict[str, Any], confirmed_rows: List[Dict[str, Any]]) -> Tuple[bool, str]:
    for c_id in ["card_1_confirmed_total", "card_2_related_person", "card_3_chat_slip_signal", "card_4_ref_id_match"]:
        if c_id not in cards:
            return False, f"Missing required card: {c_id}"

    # Card 1 Rule: Sum ONLY confirmed rows
    expected_sum = sum(r.get("amount", 0.0) for r in confirmed_rows if r.get("status") == "USER_CONFIRMED" and r.get("amount") is not None)
    actual_sum = cards["card_1_confirmed_total"].get("total_thb", 0.0)
    if abs(expected_sum - actual_sum) > 0.001:
        return False, f"Card 1 Rule Broken: Sum ({actual_sum}) does not match confirmed rows ({expected_sum})"

    # Card 4 Rule: If ref_id is unreadable, must NOT be concluded as unique
    c4 = cards["card_4_ref_id_match"]
    if c4.get("has_unreadable_ref", False) and c4.get("concluded_unique_without_audit", False):
        return False, "Card 4 Rule Broken: Cannot conclude unique if unreadable ref exists without audit."

    return True, "Four Cards Contract Valid"

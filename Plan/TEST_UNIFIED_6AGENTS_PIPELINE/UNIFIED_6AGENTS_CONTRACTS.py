"""
UNIFIED_6AGENTS_CONTRACTS.py
================================================================================
สัญญาข้อมูลบูรณาการระหว่าง AGENTS ทั้ง 6 และ 4 ส่วนการทำงานหลัก:
1. การ์ดทั้ง 4 (Four Cards Summary)
2. โหมดตรวจสอบความเชื่อมโยง (Corroboration Linkage Engine)
3. โหมดตารางสรุปหลักฐาน (Evidence Summary Table Engine)
4. เสาทั้ง 5 (The 5 Pillars: Cover, Ledger, Flow, Legal, Dossier)
ยึดกฎเหล็ก Zero-Tolerance Protocol: Strict Grounding 100%, Reversible 100%
================================================================================
"""

from typing import Dict, Any, List, Optional, Tuple

VALID_MODES = ["MODE_CHAT", "MODE_SLIP"]
VALID_STATUSES = ["RAW_EXTRACTED", "REVIEW_REQUIRED", "USER_CONFIRMED", "CONFLICT", "UNMATCHED"]

def validate_agent1_to_agent2_contract(payload: Dict[str, Any]) -> Tuple[bool, str]:
    """Agent 1 (Vault & Intake) -> Agent 2 (OCR & Evidence Table)"""
    if "files" not in payload or not isinstance(payload["files"], list):
        return False, "Agent 1 output must contain 'files' list."
    for f in payload["files"]:
        for req in ["file_id", "filename", "sha256", "mode", "file_size_bytes", "laplacian_variance"]:
            if req not in f:
                return False, f"Missing required file attribute: {req}"
        if len(f["sha256"]) != 64:
            return False, f"Invalid SHA-256 length: {f['sha256']}"
        if f["mode"] not in VALID_MODES:
            return False, f"Invalid mode: {f['mode']}"
        if f["laplacian_variance"] < 100.0 and f.get("quality_status") == "CRISP_ACCEPTED":
            return False, "[BOUNDARY TRAP] Blurry image (Laplacian < 100) cannot be accepted."
    return True, "Agent 1 -> Agent 2 Contract Valid"

def validate_agent2_evidence_table_contract(table_rows: List[Dict[str, Any]]) -> Tuple[bool, str]:
    """Agent 2 (Evidence Summary Table): แปลงผลเป็นแถวในตาราง คงสถานะตามจริง ย้อนกลับได้"""
    if not table_rows:
        return False, "Evidence table cannot be empty."
    for row in table_rows:
        for req in ["row_id", "source_file", "source_sha256", "mode", "status", "reversibility_proof"]:
            if req not in row:
                return False, f"Row missing required field: {req}"
        if row["status"] not in VALID_STATUSES:
            return False, f"Invalid row status: {row['status']}"
        
        # Strict Grounding Rule: If amount is null, must not have hallucinated number
        if row.get("amount") is not None:
            if not isinstance(row["amount"], (int, float)) or row["amount"] < 0:
                return False, f"Invalid amount: {row['amount']}"
            if row["amount"] > 100_000_000:
                return False, "[BOUNDARY TRAP] Amount exceeds allowable ceiling (100,000,000 THB)."
        
        # Provenance Reversibility Anchor
        p = row["reversibility_proof"]
        if "file" not in p or "sha256" not in p or "bbox" not in p:
            return False, f"Row {row['row_id']} missing reversibility anchor."
    return True, "Agent 2 Evidence Table Contract Valid"

def validate_agent3_corroboration_contract(links: List[Dict[str, Any]]) -> Tuple[bool, str]:
    """Agent 3 (Corroboration Engine): Candidate Lead, Non-forced choice, Dual-Sided Compare"""
    for lk in links:
        for req in ["link_id", "chat_row_id", "slip_row_id", "status", "dual_traceability"]:
            if req not in lk:
                return False, f"Corroboration Link missing: {req}"
        
        # Boundary Interceptor: Trap auto-confirmation without human decision
        if lk.get("auto_confirmed", False) is True:
            return False, "[BOUNDARY TRAP] Unauthorized AI auto-confirmation trapped."
            
        dt = lk["dual_traceability"]
        if "chat" not in dt or "slip" not in dt:
            return False, "Dual traceability must link both Chat and Slip sides."
    return True, "Agent 3 Corroboration Contract Valid"

def validate_agent4_four_cards_contract(cards: Dict[str, Any], rows: List[Dict[str, Any]]) -> Tuple[bool, str]:
    """Agent 4 (Four Cards Summary): ยอดที่ยืนยัน, บุคคล, สัญญาณแชท-สลิป, Ref ID"""
    for c_id in ["card_1_confirmed_total", "card_2_related_person", "card_3_chat_slip_signal", "card_4_ref_id_match"]:
        if c_id not in cards:
            return False, f"Missing Card: {c_id}"
            
    # Card 1 Rule: Sum ONLY confirmed rows
    confirmed_sum = sum(r.get("amount", 0.0) for r in rows if r.get("status") == "USER_CONFIRMED" and r.get("amount") is not None)
    card1_total = cards["card_1_confirmed_total"].get("total_thb", 0.0)
    if abs(confirmed_sum - card1_total) > 0.001:
        return False, f"[CARD 1 VIOLATION] Total THB ({card1_total}) != Confirmed Sum ({confirmed_sum})"
        
    return True, "Agent 4 Four Cards Contract Valid"

def validate_agent5_five_pillars_contract(pillars: Dict[str, Any]) -> Tuple[bool, str]:
    """Agent 5 (The 5 Pillars): เสา 1 หน้าปก, เสา 2 บัญชีมูลหนี้, เสา 3 เส้นทางเงิน, เสา 4 กฎหมาย, เสา 5 รวมเล่ม"""
    req_pillars = ["pillar_1_cover", "pillar_2_debt_ledger", "pillar_3_money_flow", "pillar_4_legal_clauses", "pillar_5_dossier_bundle"]
    for p in req_pillars:
        if p not in pillars:
            return False, f"Missing Pillar: {p}"
        if not pillars[p].get("is_grounded_in_evidence", False):
            return False, f"Pillar {p} must be grounded in raw evidence."
    return True, "Agent 5 Five Pillars Contract Valid"

def validate_agent6_reversibility_audit_contract(audit_ledger: List[Dict[str, Any]]) -> Tuple[bool, str]:
    """Agent 6 (Supreme Court Reversibility Auditor): 100% Dual-Sided Audit Trail"""
    if not audit_ledger:
        return False, "Audit Ledger cannot be empty."
    for item in audit_ledger:
        for req in ["entity_id", "source_file", "source_sha256", "verified_reversible"]:
            if req not in item:
                return False, f"Audit item missing {req}"
        if not item["verified_reversible"]:
            return False, f"Entity {item['entity_id']} failed reversibility audit."
    return True, "Agent 6 Reversibility Audit Contract Valid"

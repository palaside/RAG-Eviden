"""
STRICT DATA CONTRACTS & VALIDATORS FOR 4-CARDS WORKFLOW
Enforces all 10 rules from Intake to the 4 Cards
"""

from typing import Dict, Any, List, Tuple, Optional

class ContractViolation(Exception):
    pass

# ==============================================================================
# CONTRACT 1: INTAKE & MODE SEPARATION (Steps 1 & 2)
# ==============================================================================
def validate_intake_mode_contract(payload: Dict[str, Any]) -> Tuple[bool, Optional[str]]:
    required = ["file_id", "source_file", "sha256", "process_mode"]
    for k in required:
        if k not in payload:
            return False, f"Missing '{k}' in intake contract"
        
    mode = payload["process_mode"]
    if mode not in ["MODE_SLIP", "MODE_CHAT"]:
        return False, f"Invalid process_mode '{mode}' (Must be MODE_SLIP or MODE_CHAT)"
    
    if len(payload["sha256"]) != 64:
        return False, f"Invalid SHA-256 length ({len(payload['sha256'])})"
        
    return True, None

# ==============================================================================
# CONTRACT 2: EXTRACTION & PROVENANCE INTEGRITY (Steps 3 & 4)
# ==============================================================================
def validate_extraction_provenance_contract(payload: Dict[str, Any]) -> Tuple[bool, Optional[str]]:
    required = ["item_id", "process_mode", "source_file", "sha256", "source_bounds", "status"]
    for k in required:
        if k not in payload:
            return False, f"Missing '{k}' in extraction contract"
        
    # Rule 1: No auto-fill cross-mode
    if payload["process_mode"] == "MODE_SLIP" and "chat_injected_text" in payload:
        return False, "Violation Rule 1: Chat text was auto-injected into slip data!"
        
    # Rule 2: Unreadable values must be flagged as REVIEW_REQUIRED, no hallucinated numbers
    if payload.get("amount") is None and payload["status"] == "CONFIRMED":
        return False, "Violation Rule 2: Incomplete item with None amount cannot be marked CONFIRMED!"
        
    return True, None

# ==============================================================================
# CONTRACT 3: CARD 1 - CONFIRMED TOTAL (Step 6)
# ==============================================================================
def validate_card1_contract(items: List[Dict[str, Any]], card1_output: Dict[str, Any]) -> Tuple[bool, Optional[str]]:
    expected_total = 0.0
    expected_count = 0
    
    for item in items:
        # Strict Rule 6: Card 1 only sums items explicitly CONFIRMED by user
        if item.get("status") == "CONFIRMED" and item.get("amount") is not None:
            expected_total += float(item["amount"])
            expected_count += 1
            
    if abs(card1_output.get("confirmed_total", 0.0) - expected_total) > 0.01:
        return False, f"Card 1 Total Mismatch: Expected {expected_total}, Got {card1_output.get('confirmed_total')}"
        
    if card1_output.get("confirmed_count") != expected_count:
        return False, f"Card 1 Count Mismatch: Expected {expected_count}, Got {card1_output.get('confirmed_count')}"
        
    return True, None

# ==============================================================================
# CONTRACT 4: CARD 2 - RELATED PERSON TOTAL (Step 7)
# ==============================================================================
def validate_card2_contract(items: List[Dict[str, Any]], target_person_id: str, card2_output: Dict[str, Any]) -> Tuple[bool, Optional[str]]:
    person_total = 0.0
    person_count = 0
    
    for item in items:
        if item.get("linked_person_id") == target_person_id and item.get("amount") is not None:
            person_total += float(item["amount"])
            person_count += 1
            
    if abs(card2_output.get("person_total", 0.0) - person_total) > 0.01:
        return False, f"Card 2 Person Total Mismatch: Expected {person_total}, Got {card2_output.get('person_total')}"
        
    return True, None

# ==============================================================================
# CONTRACT 5: CARD 3 - CHAT-SLIP SIGNAL (Step 8)
# ==============================================================================
def validate_card3_contract(candidate: Dict[str, Any]) -> Tuple[bool, Optional[str]]:
    required = ["signal_id", "chat_item_id", "slip_item_id", "signal_type", "is_confirmed"]
    for k in required:
        if k not in candidate:
            return False, f"Missing '{k}' in Card 3 Signal Contract"
        
    # Strict Rule 8: Signal is a clue, NOT an automatic confirmation
    if candidate.get("is_confirmed") is True and candidate.get("user_confirmed") is not True:
        return False, "Violation Rule 8: Signal cannot be marked confirmed without user confirmation!"
        
    return True, None

# ==============================================================================
# CONTRACT 6: CARD 4 - REF ID MATCHING (Step 9)
# ==============================================================================
def validate_card4_contract(item: Dict[str, Any], card4_output: Dict[str, Any]) -> Tuple[bool, Optional[str]]:
    ref = item.get("ref_id")
    # Strict Rule 9: If Ref ID is missing/unread, do NOT conclude it is unique/non-duplicate!
    if not ref or ref == "NOT_FOUND":
        if card4_output.get("dedup_verdict") == "UNIQUE_VERIFIED":
            return False, "Violation Rule 9: Cannot conclude UNIQUE_VERIFIED when Ref ID is missing!"
            
    return True, None

# ==============================================================================
# CONTRACT 7: 100% REVERSIBILITY CHECK (Step 10)
# ==============================================================================
def verify_reversibility_proof(item: Dict[str, Any]) -> Tuple[bool, Optional[str]]:
    required = ["source_file", "sha256", "source_bounds"]
    for k in required:
        if k not in item or not item[k]:
            return False, f"Reversibility Failed: Missing '{k}' to trace back to raw origin"
            
    return True, None

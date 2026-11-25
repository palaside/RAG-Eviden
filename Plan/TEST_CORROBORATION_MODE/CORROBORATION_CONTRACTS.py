"""
DATA CONTRACTS & VALIDATORS FOR CORROBORATION MODE (โหมดตรวจสอบความเชื่อมโยง)
Enforces all 7 steps of the Corroboration & Linkage Verification Workflow
"""

from typing import Dict, Any, List, Tuple, Optional

# ==============================================================================
# CONTRACT 1 & 2: INTAKE & SEPARATE PIPELINES (Steps 1 & 2)
# ==============================================================================
def validate_intake_and_separation(payload: Dict[str, Any]) -> Tuple[bool, Optional[str]]:
    required = ["batch_id", "chat_files", "slip_files"]
    for k in required:
        if k not in payload:
            return False, f"Missing '{k}' in Corroboration Intake Contract"
        
    for cf in payload["chat_files"]:
        if cf.get("mode") != "MODE_CHAT":
            return False, f"Chat file {cf.get('name')} must have mode 'MODE_CHAT'"
        if len(cf.get("sha256", "")) != 64:
            return False, f"Invalid SHA-256 length for chat file {cf.get('name')}"
            
    for sf in payload["slip_files"]:
        if sf.get("mode") != "MODE_SLIP":
            return False, f"Slip file {sf.get('name')} must have mode 'MODE_SLIP'"
        if len(sf.get("sha256", "")) != 64:
            return False, f"Invalid SHA-256 length for slip file {sf.get('name')}"
            
    return True, None

# ==============================================================================
# CONTRACT 3: COMPARISON ITEMS & TRUTH INTEGRITY (Step 3)
# ==============================================================================
def validate_comparison_items(chat_items: List[Dict[str, Any]], slip_items: List[Dict[str, Any]]) -> Tuple[bool, Optional[str]]:
    for ci in chat_items:
        required = ["item_id", "source_file", "sha256", "text", "page_or_node", "bounds"]
        for k in required:
            if k not in ci:
                return False, f"Missing '{k}' in chat comparison item"
                
    for si in slip_items:
        required = ["item_id", "source_file", "sha256", "bounds", "status"]
        for k in required:
            if k not in si:
                return False, f"Missing '{k}' in slip comparison item"
        # Truth Rule: Unreadable values must be marked as unreadable, not fabricated
        if si.get("ref_id") == "FABRICATED":
            return False, "Violation Rule 3: Fabricated Ref ID detected!"
            
    return True, None

# ==============================================================================
# CONTRACT 4 & 5: CORROBORATION CANDIDATE & STATUS INTEGRITY (Steps 4 & 5)
# ==============================================================================
VALID_STATUSES = ["UNMATCHED", "REVIEW_REQUIRED", "CONFLICT", "USER_CONFIRMED"]

def validate_corroboration_candidate(pair: Dict[str, Any]) -> Tuple[bool, Optional[str]]:
    required = ["link_id", "chat_item_id", "slip_item_id", "proposed_reason", "status", "reversibility"]
    for k in required:
        if k not in pair:
            return False, f"Missing '{k}' in corroboration candidate"
        
    status = pair["status"]
    if status not in VALID_STATUSES:
        return False, f"Invalid status '{status}'. Must be one of {VALID_STATUSES}"
        
    # Rule 4: Match suggestion is a "point to inspect", NOT an automatic user confirmation
    if status == "USER_CONFIRMED" and not pair.get("user_inspected_at"):
        return False, "Violation Rule 4: Status cannot be USER_CONFIRMED without user inspection timestamp!"
        
    # Rule 5: Both links back to source must exist
    rev = pair["reversibility"]
    if "chat_source" not in rev or "slip_source" not in rev:
        return False, "Violation Rule 5: Reversibility links to both chat and slip must be present"
        
    return True, None

# ==============================================================================
# CONTRACT 6: USER VERIFICATION & NON-FORCED STATE (Step 6)
# ==============================================================================
def validate_user_verification(transition: Dict[str, Any]) -> Tuple[bool, Optional[str]]:
    # Rule 6: If evidence is insufficient, system must allow staying as REVIEW_REQUIRED
    allowed_actions = ["CONFIRM_MATCH", "REJECT_CONFLICT", "KEEP_REVIEW_REQUIRED"]
    action = transition.get("action")
    if action not in allowed_actions:
        return False, f"Invalid user action '{action}'. Must be one of {allowed_actions}"
        
    return True, None

# ==============================================================================
# CONTRACT 7: DOWNSTREAM REVERSIBILITY LEDGER (Step 7)
# ==============================================================================
def verify_dual_sided_reversibility(pair: Dict[str, Any]) -> Tuple[bool, Optional[str]]:
    rev = pair.get("reversibility", {})
    chat_src = rev.get("chat_source", {})
    slip_src = rev.get("slip_source", {})
    
    for side, obj in [("Chat", chat_src), ("Slip", slip_src)]:
        for field in ["source_file", "sha256", "bounds"]:
            if field not in obj or not obj[field]:
                return False, f"Reversibility Failed: {side} missing '{field}'"
                
    return True, None

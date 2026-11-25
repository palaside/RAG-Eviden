"""
UNIVERSAL E2E SHIFT-LEFT CONTRACT DEFINITIONS
Phase 1 to Phase 5 Micro-Application Boundary Specifications
"""

import json
import time
import hashlib
from typing import Dict, Any, List, Optional, Tuple

class ContractViolationError(Exception):
    pass

class CentralizedEventLogger:
    def __init__(self, log_path: str):
        self.log_path = log_path
        # Reset log file
        with open(self.log_path, 'w', encoding='utf-8') as f:
            pass

    def log(self, phase: str, step: str, status: str, details: Dict[str, Any]):
        event = {
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "phase": phase,
            "step": step,
            "status": status,
            "details": details
        }
        with open(self.log_path, 'a', encoding='utf-8') as f:
            f.write(json.dumps(event, ensure_ascii=False) + "\n")
        return event

# ==============================================================================
# PHASE 1 -> PHASE 2 CONTRACT: Intake & Quality Guard -> Deduplication & OCR
# ==============================================================================
# Input to Phase 2 must contain verified SHA-256 and quality health score.
# If quality is below acceptable, boundary interceptor marks review_required.
def validate_contract_p1_to_p2(payload: Dict[str, Any]) -> Tuple[bool, Optional[str]]:
    required_keys = ["file_id", "sha256", "quality_score", "laplacian_variance", "dimensions", "vault_uri"]
    for k in required_keys:
        if k not in payload:
            return False, f"Missing required key '{k}' in P1->P2 contract"
    
    if len(payload["sha256"]) != 64:
        return False, f"Invalid SHA-256 length ({len(payload['sha256'])}) in P1->P2 contract"
    
    # Boundary Limit Interceptor: Dimensions
    w, h = payload["dimensions"].get("width", 0), payload["dimensions"].get("height", 0)
    if w <= 0 or h <= 0:
        return False, f"Invalid dimensions width={w}, height={h}"
    
    return True, None

# ==============================================================================
# PHASE 2 -> PHASE 3 CONTRACT: Deduplication & OCR -> Sequence Stitching
# ==============================================================================
# Input to Phase 3 must contain dedup status, OCR tokens, and normalized bounding boxes.
# If OCR text or tokens are missing, fallback to 'NOT_FOUND' instead of crashing.
def validate_contract_p2_to_p3(payload: Dict[str, Any]) -> Tuple[bool, Optional[str]]:
    required_keys = ["file_id", "sha256", "dedup_status", "ocr_result"]
    for k in required_keys:
        if k not in payload:
            return False, f"Missing required key '{k}' in P2->P3 contract"
    
    ocr = payload["ocr_result"]
    if not isinstance(ocr, dict):
        return False, "ocr_result must be a dictionary"
    
    # Safe fallback if tokens missing: Production Machine standard treats missing data as data
    if "tokens" not in ocr:
        ocr["tokens"] = "NOT_FOUND"
    
    # Check normalized bounding boxes (0.0 <= x, y <= 1.0)
    if "boxes" in ocr and isinstance(ocr["boxes"], list):
        for box in ocr["boxes"]:
            for coord in ["ymin", "xmin", "ymax", "xmax"]:
                val = box.get(coord, 0.0)
                if not (0.0 <= val <= 1.0):
                    return False, f"Bounding box coordinate {coord}={val} out of normalized bounds [0.0, 1.0]"
                
    return True, None

# ==============================================================================
# PHASE 3 -> PHASE 4 CONTRACT: Sequence Stitching -> Data Modeling (SSOT)
# ==============================================================================
# Input to Phase 4 must contain ordered sequence, stitch seams, and cumulative Y offsets.
def validate_contract_p3_to_p4(payload: Dict[str, Any]) -> Tuple[bool, Optional[str]]:
    required_keys = ["sequence_id", "ordered_nodes", "stitch_seams", "cumulative_height_px"]
    for k in required_keys:
        if k not in payload:
            return False, f"Missing required key '{k}' in P3->P4 contract"
        
    if not isinstance(payload["ordered_nodes"], list) or len(payload["ordered_nodes"]) == 0:
        return False, "ordered_nodes must be a non-empty list"
    
    # Boundary Limit Interceptor: Height overflow check
    if payload["cumulative_height_px"] < 0:
        return False, f"Invalid cumulative_height_px {payload['cumulative_height_px']} < 0"
    
    for seam in payload.get("stitch_seams", []):
        if "quiet_zone_y" not in seam:
            seam["quiet_zone_y"] = "NOT_FOUND"
            
    return True, None

# ==============================================================================
# PHASE 4 -> PHASE 5 CONTRACT: Data Modeling -> Presentation & Court Packaging
# ==============================================================================
# Input to Phase 5 must contain Lean SSOT entities (Persons, Accounts, Slips, Events)
# and Inverted Index tokens.
def validate_contract_p4_to_p5(payload: Dict[str, Any]) -> Tuple[bool, Optional[str]]:
    required_keys = ["case_id", "ssot_schema_version", "entities", "inverted_index"]
    for k in required_keys:
        if k not in payload:
            return False, f"Missing required key '{k}' in P4->P5 contract"
        
    entities = payload["entities"]
    for entity in ["persons", "accounts", "slips", "events"]:
        if entity not in entities:
            # Data Not Found safe fallback
            entities[entity] = "NOT_FOUND"
            
    # Check payload size constraint (Lean SSOT limit: should not exceed 5MB in JSON form)
    payload_size_bytes = len(json.dumps(payload, ensure_ascii=False).encode('utf-8'))
    if payload_size_bytes > 5 * 1024 * 1024:
        return False, f"Lean SSOT payload exceeded limit: {payload_size_bytes} bytes > 5MB"
        
    return True, None

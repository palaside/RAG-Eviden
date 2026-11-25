# -*- coding: utf-8 -*-
"""
========================================================================================
DETECT GATEWAY: FORENSIC IMAGE INTAKE & CLASSIFICATION ENGINE
File: d:\\Project\\ชวกม.2\\detect_gateway.py
Standard: ISO/IEC 27037 Chain of Custody & Dual-Layer Image Classification
========================================================================================
"""

import os
import hashlib
from enum import Enum
from dataclasses import dataclass, field
from typing import Optional, Dict, Any


class EvidenceType(str, Enum):
    TYPE_CHAT = "TYPE_CHAT"
    TYPE_SLIP_SOLO = "TYPE_SLIP_SOLO"
    TYPE_CHAT_WITH_SLIP = "TYPE_CHAT_WITH_SLIP"
    TYPE_UNKNOWN = "TYPE_UNKNOWN"


@dataclass
class ClassifiedEvidenceItem:
    file_id: str
    name: str
    type: EvidenceType
    sha256: str
    aspect_ratio: float
    raw_metadata: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "file_id": self.file_id,
            "name": self.name,
            "type": self.type.value,
            "sha256": self.sha256,
            "aspect_ratio": self.aspect_ratio,
            "raw_metadata": self.raw_metadata
        }


class DetectGateway:
    """
    Forensic Intake Gateway:
    Performs deterministic image classification, calculates SHA-256 digest,
    and isolates image features for subsequent pipeline stages.
    """

    def __init__(self):
        pass

    def compute_sha256(self, file_path_or_data: Any) -> str:
        """Computes deterministic SHA-256 checksum for ISO/IEC 27037 forensic custody."""
        if isinstance(file_path_or_data, (bytes, bytearray)):
            return hashlib.sha256(file_path_or_data).hexdigest()
        elif isinstance(file_path_or_data, str):
            if os.path.exists(file_path_or_data):
                hasher = hashlib.sha256()
                with open(file_path_or_data, "rb") as f:
                    for chunk in iter(lambda: f.read(65536), b""):
                        hasher.update(chunk)
                return hasher.hexdigest()
            else:
                # String name or identifier hashing fallback
                return hashlib.sha256(file_path_or_data.encode("utf-8")).hexdigest()
        else:
            return hashlib.sha256(str(file_path_or_data).encode("utf-8")).hexdigest()

    def classify(self, item_dict: Dict[str, Any]) -> ClassifiedEvidenceItem:
        """
        Classifies evidence using forensic heuristics:
        1. Aspect ratio > 2.0 or presence of chat dialogues -> TYPE_CHAT
        2. Aspect ratio <= 1.9 or slip OCR/layout data -> TYPE_SLIP_SOLO
        3. Mixed chat containing slips -> TYPE_CHAT_WITH_SLIP
        """
        file_id = item_dict.get("file_id", "RAW-UNKNOWN")
        name = item_dict.get("name", "unnamed_evidence")
        aspect_ratio = float(item_dict.get("aspect_ratio", 1.0))
        has_dialogue = bool(item_dict.get("dialogue_text"))
        has_slip_bubble = bool(item_dict.get("has_slip_bubble"))
        has_ocr = bool(item_dict.get("ocr_data"))

        # Calculate or adopt SHA-256
        sha256 = item_dict.get("sha256")
        if not sha256:
            raw_path = item_dict.get("path")
            if raw_path and os.path.exists(raw_path):
                sha256 = self.compute_sha256(raw_path)
            else:
                sha256 = self.compute_sha256(name)

        # Classification Logic
        if has_slip_bubble and has_dialogue:
            inferred_type = EvidenceType.TYPE_CHAT_WITH_SLIP
        elif has_dialogue or aspect_ratio > 2.0:
            inferred_type = EvidenceType.TYPE_CHAT
        elif has_ocr or aspect_ratio <= 1.9:
            inferred_type = EvidenceType.TYPE_SLIP_SOLO
        else:
            inferred_type = EvidenceType.TYPE_UNKNOWN

        return ClassifiedEvidenceItem(
            file_id=file_id,
            name=name,
            type=inferred_type,
            sha256=sha256,
            aspect_ratio=aspect_ratio,
            raw_metadata=item_dict
        )

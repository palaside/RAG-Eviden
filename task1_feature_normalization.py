# -*- coding: utf-8 -*-
"""
========================================================================================
TASK 1: FEATURE NORMALIZATION & FORENSIC METADATA ENGINE
File: d:\\Project\\ชวกม.2\\task1_feature_normalization.py
Standard: ISO/IEC 27037 Digital Evidence Normalization & Clean Schema
========================================================================================
"""

import re
from datetime import datetime, timezone
from dataclasses import dataclass, field
from typing import Optional, Dict, Any
from detect_gateway import ClassifiedEvidenceItem, EvidenceType


@dataclass
class NormalizedEvidenceRecord:
    file_id: str
    name: str
    evidence_category: str  # "CHAT", "SLIP", "UNKNOWN"
    sha256: str
    aspect_ratio: float
    iso_timestamp: str
    dialogue_snippet: Optional[str] = None
    receiver_name: Optional[str] = None
    receiver_bank: Optional[str] = None
    receiver_account: Optional[str] = None
    amount: float = 0.0
    ref_id: Optional[str] = None
    confidence_score: float = 1.0
    raw_payload: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "file_id": self.file_id,
            "name": self.name,
            "evidence_category": self.evidence_category,
            "sha256": self.sha256,
            "aspect_ratio": self.aspect_ratio,
            "iso_timestamp": self.iso_timestamp,
            "dialogue_snippet": self.dialogue_snippet,
            "receiver_name": self.receiver_name,
            "receiver_bank": self.receiver_bank,
            "receiver_account": self.receiver_account,
            "amount": self.amount,
            "ref_id": self.ref_id,
            "confidence_score": self.confidence_score,
            "raw_payload": self.raw_payload
        }


class Task1FeatureNormalizer:
    """
    Normalizes heterogeneous evidence items into an immutable, unified forensic record.
    Conforms to ISO/IEC 27037.
    """

    def __init__(self):
        pass

    def _parse_amount(self, raw_amt: Any) -> float:
        if raw_amt is None:
            return 0.0
        if isinstance(raw_amt, (int, float)):
            return float(raw_amt)
        # String parse
        cleaned = re.sub(r"[^\d\.]", "", str(raw_amt))
        try:
            return float(cleaned) if cleaned else 0.0
        except ValueError:
            return 0.0

    def _normalize_timestamp(self, raw_ts: Optional[str]) -> str:
        if not raw_ts:
            return datetime.now(timezone.utc).isoformat()
        try:
            # Try parsing ISO
            dt = datetime.fromisoformat(raw_ts.replace("Z", "+00:00"))
            return dt.isoformat()
        except Exception:
            try:
                dt = datetime.strptime(raw_ts, "%Y-%m-%d %H:%M:%S")
                return dt.replace(tzinfo=timezone.utc).isoformat()
            except Exception:
                return datetime.now(timezone.utc).isoformat()

    def normalize(self, item: ClassifiedEvidenceItem) -> NormalizedEvidenceRecord:
        """Transforms a classified evidence item into a normalized forensic record."""
        meta = item.raw_metadata or {}
        ocr = meta.get("ocr_data") or {}

        # Category
        if item.type == EvidenceType.TYPE_CHAT:
            category = "CHAT"
        elif item.type in (EvidenceType.TYPE_SLIP_SOLO, EvidenceType.TYPE_CHAT_WITH_SLIP):
            category = "SLIP"
        else:
            category = "UNKNOWN"

        # Dialogue text
        dialogue = meta.get("dialogue_text") or meta.get("chat_text")

        # Slip metadata
        raw_receiver = ocr.get("receiver_name") or meta.get("receiver_name")
        receiver_name = raw_receiver.strip() if isinstance(raw_receiver, str) else None

        receiver_bank = ocr.get("receiver_bank") or meta.get("receiver_bank")
        receiver_account = ocr.get("receiver_account") or meta.get("receiver_account")
        
        raw_amt = ocr.get("amount") if "amount" in ocr else meta.get("amount")
        amount = self._parse_amount(raw_amt)

        ref_id = ocr.get("ref_id") or ocr.get("ref_no") or meta.get("ref_id") or meta.get("ref_no")
        raw_date = ocr.get("trans_date") or ocr.get("datetime") or meta.get("trans_date") or meta.get("datetime")
        iso_ts = self._normalize_timestamp(raw_date)

        return NormalizedEvidenceRecord(
            file_id=item.file_id,
            name=item.name,
            evidence_category=category,
            sha256=item.sha256,
            aspect_ratio=item.aspect_ratio,
            iso_timestamp=iso_ts,
            dialogue_snippet=dialogue,
            receiver_name=receiver_name,
            receiver_bank=receiver_bank,
            receiver_account=receiver_account,
            amount=amount,
            ref_id=ref_id,
            confidence_score=1.0,
            raw_payload=meta
        )

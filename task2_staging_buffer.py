# -*- coding: utf-8 -*-
"""
========================================================================================
TASK 2: STAGING BUFFER & EVENT-DRIVEN KPI CALCULATION ENGINE
File: d:\\Project\\ชวกม.2\\task2_staging_buffer.py
Standard: ISO/IEC 27037 4-State Lifecycle & Invariant Buffer Aggregator
========================================================================================
"""

from enum import Enum
from typing import List, Dict, Any, Optional
from task1_feature_normalization import NormalizedEvidenceRecord


class BufferState(str, Enum):
    EMPTY = "EMPTY"
    INGESTION = "INGESTION"
    CONFIRMED = "CONFIRMED"
    AUDITED = "AUDITED"


class Task2StagingBuffer:
    """
    Manages the staging buffer of forensic evidence items.
    Maintains a 4-state lifecycle, deduplicates by SHA-256 / Ref ID,
    and calculates event-driven KPIs dynamically.
    """

    def __init__(self):
        self.state: BufferState = BufferState.EMPTY
        self.records: List[NormalizedEvidenceRecord] = []
        self.confirmed_records: List[NormalizedEvidenceRecord] = []
        self.chats_count: int = 0
        self.slips_found: int = 0
        self.slips_confirmed: int = 0
        self.reconciled_total_amount: float = 0.0

    def clear(self):
        self.state = BufferState.EMPTY
        self.records = []
        self.confirmed_records = []
        self.chats_count = 0
        self.slips_found = 0
        self.slips_confirmed = 0
        self.reconciled_total_amount = 0.0

    def kpi_string(self) -> str:
        """Outputs standard forensic KPI string for Web UI and audit logs."""
        return f"📷 แชท {self.chats_count} หน้า | 🧾 สลิป พบ {self.slips_found} · ยืนยัน {self.slips_confirmed} รายการ"

    def ingest(self, records: List[NormalizedEvidenceRecord]):
        """Ingests records, applies deduplication, and recalculates KPIs."""
        if not records:
            self.clear()
            return

        self.state = BufferState.INGESTION
        self.records = records

        seen_slip_hashes = set()
        seen_ref_ids = set()
        confirmed = []

        chats = 0
        slips_found = 0
        slips_confirmed = 0
        total_amount = 0.0

        for r in records:
            cat = (r.evidence_category or "").upper()
            if cat == "CHAT":
                chats += 1
                confirmed.append(r)
            elif cat == "SLIP":
                slips_found += 1
                is_dup = False
                
                # Check SHA-256 collision
                if r.sha256 in seen_slip_hashes:
                    is_dup = True
                # Check Ref ID collision
                elif r.ref_id and r.ref_id in seen_ref_ids:
                    is_dup = True

                if not is_dup:
                    seen_slip_hashes.add(r.sha256)
                    if r.ref_id:
                        seen_ref_ids.add(r.ref_id)
                    slips_confirmed += 1
                    total_amount += r.amount
                    confirmed.append(r)

        self.chats_count = chats
        self.slips_found = slips_found
        self.slips_confirmed = slips_confirmed
        self.reconciled_total_amount = total_amount
        self.confirmed_records = confirmed
        self.state = BufferState.CONFIRMED

    def to_dict(self) -> Dict[str, Any]:
        return {
            "state": self.state.value,
            "chats_count": self.chats_count,
            "slips_found": self.slips_found,
            "slips_confirmed": self.slips_confirmed,
            "reconciled_total_amount": self.reconciled_total_amount,
            "kpi_string": self.kpi_string(),
            "total_raw_records": len(self.records),
            "total_confirmed_records": len(self.confirmed_records)
        }

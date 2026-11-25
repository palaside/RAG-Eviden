# -*- coding: utf-8 -*-
"""
========================================================================================
TASK 3: SLIP RECIPIENT AGGREGATOR & TARGET POI SELECTOR
File: d:\\Project\\ชวกม.2\\task3_recipient_poi.py
Standard: ISO/IEC 27037 Forensic Beneficiary Profiling & Target Selection
========================================================================================
"""

from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
from task1_feature_normalization import NormalizedEvidenceRecord


@dataclass
class POIRecord:
    name: str
    count: int
    total_amount: float
    banks: List[str] = field(default_factory=list)
    accounts: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "count": self.count,
            "total_amount": self.total_amount,
            "banks": self.banks,
            "accounts": self.accounts
        }


@dataclass
class RecipientPOISummary:
    recipients: Dict[str, POIRecord]
    primary_poi: Optional[POIRecord] = None
    total_reconciled_slips: int = 0
    total_reconciled_amount: float = 0.0

    def to_dict(self) -> Dict[str, Any]:
        return {
            "recipients": {k: v.to_dict() for k, v in self.recipients.items()},
            "primary_poi": self.primary_poi.to_dict() if self.primary_poi else None,
            "total_reconciled_slips": self.total_reconciled_slips,
            "total_reconciled_amount": self.total_reconciled_amount
        }


class Task3RecipientSelector:
    """
    Aggregates beneficiary profiles from normalized slip records.
    Identifies primary persons of interest (Whales) and enables focused court filtering.
    """

    def __init__(self):
        pass

    def aggregate(self, records: List[NormalizedEvidenceRecord]) -> RecipientPOISummary:
        """Aggregates all recipients and calculates financial totals."""
        groups: Dict[str, Dict[str, Any]] = {}
        total_slips = 0
        total_amt = 0.0

        for r in records:
            if (r.evidence_category or "").upper() != "SLIP":
                continue
            name = (r.receiver_name or "ไม่ระบุชื่อผู้รับ").strip()
            total_slips += 1
            total_amt += r.amount

            if name not in groups:
                groups[name] = {
                    "count": 0,
                    "total_amount": 0.0,
                    "banks": set(),
                    "accounts": set()
                }

            groups[name]["count"] += 1
            groups[name]["total_amount"] += r.amount
            if r.receiver_bank:
                groups[name]["banks"].add(r.receiver_bank)
            if r.receiver_account:
                groups[name]["accounts"].add(r.receiver_account)

        poi_dict: Dict[str, POIRecord] = {}
        primary_poi: Optional[POIRecord] = None
        max_amount = -1.0

        for name, data in groups.items():
            record = POIRecord(
                name=name,
                count=data["count"],
                total_amount=data["total_amount"],
                banks=sorted(list(data["banks"])),
                accounts=sorted(list(data["accounts"]))
            )
            poi_dict[name] = record

            # Select Whale by total financial volume (or frequency if volume equal)
            if record.total_amount > max_amount or (record.total_amount == max_amount and (primary_poi and record.count > primary_poi.count)):
                max_amount = record.total_amount
                primary_poi = record

        return RecipientPOISummary(
            recipients=poi_dict,
            primary_poi=primary_poi,
            total_reconciled_slips=total_slips,
            total_reconciled_amount=total_amt
        )

    def filter_by_recipient(
        self,
        records: List[NormalizedEvidenceRecord],
        recipient_name: str
    ) -> List[NormalizedEvidenceRecord]:
        """Filters evidence records specifically targeting a given recipient POI."""
        target = recipient_name.strip()
        return [
            r for r in records
            if (r.evidence_category or "").upper() == "SLIP" and (r.receiver_name or "").strip() == target
        ]

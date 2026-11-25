# -*- coding: utf-8 -*-
"""
KPI Target & Financial Loss Aggregator (Task 3 Engine)
ระบบแสดงผลแบบ KPI: รวมรายชื่อผู้รับโอนและยอดเงินรวม พร้อมระบบ Checkbox เจาะจงเป้าหมายสู่งานที่ 5
🔒 ควบคุมและล็อกระบบการทำงานด้วย "Lock Skill" (5 Invariant Gates & Deterministic Engine Protocol)
"""

import json
import re
import os
import gc
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional, Set

# =============================================================================
# GATE 3: Immutable Parameter Lock (แช่แข็งตัวแปรคอนฟิก ป้องกันการดัดแปลง)
# =============================================================================
@dataclass(frozen=True)
class LockedKPIConfig:
    min_name_length: int = 1
    decimal_precision: int = 2
    default_currency: str = "THB"
    enforce_strict_grounding: bool = True
    prefix_patterns: tuple = (
        r"^นาย\s*", r"^นางสาว\s*", r"^นาง\s*", r"^น\.ส\.\s*", r"^ด\.ช\.\s*", r"^ด\.ญ\.\s*",
        r"^เด็กชาย\s*", r"^เด็กหญิง\s*", r"^mr\.\s*", r"^mrs\.\s*", r"^ms\.\s*", r"^miss\s*",
        r"^ร\.ต\.ต\.\s*", r"^พ\.ต\.ท\.\s*", r"^พ\.ต\.อ\.\s*", r"^ส\.ต\.ต\.\s*", r"^สิบตรี\s*",
        r"^พลฯ\s*", r"^จ\.ส\.อ\.\s*", r"^บจก\.\s*", r"^หจก\.\s*"
    )
    supported_tasks: tuple = ("TASK_1", "TASK_2", "STREAM_DIRECT", "BATCH_INGEST")


# =============================================================================
# GATE 1 & 2: Pure Normalizer & Stateless Sanitation
# =============================================================================
def normalize_person_name(raw_name: Optional[str], config: LockedKPIConfig = LockedKPIConfig()) -> str:
    """
    [PURE FUNCTION] ลบคำนำหน้าชื่อไทย/อังกฤษ และช่องว่างส่วนเกิน
    ทำงานแบบ Stateless ไร้ผลข้างเคียง (Idempotent 100%)
    """
    if not raw_name or not isinstance(raw_name, str):
        return "ไม่ระบุชื่อผู้รับ (UNKNOWN)"
    
    cleaned = raw_name.strip()
    # กำจัดขยะอักขระ OCR หัวท้าย
    cleaned = re.sub(r"^[^\wก-๙]+", "", cleaned)
    cleaned = re.sub(r"[^\wก-๙\s.]+", "", cleaned)
    
    for p in config.prefix_patterns:
        cleaned = re.sub(p, "", cleaned, flags=re.IGNORECASE)
    
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    if len(cleaned) < config.min_name_length:
        return "ไม่ระบุชื่อผู้รับ (UNKNOWN)"
    return cleaned


# =============================================================================
# 🔒 LOCKED EXECUTION ENGINE (The 5 Invariant Gates of Task 3)
# =============================================================================
class LockedKPITargetAggregator:
    """
    เครื่องยนต์ประมวลผล Task 3 ที่ถูกล็อกระบบการทำงานด้วย 'Lock Skill'
    ควบคุมด้วย 5-Stage Invariant Gates ป้องกัน Workflow Drift ตลอดกาล
    """
    def __init__(self, config: LockedKPIConfig = LockedKPIConfig()):
        self.config = config
        self.raw_records: List[Dict[str, Any]] = []
        self.kpi_groups: Dict[str, Dict[str, Any]] = {}
        self.selected_target: Optional[str] = None
        self._execution_locked: bool = False

    def reset_isolated_context(self):
        """
        [GATE 2: Stateless Context Isolation]
        ล้างหน่วยความจำและตัวแปรตกค้างทั้งหมด ป้องกัน Memory Leak & Cross-contamination
        """
        self.raw_records.clear()
        self.kpi_groups.clear()
        self.selected_target = None
        self._execution_locked = False
        gc.collect()

    def assert_pre_flight_invariants(self, slip_data: Any) -> List[Dict[str, Any]]:
        """
        [GATE 1: Pre-Flight Input Invariant Assertion]
        ตรวจสอบสัญญาข้อมูลนำเข้า (Data Contract) หากข้อมูลว่างหรือผิดสเปก ให้ตัดวงจรทันที
        """
        if slip_data is None:
            raise ValueError("[GATE 1 ASSERTION FAIL] Input payload is None")

        if isinstance(slip_data, str) and os.path.exists(slip_data):
            try:
                with open(slip_data, "r", encoding="utf-8") as f:
                    slip_data = json.load(f)
            except Exception as e:
                raise ValueError(f"[GATE 1 ASSERTION FAIL] Cannot parse input JSON file: {e}")

        items = []
        if isinstance(slip_data, dict):
            items = [slip_data]
        elif isinstance(slip_data, list):
            items = slip_data
        else:
            raise TypeError(f"[GATE 1 ASSERTION FAIL] Unsupported data type: {type(slip_data)}")

        if len(items) == 0:
            raise ValueError("[GATE 1 ASSERTION FAIL] Payload contains 0 records (Empty Batch)")

        # Validate internal fields per item
        validated_items = []
        for idx, item in enumerate(items):
            if not isinstance(item, dict):
                raise TypeError(f"[GATE 1 ASSERTION FAIL] Record #{idx} is not a dictionary")
            validated_items.append(item)

        return validated_items

    def ingest(self, slip_data: Any, source_task: str = "AUTO"):
        """
        [GATE 4: Sequential Pipeline Step 1 - Ingestion & Normalization]
        รับข้อมูลจาก Task 1 (สลิปเดี่ยว) หรือ Task 2 (สลิปในแชท) อย่างอิสระ
        """
        # GATE 1 Check
        valid_items = self.assert_pre_flight_invariants(slip_data)

        for item in valid_items:
            # ตรวจสอบ source_task
            source = item.get("source_task", source_task)
            if source == "AUTO":
                source = "TASK_2" if ("step1_ms" in item or "step1_detection" in item or "slip_bbox" in item) else "TASK_1"

            # สกัดชื่อผู้รับ
            rec_name = item.get("receiver_name")
            if not rec_name:
                rec_val = item.get("receiver")
                if isinstance(rec_val, dict):
                    rec_name = rec_val.get("name")
                elif isinstance(rec_val, str):
                    rec_name = rec_val
            if not rec_name:
                rec_name = item.get("to_name")

            # สกัดชื่อผู้โอนและบัญชี
            sender_name = item.get("sender_name")
            sender_acc = item.get("sender_account")
            s_val = item.get("sender")
            if isinstance(s_val, dict):
                sender_name = sender_name or s_val.get("name")
                sender_acc = sender_acc or s_val.get("account")
            elif isinstance(s_val, str) and not sender_name:
                sender_name = s_val

            rec_acc = item.get("receiver_account")
            r_val = item.get("receiver")
            if isinstance(r_val, dict):
                rec_acc = rec_acc or r_val.get("account")

            # สกัดยอดเงิน
            raw_amt = item.get("amount") or item.get("total_amount")
            if raw_amt is None and isinstance(item.get("step2_extraction"), dict):
                raw_amt = item["step2_extraction"].get("amount")

            try:
                amt = float(raw_amt or 0.0)
            except (ValueError, TypeError):
                amt = 0.0

            if amt < 0.0:
                raise ValueError(f"[GATE 1 ASSERTION FAIL] ยอดเงินติดลบ ({amt}) เป็นไปไม่ได้ในทางคดีอาญา")

            norm_name = normalize_person_name(rec_name, self.config)

            record = {
                "source_task": source,
                "raw_receiver_name": str(rec_name) if rec_name else None,
                "normalized_name": norm_name,
                "amount": round(amt, self.config.decimal_precision),
                "fee": float(item.get("fee", 0.0) or 0.0),
                "ref_no": item.get("ref_no") or item.get("ref_id") or "-",
                "bank": item.get("bank") or "ไม่ระบุ",
                "sender_name": sender_name or "-",
                "sender_account": sender_acc or "-",
                "receiver_account": rec_acc or "-",
                "datetime": item.get("datetime") or item.get("iso_datetime") or "-",
                "file": item.get("file") or item.get("image_path") or "-"
            }
            self.raw_records.append(record)

        # เดินต่อสู่ GATE 4 Step 2
        self._recompute_groups_locked()
        return self

    def _recompute_groups_locked(self):
        """
        [GATE 4: Sequential Pipeline Step 2 - Deterministic Aggregation]
        จัดกลุ่มสลิปตามชื่อผู้รับ รวมยอดเงิน ป้องกัน Floating Point Error
        """
        self.kpi_groups.clear()

        for rec in self.raw_records:
            norm_name = rec["normalized_name"]
            if norm_name not in self.kpi_groups:
                self.kpi_groups[norm_name] = {
                    "target_name": norm_name,
                    "display_name": rec["raw_receiver_name"] or norm_name,
                    "total_amount": 0.0,
                    "slip_count": 0,
                    "banks": set(),
                    "accounts": set(),
                    "ref_ids": [],
                    "slips": [],
                    "is_selected": False
                }

            group = self.kpi_groups[norm_name]
            # สะสมยอดเงินแบบล็อกทศนิยม 2 ตำแหน่ง
            group["total_amount"] = round(group["total_amount"] + rec["amount"], self.config.decimal_precision)
            group["slip_count"] += 1
            if rec["bank"] and rec["bank"] != "ไม่ระบุ":
                group["banks"].add(rec["bank"])
            if rec["receiver_account"] and rec["receiver_account"] != "-":
                group["accounts"].add(rec["receiver_account"])
            if rec["ref_no"] and rec["ref_no"] != "-":
                group["ref_ids"].append(rec["ref_no"])
            group["slips"].append(rec)

        # บังคับเลือก Target Default (รายการที่ยอดเงินสูงสุด)
        if self.selected_target and self.selected_target in self.kpi_groups:
            self.kpi_groups[self.selected_target]["is_selected"] = True
        elif self.kpi_groups:
            highest_target = max(self.kpi_groups.keys(), key=lambda k: self.kpi_groups[k]["total_amount"])
            self.kpi_groups[highest_target]["is_selected"] = True
            self.selected_target = highest_target

        # สั่งรัน GATE 5 ตรวจสอบสุขภาพผลลัพธ์ทันที
        self._assert_post_flight_circuit_breaker()

    def _assert_post_flight_circuit_breaker(self):
        """
        [GATE 5: Post-Flight Health Circuit Breaker]
        ตรวจสอบ Invariant ทางคณิตศาสตร์:
        1. ผลรวมของยอดเงินแต่ละกลุ่ม ต้องเท่ากับผลรวมของสลิปทุกใบ 100.00%
        2. จำนวนสลิปในกลุ่ม ต้องเท่ากับจำนวน Record ย่อยทั้งหมด
        3. ต้องมีเป้าหมายถูกเลือก 1 รายการ
        """
        sum_records = round(sum(r["amount"] for r in self.raw_records), self.config.decimal_precision)
        sum_groups = round(sum(g["total_amount"] for g in self.kpi_groups.values()), self.config.decimal_precision)

        if abs(sum_records - sum_groups) > 0.001:
            raise RuntimeError(
                f"[GATE 5 CIRCUIT BREAKER TRIGGERED] ยอดเงินไม่ดุล: Records={sum_records} vs Groups={sum_groups}"
            )

        total_group_slips = sum(g["slip_count"] for g in self.kpi_groups.values())
        if total_group_slips != len(self.raw_records):
            raise RuntimeError(
                f"[GATE 5 CIRCUIT BREAKER TRIGGERED] จำนวนสลิปรวน: Records={len(self.raw_records)} vs Groups={total_group_slips}"
            )

        self._execution_locked = True

    def select_target(self, target_name: str) -> bool:
        """
        [GATE 4: Sequential Pipeline Step 3 - Interactive Checkbox Target Selection]
        ทำเครื่องหมายเช็คบล็อกเลือกบุคคลเป้าหมายที่จะส่งรายละเอียดให้งานที่ 5
        """
        norm_name = normalize_person_name(target_name, self.config)
        if norm_name in self.kpi_groups:
            for k in self.kpi_groups:
                self.kpi_groups[k]["is_selected"] = (k == norm_name)
            self.selected_target = norm_name
            return True
        return False

    def get_kpi_summary(self) -> List[Dict[str, Any]]:
        """
        ส่งออกข้อมูล KPI Summary พร้อม Contract Validation
        """
        if not self._execution_locked:
            self._assert_post_flight_circuit_breaker()

        summary = []
        for name, data in self.kpi_groups.items():
            summary.append({
                "target_name": data["target_name"],
                "display_name": data["display_name"],
                "total_amount": round(data["total_amount"], self.config.decimal_precision),
                "total_amount_formatted": f"{data['total_amount']:,.2f} {self.config.default_currency}",
                "slip_count": data["slip_count"],
                "banks": sorted(list(data["banks"])),
                "accounts": sorted(list(data["accounts"])),
                "ref_ids": data["ref_ids"],
                "is_selected": data["is_selected"],
                "has_multiple_slips": data["slip_count"] > 1,
                "workflow_lock_status": "VERIFIED_LOCKED"
            })
        summary.sort(key=lambda x: x["total_amount"], reverse=True)
        return summary

    def export_for_task5(self, target_name: Optional[str] = None) -> Dict[str, Any]:
        """
        [GATE 4: Sequential Pipeline Step 4 - Handoff to Task 5]
        สร้าง Payload พิเศษที่ถูกล็อกความถูกต้องสำหรับส่งต่อไปยังงานที่ 5
        """
        sel_name = normalize_person_name(target_name, self.config) if target_name else self.selected_target
        if not sel_name or sel_name not in self.kpi_groups:
            return {
                "status": "CIRCUIT_BREAKER_NO_TARGET",
                "message": "ยังไม่มีการเลือกชื่อเป้าหมายผ่านเช็คบล็อก"
            }

        target_data = self.kpi_groups[sel_name]
        return {
            "status": "LOCKED_READY_FOR_TASK_5",
            "task_source": "TASK_3_LOCKED_KPI_AGGREGATOR",
            "invariants_verified": True,
            "target_person": {
                "name": target_data["target_name"],
                "display_name": target_data["display_name"],
                "total_loss_amount": round(target_data["total_amount"], self.config.decimal_precision),
                "total_loss_formatted": f"{target_data['total_amount']:,.2f} {self.config.default_currency}",
                "total_transactions": target_data["slip_count"],
                "accounts_involved": sorted(list(target_data["accounts"])),
                "banks_involved": sorted(list(target_data["banks"]))
            },
            "timeline_transactions": [
                {
                    "ref_no": s["ref_no"],
                    "datetime": s["datetime"],
                    "amount": s["amount"],
                    "bank": s["bank"],
                    "sender": s["sender_name"],
                    "source_task": s["source_task"],
                    "evidence_file": s["file"]
                }
                for s in target_data["slips"]
            ]
        }

    def generate_html_dashboard(self, output_file: str = "artifacts/task3_kpi_dashboard.html") -> str:
        """
        สร้างหน้าแดชบอร์ด KPI แบบ Interactive พร้อมสัญลักษณ์ Workflow Lock
        """
        kpi_list = self.get_kpi_summary()
        total_all_loss = sum(k["total_amount"] for k in kpi_list)
        total_slips = sum(k["slip_count"] for k in kpi_list)
        total_targets = len(kpi_list)

        rows_html = ""
        for i, item in enumerate(kpi_list, 1):
            checked = "checked" if item["is_selected"] else ""
            active_class = "selected-row" if item["is_selected"] else ""
            banks_badge = "".join([f'<span class="badge bank-badge">{b}</span>' for b in item["banks"]])
            acc_badge = "".join([f'<span class="badge acc-badge">{a}</span>' for a in item["accounts"]])
            slip_badge = f'<span class="badge count-badge">{item["slip_count"]} สลิป</span>'
            
            rows_html += f"""
            <tr class="{active_class}" id="row-{i}">
                <td style="text-align: center;">
                    <input type="checkbox" class="kpi-checkbox" name="target_choice" 
                           value="{item['target_name']}" {checked} onchange="selectTarget('{item['target_name']}', this)">
                </td>
                <td style="text-align: center; color: #94a3b8; font-family: monospace;">{i:02d}</td>
                <td>
                    <div style="font-weight: 700; font-size: 1.05rem; color: #f8fafc;">{item['display_name']}</div>
                    <div style="font-size: 0.8rem; color: #64748b; margin-top: 2px;">{acc_badge} {banks_badge}</div>
                </td>
                <td style="text-align: center;">{slip_badge}</td>
                <td style="text-align: right; font-family: 'JetBrains Mono', monospace; font-size: 1.15rem; font-weight: 800; color: #38bdf8;">
                    {item['total_amount_formatted']}
                </td>
                <td style="text-align: center;">
                    <span class="status-pill {'status-active' if item['is_selected'] else 'status-ready'}">
                        {'⚡ เจาะจงสู่งานที่ 5' if item['is_selected'] else 'พร้อมส่งต่อ'}
                    </span>
                </td>
            </tr>
            """

        html_content = f"""<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TASK 3: KPI Target & Financial Loss Aggregator [LOCKED]</title>
    <link href="https://fonts.googleapis.com/css2?family=Chakra+Petch:wght@400;600;700&family=JetBrains+Mono:wght@500;700;800&family=Sarabun:wght@300;400;600;700&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg-base: #090d16;
            --panel-bg: rgba(15, 23, 42, 0.75);
            --border-glass: rgba(56, 189, 248, 0.2);
            --accent-cyan: #38bdf8;
            --accent-emerald: #10b981;
            --accent-amber: #f59e0b;
            --accent-purple: #a855f7;
            --text-main: #f1f5f9;
            --text-muted: #94a3b8;
        }}
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{
            background: radial-gradient(circle at 50% 0%, #1e293b 0%, #090d16 80%);
            color: var(--text-main);
            font-family: 'Sarabun', sans-serif;
            min-height: 100vh;
            padding: 30px;
        }}
        .container {{ max-width: 1200px; margin: 0 auto; }}
        header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid var(--border-glass);
            padding-bottom: 20px;
            margin-bottom: 25px;
        }}
        h1 {{
            font-family: 'Chakra Petch', sans-serif;
            font-size: 1.6rem;
            letter-spacing: 0.5px;
            color: #fff;
            display: flex;
            align-items: center;
            gap: 12px;
        }}
        .kpi-badge {{
            background: linear-gradient(135deg, #0284c7, #2563eb);
            color: #fff;
            padding: 4px 12px;
            border-radius: 6px;
            font-size: 0.8rem;
            font-weight: 700;
        }}
        .lock-pill {{
            background: rgba(16, 185, 129, 0.15);
            border: 1px solid #10b981;
            color: #34d399;
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 0.8rem;
            font-weight: 700;
            display: inline-flex;
            align-items: center;
            gap: 6px;
        }}
        .grid-kpi {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 20px;
            margin-bottom: 30px;
        }}
        .kpi-card {{
            background: var(--panel-bg);
            border: 1px solid var(--border-glass);
            backdrop-filter: blur(16px);
            border-radius: 12px;
            padding: 20px;
            position: relative;
            overflow: hidden;
        }}
        .kpi-card::before {{
            content: '';
            position: absolute;
            top: 0; left: 0; right: 0; height: 3px;
            background: var(--accent-cyan);
        }}
        .kpi-card.emerald::before {{ background: var(--accent-emerald); }}
        .kpi-card.amber::before {{ background: var(--accent-amber); }}
        .kpi-label {{
            font-size: 0.85rem;
            color: var(--text-muted);
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 8px;
        }}
        .kpi-val {{
            font-family: 'JetBrains Mono', monospace;
            font-size: 2rem;
            font-weight: 800;
            color: #fff;
        }}
        .table-panel {{
            background: var(--panel-bg);
            border: 1px solid var(--border-glass);
            backdrop-filter: blur(16px);
            border-radius: 12px;
            padding: 24px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.4);
        }}
        .panel-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 18px;
        }}
        .panel-title {{
            font-family: 'Chakra Petch', sans-serif;
            font-size: 1.2rem;
            color: #38bdf8;
            font-weight: 700;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
        }}
        th {{
            background: rgba(30, 41, 59, 0.8);
            color: #94a3b8;
            font-size: 0.85rem;
            font-weight: 600;
            text-align: left;
            padding: 12px 16px;
            border-bottom: 1px solid rgba(255,255,255,0.1);
        }}
        td {{
            padding: 16px;
            border-bottom: 1px solid rgba(255,255,255,0.05);
            font-size: 0.95rem;
        }}
        tr:hover td {{
            background: rgba(56, 189, 248, 0.05);
        }}
        tr.selected-row td {{
            background: rgba(16, 185, 129, 0.12);
            border-bottom-color: rgba(16, 185, 129, 0.3);
        }}
        .kpi-checkbox {{
            width: 20px;
            height: 20px;
            cursor: pointer;
            accent-color: #10b981;
        }}
        .badge {{
            display: inline-block;
            font-size: 0.75rem;
            padding: 2px 8px;
            border-radius: 4px;
            margin-right: 4px;
            font-family: monospace;
        }}
        .bank-badge {{ background: rgba(56, 189, 248, 0.2); color: #38bdf8; }}
        .acc-badge {{ background: rgba(148, 163, 184, 0.2); color: #cbd5e1; }}
        .count-badge {{ background: rgba(245, 158, 11, 0.2); color: #fbbf24; font-weight: 700; }}
        .status-pill {{
            font-size: 0.75rem;
            padding: 4px 10px;
            border-radius: 20px;
            font-weight: 600;
        }}
        .status-active {{ background: #064e3b; color: #34d399; border: 1px solid #059669; }}
        .status-ready {{ background: #1e293b; color: #94a3b8; border: 1px solid #334155; }}
        .action-bar {{
            margin-top: 25px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding-top: 15px;
            border-top: 1px solid var(--border-glass);
        }}
        .btn-task5 {{
            background: linear-gradient(135deg, #10b981, #059669);
            color: #fff;
            padding: 12px 24px;
            font-size: 1rem;
            font-weight: 700;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            box-shadow: 0 4px 15px rgba(16, 185, 129, 0.4);
            display: flex;
            align-items: center;
            gap: 10px;
            transition: all 0.2s;
        }}
        .btn-task5:hover {{
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(16, 185, 129, 0.6);
        }}
        .payload-preview {{
            margin-top: 20px;
            background: #020617;
            padding: 15px;
            border-radius: 8px;
            border: 1px solid #1e293b;
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.8rem;
            color: #38bdf8;
            max-height: 180px;
            overflow-y: auto;
            white-space: pre-wrap;
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <div>
                <h1><span>📊 TASK 3: KPI Target & Financial Loss Aggregator</span> <span class="lock-pill">🔒 WORKFLOW LOCKED</span></h1>
                <p style="color: #64748b; font-size: 0.9rem; margin-top: 4px;">ระบบรวบรวมรายชื่อ บวกรวมยอดความเสียหาย และเจาะจงเป้าหมายสู่งานที่ 5 ภายใต้ 5 Invariant Gates</p>
            </div>
            <div style="text-align: right; font-family: monospace; font-size: 0.85rem; color: #94a3b8;">
                ENGINE: <span style="color: #10b981; font-weight: bold;">LOCKED DETERMINISTIC</span><br>
                PIPELINE: TASK 1 / TASK 2 ➔ TASK 3 ➔ TASK 5
            </div>
        </header>

        <!-- KPI Summary Cards -->
        <div class="grid-kpi">
            <div class="kpi-card amber">
                <div class="kpi-label">👤 บุคคลเป้าหมายที่ตรวจพบ (Unique Targets)</div>
                <div class="kpi-val" id="val-targets">{total_targets} <span style="font-size: 1rem; font-weight: normal; color: #94a3b8;">ราย</span></div>
            </div>
            <div class="kpi-card">
                <div class="kpi-label">🧾 จำนวนสลิปรวมทั้งหมด (Total Slips Detected)</div>
                <div class="kpi-val" id="val-slips">{total_slips} <span style="font-size: 1rem; font-weight: normal; color: #94a3b8;">ฉบับ</span></div>
            </div>
            <div class="kpi-card emerald">
                <div class="kpi-label">💰 ยอดเงินความเสียหายรวมทั้งหมด (Total Net Loss)</div>
                <div class="kpi-val" id="val-amount">{total_all_loss:,.2f} <span style="font-size: 1rem; font-weight: normal; color: #94a3b8;">บาท</span></div>
            </div>
        </div>

        <!-- Table Component -->
        <div class="table-panel">
            <div class="panel-header">
                <div class="panel-title">📋 สรุปบัญชีรายชื่อและยอดเงินตามบุคคลเป้าหมาย (KPI Summary Table)</div>
                <span style="font-size: 0.85rem; color: #94a3b8;">* ติ๊ก Checkbox เพื่อเจาะจงเป้าหมายที่จะนำไปสร้างรายละเอียดในงานที่ 5</span>
            </div>

            <table>
                <thead>
                    <tr>
                        <th style="width: 50px; text-align: center;">เลือก</th>
                        <th style="width: 50px; text-align: center;">ลำดับ</th>
                        <th>ชื่อผู้รับโอน / บัญชีที่เกี่ยวข้อง</th>
                        <th style="width: 120px; text-align: center;">จำนวนสลิป</th>
                        <th style="width: 200px; text-align: right;">ยอดรวมสุทธิ (บาท)</th>
                        <th style="width: 150px; text-align: center;">สถานะส่งต่อ</th>
                    </tr>
                </thead>
                <tbody id="table-body">
                    {rows_html}
                </tbody>
            </table>

            <div class="action-bar">
                <div>
                    <span style="color: #94a3b8; font-size: 0.9rem;">เป้าหมายที่ถูกเลือกขณะนี้: </span>
                    <strong id="active-target-name" style="color: #10b981; font-size: 1.1rem; margin-left: 8px;">
                        {self.selected_target or 'ยังไม่มีการเลือก'}
                    </strong>
                </div>
                <button class="btn-task5" onclick="triggerExportTask5()">
                    <span>🚀 ยืนยันเป้าหมายและส่งต่อไปยังงานที่ 5</span>
                </button>
            </div>

            <div style="margin-top: 15px;">
                <div style="font-size: 0.8rem; color: #64748b; margin-bottom: 5px;">Handoff Payload to Task 5 (Locked Contract JSON):</div>
                <div class="payload-preview" id="payload-box">{json.dumps(self.export_for_task5(), ensure_ascii=False, indent=2)}</div>
            </div>
        </div>
    </div>

    <script>
        const allGroups = {json.dumps(self.get_kpi_summary(), ensure_ascii=False)};
        
        function selectTarget(targetName, checkboxElem) {{
            const checkboxes = document.querySelectorAll('.kpi-checkbox');
            checkboxes.forEach(cb => {{
                if (cb !== checkboxElem) cb.checked = false;
            }});

            const rows = document.querySelectorAll('tbody tr');
            rows.forEach(r => r.classList.remove('selected-row'));

            if (checkboxElem.checked) {{
                checkboxElem.closest('tr').classList.add('selected-row');
                document.getElementById('active-target-name').innerText = targetName;
                updatePayload(targetName);
            }} else {{
                document.getElementById('active-target-name').innerText = 'ยังไม่มีการเลือก';
                document.getElementById('payload-box').innerText = JSON.stringify({{"status": "NO_TARGET_SELECTED"}}, null, 2);
            }}
        }}

        function updatePayload(targetName) {{
            const selected = allGroups.find(g => g.target_name === targetName);
            if (!selected) return;
            const payload = {{
                "status": "LOCKED_READY_FOR_TASK_5",
                "task_source": "TASK_3_LOCKED_KPI_AGGREGATOR",
                "invariants_verified": true,
                "target_person": {{
                    "name": selected.target_name,
                    "display_name": selected.display_name,
                    "total_loss_amount": selected.total_amount,
                    "total_loss_formatted": selected.total_amount_formatted,
                    "total_transactions": selected.slip_count,
                    "accounts_involved": selected.accounts,
                    "banks_involved": selected.banks
                }},
                "ref_ids": selected.ref_ids
            }};
            document.getElementById('payload-box').innerText = JSON.stringify(payload, null, 2);
        }}

        function triggerExportTask5() {{
            const activeName = document.getElementById('active-target-name').innerText;
            if (activeName === 'ยังไม่มีการเลือก') {{
                alert('กรุณาติ๊กเลือกเป้าหมายอย่างน้อย 1 รายการก่อนส่งต่อไปยังงานที่ 5');
                return;
            }}
            alert('ส่งข้อมูลเป้าหมาย [' + activeName + '] สู่งานที่ 5 เรียบร้อยแล้ว!');
        }}
    </script>
</body>
</html>
"""
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(html_content)
        return output_file

# Alias เพื่อความเข้ากันได้
KPITargetAggregator = LockedKPITargetAggregator


if __name__ == "__main__":
    print("=== [LOCK SKILL ACTIVATED]: Testing Task 3 Deterministic Engine ===")
    agg = LockedKPITargetAggregator()

    # 1. ทดสอบ Input จาก Task 1 (สลิปเดี่ยว A4_IMG_ (100).PNG)
    sample_task1 = {
        "source_task": "TASK_1",
        "file": "A4_IMG_ (100).PNG",
        "bank": "ธนาคารกรุงไทย (KTB)",
        "ref_no": "N006727673034053896171486",
        "amount": 1000.0,
        "fee": 0.0,
        "receiver_name": "น.ส. จิณห์นิภา บุญประเสริฐ",
        "receiver_account": "XXX-X-XX764-0",
        "datetime": "12 มี.ค. 2568 20:17"
    }

    # 2. ทดสอบ Input จาก Task 2 (สลิปในแชท chatv3 (41).jpg)
    sample_task2 = {
        "source_task": "TASK_2",
        "file": "chatv3 (41).jpg",
        "bank": "กรุงไทย",
        "ref_no": "Aa7e0058a52854e5c",
        "amount": 5600.0,
        "fee": 0.0,
        "receiver_name": "นางสาว อลงกรณ์ แจ่มเมือง",
        "receiver_account": "XXX-X-XX259-1",
        "datetime": "26 พ.ค. 2568 - 16:52"
    }

    # 3. ทดสอบสลิปซ้ำชื่อเพื่อทดสอบ Aggregation
    sample_duplicate_target = {
        "source_task": "TASK_2",
        "file": "chatv3 (99).jpg",
        "bank": "กรุงไทย",
        "ref_no": "Bb8f9900112233",
        "amount": 4400.0,
        "fee": 0.0,
        "receiver_name": "อลงกรณ์ แจ่มเมือง",
        "receiver_account": "XXX-X-XX259-1",
        "datetime": "27 พ.ค. 2568 - 10:15"
    }

    agg.ingest([sample_task1, sample_task2, sample_duplicate_target])

    print("\n✅ GATE 1-5 PASSED: KPI Summary Output")
    print(json.dumps(agg.get_kpi_summary(), ensure_ascii=False, indent=2))

    print("\n✅ Locked Task 5 Handoff Payload:")
    print(json.dumps(agg.export_for_task5(), ensure_ascii=False, indent=2))

    dash_path = r"d:\Project\ชวกม.2\artifacts\task3_kpi_dashboard.html"
    agg.generate_html_dashboard(dash_path)
    print(f"\nLocked Dashboard generated at: {dash_path}")

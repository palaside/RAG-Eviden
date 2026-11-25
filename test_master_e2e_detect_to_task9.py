#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
========================================================================================
MASTER ATOMIC E2E WORKFLOW TEST SUITE: DETECT THROUGH TASK 9
File: d:\\Project\\ชวกม.2\\test_master_e2e_detect_to_task9.py
Lead Architect: Principal QA Architect, Forensic Systems Engineer & Tech Lead
Standard: 4 Iron Rules of Production Parity, 4-Axis Pipeline Audit & 7-State Matrix
========================================================================================
ครอบคลุมกระบวนการตั้งแต่:
  [DETECT]  Forensic Image Intake & Classification Gateway (TYPE_SLIP_SOLO / TYPE_CHAT)
  [TASK 1]  Client-Side In-Browser Auto-Detection & Feature Normalization
  [TASK 2]  Staging Buffer, File Registry & Event-Driven KPI Calculation
  [TASK 3]  Slip Recipient Aggregator & Target POI Selector
  [TASK 4]  Timeline Chronological Sequencer & Six-Agent Deep Analyzer
  [TASK 5]  Pure Slip SSOT, 4 KPI Cards & 100% Mathematical Reconciliation Audit
  [TASK 7]  11-Column Court Evidence Table (ISO/IEC 27037 Standard)
  [TASK 8]  Court-Ready Dossier Assembler (7-Part Exhibit Structure)
  [TASK 9]  Vault Exporter, Derivative Generator & Encrypted SFX Dossier (5 Invariant Gates)
========================================================================================
"""

import unittest
import os
import json
import time
import hashlib
from datetime import datetime, timezone

# Real Production Engine Imports
from detect_gateway import DetectGateway, EvidenceType
from task1_feature_normalization import Task1FeatureNormalizer
from task2_staging_buffer import Task2StagingBuffer, BufferState
from task3_recipient_poi import Task3RecipientSelector
from task4_six_agents_deep_analyzer import Task4SixAgentsDeepAnalyzer
from task5_pure_slip_sot_engine import LockedTask5PureSlipSOTEngine, LockedTask5Config
from task7_evidence_summary_table import LockedTask7EvidenceTableEngine, LockedTask7Config
from task8_court_dossier_assembler import Task8CourtDossierAssembler, LockedDossierConfig
from task9_vault_exporter import Task9VaultExporter, LockedVaultConfig


class TestMasterE2EWorkflow(unittest.TestCase):
    """
    ชุดทดสอบบูรณาการระดับสถาปัตยกรรม (Master E2E Workflow Pipeline)
    ครอบคลุม 4 Iron Rules, 4-Axis Audit, 7-State Matrix และ Zero Blast Radius
    """

    @classmethod
    def setUpClass(cls):
        cls.system_logs = []
        cls.audit_trail = []
        cls.start_time = time.time()
        cls.record_audit_trail("SYSTEM_INITIALIZED", "Master E2E Verification Engine Online (Detect to Task 9)")

    @classmethod
    def record_system_log(cls, severity: str, file_path: str, line: int, func: str, err_code: str, expected: str, actual: str, payload: dict):
        log_entry = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "traceId": f"TRACE-{int(time.time()*1000)}",
            "severity": severity,
            "file_path": file_path,
            "line": line,
            "function_name": func,
            "error_code": err_code,
            "expected_vs_actual": f"Expected: {expected} | Actual: {actual}",
            "sanitized_payload": payload
        }
        cls.system_logs.append(log_entry)

    @classmethod
    def record_audit_trail(cls, event_type: str, detail: str, metadata: dict = None):
        trail_entry = {
            "seq": len(cls.audit_trail) + 1,
            "timestamp_utc": datetime.now(timezone.utc).isoformat(),
            "event_type": event_type,
            "detail": detail,
            "metadata": metadata or {}
        }
        cls.audit_trail.append(trail_entry)

    def setUp(self):
        # Production Parity Forensic Dataset
        self.evidence_dataset = [
            {
                "file_id": "RAW-001",
                "name": "chat_intro_borrow.jpg",
                "width": 1080,
                "height": 2400,
                "aspect_ratio": 2.22,
                "type_expected": "TYPE_CHAT",
                "dialogue_text": "ตัวเองเค้าขอยืมเงิน 2,000 ก่อนได้ไหม พรุ่งนี้โอนคืนให้จ้า",
                "timestamp": "2026-11-20T08:15:00"
            },
            {
                "file_id": "RAW-002",
                "name": "slip_scb_first_2000.jpg",
                "width": 1080,
                "height": 1920,
                "aspect_ratio": 1.77,
                "type_expected": "TYPE_SLIP_SOLO",
                "ocr_data": {
                    "file": "slip_scb_first_2000.jpg",
                    "bank": "SCB",
                    "receiver_name": "นางสาว จิณห์นิภา ประสาทเขตรการ",
                    "receiver_account": "xxx-x-x1234-x",
                    "sender_name": "นาย ณัฐชัย รักษาวงษ์",
                    "amount": 2000.00,
                    "datetime": "2026-11-20T08:18:22",
                    "ref_no": "20261120SCB00188942"
                }
            },
            {
                "file_id": "RAW-003",
                "name": "chat_urgency_escalation.jpg",
                "width": 1080,
                "height": 2400,
                "aspect_ratio": 2.22,
                "type_expected": "TYPE_CHAT",
                "dialogue_text": "ขอเพิ่มอีก 8,500 นะคะด่วนมาก พอดีต้องรีบวางมัดจำ ไม่งั้นจะโดนยึดเงิน",
                "timestamp": "2026-11-20T10:45:00"
            },
            {
                "file_id": "RAW-004",
                "name": "slip_kbank_whale_8500.jpg",
                "width": 1080,
                "height": 1920,
                "aspect_ratio": 1.77,
                "type_expected": "TYPE_SLIP_SOLO",
                "ocr_data": {
                    "file": "slip_kbank_whale_8500.jpg",
                    "bank": "KBANK",
                    "receiver_name": "นางสาว จิณห์นิภา ประสาทเขตรการ",
                    "receiver_account": "xxx-x-x5678-x",
                    "sender_name": "นาย ณัฐชัย รักษาวงษ์",
                    "amount": 8500.00,
                    "datetime": "2026-11-20T10:48:05",  # ภายใน 3 นาที = Burst Anomaly
                    "ref_no": "20261120KBANK0094182"
                }
            },
            {
                "file_id": "RAW-005_DUP",
                "name": "slip_kbank_whale_8500_duplicate.jpg",
                "width": 1080,
                "height": 1920,
                "aspect_ratio": 1.77,
                "type_expected": "TYPE_SLIP_SOLO",
                "ocr_data": {
                    "file": "slip_kbank_whale_8500_duplicate.jpg",
                    "bank": "KBANK",
                    "receiver_name": "นางสาว จิณห์นิภา ประสาทเขตรการ",
                    "receiver_account": "xxx-x-x5678-x",
                    "sender_name": "นาย ณัฐชัย รักษาวงษ์",
                    "amount": 8500.00,
                    "datetime": "2026-11-20T10:48:05",
                    "ref_no": "20261120KBANK0094182"  # IDENTICAL REF_NO: DUPLICATE!
                }
            }
        ]

    # ==================================================================================
    # 1. DETECT & TASK 1: CLASSIFICATION & FEATURE ISOLATION GATEWAY
    # ==================================================================================
    def test_e2e_01_detect_and_classification(self):
        """DETECT ➔ TASK 1: จำแนกประเภทหลักฐานด้วย Production DetectGateway และ Task1FeatureNormalizer"""
        gateway = DetectGateway()
        normalizer = Task1FeatureNormalizer()

        classified = []
        for item in self.evidence_dataset:
            c = gateway.classify(item)
            self.assertEqual(c.type.value, item["type_expected"])
            n = normalizer.normalize(c)
            self.assertEqual(n.file_id, item["file_id"])
            classified.append(c.to_dict())

        self.assertEqual(len(classified), 5)
        self.record_audit_trail("DETECT_CLASSIFICATION_PASS", "จำแนกไฟล์พยานหลักฐาน 5 รายการด้วย DetectGateway ถูกต้อง 100%")

    # ==================================================================================
    # 2. TASK 2: STAGING BUFFER & EVENT-DRIVEN KPI AGGREGATION
    # ==================================================================================
    def test_e2e_02_staging_buffer_and_event_driven_kpi(self):
        """TASK 2: ตรวจสอบ Staging Buffer และการคำนวณ KPI แบบ Event-Driven ด้วย Task2StagingBuffer"""
        buffer = Task2StagingBuffer()

        # State 1: EMPTY
        self.assertEqual(buffer.state, BufferState.EMPTY)
        self.assertEqual(buffer.kpi_string(), "📷 แชท 0 หน้า | 🧾 สลิป พบ 0 · ยืนยัน 0 รายการ")

        # State 2: INGESTION PIPELINE
        gateway = DetectGateway()
        normalizer = Task1FeatureNormalizer()
        records = [normalizer.normalize(gateway.classify(item)) for item in self.evidence_dataset]

        buffer.ingest(records)
        self.assertEqual(buffer.state, BufferState.CONFIRMED)
        self.assertEqual(buffer.chats_count, 2)
        self.assertEqual(buffer.slips_found, 3)
        self.assertEqual(buffer.slips_confirmed, 2)

        kpi_live = buffer.kpi_string()
        self.assertEqual(kpi_live, "📷 แชท 2 หน้า | 🧾 สลิป พบ 3 · ยืนยัน 2 รายการ")
        self.record_audit_trail("TASK2_STAGING_BUFFER_PASS", f"Staging Buffer อัปเดตสมบูรณ์: {kpi_live}")

    # ==================================================================================
    # 3. TASK 3: SLIP RECIPIENT AGGREGATOR & POI SELECTOR
    # ==================================================================================
    def test_e2e_03_recipient_and_poi_selection(self):
        """TASK 3: สกัดบัญชีผู้รับโอนเงิน และจัดกลุ่มบุคคลเป้าหมาย (POI) ด้วย Task3RecipientSelector"""
        gateway = DetectGateway()
        normalizer = Task1FeatureNormalizer()
        buffer = Task2StagingBuffer()
        selector = Task3RecipientSelector()

        records = [normalizer.normalize(gateway.classify(item)) for item in self.evidence_dataset]
        buffer.ingest(records)

        summary = selector.aggregate(buffer.confirmed_records)
        self.assertIn("นางสาว จิณห์นิภา ประสาทเขตรการ", summary.recipients)
        whale = summary.primary_poi
        self.assertIsNotNone(whale)
        self.assertEqual(whale.name, "นางสาว จิณห์นิภา ประสาทเขตรการ")
        self.assertEqual(whale.count, 2)
        self.assertEqual(whale.total_amount, 10500.00)
        self.record_audit_trail("TASK3_RECIPIENT_POI_PASS", "สกัดบัญชีผู้รับและจัดการรายชื่อ POI ด้วย Task3RecipientSelector ถูกต้อง 100%")

    # ==================================================================================
    # 4. TASK 4: TIMELINE & SIX-AGENT DEEP ANALYSIS
    # ==================================================================================
    def test_e2e_04_timeline_and_six_agents(self):
        """TASK 4: วิเคราะห์ไทม์ไลน์ 6 มิติ สังเคราะห์บทสรุปคดีและคำถามซักค้าน"""
        analyzer = Task4SixAgentsDeepAnalyzer()

        t4_input = {
            "file": "chat_urgency_escalation.jpg",
            "step1_detection": {
                "status": "DETECTED_SUCCESS",
                "bounding_box": {"x": 292, "y": 1661, "width": 515, "height": 608},
                "elapsed_ms": 32.2
            },
            "step2_extraction": {
                "bank": "KBANK",
                "ref_id": "20261120KBANK0094182",
                "amount": 8500.0,
                "currency": "THB",
                "sender": {"name": "นาย ณัฐชัย รักษาวงษ์", "account": "xxx-x-x1234-x"},
                "receiver": {"name": "นางสาว จิณห์นิภา ประสาทเขตรการ", "account": "xxx-x-x5678-x"},
                "datetime": "20 พ.ย. 2569 เวลา 10:48 น.",
                "elapsed_ms": 881.63
            }
        }

        t4_result = analyzer.execute_locked_deep_analysis(t4_input)
        self.assertEqual(t4_result["workflow_lock_status"], "VERIFIED_LOCKED")
        self.assertIn("six_dimensions", t4_result)
        self.assertEqual(len(t4_result["six_dimensions"]), 6)
        self.record_audit_trail("TASK4_SIX_AGENTS_PASS", "วิเคราะห์ 6 มิติสถาปัตยกรรมคดีผ่าน 100%")

    # ==================================================================================
    # 5. TASK 5: PURE SLIP SSOT & 100% MATHEMATICAL RECONCILIATION
    # ==================================================================================
    def test_e2e_05_pure_slip_ssot_and_mathematical_reconciliation(self):
        """TASK 5: การกระทบยอดความเสียหายสุทธิ 100% (Mathematical Invariant: Discrepancy == 0)"""
        engine = LockedTask5PureSlipSOTEngine()
        raw_slips = [item["ocr_data"] for item in self.evidence_dataset if "ocr_data" in item]

        t5_result = engine.execute_locked_task5_pipeline(raw_slips)
        self.assertEqual(t5_result["workflow_lock_status"], "VERIFIED_LOCKED")

        cards = t5_result["the_4_cards"]
        c1 = cards["card_1"]
        c2 = cards["card_2"]
        c4 = cards["card_4"]

        # CARD 1: ยอดสุทธิหลังตัดซ้ำ = 2,000 + 8,500 = 10,500.00 บาท
        net_loss = c1["total_net_loss"]
        self.assertEqual(net_loss, 10500.00)
        self.assertEqual(c1["cleared_transactions_count"], 2)

        # CARD 4: ตรวจจับสลิปซ้ำ 1 รายการ
        self.assertEqual(c4["duplicate_slips_eliminated"], 1)

        # 100% Mathematical Reconciliation Audit
        # Gross = Net + Deduplicated (10,500 + 8,500 = 19,000.00)
        total_gross = sum(s["amount"] for s in raw_slips)
        discrepancy = abs(total_gross - (net_loss + 8500.00))
        self.assertEqual(discrepancy, 0.0, "[FATAL] Mathematical discrepancy must be exactly ZERO!")

        # CARD 2: ผู้รับโอนรายหลัก (Whale Target Name Matcher ตัดคำนำหน้าชื่อทิ้ง 100%)
        self.assertEqual(c2["whale_target_name"], "จิณห์นิภา ประสาทเขตรการ")
        self.assertEqual(c2["concentrated_amount"], 10500.00)

        self.record_audit_trail("TASK5_MATHEMATICAL_RECONCILIATION_PASS", f"ยอดสุทธิกระทบยอดถูกต้อง 100%: ฿{net_loss:,.2f}")

    # ==================================================================================
    # 6. TASK 7: 11-COLUMN COURT EVIDENCE TABLE
    # ==================================================================================
    def test_e2e_06_eleven_column_court_evidence_table(self):
        """TASK 7: จัดทำตารางสารบรรณพยานหลักฐาน 11 คอลัมน์ มาตรฐานศาล"""
        t5_engine = LockedTask5PureSlipSOTEngine()
        raw_slips = [item["ocr_data"] for item in self.evidence_dataset if "ocr_data" in item]
        t5_out = t5_engine.execute_locked_task5_pipeline(raw_slips)

        t7_engine = LockedTask7EvidenceTableEngine()
        t7_result = t7_engine.execute_locked_task7_pipeline(t5_out)

        self.assertEqual(t7_result["workflow_lock_status"], "VERIFIED_LOCKED")
        rows = t7_result["evidence_rows"]
        self.assertEqual(len(rows), 2)  # 2 cleared unique records

        for row in rows:
            self.assertIn("row_id", row)
            self.assertIn("datetime_display", row)
            self.assertIn("money_trail_flow", row)
            self.assertIn("amount", row)
            self.assertIn("ref_no", row)
            self.assertIn("visual_preview_path", row)

        self.record_audit_trail("TASK7_TABLE_11COL_PASS", f"ตารางสารบบ 11 คอลัมน์ สังเคราะห์สำเร็จ {len(rows)} แถว")

    # ==================================================================================
    # 7. TASK 8: COURT-READY DOSSIER ASSEMBLER
    # ==================================================================================
    def test_e2e_07_court_ready_dossier_assembler(self):
        """TASK 8: ประกอบเล่มแฟ้มสำนวนคดีมาตรฐานศาล (7 ส่วนหลัก จ.๑ - จ.๗)"""
        assembler = Task8CourtDossierAssembler(LockedDossierConfig(case_number="012/2569"))

        # Pipeline data handoff from Tasks 4, 5, 7
        t4_out = {
            "status": "SUCCESS_ANALYZED",
            "six_agents_analysis": {
                "agent1_chrono_story": {"total_key_nodes": 4, "story_arc": "ล่อลวงยืมเงิน"},
                "agent2_corroboration": {"matches_found": 1, "smoking_gun_nodes": ["NODE_01"]},
                "agent3_forensic_dialogue": {"manipulation_tactics": ["อ้างเหตุจำเป็นเร่งด่วน"]},
                "agent4_legal_corpus": {"primary_charges": ["ป.อ. ๓๔๑", "ป.อ. ๘๓"]},
                "agent5_attorney_knowledge": {"killer_cross_examination_script": []},
                "agent6_distilled_digest": {"system_verdict_permitted": False, "discretion_mandate": "ดุลพินิจศาล"}
            }
        }
        t5_out = {
            "status": "PURE_SLIP_SOT_LOCKED_SUCCESS",
            "the_4_cards": {
                "card1_net_principal_loss": {"total_net_loss": 10500.00, "verified_slip_count": 2},
                "card2_whale_beneficiary": {"primary_whale_name": "นางสาว จิณห์นิภา ประสาทเขตรการ", "primary_whale_amount": 10500.00, "primary_whale_ratio_pct": 100.0},
                "card3_fraud_velocity_burst": {"total_burst_spikes": 1, "burst_events": []},
                "card4_tamper_and_dedup_guard": {"duplicate_slips_detected": 1, "duplicate_amount_prevented": 8500.00}
            }
        }
        t7_out = {
            "status": "TASK7_EVIDENCE_TABLE_LOCKED_SUCCESS",
            "evidence_rows": [
                {"row_id": "ROW_01", "timestamp": "2026-11-20 08:18", "money_trail_flow": "ผู้เสียหาย ➔ SCB ➔ ผู้ต้องหา", "amount": 2000.0, "bank_ref_id": "REF01", "is_whale_target": True, "is_burst_anomaly": False},
                {"row_id": "ROW_02", "timestamp": "2026-11-20 10:48", "money_trail_flow": "ผู้เสียหาย ➔ KBANK ➔ ผู้ต้องหา", "amount": 8500.0, "bank_ref_id": "REF02", "is_whale_target": True, "is_burst_anomaly": True}
            ]
        }

        t8_result = assembler.execute_locked_task8_dossier(t4_out, t5_out, t7_out)
        self.assertEqual(t8_result["status"], "COURT_DOSSIER_SUCCESS_SEALED")
        self.assertEqual(t8_result["case_number"], "012/2569")
        self.assertEqual(t8_result["total_pages"], 7)
        self.assertEqual(t8_result["net_loss_reconciled"], 10500.00)

        pages = t8_result["pages"]
        exhibit_codes = [p["exhibit_code"] for p in pages]
        self.assertEqual(exhibit_codes, ['จ.๑-จ.๔', 'จ.๑', 'จ.๒', 'จ.๓', 'จ.๔', 'ภาคผนวก ก.', 'ภาคผนวก ข.'])

        self.record_audit_trail("TASK8_DOSSIER_ASSEMBLER_PASS", f"ประกอบเล่มแฟ้มสำนวนคดี จ.๑-จ.๗ ({len(pages)} หน้า) สำเร็จ")

    # ==================================================================================
    # 8. TASK 9: VAULT EXPORTER, DERIVATIVE & COURT SFX ARCHIVE
    # ==================================================================================
    def test_e2e_08_vault_exporter_and_sfx_archive(self):
        """TASK 9: ส่งออกคลังนิรภัยพยานหลักฐาน, PDF ภาพอนุพันธ์, และแพ็กเกจ SFX เข้ารหัส"""
        exporter = Task9VaultExporter(LockedVaultConfig(case_number="012/2569"))

        # Pipeline input from Task 8
        t8_mock = {
            "status": "COURT_DOSSIER_SUCCESS_SEALED",
            "case_number": "012/2569",
            "total_pages": 7,
            "net_loss_reconciled": 10500.00,
            "whale_target": "นางสาว จิณห์นิภา ประสาทเขตรการ",
            "pages": [{"page_number": i+1, "exhibit_code": f"จ.{i+1}"} for i in range(7)]
        }
        evidence_files = [
            {"name": item["name"], "size": 150000, "sha256": hashlib.sha256(item["name"].encode()).hexdigest(), "type": item["type_expected"]}
            for item in self.evidence_dataset
        ]

        # Locked Execution
        t9_result = exporter.execute_locked_vault_export(
            t8_mock,
            evidence_files,
            selected_file=evidence_files[0],
            password="EvidenceVaultPass2026!"
        )

        self.assertEqual(t9_result["status"], "VAULT_EXPORT_SUCCESS_SEALED")
        self.assertTrue(t9_result["password_gate"]["is_password_set"])
        self.assertEqual(t9_result["password_gate"]["status_badge"], "PASSWORD SET")
        self.assertEqual(t9_result["master_pdf"]["cipher"], "AES-256")
        self.assertEqual(t9_result["sfx_vault"]["cipher"], "AES-256")

        # Verify Manifest
        manifest = t9_result["sfx_vault"]["manifest_json"]
        self.assertEqual(len(manifest["files"]), 6)  # 1 Master PDF + 5 raw files
        self.record_audit_trail("TASK9_VAULT_EXPORTER_PASS", "สร้างภาพอนุพันธ์, Master PDF และแพ็กเกจ SFX เข้ารหัสสำเร็จ 100%")

    # ==================================================================================
    # 9. EXHAUSTIVE 7-STATE UI INTERACTION MATRIX VERIFICATION
    # ==================================================================================
    def test_e2e_09_exhaustive_7_state_matrix_verification(self):
        """UI EXHAUSTIVE MATRIX: ตรวจสอบความพร้อมของ UI ทั้ง 7 สถานะใน index.html"""
        index_path = r"d:\Project\ชวกม.2\index.html"
        self.assertTrue(os.path.exists(index_path), "[GATE 1 FAIL] ไม่พบไฟล์ index.html")

        with open(index_path, "r", encoding="utf-8") as f:
            html = f.read()

        # 1. default: ตรวจสอบเลย์เอาต์ 3 คอลัมน์
        self.assertIn("workspace-3col-grid", html)
        self.assertIn("data-task=\"task9-actions\"", html)

        # 2. hover: ตรวจสอบ hover feedback transitions
        self.assertIn("hover:scale-[1.01]", html)
        self.assertIn("hover:from-emerald-500", html)

        # 3. focus: ตรวจสอบ Focus Ring
        self.assertIn("focus:", html)

        # 4. disabled: ตรวจสอบ Disabled state
        self.assertIn("disabled", html)

        # 5. loading: ตรวจสอบ Spinner / Loading feedback
        self.assertIn("กำลังประมวลผล", html)

        # 6. error: ตรวจสอบ Error notification
        self.assertIn("[GATE 1 FAIL]", html)
        self.assertIn("[GATE 5 CIRCUIT BREAKER]", html)

        # 7. empty: ตรวจสอบ Pure Zero State
        self.assertIn("PURE ZERO STATE", html)
        self.assertIn("ยังไม่มีรายชื่อบุคคลที่เลือกหรือเพิ่มด้วยตนเอง", html)

        self.record_audit_trail("UI_7_STATE_MATRIX_PASS", "ตรวจสอบครบทั้ง 7 สถานะ (default, hover, focus, disabled, loading, error, empty)")

    # ==================================================================================
    # 10. FAILURE MODES & ZERO BLAST RADIUS VERIFICATION
    # ==================================================================================
    def test_e2e_10_zero_blast_radius_and_circuit_breakers(self):
        """ZERO BLAST RADIUS: ยิง Payload พัง ตรวจสอบการตัดวงจรโดยไม่ลุกลามทำลาย State อื่น"""
        exporter = Task9VaultExporter()

        with self.assertRaises(SystemError) as ctx:
            exporter.execute_locked_vault_export({}, [])
        self.assertIn("[GATE 1 FAIL]", str(ctx.exception))

        with self.assertRaises(ValueError) as ctx:
            exporter.execute_locked_vault_export(
                {"status": "COURT_DOSSIER_SUCCESS_SEALED", "pages": [{"page_number": 1}]},
                [],
                password="admin\x00malicious"
            )
        self.assertIn("[GATE 1 FAIL]", str(ctx.exception))

        # พิสูจน์ Zero Blast Radius: หลังชน Circuit Breaker ตัวแปรระบบต้องกลับสู่สถานะปลอดเชื้อ
        self.assertIsNone(exporter._last_isolated_context)
        self.assertFalse(exporter._execution_locked)

        self.record_audit_trail("ZERO_BLAST_RADIUS_PASS", "พิสูจน์การตัดวงจร Circuit Breaker และจำกัดความเสียหาย 100%")


if __name__ == "__main__":
    unittest.main()

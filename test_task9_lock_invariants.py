#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
========================================================================================
UNIT TEST & INVARIANT VERIFICATION SUITE FOR TASK 9
ทดสอบการทำงานของ Task9VaultExporter และการล็อกระบบด้วย 5 Invariant Gates (สกิล Lock 100%)
========================================================================================
"""

import unittest
import os
import json
from dataclasses import FrozenInstanceError
from task9_vault_exporter import Task9VaultExporter, LockedVaultConfig

class TestTask9LockInvariants(unittest.TestCase):

    def setUp(self):
        self.exporter = Task9VaultExporter()

        # Mock valid output from Task 8
        self.valid_task8_dossier = {
            "status": "COURT_DOSSIER_SUCCESS_SEALED",
            "case_number": "012/2569",
            "total_pages": 7,
            "net_loss_reconciled": 10500.00,
            "whale_target": "นางสาว จิณห์นิภา ประสาทเขตรการ",
            "pages": [
                {"page_number": 1, "title": "หน้าปกแฟ้มพยานหลักฐาน", "type": "COVER", "exhibit_code": "จ.๑"},
                {"page_number": 2, "title": "ผังโครงสร้างขบวนการ", "type": "NETWORK", "exhibit_code": "จ.๒"},
                {"page_number": 3, "title": "ใบสรุปข้อมูลและเส้นทางการเงิน", "type": "SUMMARY", "exhibit_code": "จ.๓"},
                {"page_number": 4, "title": "ตารางคำนวณดอกเบี้ยผิดนัด", "type": "INTEREST", "exhibit_code": "จ.๔"},
                {"page_number": 5, "title": "สารบบหลักฐานไทม์ไลน์ ๑๑ มิติ", "type": "TIMELINE_11D", "exhibit_code": "จ.๕"},
                {"page_number": 6, "title": "บัญชีคุมลายนิ้วมือดิจิทัล SHA-256", "type": "HASH_MANIFEST", "exhibit_code": "จ.๖"},
                {"page_number": 7, "title": "ร่างคำขอออกหมายเรียกพยานเอกสาร", "type": "SUBPOENA", "exhibit_code": "จ.๗"}
            ]
        }

        # Mock uploaded evidence files
        self.valid_evidence_files = [
            {"name": "chat_01.jpg", "size": 154200, "sha256": "a" * 64, "type": "TYPE_CHAT"},
            {"name": "slip_01.jpg", "size": 98500, "sha256": "b" * 64, "type": "TYPE_SLIP_SOLO"}
        ]

    # ==================================================================================
    # GATE 1 TESTS: PRE-FLIGHT SYSTEM INVARIANT ASSERTION
    # ==================================================================================
    def test_gate1_valid_execution(self):
        """GATE 1 PASS: อินพุตสมบูรณ์ รันผ่าน 100%"""
        result = self.exporter.execute_locked_vault_export(
            self.valid_task8_dossier,
            self.valid_evidence_files,
            selected_file=self.valid_evidence_files[0],
            password="SecurePass2026!"
        )
        self.assertEqual(result["status"], "VAULT_EXPORT_SUCCESS_SEALED")
        self.assertTrue(result["password_gate"]["is_password_set"])
        self.assertEqual(result["password_gate"]["status_badge"], "PASSWORD SET")

    def test_gate1_missing_task8_status_fail(self):
        """GATE 1 FAIL: Task 8 ไม่ผ่านการรับรอง ต้องตัดการทำงานทันที (Fail-Fast)"""
        bad_task8 = {"status": "FAILED_DRAFT", "pages": []}
        with self.assertRaises(SystemError) as ctx:
            self.exporter.execute_locked_vault_export(bad_task8, self.valid_evidence_files)
        self.assertIn("[GATE 1 FAIL]", str(ctx.exception))

    def test_gate1_invalid_password_null_byte_fail(self):
        """GATE 1 FAIL: รหัสผ่านมี Null Byte ต้องดักจับได้ทันที"""
        with self.assertRaises(ValueError) as ctx:
            self.exporter.execute_locked_vault_export(
                self.valid_task8_dossier,
                self.valid_evidence_files,
                password="test\x00password"
            )
        self.assertIn("[GATE 1 FAIL]", str(ctx.exception))

    def test_gate1_oversized_password_fail(self):
        """GATE 1 FAIL: รหัสผ่านยาวเกิน 128 ตัวอักษร ต้องปฏิเสธ"""
        with self.assertRaises(ValueError) as ctx:
            self.exporter.execute_locked_vault_export(
                self.valid_task8_dossier,
                self.valid_evidence_files,
                password="X" * 129
            )
        self.assertIn("[GATE 1 FAIL]", str(ctx.exception))

    # ==================================================================================
    # GATE 2 TESTS: STATELESS CONTEXT ISOLATION
    # ==================================================================================
    def test_gate2_stateless_context_isolation(self):
        """GATE 2: ตรวจสอบการล้าง Memory Leak และบริบทการทำงานแยกขาดจากกัน 100%"""
        self.exporter.execute_locked_vault_export(self.valid_task8_dossier, self.valid_evidence_files)
        self.assertIsNotNone(self.exporter._last_isolated_context)
        self.assertTrue(self.exporter._execution_locked)

        self.exporter.reset_isolated_context()
        self.assertIsNone(self.exporter._last_isolated_context)
        self.assertFalse(self.exporter._execution_locked)

    # ==================================================================================
    # GATE 3 TESTS: IMMUTABLE PARAMETER LOCK
    # ==================================================================================
    def test_gate3_immutable_parameter_lock(self):
        """GATE 3: แช่แข็งคอนฟิก ห้ามแก้ไขตัวแปรระหว่างรัน (FrozenInstanceError)"""
        with self.assertRaises(FrozenInstanceError):
            self.exporter.config.case_number = "999/9999"

        with self.assertRaises(FrozenInstanceError):
            self.exporter.config.encryption_cipher = "WEAK_DES"

    # ==================================================================================
    # GATE 4 TESTS: SEQUENTIAL PIPELINE ENFORCEMENT
    # ==================================================================================
    def test_gate4_sequential_pipeline_artifacts(self):
        """GATE 4: บังคับเดินตามท่อครบทั้ง 3 ชิ้นส่วน (Derivative, Master PDF, SFX Vault)"""
        result = self.exporter.execute_locked_vault_export(
            self.valid_task8_dossier,
            self.valid_evidence_files,
            selected_file=self.valid_evidence_files[1],
            password=None
        )

        # 1. ตรวจชิ้นส่วนภาพอนุพันธ์ (Derivative)
        self.assertIn("derivative_pdf", result)
        self.assertEqual(result["derivative_pdf"]["source_file"], "slip_01.jpg")
        self.assertEqual(result["derivative_pdf"]["source_raw_hash"], "b" * 64)
        self.assertNotEqual(result["derivative_pdf"]["derivative_sha256"], "b" * 64)

        # 2. ตรวจชิ้นส่วน Master PDF
        self.assertIn("master_pdf", result)
        self.assertEqual(result["master_pdf"]["artifact_name"], "Digital_Evidence_Report.pdf")
        self.assertFalse(result["master_pdf"]["is_password_protected"])

        # 3. ตรวจชิ้นส่วน SFX Vault
        self.assertIn("sfx_vault", result)
        self.assertEqual(result["sfx_vault"]["artifact_name"], "Digital_Evidence_Case_012-2569.exe")
        self.assertEqual(len(result["sfx_vault"]["manifest_json"]["files"]), 3)  # PDF + 2 raw evidence

    def test_gate4_password_propagation_invariant(self):
        """GATE 4: เมื่อตั้งรหัสผ่าน ต้องซิงก์ค่าเดียวกันไปยังทั้ง Master PDF และ SFX Vault"""
        result = self.exporter.execute_locked_vault_export(
            self.valid_task8_dossier,
            self.valid_evidence_files,
            password="MySecretPassword123"
        )
        self.assertTrue(result["password_gate"]["is_password_set"])
        self.assertTrue(result["master_pdf"]["is_password_protected"])
        self.assertTrue(result["sfx_vault"]["is_password_protected"])
        self.assertEqual(result["master_pdf"]["cipher"], "AES-256")
        self.assertEqual(result["sfx_vault"]["cipher"], "AES-256")

    # ==================================================================================
    # GATE 5 TESTS: POST-FLIGHT HEALTH CIRCUIT BREAKER
    # ==================================================================================
    def test_gate5_circuit_breaker_on_corrupt_hash(self):
        """GATE 5 CIRCUIT BREAKER: แฮชไม่ตรงตามข้อกำหนด 64 ตัวอักษร ต้องตัดวงจรทันที"""
        with self.assertRaises(RuntimeError) as ctx:
            # จำลองผลลัพธ์ที่แฮชบิดเบือน
            corrupt_result = {
                "derivative_pdf": {"derivative_sha256": "SHORT_HASH", "byte_size": 200},
                "master_pdf": {"master_pdf_sha256": "a" * 64, "byte_size": 200},
                "sfx_vault": {"sfx_package_sha256": "c" * 64, "byte_size": 500}
            }
            self.exporter._assert_postflight_health(corrupt_result)
        self.assertIn("[GATE 5 CIRCUIT BREAKER]", str(ctx.exception))

    def test_gate5_circuit_breaker_on_zero_bytes(self):
        """GATE 5 CIRCUIT BREAKER: ไบต์ของเอกสารว่างเปล่า ต้องตัดวงจรทันที"""
        with self.assertRaises(RuntimeError) as ctx:
            corrupt_result = {
                "derivative_pdf": {"derivative_sha256": "a" * 64, "byte_size": 200},
                "master_pdf": {"master_pdf_sha256": "b" * 64, "byte_size": 10},  # < 128 bytes
                "sfx_vault": {"sfx_package_sha256": "c" * 64, "byte_size": 500}
            }
            self.exporter._assert_postflight_health(corrupt_result)
        self.assertIn("[GATE 5 CIRCUIT BREAKER]", str(ctx.exception))


if __name__ == "__main__":
    unittest.main()

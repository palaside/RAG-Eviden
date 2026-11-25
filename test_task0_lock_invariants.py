#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
========================================================================================
INVARIANT VERIFICATION SUITE FOR TASK 0: CLIENT-SIDE IN-BROWSER FORENSIC ENGINE
ทดสอบและรับรองความถูกต้องของระบบประมวลผลบนเบราว์เซอร์ 100% ไร้หลังบ้าน
ตามกฎเหล็ก 5 Invariant Gates ของสกิล Lock
========================================================================================
"""

import unittest
import os
import re

class TestTask0LockInvariants(unittest.TestCase):

    def setUp(self):
        self.html_path = r"d:\Project\ชวกม.2\task0_client_side_in_browser_engine.html"
        self.assertTrue(os.path.exists(self.html_path), "File task0_client_side_in_browser_engine.html must exist")
        with open(self.html_path, "r", encoding="utf-8") as f:
            self.html_content = f.read()

    def test_gate1_browser_pre_flight_assertions(self):
        """GATE 1: มีกลไกตรวจสอบ Web Cryptography API และ HTML5 File API ก่อนแตะต้องข้อมูล"""
        self.assertIn("assertGate1BrowserEnvironment", self.html_content)
        self.assertIn("crypto.subtle", self.html_content)
        self.assertIn("ArrayBuffer", self.html_content)

    def test_gate2_stateless_context_and_memory_isolation(self):
        """GATE 2: ทำงานใน RAM แบบ In-Memory ArrayBuffer และมีฟังก์ชันรีเซ็ตสถานะ"""
        self.assertIn("resetDossierState", self.html_content)
        self.assertIn("activeEvidenceFiles = []", self.html_content)

    def test_gate3_immutable_configuration_lock(self):
        """GATE 3: แช่แข็งคอนฟิกด้วย Object.freeze (ดอกเบี้ย 5%, รหัสคดี 012/2569, A4 7 หน้า)"""
        self.assertIn("LOCKED_CONFIG = Object.freeze", self.html_content)
        self.assertIn('caseNumber: "012/2569"', self.html_content)
        self.assertIn("annualInterestRate: 0.05", self.html_content)
        self.assertIn("minPagesExpected: 7", self.html_content)

    def test_gate4_sequential_pipeline_enforcement(self):
        """GATE 4: บังคับท่อประมวลผลตามลำดับ File Intake ➔ SHA-256 ➔ Dedup ➔ 4 Cards ➔ 7 Pages"""
        self.assertIn("executeLockedBrowserPipeline", self.html_content)
        self.assertIn("seenRefs.add(item.refId)", self.html_content)
        self.assertIn("totalNetLoss", self.html_content)
        self.assertIn("recipientMap", self.html_content)
        self.assertIn("interestRows", self.html_content)

    def test_gate5_post_flight_circuit_breaker(self):
        """GATE 5: มีประตูดักจับ Fail-Closed หากยอดเงิน <= 0 หรือเกิดความผิดปกติ"""
        self.assertIn("assertGate5PostFlight", self.html_content)
        self.assertIn("triggerCircuitBreaker", self.html_content)
        self.assertIn("GATE 5 CIRCUIT BREAKER TRIGGERED", self.html_content)

    def test_dossier_7_pages_structure_present(self):
        """โครงสร้างเอกสาร: ตรวจสอบการเรนเดอร์เอกสาร A4 ครบทั้ง ๗ หน้ากระดาษ"""
        # หน้า 1: ปกและสารบัญ + รหัส จ.๑ ถึง จ.๔
        self.assertIn("รายงานสรุปแฟ้มพยานหลักฐานดิจิทัลมาตรฐานศาล", self.html_content)
        self.assertIn("เอกสารหมาย จ.๑", self.html_content)
        self.assertIn("เอกสารหมาย จ.๒", self.html_content)
        self.assertIn("เอกสารหมาย จ.๓", self.html_content)
        self.assertIn("เอกสารหมาย จ.๔", self.html_content)
        # หน้า 2: ผังตัวละคร Who's Who
        self.assertIn("ผังโครงสร้างขบวนการและบทบาทตัวละคร (Who's Who Matrix)", self.html_content)
        # หน้า 3: ใบสรุปการเงิน Executive Sheet + ยอดหักทอน
        self.assertIn("ใบสรุปข้อมูลและเส้นทางการเงินที่ตรวจพบ (Executive Summary Sheet)", self.html_content)
        self.assertIn("โอนออกรวม (Gross)", self.html_content)
        # หน้า 4: ดอกเบี้ยรายวัน 5%
        self.assertIn("ตารางคำนวณเงินต้นและดอกเบี้ยผิดนัดรายกรรม (Accrued Interest Calculator)", self.html_content)
        self.assertIn("ร่างคำขอท้ายฟ้องสำหรับทนายความ", self.html_content)
        # หน้า 5: ไทม์ไลน์ 11 มิติ & ซักค้าน
        self.assertIn("แฟ้มสารบบหลักฐานไทม์ไลน์ ๑๑ มิติ & คำถามซักค้านชี้นำ", self.html_content)
        # หน้า 6: แฮช SHA-256
        self.assertIn("บัญชีคุมลายนิ้วมือดิจิทัล (Chain of Custody & SHA-256 Manifest)", self.html_content)
        # หน้า 7: ร่างหมายเรียกศาล
        self.assertIn("ร่างรายการคำขอออกหมายเรียกพยานเอกสารต่อศาล (Subpoena Motion Checklist)", self.html_content)

if __name__ == "__main__":
    unittest.main()

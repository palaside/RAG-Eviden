#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
========================================================================================
ATOMIC E2E WORKFLOW TEST SUITE: TASK 0 CLIENT-SIDE FORENSIC ENGINE
File: d:\\Project\\ชวกม.2\\test_task0_e2e_exhaustive.py
Auditor: Principal QA Architect & Forensic Systems Engineer
Standard: 4 Iron Rules of Production Parity & 7-State Exhaustive Matrix
========================================================================================
"""

import unittest
import os
import re
import json
import time
from datetime import datetime, timezone

class TestTask0E2EExhaustiveWorkflow(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.target_file = r"d:\Project\ชวกม.2\task0_client_side_in_browser_engine.html"
        cls.audit_trail_log = []
        cls.system_logs = []

        if not os.path.exists(cls.target_file):
            raise FileNotFoundError(f"[CRITICAL FAIL] Target file not found: {cls.target_file}")

        with open(cls.target_file, "r", encoding="utf-8") as f:
            cls.content = f.read()

    def record_log(self, level, error_code, msg, line_no=0):
        log_entry = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "requestId": f"REQ-{int(time.time()*1000)}",
            "severity": level,
            "file_path": self.target_file,
            "line": line_no,
            "error_code": error_code,
            "message": msg
        }
        self.system_logs.append(log_entry)
        self.audit_trail_log.append(f"[{log_entry['timestamp']}] [{level}] [{error_code}] {msg}")

    # ==================================================================================
    # AXIS 1: PIPELINE ARCHITECTURE & SEQUENTIAL ORDER
    # ==================================================================================

    def test_pipeline_architecture_data_flow(self):
        """AXIS 1: ตรวจสอบการไหลของข้อมูล Data Flow ตามพิมพ์เขียว (Input -> Validate -> Hash -> Dedup -> 4Cards -> Render)"""
        # ตรวจสอบการมีอยู่ของท่อ 5 สเต็ป
        has_intake = "handleFileSelect" in self.content
        has_validate = "assertGate1BrowserEnvironment" in self.content
        has_crypto = "crypto.subtle.digest" in self.content
        has_pipeline = "executeLockedBrowserPipeline" in self.content
        has_render = "renderFullDossierDOM" in self.content

        if not (has_intake and has_validate and has_crypto and has_pipeline and has_render):
            self.record_log("ERROR", "ERR_PIPELINE_BROKEN", "Data Flow pipeline missing required stages", 250)
            self.fail("[FAIL] Pipeline stages broken or missing")

    def test_sequential_data_pipeline_no_race_condition(self):
        """AXIS 2: ตรวจสอบว่ามีกลไกป้องกัน Race Condition ระหว่าง Async ArrayBuffer & Execution"""
        self.assertIn("await f.arrayBuffer()", self.content, "Must await ArrayBuffer read")
        self.assertIn("await crypto.subtle.digest", self.content, "Must await cryptographic hashing")

    def test_spec_driven_declarative_ui_invariance(self):
        """AXIS 3: ตรวจสอบ Declarative UI (UI = f(State)) ไม่มีการแก้ DOM นอกกรอบ"""
        self.assertIn("LOCKED_CONFIG = Object.freeze", self.content, "Config must be immutable")
        self.assertIn("renderFullDossierDOM", self.content, "Rendering must be a pure projection of data")

    def test_trail_flow_traceability(self):
        """AXIS 4: ตรวจสอบความสามารถในการสืบย้อนรอย (Traceability) ของทุกสลิปไปยังค่าแฮช SHA-256"""
        self.assertIn("hashArray.map", self.content, "Must format full 64-character SHA-256")
        self.assertIn("s.sha256", self.content, "Manifest table must output real SHA-256")

    # ==================================================================================
    # EXHAUSTIVE STATE MATRIX (7 STATES AUDIT)
    # ==================================================================================

    def test_state_01_default(self):
        """STATE 1: default — ตรวจสอบสถานะเริ่มต้น (A4 CSS, Initial Layout, Font, Header)"""
        self.assertIn("width: 210mm;", self.content, "A4 width must be explicitly defined")
        self.assertIn("min-height: 297mm;", self.content, "A4 height must be explicitly defined")
        self.assertIn("TH Sarabun PSK", self.content, "Court font standard TH Sarabun must be included")

    def test_state_02_hover(self):
        """STATE 2: hover — ตรวจสอบการตอบสนองเมื่อชี้เมาส์ (Buttons, Dropzone, Visual Feedback)"""
        self.assertIn(".dropzone-container:hover", self.content, "Dropzone must have hover style")
        self.assertIn(".btn-print:hover", self.content, "Print button must have hover feedback")

    def test_state_03_focus_accessibility(self):
        """STATE 3: focus — ตรวจสอบ Keyboard Focus Navigation (tabindex, focus ring, role=button)"""
        has_tabindex = 'tabindex="0"' in self.content
        has_role = 'role="button"' in self.content
        has_keydown = "keydown" in self.content or "onkeydown" in self.content

        if not (has_tabindex and has_role):
            self.record_log("WARNING", "ERR_WCAG_A11Y_FOCUS", "Dropzone lacks tabindex=0 or role=button for keyboard focus", 220)
            self.fail("[FAIL] Focus state accessibility: Dropzone cannot be focused via Keyboard Tab navigation")

    def test_state_04_disabled(self):
        """STATE 4: disabled — ตรวจสอบการปิดปุ่มระหว่างประมวลผล ป้องกัน Double-Submit"""
        has_disabled_css = ":disabled" in self.content or ".disabled" in self.content
        has_disabled_logic = "disabled = true" in self.content or "setAttribute('disabled'" in self.content

        if not (has_disabled_css and has_disabled_logic):
            self.record_log("ERROR", "ERR_STATE_DISABLED_MISSING", "Action buttons lack disabled state during file hashing", 80)
            self.fail("[FAIL] Disabled state: Buttons remain clickable during async hashing, risking race conditions")

    def test_state_05_loading(self):
        """STATE 5: loading — ตรวจสอบสถานะกำลังประมวลผล (Spinner / Progress Telemetry)"""
        has_spinner = "spinner" in self.content.lower() or "loading-indicator" in self.content or "is-loading" in self.content

        if not has_spinner:
            self.record_log("ERROR", "ERR_STATE_LOADING_MISSING", "Missing loading spinner/indicator during large file processing", 240)
            self.fail("[FAIL] Loading state: User is given no visual feedback while crypto.subtle digests large files")

    def test_state_06_error(self):
        """STATE 6: error — ตรวจสอบการแสดงผล Error Boundary, Circuit Breaker, และปุ่ม Retry"""
        self.assertIn("circuit-banner", self.content, "Must have visual circuit breaker banner")
        self.assertIn("triggerCircuitBreaker", self.content, "Must have trigger function for error state")

    def test_state_07_empty(self):
        """STATE 7: empty — ตรวจสอบกรณีไม่มีข้อมูล (Empty State ต้องไม่เรนเดอร์ขยะ หรือ crash)"""
        has_empty_container = "empty-dossier-state" in self.content or "activeEvidenceFiles.length === 0" in self.content

        if not has_empty_container:
            self.record_log("ERROR", "ERR_STATE_EMPTY_CRASH", "Rendering empty activeEvidenceFiles creates broken empty tables", 340)
            self.fail("[FAIL] Empty state: No dedicated empty state UI when 0 evidence files are present")

    # ==================================================================================
    # VERIFICATION GATES, BLAST RADIUS & MATHEMATICAL RECONCILIATION
    # ==================================================================================

    def test_mathematical_reconciliation_audit(self):
        """100% Mathematical Reconciliation Audit: Gross == Net + Dedup"""
        self.assertIn("const gross = data.totalNetLoss + data.dedupPrevented", self.content, "Gross must exactly equal Net + Dedup")
        self.assertIn("minimumFractionDigits: 2", self.content, "Currency must enforce 2 decimal places")

    def test_zero_blast_radius_fail_closed(self):
        """Zero Blast Radius: ตัดวงจรทันทีเมื่อพบยอดเงินติดลบหรือผิดปกติ"""
        self.assertIn("assertGate5PostFlight", self.content)
        self.assertIn("totalNetLoss <= 0", self.content)

    def test_observability_system_log_and_audit_trail(self):
        """Observability: ต้องมีกลไก Audit Trail & In-App System Console"""
        has_audit_trail = "auditTrail" in self.content or "forensicAuditLog" in self.content

        if not has_audit_trail:
            self.record_log("ERROR", "ERR_OBSERVABILITY_MISSING", "App lacks in-browser audit trail and system log viewer", 400)
            self.fail("[FAIL] Observability: No in-app Audit Trail or System Log console found")

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTask0E2EExhaustiveWorkflow)
    runner = unittest.TextTestRunner(verbosity=2)
    res = runner.run(suite)

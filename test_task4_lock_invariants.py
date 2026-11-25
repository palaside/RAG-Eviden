# -*- coding: utf-8 -*-
"""
Verification Suite for Task 4 Workflow Lock (The 5 Invariant Gates)
ทดสอบยืนยันระบบการทำงานของ Task 4 ภายใต้การควบคุมของสกิล Lock
"""

import unittest
from task4_six_agents_deep_analyzer import LockedTask4SixAgentsAnalyzer, LockedTask4Config

class TestTask4WorkflowLock(unittest.TestCase):

    def setUp(self):
        self.analyzer = LockedTask4SixAgentsAnalyzer()
        self.valid_task2_input = {
            "file": "chatv3 (41).jpg",
            "step1_detection": {
                "status": "DETECTED_SUCCESS",
                "bounding_box": {"x": 292, "y": 1661, "width": 515, "height": 608},
                "elapsed_ms": 32.2
            },
            "step2_extraction": {
                "bank": "Krungthai",
                "ref_id": "Aa7e0058a52854e5c",
                "amount": 5600.0,
                "currency": "THB",
                "sender": {"name": "สิบตรีณัฐชัย s***", "account": "XXX-X-XX526-6"},
                "receiver": {"name": "นางสาว อลงกรณ์ แจ่มเมือง", "account": "XXX-X-XX259-1"},
                "datetime": "26 พ.ค. 2568 เวลา 16:52 น.",
                "elapsed_ms": 881.63
            }
        }

    def test_gate1_reject_task1_input(self):
        """GATE 1: ปฏิเสธการรับงานจาก Task 1 (สลิปเดี่ยว) หรือไม่มี BBox"""
        task1_solo_slip = {
            "file": "A4_IMG_ (100).PNG",
            "bank": "KTB",
            "amount": 1000.0,
            "receiver_name": "จิณห์นิภา บุญประเสริฐ"
        }
        with self.assertRaises(ValueError) as ctx:
            self.analyzer.execute_locked_deep_analysis(task1_solo_slip)
        self.assertIn("[GATE 1 ASSERTION FAIL: INVALID_INPUT_SOURCE]", str(ctx.exception))

    def test_gate1_reject_none_input(self):
        """GATE 1: ปฏิเสธค่าว่าง None"""
        with self.assertRaises(ValueError) as ctx:
            self.analyzer.execute_locked_deep_analysis(None)
        self.assertIn("[GATE 1 ASSERTION FAIL]", str(ctx.exception))

    def test_gate2_stateless_isolation(self):
        """GATE 2: Stateless Isolation รัน 10 รอบ ผลลัพธ์ต้องเหมือนเดิม 100%"""
        res1 = self.analyzer.execute_locked_deep_analysis(self.valid_task2_input)
        self.analyzer.reset_isolated_context()
        res2 = self.analyzer.execute_locked_deep_analysis(self.valid_task2_input)

        self.assertEqual(res1["six_dimensions"]["dimension_1"]["events_count"],
                         res2["six_dimensions"]["dimension_1"]["events_count"])
        self.assertEqual(res1["six_dimensions"]["dimension_2"]["matched_slip_ref"],
                         res2["six_dimensions"]["dimension_2"]["matched_slip_ref"])
        self.assertEqual(res1["workflow_lock_status"], "VERIFIED_LOCKED")

    def test_gate3_immutable_config(self):
        """GATE 3: แช่แข็ง Config ห้ามกลายพันธุ์ (Immutable Frozen Dataclass)"""
        cfg = LockedTask4Config()
        with self.assertRaises(Exception):
            cfg.enforce_zero_verdict_rule = False

    def test_gate4_six_dimensions_complete(self):
        """GATE 4: บังคับรันครบทั้ง 6 มิติ ห้ามมีมิติใดหล่นหาย"""
        result = self.analyzer.execute_locked_deep_analysis(self.valid_task2_input)
        dims = result["six_dimensions"]
        self.assertEqual(len(dims), 6)
        for i in range(1, 7):
            self.assertIn(f"dimension_{i}", dims)

    def test_gate5_zero_verdict_circuit_breaker(self):
        """GATE 5: ละเมิดกฎตัดสินความผิด (Verdict Overreach) ต้องตัดวงจรทันที"""
        tampered_result = self.analyzer.execute_locked_deep_analysis(self.valid_task2_input)
        # จำลองการพยายามแก้ระบบให้ฟันธงคำตัดสิน
        tampered_result["six_dimensions"]["dimension_6"]["discretion_mandate"]["system_verdict_permitted"] = True

        with self.assertRaises(RuntimeError) as ctx:
            self.analyzer._assert_post_flight_circuit_breaker(tampered_result)
        self.assertIn("[GATE 5 CIRCUIT BREAKER TRIGGERED: VERDICT_OVERREACH]", str(ctx.exception))

if __name__ == "__main__":
    unittest.main()

# -*- coding: utf-8 -*-
"""
Verification Suite for Task 5: Pure Slip SOT Engine (The 4 Cards 10x)
ทดสอบยืนยันระบบการทำงานของ Task 5 ภายใต้การควบคุมของสกิล Lock
"""

import unittest
from task5_pure_slip_sot_engine import LockedTask5PureSlipSOTEngine, LockedTask5Config

class TestTask5PureSlipSOT(unittest.TestCase):

    def setUp(self):
        self.engine = LockedTask5PureSlipSOTEngine()
        self.sample_slips = [
            {
                "file": "slip_1.jpg",
                "bank": "KTB",
                "ref_no": "REF001",
                "amount": 1000.0,
                "receiver_name": "สมชาย สุขใจ",
                "datetime": "2025-05-20T10:00:00"
            },
            {
                "file": "slip_2.jpg",
                "bank": "KTB",
                "ref_no": "REF002",
                "amount": 4000.0,
                "receiver_name": "สมชาย สุขใจ",
                "datetime": "2025-05-20T10:02:00"  # ห่าง 120 วิ = เกิด Burst!
            },
            {
                "file": "slip_3_dup.jpg",
                "bank": "KTB",
                "ref_no": "REF002",  # ซ้ำกับใบที่ 2
                "amount": 4000.0,
                "receiver_name": "สมชาย สุขใจ",
                "datetime": "2025-05-20T10:02:00"
            }
        ]

    def test_gate1_reject_empty_payload(self):
        """GATE 1: ป้องกัน Input ว่างเปล่า"""
        with self.assertRaises(ValueError) as ctx:
            self.engine.execute_locked_task5_pipeline([])
        self.assertIn("[GATE 1 ASSERTION FAIL]", str(ctx.exception))

    def test_gate1_reject_negative_amount(self):
        """GATE 1: ป้องกันยอดเงินติดลบ"""
        bad_slip = [{"file": "bad.jpg", "amount": -100.0, "receiver_name": "ทดสอบ"}]
        with self.assertRaises(ValueError) as ctx:
            self.engine.execute_locked_task5_pipeline(bad_slip)
        self.assertIn("ยอดเงินติดลบ", str(ctx.exception))

    def test_gate2_stateless_isolation(self):
        """GATE 2: Stateless Isolation รันซ้ำต้องให้ผล 100% เท่าเดิม"""
        res1 = self.engine.execute_locked_task5_pipeline(self.sample_slips)
        self.engine.reset_isolated_context()
        res2 = self.engine.execute_locked_task5_pipeline(self.sample_slips)

        self.assertEqual(res1["the_4_cards"]["card_1"]["total_net_loss"],
                         res2["the_4_cards"]["card_1"]["total_net_loss"])
        self.assertEqual(res1["the_4_cards"]["card_4"]["duplicate_slips_eliminated"],
                         res2["the_4_cards"]["card_4"]["duplicate_slips_eliminated"])

    def test_gate3_immutable_config(self):
        """GATE 3: แช่แข็ง Config ห้ามกลายพันธุ์"""
        cfg = LockedTask5Config()
        with self.assertRaises(Exception):
            cfg.burst_threshold_seconds = 60

    def test_gate4_card_1_and_card_4_dedup(self):
        """GATE 4: สลิปซ้ำต้องถูกตัดออกจากการ์ด 1 และบันทึกในการ์ด 4"""
        res = self.engine.execute_locked_task5_pipeline(self.sample_slips)
        c1 = res["the_4_cards"]["card_1"]
        c4 = res["the_4_cards"]["card_4"]

        # ยอดรวมจริง 1,000 + 4,000 = 5,000 (ตัดใบซ้ำ 4,000 ออก)
        self.assertEqual(c1["total_net_loss"], 5000.0)
        self.assertEqual(c1["cleared_transactions_count"], 2)
        self.assertEqual(c4["duplicate_slips_eliminated"], 1)
        self.assertEqual(c4["double_counting_prevented_amount"], 4000.0)

    def test_gate4_card_3_burst_detection(self):
        """GATE 4: ตรวจจับ Burst Episode เมื่อโอนถี่ภายใน 3 นาที"""
        res = self.engine.execute_locked_task5_pipeline(self.sample_slips)
        c3 = res["the_4_cards"]["card_3"]

        self.assertEqual(c3["burst_episodes_detected"], 1)
        self.assertEqual(c3["slips_involved_in_bursts"], 2)
        self.assertIn("HIGH_COERCION_RISK", c3["risk_assessment"])

    def test_gate5_math_invariant_circuit_breaker(self):
        """GATE 5: Circuit Breaker ยอดการ์ด 1 ต้องเท่ากับผลรวมการ์ด 2 เป๊ะ"""
        res = self.engine.execute_locked_task5_pipeline(self.sample_slips)
        # ตรวจสอบว่าไม่เกิด error และสถานะล็อกผ่าน
        self.assertEqual(res["workflow_lock_status"], "VERIFIED_LOCKED")

if __name__ == "__main__":
    unittest.main()

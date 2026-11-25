# -*- coding: utf-8 -*-
"""
Verification Suite for Task 3 Workflow Lock (The 5 Invariant Gates)
ทดสอบยืนยันระบบการทำงานของ Task 3 ภายใต้การควบคุมของสกิล Lock
"""

import unittest
from kpi_target_aggregator import LockedKPITargetAggregator, LockedKPIConfig

class TestTask3WorkflowLock(unittest.TestCase):

    def setUp(self):
        self.engine = LockedKPITargetAggregator()

    def test_gate1_empty_payload(self):
        """GATE 1: ป้องกัน Input ว่างเปล่า"""
        with self.assertRaises(ValueError) as ctx:
            self.engine.ingest([])
        self.assertIn("[GATE 1 ASSERTION FAIL]", str(ctx.exception))

    def test_gate1_negative_amount(self):
        """GATE 1: ป้องกันยอดเงินติดลบ"""
        bad_slip = {
            "receiver_name": "นาย ทดสอบ",
            "amount": -500.0
        }
        with self.assertRaises(ValueError) as ctx:
            self.engine.ingest([bad_slip])
        self.assertIn("ยอดเงินติดลบ", str(ctx.exception))

    def test_gate2_stateless_isolation(self):
        """GATE 2: ตรวจสอบความปลอดเชื้อ (Stateless Isolation) รันซ้ำต้องไม่รั่วไหล"""
        slip_a = {"receiver_name": "นาย เอ ทดสอบ", "amount": 1000.0}
        self.engine.ingest([slip_a])
        self.assertEqual(len(self.engine.get_kpi_summary()), 1)

        # สั่งรีเซ็ตและรันด้วยข้อมูลใหม่
        self.engine.reset_isolated_context()
        slip_b = {"receiver_name": "นางสาว บี ทดสอบ", "amount": 2500.0}
        self.engine.ingest([slip_b])
        
        summary = self.engine.get_kpi_summary()
        self.assertEqual(len(summary), 1)
        self.assertEqual(summary[0]["target_name"], "บี ทดสอบ")
        self.assertEqual(summary[0]["total_amount"], 2500.0)

    def test_gate3_immutable_config(self):
        """GATE 3: แช่แข็ง Config ห้ามกลายพันธุ์ (Immutable Config)"""
        cfg = LockedKPIConfig()
        with self.assertRaises(Exception):
            cfg.decimal_precision = 4

    def test_gate4_name_dedup_and_sum(self):
        """GATE 4: สลิปหลายใบชื่อตรงกัน ต้องแสดงรายชื่อเดียวพร้อมยอดรวม"""
        slips = [
            {"receiver_name": "นาย สมชาย ใจดี", "amount": 1200.0, "ref_no": "R01"},
            {"receiver_name": "สมชาย ใจดี", "amount": 800.0, "ref_no": "R02"},
            {"receiver_name": "น.ส. สมหญิง สุขใจ", "amount": 3000.0, "ref_no": "R03"}
        ]
        self.engine.ingest(slips)
        summary = self.engine.get_kpi_summary()

        self.assertEqual(len(summary), 2)  # สมชาย 1, สมหญิง 1
        somchai = next(s for s in summary if s["target_name"] == "สมชาย ใจดี")
        self.assertEqual(somchai["total_amount"], 2000.0)
        self.assertEqual(somchai["slip_count"], 2)

    def test_gate5_target_selection_for_task5(self):
        """GATE 4 & 5: การติ๊ก Checkbox เจาะจงชื่อเป้าหมายเพื่อส่งต่อให้งานที่ 5"""
        slips = [
            {"receiver_name": "นาย ก", "amount": 5000.0, "ref_no": "K01"},
            {"receiver_name": "นาง ข", "amount": 2000.0, "ref_no": "K02"}
        ]
        self.engine.ingest(slips)

        # เลือก นาย ข
        self.engine.select_target("ข")
        payload = self.engine.export_for_task5()

        self.assertEqual(payload["status"], "LOCKED_READY_FOR_TASK_5")
        self.assertEqual(payload["target_person"]["name"], "ข")
        self.assertEqual(payload["target_person"]["total_loss_amount"], 2000.0)
        self.assertEqual(len(payload["timeline_transactions"]), 1)

if __name__ == "__main__":
    unittest.main()

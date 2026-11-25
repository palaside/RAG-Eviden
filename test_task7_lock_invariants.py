# -*- coding: utf-8 -*-
"""
Verification Suite for Task 7: Evidence Summary Table (The 5 Invariant Gates)
ทดสอบยืนยันระบบการทำงานของ Task 7 ภายใต้การควบคุมของสกิล Lock
"""

import unittest
from task7_evidence_summary_table import LockedTask7EvidenceTableEngine, LockedTask7Config

class TestTask7EvidenceTableLock(unittest.TestCase):

    def setUp(self):
        self.engine = LockedTask7EvidenceTableEngine()
        self.valid_task5_input = {
            "task_id": "TASK_05",
            "the_4_cards": {
                "card_1": {
                    "card_id": "CARD_01_NET_PRINCIPAL_LOSS",
                    "total_net_loss": 5000.0,
                    "cleared_transactions_count": 2
                },
                "card_2": {
                    "card_id": "CARD_02_WHALE_BENEFICIARY_INDEX",
                    "whale_target_name": "สมชาย สุขใจ",
                    "concentrated_amount": 5000.0,
                    "percentage_of_total_loss": 100.0,
                    "all_targets_ranked": [
                        {"name": "สมชาย สุขใจ", "total_amount": 5000.0, "count": 2, "percentage": 100.0}
                    ]
                },
                "card_3": {
                    "card_id": "CARD_03_FRAUD_VELOCITY_BURST",
                    "burst_episodes_detected": 1,
                    "burst_details": []
                },
                "card_4": {
                    "card_id": "CARD_04_TAMPER_DEDUP_GUARD",
                    "duplicate_slips_eliminated": 0
                }
            },
            "raw_unique_slips": [
                {
                    "raw_file": "slip_1.jpg",
                    "amount": 2000.0,
                    "fee": 0.0,
                    "ref_no": "REF001",
                    "receiver_name": "สมชาย สุขใจ",
                    "bank": "KTB",
                    "datetime_str": "2025-05-20 10:00:00"
                },
                {
                    "raw_file": "slip_2.jpg",
                    "amount": 3000.0,
                    "fee": 0.0,
                    "ref_no": "REF002",
                    "receiver_name": "สมชาย สุขใจ",
                    "bank": "KTB",
                    "datetime_str": "2025-05-20 10:02:00"
                }
            ]
        }

    def test_gate1_reject_none_input(self):
        """GATE 1: ปฏิเสธค่าว่าง None"""
        with self.assertRaises(ValueError) as ctx:
            self.engine.execute_locked_task7_pipeline(None)
        self.assertIn("[GATE 1 ASSERTION FAIL]", str(ctx.exception))

    def test_gate1_reject_invalid_source(self):
        """GATE 1: ปฏิเสธข้อมูลที่ไม่ได้มาจาก Task 5"""
        invalid_input = {"task_id": "TASK_01", "file": "some.jpg"}
        with self.assertRaises(ValueError) as ctx:
            self.engine.execute_locked_task7_pipeline(invalid_input)
        self.assertIn("[GATE 1 ASSERTION FAIL: INVALID_INPUT_SOURCE]", str(ctx.exception))

    def test_gate1_reject_empty_slips(self):
        """GATE 1: ปฏิเสธ Task 5 ที่ไม่มีรายการสลิป (0 records)"""
        empty_input = {
            "task_id": "TASK_05",
            "the_4_cards": {},
            "raw_unique_slips": []
        }
        with self.assertRaises(ValueError) as ctx:
            self.engine.execute_locked_task7_pipeline(empty_input)
        self.assertIn("[GATE 1 ASSERTION FAIL]", str(ctx.exception))

    def test_gate2_stateless_isolation(self):
        """GATE 2: Stateless Context Isolation รันซ้ำผลลัพธ์ต้องเหมือนเดิม 100%"""
        res1 = self.engine.execute_locked_task7_pipeline(self.valid_task5_input)
        self.engine.reset_isolated_context()
        res2 = self.engine.execute_locked_task7_pipeline(self.valid_task5_input)

        self.assertEqual(res1["table_metadata"]["total_reconciled_amount"],
                         res2["table_metadata"]["total_reconciled_amount"])
        self.assertEqual(res1["table_metadata"]["total_rows_count"],
                         res2["table_metadata"]["total_rows_count"])

    def test_gate3_immutable_config(self):
        """GATE 3: แช่แข็ง Config ห้ามแก้ไข"""
        cfg = LockedTask7Config()
        with self.assertRaises(Exception):
            cfg.strict_source_task = "TASK_01"

    def test_gate4_money_trail_flow_and_whale(self):
        """GATE 4: ตรวจสอบการสร้าง Money Trail Flow และแท็ก Whale Target"""
        res = self.engine.execute_locked_task7_pipeline(self.valid_task5_input)
        rows = res["evidence_rows"]
        self.assertEqual(len(rows), 2)
        self.assertTrue(rows[0]["is_whale_target"])
        self.assertIn("ผู้เสียหาย (บัญชีต้นทาง) ➔ [KTB] ➔ สมชาย สุขใจ", rows[0]["money_trail_flow"])

    def test_gate4_visual_preview_and_reversibility(self):
        """GATE 4: บังคับให้ทุกแถวมี Visual Preview Path และ Reversibility Proof"""
        res = self.engine.execute_locked_task7_pipeline(self.valid_task5_input)
        for r in res["evidence_rows"]:
            self.assertTrue(len(r["visual_preview_path"]) > 0)
            self.assertIn("SHA256_HASH_VERIFIED", r["reversibility_proof"])

    def test_gate5_math_reconciliation_circuit_breaker(self):
        """GATE 5: ยอดเงินในตารางต้องตรงกับ Card 1 Task 5 เป๊ะ หากไม่ตรงต้องตัดวงจรทันที"""
        tampered_input = dict(self.valid_task5_input)
        # ปรับยอดเงินในการ์ด 1 ให้ไม่ตรงกับผลรวมสลิป
        tampered_input["the_4_cards"]["card_1"]["total_net_loss"] = 99999.0

        with self.assertRaises(RuntimeError) as ctx:
            self.engine.execute_locked_task7_pipeline(tampered_input)
        self.assertIn("[GATE 5 CIRCUIT BREAKER TRIGGERED: DISCREPANCY_DETECTED]", str(ctx.exception))

if __name__ == "__main__":
    unittest.main()

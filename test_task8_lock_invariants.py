#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
========================================================================================
UNIT TEST & INVARIANT VERIFICATION SUITE FOR TASK 8
ทดสอบการทำงานของ Task8CourtDossierAssembler และการล็อกระบบด้วย 5 Invariant Gates
========================================================================================
"""

import unittest
import os
import json
from task8_court_dossier_assembler import Task8CourtDossierAssembler, LockedDossierConfig

class TestTask8LockInvariants(unittest.TestCase):

    def setUp(self):
        self.assembler = Task8CourtDossierAssembler()

        # Mock valid outputs from Tasks 4, 5, 7
        self.valid_t4 = {
            "status": "SUCCESS_ANALYZED",
            "six_agents_analysis": {
                "agent1_chrono_story": {
                    "total_key_nodes": 7,
                    "story_arc": "ล่อลวงยืมเงิน 2,000 บาทเปิดหัว แล้วยกระดับเป็น 10,000 บาท"
                },
                "agent2_corroboration": {
                    "matches_found": 1,
                    "smoking_gun_nodes": ["NODE_BURST_01"]
                },
                "agent3_forensic_dialogue": {
                    "manipulation_tactics": ["อ้างบุคคลที่สาม", "สั่งเปลี่ยนบัญชีก่อนโอน 60 วินาที"]
                },
                "agent4_legal_corpus": {
                    "primary_charges": ["ป.อ. ๓๔๑", "ป.อ. ๓๔๓", "ป.อ. ๘๓", "พ.ร.ก.บัญชีม้า ๒๕๖๖"]
                },
                "agent5_attorney_knowledge": {
                    "killer_cross_examination_script": [
                        {
                            "question_id": "Q1",
                            "question_text": "จำเลยเป็นผู้สั่งให้ผู้เสียหายโอนเงินเข้าบัญชี น.ส. อลงกรณ์ แจ่มเมือง ใช่หรือไม่?",
                            "reference_evidence": "แชท 16:51 น.",
                            "target_confession": "ยอมรับคำสั่งโอน"
                        },
                        {
                            "question_id": "Q2",
                            "question_text": "จำเลยไม่เคยมีนิติสัมพันธ์หรือสัญญาหนี้สินใดๆ กับเจ้าของบัญชีปลายทาง ใช่หรือไม่?",
                            "reference_evidence": "สลิป 5,600 บาท",
                            "target_confession": "มัดตัวการร่วมบัญชีม้า"
                        }
                    ]
                },
                "agent6_distilled_digest": {
                    "system_verdict_permitted": False,
                    "discretion_mandate": "ขึ้นอยู่กับดุลพินิจของทนายความและศาล 100%"
                }
            }
        }

        self.valid_t5 = {
            "status": "PURE_SLIP_SOT_LOCKED_SUCCESS",
            "the_4_cards": {
                "card1_net_principal_loss": {
                    "total_net_loss": 11000.00,
                    "verified_slip_count": 3
                },
                "card2_whale_beneficiary": {
                    "primary_whale_name": "นางสาว อลงกรณ์ แจ่มเมือง",
                    "primary_whale_amount": 10000.00,
                    "primary_whale_ratio_pct": 90.91
                },
                "card3_fraud_velocity_burst": {
                    "total_burst_spikes": 1,
                    "burst_events": [
                        {
                            "burst_id": "BURST_01",
                            "time_delta_seconds": 90.0,
                            "risk_tier": "🚨 HIGH_COERCION_RISK"
                        }
                    ]
                },
                "card4_tamper_and_dedup_guard": {
                    "duplicate_slips_detected": 1,
                    "duplicate_amount_prevented": 5600.00
                }
            }
        }

        self.valid_t7 = {
            "status": "TASK7_EVIDENCE_TABLE_LOCKED_SUCCESS",
            "evidence_rows": [
                {
                    "row_id": "ROW_01",
                    "timestamp": "12 มี.ค. 2568 20:17 น.",
                    "money_trail_flow": "ผู้เสียหาย (บัญชีต้นทาง) ➔ [KTB] ➔ น.ส. จิณห์นิภา บุญประเสริฐ",
                    "amount": 1000.00,
                    "bank_ref_id": "N006727673034053896171486",
                    "is_whale_target": False,
                    "is_burst_anomaly": False
                },
                {
                    "row_id": "ROW_02",
                    "timestamp": "26 พ.ค. 2568 16:50:00 น.",
                    "money_trail_flow": "ผู้เสียหาย (บัญชีต้นทาง) ➔ [KTB] ➔ นางสาว อลงกรณ์ แจ่มเมือง",
                    "amount": 5600.00,
                    "bank_ref_id": "Aa7e0058a52854e5c",
                    "is_whale_target": True,
                    "is_burst_anomaly": True
                },
                {
                    "row_id": "ROW_03",
                    "timestamp": "26 พ.ค. 2568 16:51:30 น.",
                    "money_trail_flow": "ผู้เสียหาย (บัญชีต้นทาง) ➔ [KTB] ➔ นางสาว อลงกรณ์ แจ่มเมือง",
                    "amount": 4400.00,
                    "bank_ref_id": "Bb8f9900112233",
                    "is_whale_target": True,
                    "is_burst_anomaly": True
                }
            ],
            "reconciliation_audit": {
                "table_rows_sum": 11000.00,
                "target_net_loss": 11000.00,
                "reconciliation_error": 0.00
            }
        }

    def test_gate1_rejection_on_missing_input(self):
        """GATE 1: ปฏิเสธทันทีหากข้อมูลนำเข้าขาดหาย"""
        with self.assertRaises(ValueError) as ctx:
            self.assembler.assemble_dossier({}, self.valid_t5, self.valid_t7)
        self.assertIn("GATE 1 REJECTED", str(ctx.exception))

    def test_gate1_rejection_on_amount_mismatch(self):
        """GATE 1: ปฏิเสธทันทีหากยอดเงิน Task 5 และ Task 7 ไม่ตรงกัน"""
        corrupted_t5 = dict(self.valid_t5)
        corrupted_t5["the_4_cards"] = dict(self.valid_t5["the_4_cards"])
        corrupted_t5["the_4_cards"]["card1_net_principal_loss"] = {
            "total_net_loss": 9999.00,
            "verified_slip_count": 3
        }
        with self.assertRaises(ValueError) as ctx:
            self.assembler.assemble_dossier(self.valid_t4, corrupted_t5, self.valid_t7)
        self.assertIn("ยอดเงินไม่ตรงกัน", str(ctx.exception))

    def test_gate2_stateless_context(self):
        """GATE 2: สร้าง Isolated Context แยกส่วนและไม่แตะ Global State"""
        ctx = self.assembler._create_isolated_context(self.valid_t4, self.valid_t5, self.valid_t7, "2026-11-24")
        self.assertEqual(ctx["financials"]["net_actionable_loss"], 11000.00)
        self.assertEqual(ctx["financials"]["whale_name"], "นางสาว อลงกรณ์ แจ่มเมือง")
        self.assertEqual(ctx["financials"]["gross_outflow"], 16600.00)  # 11,000 + 5,600 dedup

    def test_gate3_immutable_config(self):
        """GATE 3: ตรวจสอบความคงที่ของคอนฟิกูเรชันล็อก (Frozen Dataclass)"""
        cfg = LockedDossierConfig()
        self.assertEqual(cfg.annual_interest_rate, 0.05)
        self.assertEqual(cfg.case_number, "012/2569")
        with self.assertRaises(Exception):
            cfg.annual_interest_rate = 0.075

    def test_gate4_sequential_pages_count_and_titles(self):
        """GATE 4: ตรวจสอบการประกอบหน้ากระดาษครบทั้ง 7 หน้าตามลำดับ"""
        res = self.assembler.assemble_dossier(self.valid_t4, self.valid_t5, self.valid_t7)
        self.assertEqual(res["total_pages"], 7)
        page_types = [p["type"] for p in res["pages"]]
        expected_types = ["COVER", "NETWORK", "SUMMARY", "INTEREST", "TIMELINE_11D", "HASH_MANIFEST", "SUBPOENA"]
        self.assertEqual(page_types, expected_types)

    def test_gate4_page1_and_page3_integrated_items(self):
        """GATE 4: ตรวจสอบ 2 เรื่องที่รวมในแผ่นเดิม (รหัส จ.๑-จ.๔ ในหน้าปก + หักทอนในหน้าสรุป)"""
        res = self.assembler.assemble_dossier(self.valid_t4, self.valid_t5, self.valid_t7)
        pages = res["pages"]
        # แผ่นที่ 1 ต้องมีรหัสเอกสารหมาย จ.
        self.assertEqual(pages[0]["exhibit_code"], "จ.๑-จ.๔")
        # แผ่นที่ 3 ต้องมียอดหักทอน Gross, Offset, Net
        p3_html = res["visual_preview_html"]
        self.assertIn("ยอดโอนออกรวม (Gross): ฿16,600.00", p3_html)
        self.assertIn("ยอดโอนคืน/หมุนเวียน (Offset): ฿0.00", p3_html)
        self.assertIn("ยอดติดค้างฟ้องร้องสุทธิ: ฿11,000.00", p3_html)

    def test_gate4_page4_daily_interest_calculation(self):
        """GATE 4: ตรวจสอบการคำนวณดอกเบี้ยรายวันตาม ป.พ.พ. ม.๗/ม.๒๒๔ (๕% ต่อปี)"""
        res = self.assembler.assemble_dossier(self.valid_t4, self.valid_t5, self.valid_t7, calculation_date="2026-11-24")
        html = res["visual_preview_html"]
        self.assertIn("ตารางคำนวณเงินต้นและดอกเบี้ยผิดนัดรายกรรม", html)
        self.assertIn("5% ×", html)
        self.assertIn("ข้อความสำหรับทนายความนำไปใส่ใน \"คำขอท้ายฟ้อง\"", html)

    def test_gate4_page_subpoena_motion(self):
        """GATE 4: ตรวจสอบแผ่นขอออกหมายเรียกพยานเอกสาร (Subpoena Motion)"""
        res = self.assembler.assemble_dossier(self.valid_t4, self.valid_t5, self.valid_t7)
        pages = res["pages"]
        self.assertEqual(pages[6]["type"], "SUBPOENA")
        self.assertEqual(pages[6]["exhibit_code"], "ภาคผนวก ข.")
        html = res["visual_preview_html"]
        self.assertIn("หมายเรียกเอกสารจาก ธนาคารกรุงไทย จำกัด (มหาชน)", html)
        self.assertIn("หมายเรียกเอกสารจาก ผู้ให้บริการเครือข่ายโทรศัพท์และแอปพลิเคชัน LINE", html)

    def test_gate5_circuit_breaker_pass(self):
        """GATE 5: Circuit Breaker ตรวจสอบความสมบูรณ์และประทับตราชนะคดี"""
        res = self.assembler.assemble_dossier(self.valid_t4, self.valid_t5, self.valid_t7)
        self.assertEqual(res["status"], "COURT_DOSSIER_SUCCESS_SEALED")
        self.assertEqual(res["forensic_seal"]["circuit_breaker"], "PASS_ALL_INVARIANTS")
        self.assertEqual(res["net_loss_reconciled"], 11000.00)
        self.assertTrue(self.assembler._execution_locked)

    def test_lock_skill_stateless_reset_and_wrapper(self):
        """LOCK SKILL: ตรวจสอบ execute_locked_task8_dossier และ reset_isolated_context"""
        res = self.assembler.execute_locked_task8_dossier(self.valid_t4, self.valid_t5, self.valid_t7)
        self.assertEqual(res["total_pages"], 7)
        self.assertTrue(self.assembler._execution_locked)
        self.assembler.reset_isolated_context()
        self.assertFalse(self.assembler._execution_locked)

if __name__ == "__main__":
    unittest.main()

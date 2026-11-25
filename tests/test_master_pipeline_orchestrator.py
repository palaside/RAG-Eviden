import unittest
from master_pipeline_orchestrator import MasterPipelineOrchestrator

class TestMasterPipelineOrchestrator(unittest.TestCase):
    def setUp(self):
        self.orchestrator = MasterPipelineOrchestrator(case_number="012/2569")
        self.dataset = [
            {
                "file_id": "RAW-001",
                "name": "chat_page_01.jpg",
                "aspect_ratio": 2.15,
                "dialogue_text": "เตงโอนให้หน่อย 2,000",
                "type_expected": "TYPE_CHAT"
            },
            {
                "file_id": "RAW-002",
                "name": "chat_page_02.jpg",
                "aspect_ratio": 2.30,
                "dialogue_text": "ขอเพิ่มอีก 8,500 นะ ด่วนมาก",
                "type_expected": "TYPE_CHAT"
            },
            {
                "file_id": "RAW-003",
                "name": "slip_scb_2000.jpg",
                "aspect_ratio": 1.77,
                "type_expected": "TYPE_SLIP_SOLO",
                "ocr_data": {
                    "bank": "SCB",
                    "receiver_name": "นางสาว จิณห์นิภา ประสาทเขตรการ",
                    "receiver_bank": "SCB",
                    "receiver_account": "123-4-56789-0",
                    "amount": 2000.0,
                    "trans_date": "2026-11-20 08:18:00",
                    "ref_id": "20261120SCB001"
                }
            },
            {
                "file_id": "RAW-004",
                "name": "slip_kbank_8500.jpg",
                "aspect_ratio": 1.78,
                "type_expected": "TYPE_SLIP_SOLO",
                "ocr_data": {
                    "bank": "KBANK",
                    "receiver_name": "นางสาว จิณห์นิภา ประสาทเขตรการ",
                    "receiver_bank": "KBANK",
                    "receiver_account": "987-6-54321-0",
                    "amount": 8500.0,
                    "trans_date": "2026-11-20 10:48:00",
                    "ref_id": "20261120KBANK002"
                }
            },
            {
                "file_id": "RAW-005_DUP",
                "name": "slip_kbank_8500_dup.jpg",
                "aspect_ratio": 1.77,
                "type_expected": "TYPE_SLIP_SOLO",
                "ocr_data": {
                    "bank": "KBANK",
                    "receiver_name": "นางสาว จิณห์นิภา ประสาทเขตรการ",
                    "receiver_bank": "KBANK",
                    "receiver_account": "987-6-54321-0",
                    "amount": 8500.0,
                    "trans_date": "2026-11-20 10:48:00",
                    "ref_id": "20261120KBANK002"  # duplicate
                }
            }
        ]

    def test_run_full_master_pipeline(self):
        result = self.orchestrator.execute_full_pipeline(self.dataset)
        self.assertEqual(result["status"], "MASTER_PIPELINE_COMPLETE")
        self.assertEqual(result["detect_summary"]["total_classified"], 5)
        self.assertEqual(result["staging_summary"]["chats_count"], 2)
        self.assertEqual(result["staging_summary"]["slips_found"], 3)
        self.assertEqual(result["staging_summary"]["slips_confirmed"], 2)
        self.assertEqual(result["staging_summary"]["reconciled_total_amount"], 10500.0)
        self.assertEqual(result["recipient_summary"]["primary_poi"]["name"], "นางสาว จิณห์นิภา ประสาทเขตรการ")
        self.assertEqual(result["t5_result"]["the_4_cards"]["card_1"]["total_net_loss"], 10500.0)
        self.assertEqual(result["t8_result"]["status"], "COURT_DOSSIER_SUCCESS_SEALED")
        self.assertEqual(result["t9_result"]["status"], "VAULT_EXPORT_LOCKED_SUCCESS")

if __name__ == "__main__":
    unittest.main()

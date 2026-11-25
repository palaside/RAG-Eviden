import unittest
from detect_gateway import ClassifiedEvidenceItem, EvidenceType
from task1_feature_normalization import Task1FeatureNormalizer, NormalizedEvidenceRecord

class TestTask1FeatureNormalization(unittest.TestCase):
    def setUp(self):
        self.normalizer = Task1FeatureNormalizer()

    def test_normalize_chat_item(self):
        classified = ClassifiedEvidenceItem(
            file_id="RAW-001",
            name="chat_page_01.jpg",
            type=EvidenceType.TYPE_CHAT,
            sha256="e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
            aspect_ratio=2.15,
            raw_metadata={"dialogue_text": "เตงโอนให้หน่อย", "page_no": 1}
        )
        record = self.normalizer.normalize(classified)
        self.assertEqual(record.file_id, "RAW-001")
        self.assertEqual(record.evidence_category, "CHAT")
        self.assertEqual(record.dialogue_snippet, "เตงโอนให้หน่อย")
        self.assertIsNotNone(record.iso_timestamp)

    def test_normalize_slip_item(self):
        classified = ClassifiedEvidenceItem(
            file_id="RAW-003",
            name="slip_kbank_5000.jpg",
            type=EvidenceType.TYPE_SLIP_SOLO,
            sha256="bf529a67e1a30f30c6a1cf8b73656fe2b236fa79659f1c7d2c14041a996fa1d5",
            aspect_ratio=1.77,
            raw_metadata={
                "ocr_data": {
                    "receiver_name": "  นางสาว จิณห์นิภา ประสาทเขตรการ  ",
                    "receiver_bank": "KBANK",
                    "receiver_account": "123-4-56789-0",
                    "amount": "5,000.00",
                    "trans_date": "2026-11-20 14:30:00",
                    "ref_id": "202611200001"
                }
            }
        )
        record = self.normalizer.normalize(classified)
        self.assertEqual(record.evidence_category, "SLIP")
        self.assertEqual(record.receiver_name, "นางสาว จิณห์นิภา ประสาทเขตรการ")
        self.assertEqual(record.amount, 5000.0)
        self.assertEqual(record.receiver_bank, "KBANK")
        self.assertEqual(record.ref_id, "202611200001")

if __name__ == "__main__":
    unittest.main()

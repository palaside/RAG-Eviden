import unittest
import hashlib
from detect_gateway import DetectGateway, ClassifiedEvidenceItem, EvidenceType

class TestDetectGateway(unittest.TestCase):
    def setUp(self):
        self.gateway = DetectGateway()

    def test_classify_chat_dialogue(self):
        item = {
            "file_id": "RAW-001",
            "name": "chat_page_01.jpg",
            "aspect_ratio": 2.15,
            "dialogue_text": "เตงโอนให้หน่อย"
        }
        res = self.gateway.classify(item)
        self.assertEqual(res.type, EvidenceType.TYPE_CHAT)
        self.assertEqual(res.file_id, "RAW-001")
        self.assertTrue(len(res.sha256) == 64)

    def test_classify_slip_solo(self):
        item = {
            "file_id": "RAW-003",
            "name": "slip_kbank_5000.jpg",
            "aspect_ratio": 1.77,
            "ocr_data": {"amount": 5000.0, "receiver_name": "สมชาย"}
        }
        res = self.gateway.classify(item)
        self.assertEqual(res.type, EvidenceType.TYPE_SLIP_SOLO)
        self.assertEqual(res.aspect_ratio, 1.77)

    def test_classify_chat_with_slip(self):
        item = {
            "file_id": "RAW-004",
            "name": "chat_with_slip.jpg",
            "aspect_ratio": 2.2,
            "dialogue_text": "ส่งสลิปให้แล้วนะ",
            "has_slip_bubble": True
        }
        res = self.gateway.classify(item)
        self.assertEqual(res.type, EvidenceType.TYPE_CHAT_WITH_SLIP)

    def test_classify_unknown(self):
        item = {
            "file_id": "RAW-999",
            "name": "random_corrupted.bin",
            "aspect_ratio": 0.5
        }
        res = self.gateway.classify(item)
        self.assertEqual(res.type, EvidenceType.TYPE_UNKNOWN)

if __name__ == "__main__":
    unittest.main()

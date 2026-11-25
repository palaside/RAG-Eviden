import unittest
from task1_feature_normalization import NormalizedEvidenceRecord
from task3_recipient_poi import Task3RecipientSelector, RecipientPOISummary

class TestTask3RecipientPOI(unittest.TestCase):
    def setUp(self):
        self.selector = Task3RecipientSelector()

    def test_aggregate_and_detect_whale(self):
        records = [
            NormalizedEvidenceRecord(
                file_id="RAW-001",
                name="slip1.jpg",
                evidence_category="SLIP",
                sha256="h1",
                aspect_ratio=1.77,
                iso_timestamp="2026-11-20T10:00:00Z",
                receiver_name="นางสาว จิณห์นิภา ประสาทเขตรการ",
                receiver_bank="KBANK",
                receiver_account="123-4-56789-0",
                amount=5000.0
            ),
            NormalizedEvidenceRecord(
                file_id="RAW-002",
                name="slip2.jpg",
                evidence_category="SLIP",
                sha256="h2",
                aspect_ratio=1.78,
                iso_timestamp="2026-11-20T11:00:00Z",
                receiver_name="นางสาว จิณห์นิภา ประสาทเขตรการ",
                receiver_bank="KBANK",
                receiver_account="123-4-56789-0",
                amount=10000.0
            ),
            NormalizedEvidenceRecord(
                file_id="RAW-003",
                name="slip3.jpg",
                evidence_category="SLIP",
                sha256="h3",
                aspect_ratio=1.77,
                iso_timestamp="2026-11-20T12:00:00Z",
                receiver_name="นางสาว จิณห์นิภา ประสาทเขตรการ",
                receiver_bank="KBANK",
                receiver_account="123-4-56789-0",
                amount=4000.0
            ),
            NormalizedEvidenceRecord(
                file_id="RAW-004",
                name="slip4.jpg",
                evidence_category="SLIP",
                sha256="h4",
                aspect_ratio=1.77,
                iso_timestamp="2026-11-20T13:00:00Z",
                receiver_name="นายสมชาย ม้าเร็ว",
                receiver_bank="SCB",
                receiver_account="987-6-54321-0",
                amount=1000.0
            )
        ]

        summary = self.selector.aggregate(records)
        self.assertEqual(len(summary.recipients), 2)
        
        # Primary POI / Whale
        self.assertIsNotNone(summary.primary_poi)
        self.assertEqual(summary.primary_poi.name, "นางสาว จิณห์นิภา ประสาทเขตรการ")
        self.assertEqual(summary.primary_poi.count, 3)
        self.assertEqual(summary.primary_poi.total_amount, 19000.0)

        # Filtering POI transactions
        filtered = self.selector.filter_by_recipient(records, "นางสาว จิณห์นิภา ประสาทเขตรการ")
        self.assertEqual(len(filtered), 3)

if __name__ == "__main__":
    unittest.main()

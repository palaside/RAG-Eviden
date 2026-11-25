import unittest
from task1_feature_normalization import NormalizedEvidenceRecord
from task2_staging_buffer import Task2StagingBuffer, BufferState

class TestTask2StagingBuffer(unittest.TestCase):
    def setUp(self):
        self.buffer = Task2StagingBuffer()

    def test_buffer_lifecycle_empty(self):
        self.assertEqual(self.buffer.state, BufferState.EMPTY)
        self.assertEqual(self.buffer.kpi_string(), "📷 แชท 0 หน้า | 🧾 สลิป พบ 0 · ยืนยัน 0 รายการ")

    def test_buffer_ingestion_and_kpi(self):
        records = [
            NormalizedEvidenceRecord(
                file_id="RAW-001",
                name="chat1.jpg",
                evidence_category="CHAT",
                sha256="hash1",
                aspect_ratio=2.15,
                iso_timestamp="2026-11-20T10:00:00Z"
            ),
            NormalizedEvidenceRecord(
                file_id="RAW-002",
                name="chat2.jpg",
                evidence_category="CHAT",
                sha256="hash2",
                aspect_ratio=2.30,
                iso_timestamp="2026-11-20T10:05:00Z"
            ),
            NormalizedEvidenceRecord(
                file_id="RAW-003",
                name="slip1.jpg",
                evidence_category="SLIP",
                sha256="hash3",
                aspect_ratio=1.77,
                iso_timestamp="2026-11-20T10:10:00Z",
                amount=5000.0,
                receiver_name="จิณห์นิภา"
            ),
            NormalizedEvidenceRecord(
                file_id="RAW-004",
                name="slip2.jpg",
                evidence_category="SLIP",
                sha256="hash4",
                aspect_ratio=1.78,
                iso_timestamp="2026-11-20T10:15:00Z",
                amount=10000.0,
                receiver_name="จิณห์นิภา"
            ),
            NormalizedEvidenceRecord(
                file_id="RAW-005_DUP",
                name="slip1_dup.jpg",
                evidence_category="SLIP",
                sha256="hash3",  # duplicate hash
                aspect_ratio=1.77,
                iso_timestamp="2026-11-20T10:10:00Z",
                amount=5000.0,
                receiver_name="จิณห์นิภา"
            )
        ]
        self.buffer.ingest(records)
        self.assertEqual(self.buffer.state, BufferState.CONFIRMED)
        self.assertEqual(self.buffer.chats_count, 2)
        self.assertEqual(self.buffer.slips_found, 3)
        self.assertEqual(self.buffer.slips_confirmed, 2)
        self.assertEqual(self.buffer.kpi_string(), "📷 แชท 2 หน้า | 🧾 สลิป พบ 3 · ยืนยัน 2 รายการ")
        self.assertEqual(self.buffer.reconciled_total_amount, 15000.0)

if __name__ == "__main__":
    unittest.main()

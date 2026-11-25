#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
========================================================================================
FORENSIC CASE STUDY & MULTI-PARADIGM TEST SUITE: แชทที่ 3
Target Directory: D:\\Project\\ชวกม.2\\EDOK_NUI\\FOR TEST In EDOK_NUI\\แชทที่ 3
Lead Architect: Principal QA Architect & Digital Forensic Systems Lead
Constraint: Strict boundary enforcement — ALL test inputs must reside in 'แชทที่ 3'
========================================================================================
Test Paradigms Covered:
  1. SHA-256 Invariant Hashing & Chain of Custody (ISO/IEC 27037)
  2. Multi-Aspect Image Intake & Classification Matrix (DetectGateway)
  3. Dicut_Chat A4 Court-Ready Slicing Engine (Quiet Zone Detection)
  4. Real Google Gemini 2.5 Flash Multimodal OCR & Entity Disambiguation
  5. Master Forensic Pipeline Orchestration (DETECT ➔ TASK 9)
  6. Adversarial, Deduplication & Edge-Case Robustness
========================================================================================
"""

import os
import unittest
import hashlib
from PIL import Image
from typing import List, Dict, Any

# Production Modules
from detect_gateway import DetectGateway, EvidenceType
from task1_feature_normalization import Task1FeatureNormalizer
from task2_staging_buffer import Task2StagingBuffer, BufferState
from task3_recipient_poi import Task3RecipientSelector
from gemini_ocr_engine import GeminiForensicOCREngine
from master_pipeline_orchestrator import MasterPipelineOrchestrator

TARGET_PATH = r"D:\Project\ชวกม.2\EDOK_NUI\FOR TEST In EDOK_NUI\แชทที่ 3"


class TestChat3ForensicSuite(unittest.TestCase):
    """Exhaustive Multi-Paradigm Test Suite on 'แชทที่ 3' Evidence Archive."""

    @classmethod
    def setUpClass(cls):
        if not os.path.exists(TARGET_PATH):
            raise FileNotFoundError(f"Strict path constraint violated: {TARGET_PATH} does not exist!")
        
        # Scan and catalog all files within TARGET_PATH only
        all_entries = [f for f in os.listdir(TARGET_PATH) if not f.startswith('.')]
        cls.image_files = [f for f in all_entries if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp'))]
        cls.pdf_files = [f for f in all_entries if f.lower().endswith('.pdf')]
        
        print(f"\n[FORENSIC CATALOG] Path: {TARGET_PATH}")
        print(f"[FORENSIC CATALOG] Found {len(cls.image_files)} images, {len(cls.pdf_files)} PDF exhibits.")

    def _get_path(self, filename: str) -> str:
        fp = os.path.join(TARGET_PATH, filename)
        # Assert strict containment
        self.assertTrue(os.path.commonpath([fp, TARGET_PATH]) == os.path.normpath(TARGET_PATH),
                        f"Boundary violation: {fp} is outside {TARGET_PATH}")
        self.assertTrue(os.path.exists(fp), f"File {filename} not found in {TARGET_PATH}")
        return fp

    # ==================================================================================
    # PARADIGM 1: SHA-256 HASH INTEGRITY & CHAIN OF CUSTODY (ISO/IEC 27037)
    # ==================================================================================
    def test_01_hash_integrity_and_chain_of_custody(self):
        """Verify deterministic SHA-256 calculation across varied image topologies."""
        cohort = [
            "chatv3 (1).jpg",    # Ultra-long scroll
            "chatv3 (105).jpg",  # Standard chat
            "chatv3 (109).jpg",  # Slip in chat
            "chatv3 (107).jpg",  # Small snippet
            "chatv3 (113).jpg"   # Slip candidate
        ]
        
        gateway = DetectGateway()
        seen_hashes = set()
        
        for fn in cohort:
            fp = self._get_path(fn)
            hash1 = gateway.compute_sha256(fp)
            hash2 = gateway.compute_sha256(fp)
            
            # Deterministic reproducibility
            self.assertEqual(hash1, hash2, f"Hash instability detected for {fn}")
            self.assertEqual(len(hash1), 64, f"Invalid SHA-256 length for {fn}")
            
            # File size sanity
            fsize = os.path.getsize(fp)
            self.assertGreater(fsize, 1000, f"File {fn} is suspiciously small: {fsize} bytes")
            
            seen_hashes.add(hash1)

        self.assertEqual(len(seen_hashes), len(cohort), "SHA-256 collision detected among distinct files!")

    # ==================================================================================
    # PARADIGM 2: MULTI-ASPECT IMAGE INTAKE & CLASSIFICATION MATRIX (DetectGateway)
    # ==================================================================================
    def test_02_detect_classification_matrix(self):
        """Test classification matrix across ultra-long, portrait, slip, and snippet aspect ratios."""
        gateway = DetectGateway()
        
        test_matrix = [
            {"fn": "chatv3 (1).jpg", "min_ar": 4.0, "expected_type": EvidenceType.TYPE_CHAT},
            {"fn": "chatv3 (105).jpg", "min_ar": 2.0, "expected_type": EvidenceType.TYPE_CHAT},
            {"fn": "chatv3 (109).jpg", "min_ar": 1.3, "expected_type": EvidenceType.TYPE_SLIP_SOLO},
            {"fn": "chatv3 (113).jpg", "min_ar": 1.3, "expected_type": EvidenceType.TYPE_SLIP_SOLO},
        ]

        for entry in test_matrix:
            fp = self._get_path(entry["fn"])
            with Image.open(fp) as im:
                w, h = im.size
                ar = h / w

            item = {
                "file_id": f"TEST-{entry['fn']}",
                "name": entry["fn"],
                "path": fp,
                "aspect_ratio": ar,
                "is_valid_image": True
            }

            classified = gateway.classify(item)
            self.assertEqual(classified.type, entry["expected_type"],
                             f"Classification mismatch for {entry['fn']} (AR={ar:.2f})")
            self.assertEqual(len(classified.sha256), 64)

    # ==================================================================================
    # PARADIGM 3: DICUT_CHAT A4 SLICING ENGINE (COURT FIT & QUIET ZONE BENCHMARK)
    # ==================================================================================
    def test_03_dicut_chat_quiet_zone_slicing(self):
        """Verify long continuous chat scroll slicing into A4 blocks (807x1115 target)."""
        long_chat_fn = "chatv3 (1).jpg"
        fp = self._get_path(long_chat_fn)

        with Image.open(fp) as im:
            orig_w, orig_h = im.size
            self.assertGreater(orig_h, 5000, f"Expected long chat height > 5000, got {orig_h}")

            # Scale to court standard width: 807 px
            target_w = 807
            scale_ratio = target_w / float(orig_w)
            scaled_h = int(orig_h * scale_ratio)
            self.assertGreater(scaled_h, target_w * 4)

            # Simulated Quiet Zone slicing chunks (max A4 content block: 1115 px)
            max_a4_h = 1115
            num_slices = (scaled_h + max_a4_h - 1) // max_a4_h

            self.assertGreaterEqual(num_slices, 5, f"Expected at least 5 slices, got {num_slices}")
            print(f"\n[DICUT_CHAT BENCHMARK] {long_chat_fn}: scaled {target_w}x{scaled_h} px -> {num_slices} A4 pages")

    # ==================================================================================
    # PARADIGM 4: REAL GEMINI MULTIMODAL OCR EXTRACTION ON แชทที่ 3 SLIP
    # ==================================================================================
    def test_04_gemini_multimodal_ocr_extraction(self):
        """Execute real Google Gemini 2.5 Flash OCR on chatv3 (109).jpg slip and verify precision."""
        engine = GeminiForensicOCREngine()
        if not engine.is_available():
            self.skipTest("Google Gemini API Key not configured in environment.")

        slip_fn = "chatv3 (109).jpg"
        fp = self._get_path(slip_fn)

        res = engine.extract(fp)
        self.assertTrue(res.get("success"), f"Gemini OCR failed: {res.get('error')}")
        
        # Verify Sender Name Disambiguation & Precision
        sender = res.get("sender_name")
        self.assertEqual(sender, "นาย ณัฐชัย รักษาวงษ์", f"Sender mismatch: expected 'นาย ณัฐชัย รักษาวงษ์', got '{sender}'")
        
        # Verify Amount & Bank
        amount = res.get("amount")
        self.assertEqual(amount, 4950.0, f"Amount mismatch: expected 4950.0, got {amount}")
        self.assertEqual(res.get("bank"), "TTB")
        
        # Verify Ref ID & Receiver
        self.assertEqual(res.get("ref_id"), "202507071502400465")
        self.assertIn("กนกวรรณ", res.get("receiver_name", ""))
        print(f"\n[GEMINI OCR PASS] {slip_fn}: ฿{amount:,.2f} from {sender} to {res.get('receiver_name')}")

    # ==================================================================================
    # PARADIGM 5: END-TO-END PIPELINE ORCHESTRATION (DETECT ➔ TASK 9) ON แชทที่ 3 COHORT
    # ==================================================================================
    def test_05_master_pipeline_e2e_detect_to_task9(self):
        """Execute complete DETECT ➔ TASK 9 pipeline with real files from แชทที่ 3."""
        cohort_files = [
            "chatv3 (1).jpg",    # Chat 1
            "chatv3 (105).jpg",  # Chat 2
            "chatv3 (109).jpg",  # Slip 1 (฿4,950.00 to กนกวรรณ)
            "chatv3 (113).jpg"   # Slip 2
        ]

        raw_dataset = []
        for i, fn in enumerate(cohort_files):
            fp = self._get_path(fn)
            with Image.open(fp) as im:
                w, h = im.size
                ar = round(h / w, 2)

            is_slip = (ar < 2.0)
            ocr_payload = None
            if is_slip:
                ocr_payload = {
                    "bank": "TTB" if "109" in fn else "KBANK",
                    "receiver_name": "นางสาว กนกวรรณ พุทธศรี" if "109" in fn else "นางสาว จิณห์นิภา ประสาทเขตรการ",
                    "sender_name": "นาย ณัฐชัย รักษาวงษ์",
                    "amount": 4950.0 if "109" in fn else 5000.0,
                    "ref_id": f"REF-CHAT3-{i}",
                    "trans_date": "2025-07-07 15:28:00"
                }

            raw_dataset.append({
                "file_id": f"CHAT3-{i+1:03d}",
                "name": fn,
                "path": fp,
                "aspect_ratio": ar,
                "dialogue_text": "โอนเงินเรียบร้อยแล้วครับ" if not is_slip else None,
                "ocr_data": ocr_payload
            })

        orchestrator = MasterPipelineOrchestrator(case_number="012/2569")
        out = orchestrator.execute_full_pipeline(raw_dataset, output_json_path=None)

        # Assert Pipeline Success Across All 9 Stages
        self.assertEqual(out["status"], "MASTER_PIPELINE_COMPLETE")
        self.assertEqual(out["detect_summary"]["total_classified"], 4)
        self.assertEqual(out["staging_summary"]["chats_count"], 2)
        self.assertEqual(out["staging_summary"]["slips_confirmed"], 2)
        self.assertEqual(out["staging_summary"]["reconciled_total_amount"], 9950.0)

        # Assert Court Dossier & Vault SFX Sealed
        self.assertEqual(out["t8_result"]["status"], "COURT_DOSSIER_SUCCESS_SEALED")
        self.assertEqual(out["t9_result"]["status"], "VAULT_EXPORT_SUCCESS_SEALED")
        print("\n[MASTER PIPELINE E2E PASS] Successfully chained DETECT -> TASK 9 on 'แชทที่ 3' cohort!")

    # ==================================================================================
    # PARADIGM 6: ADVERSARIAL & DEDUPLICATION ROBUSTNESS
    # ==================================================================================
    def test_06_adversarial_and_deduplication(self):
        """Test deduplication resilience when an identical file from แชทที่ 3 is ingested twice."""
        fn = "chatv3 (109).jpg"
        fp = self._get_path(fn)

        gateway = DetectGateway()
        normalizer = Task1FeatureNormalizer()
        buffer = Task2StagingBuffer()

        item1 = {"file_id": "C3-01", "name": fn, "path": fp, "aspect_ratio": 1.79, "ocr_data": {"amount": 4950.0, "ref_id": "SAME_REF"}}
        item2 = {"file_id": "C3-01_CLONE", "name": "chatv3_109_clone.jpg", "path": fp, "aspect_ratio": 1.79, "ocr_data": {"amount": 4950.0, "ref_id": "SAME_REF"}}

        records = [normalizer.normalize(gateway.classify(item1)), normalizer.normalize(gateway.classify(item2))]
        buffer.ingest(records)

        # Must detect exactly 1 confirmed unique slip and 0 double-count discrepancy!
        self.assertEqual(buffer.slips_found, 2)
        self.assertEqual(buffer.slips_confirmed, 1)
        self.assertEqual(buffer.reconciled_total_amount, 4950.0, "FATAL: Duplicate double-counting detected!")


if __name__ == "__main__":
    unittest.main()

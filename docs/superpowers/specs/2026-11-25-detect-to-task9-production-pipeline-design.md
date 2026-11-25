# Design Specification: DETECT to TASK 9 Production Pipeline Implementation

**Date:** 2026-11-25  
**Project:** ชวกม.2 (Digital Evidence Forensic Suite)  
**Standard:** ISO/IEC 27037 Digital Evidence Forensics & 4 Iron Rules of Production Parity  
**Status:** Approved  

---

## 1. Overview & Objective
This specification defines the production implementation for the end-to-end evidence processing pipeline:
`DETECT` ➔ `TASK 1` ➔ `TASK 2` ➔ `TASK 3` ➔ `TASK 4` ➔ `TASK 5` ➔ `TASK 7` ➔ `TASK 8` ➔ `TASK 9`.

Previously, tasks 4, 5, 7, 8, 9 had dedicated locked Python engines, while DETECT and Tasks 1-3 were tested via inline assertions in `test_master_e2e_detect_to_task9.py`. This design establishes standalone, clean-architecture production modules for DETECT through Task 3, coupled through a master pipeline orchestrator, and surfaced to the Web UI (`index.html`).

---

## 2. Architecture & Modules

### 2.1 Module 1: `detect_gateway.py` (Forensic Image Intake & Classification Gateway)
- **Role:** First-line intake gateway for forensic digital evidence.
- **Inputs:** Raw image path or binary bytes, file metadata.
- **Classification Rules:**
  - `TYPE_CHAT`: Aspect ratio > 2.0 or detected dialogue bubbles/pills.
  - `TYPE_SLIP_SOLO`: Aspect ratio <= 1.9, bank transfer slip layout or OCR payload.
  - `TYPE_CHAT_WITH_SLIP`: Mixed chat containing embedded bank transfer slips.
  - `TYPE_UNKNOWN`: Fallback for unrecognized formats.
- **Forensic Integrity:** Generates SHA-256 hash immediately upon intake for ISO/IEC 27037 Chain of Custody.
- **Output:** `ClassifiedEvidenceItem` dataclass/dictionary.

### 2.2 Module 2: `task1_feature_normalization.py` (Feature Normalization & ISO Metadata Engine)
- **Role:** Normalizes heterogeneous OCR outputs, bounding boxes, text streams, and timestamps.
- **Inputs:** `ClassifiedEvidenceItem` from DETECT.
- **Transformations:**
  - Standardizes timestamps to ISO 8601 (`YYYY-MM-DDTHH:mm:ssZ`).
  - Normalizes monetary values to 2 decimal places (`float`).
  - Extracts and trims Thai receiver/sender names and bank account numbers.
  - Preserves OCR bounding boxes (`x, y, w, h`).
- **Output:** `NormalizedEvidenceRecord`.

### 2.3 Module 3: `task2_staging_buffer.py` (Staging Buffer & Event-Driven KPI Calculator)
- **Role:** Staging buffer manager maintaining live state and computing event-driven metrics.
- **Lifecycle States:** `EMPTY` ➔ `INGESTION` ➔ `CONFIRMED` ➔ `AUDITED`.
- **KPI Metrics:**
  - `chats_count`: Total chat screens/pages.
  - `slips_found`: Total slips detected.
  - `slips_confirmed`: Deduplicated and verified slips.
  - `net_amount`: Total financial damages reconciled.
- **Output:** `BufferStateSnapshot`.

### 2.4 Module 4: `task3_recipient_poi.py` (Slip Recipient Aggregator & Target POI Selector)
- **Role:** Aggregates bank slip recipients and categorizes persons of interest (POI).
- **Functionality:**
  - Groups slips by receiver name and bank/promptpay.
  - Identifies "Whale" / Primary POI (highest volume/amount).
  - Categorizes secondary recipients and proxy accounts.
  - Filters POI-specific transaction ledger for indictment.
- **Output:** `RecipientPOISummary`.

### 2.5 Master Orchestrator: `master_pipeline_orchestrator.py`
- **Role:** Seamlessly chains all 9 stages:
  1. `DetectGateway.process()`
  2. `Task1FeatureNormalizer.process()`
  3. `Task2StagingBuffer.process()`
  4. `Task3RecipientSelector.process()`
  5. `Task4SixAgentsDeepAnalyzer.analyze()`
  6. `LockedTask5PureSlipSOTEngine.reconcile()`
  7. `LockedTask7EvidenceTableEngine.build_table()`
  8. `Task8CourtDossierAssembler.assemble()`
  9. `Task9VaultExporter.export()`
- **Output Manifest:** Produces `MASTER_PIPELINE_OUTPUT.json` consumed by Web UI (`index.html`) Canvas A4 and Ledger tabs.

---

## 3. Data Integrity & Invariants
1. **Zero State Drift:** Execution is 100% deterministic given identical input bytes.
2. **Frozen Agents:** `agent1_*.py` through `agent6_*.py` remain completely untouched (frozen).
3. **Chain of Custody:** Every record carries immutable SHA-256 and ISO/IEC 27037 compliant audit timestamps.
4. **Production Parity:** All tests in `test_master_e2e_detect_to_task9.py` must pass using the real production classes instead of inline mocks.

---

## 4. Web UI Synchronization
`index.html` receives real data generated from `MASTER_PIPELINE_OUTPUT.json`:
- Stepper updates to Step 2 & Step 3.
- Dicut_Chat 807x1115 A4 Canvas renders actual sliced chat pages.
- Status capsule reflects confirmed slips and net total amount.
- Quick summary cards populate with real recipient and timeline metrics.

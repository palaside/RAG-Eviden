# DETECT to TASK 9 Production Pipeline Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Implement standalone production Python engines for DETECT, TASK 1, TASK 2, and TASK 3, connect them to existing TASKS 4-9 via a master pipeline orchestrator, and synchronize live evidence data into the Web UI (`index.html`).

**Architecture:** A clean modular forensic architecture based on ISO/IEC 27037 standards where raw evidence flows through deterministic invariant stages: Image Classification (DETECT) ➔ Feature Normalization (TASK 1) ➔ Staging Buffer & KPIs (TASK 2) ➔ Recipient & POI Analysis (TASK 3) ➔ 6-Agent Timeline Analysis (TASK 4) ➔ Pure Slip SOT (TASK 5) ➔ 11-Col Evidence Table (TASK 7) ➔ Court Dossier (TASK 8) ➔ Vault SFX Packaging (TASK 9).

**Tech Stack:** Python 3.10+, SHA-256, OpenCV, Pytesseract, unittest, Node.js HTTP server, Tailwind/Glassmorphism Web UI.

## Global Constraints
- Preserve frozen agents (`agent1_*.py` through `agent6_*.py`) without modifying a single line.
- Maintain 100% deterministic execution and strict ISO/IEC 27037 Chain of Custody hashes.
- Real production modules only — no inline mock classes in `test_master_e2e_detect_to_task9.py`.
- No alert() popups or blocking UI dialogs in Web UI; adhere strictly to Non-blocking Event-Driven Toasts.

---

### Task 1: `detect_gateway.py` (Forensic Image Intake & Classification Gateway)

**Files:**
- Create: `detect_gateway.py`
- Test: `tests/test_detect_gateway.py`

**Interfaces:**
- Consumes: Raw image file paths or image bytes, aspect ratios, optional dialogue texts.
- Produces: `ClassifiedEvidenceItem` with `file_id`, `name`, `type` (`TYPE_CHAT`, `TYPE_SLIP_SOLO`, `TYPE_CHAT_WITH_SLIP`, `TYPE_UNKNOWN`), `sha256`, `aspect_ratio`.

- [ ] **Step 1: Write failing test in `tests/test_detect_gateway.py`**
- [ ] **Step 2: Run test to confirm it fails**
- [ ] **Step 3: Implement `detect_gateway.py`**
- [ ] **Step 4: Run test to verify it passes**
- [ ] **Step 5: Git commit task 1**

---

### Task 2: `task1_feature_normalization.py` (Feature Normalization & ISO Metadata Engine)

**Files:**
- Create: `task1_feature_normalization.py`
- Test: `tests/test_task1_feature_normalization.py`

**Interfaces:**
- Consumes: `ClassifiedEvidenceItem` from `detect_gateway.py`.
- Produces: `NormalizedEvidenceRecord` standardizing ISO timestamps, monetary amounts, receiver/sender accounts, OCR bounding boxes.

- [ ] **Step 1: Write failing test in `tests/test_task1_feature_normalization.py`**
- [ ] **Step 2: Run test to confirm it fails**
- [ ] **Step 3: Implement `task1_feature_normalization.py`**
- [ ] **Step 4: Run test to verify it passes**
- [ ] **Step 5: Git commit task 2**

---

### Task 3: `task2_staging_buffer.py` (Staging Buffer & Event-Driven KPI Calculator)

**Files:**
- Create: `task2_staging_buffer.py`
- Test: `tests/test_task2_staging_buffer.py`

**Interfaces:**
- Consumes: List of `NormalizedEvidenceRecord`.
- Produces: `BufferStateSnapshot` with states `EMPTY`, `INGESTION`, `CONFIRMED`, `AUDITED`, and live KPI string format: `📷 แชท X หน้า | 🧾 สลิป พบ Y · ยืนยัน Z รายการ`.

- [ ] **Step 1: Write failing test in `tests/test_task2_staging_buffer.py`**
- [ ] **Step 2: Run test to confirm it fails**
- [ ] **Step 3: Implement `task2_staging_buffer.py`**
- [ ] **Step 4: Run test to verify it passes**
- [ ] **Step 5: Git commit task 3**

---

### Task 4: `task3_recipient_poi.py` (Slip Recipient Aggregator & Target POI Selector)

**Files:**
- Create: `task3_recipient_poi.py`
- Test: `tests/test_task3_recipient_poi.py`

**Interfaces:**
- Consumes: Reconciled records from `task2_staging_buffer.py`.
- Produces: `RecipientPOISummary` mapping receiver names to transaction counts, total amounts, identified "Whale" / Primary POI, and filtered target transactions.

- [ ] **Step 1: Write failing test in `tests/test_task3_recipient_poi.py`**
- [ ] **Step 2: Run test to confirm it fails**
- [ ] **Step 3: Implement `task3_recipient_poi.py`**
- [ ] **Step 4: Run test to verify it passes**
- [ ] **Step 5: Git commit task 4**

---

### Task 5: `master_pipeline_orchestrator.py` (End-to-End Orchestrator)

**Files:**
- Create: `master_pipeline_orchestrator.py`
- Test: `tests/test_master_pipeline_orchestrator.py`

**Interfaces:**
- Consumes: Raw dataset or folder of evidence files.
- Produces: Executes DETECT ➔ TASK 1 ➔ TASK 2 ➔ TASK 3 ➔ TASK 4 ➔ TASK 5 ➔ TASK 7 ➔ TASK 8 ➔ TASK 9, writing `MASTER_PIPELINE_OUTPUT.json`.

- [ ] **Step 1: Write failing test for orchestrator execution**
- [ ] **Step 2: Run test to confirm it fails**
- [ ] **Step 3: Implement `master_pipeline_orchestrator.py`**
- [ ] **Step 4: Run test to verify all 9 tasks chain cleanly**
- [ ] **Step 5: Git commit task 5**

---

### Task 6: Refactor `test_master_e2e_detect_to_task9.py` to Production Parity

**Files:**
- Modify: `test_master_e2e_detect_to_task9.py`

**Interfaces:**
- Consumes: Production classes `DetectGateway`, `Task1FeatureNormalizer`, `Task2StagingBuffer`, `Task3RecipientSelector`.
- Produces: Full passing suite across 10 E2E tests using real production modules without inline mocks.

- [ ] **Step 1: Update `test_master_e2e_detect_to_task9.py` imports and tests 1, 2, 3**
- [ ] **Step 2: Run `python test_master_e2e_detect_to_task9.py`**
- [ ] **Step 3: Confirm 10/10 tests pass with zero regression**
- [ ] **Step 4: Git commit task 6**

---

### Task 7: Synchronize Web UI (`index.html`) with Real Pipeline Output

**Files:**
- Modify: `index.html`

**Interfaces:**
- Consumes: `MASTER_PIPELINE_OUTPUT.json`.
- Produces: Web UI displays verified real data on Canvas A4, Recipient Ledger, Status Capsule, and Stepper without mock data.

- [ ] **Step 1: Update `index.html` to load and bind `MASTER_PIPELINE_OUTPUT.json`**
- [ ] **Step 2: Verify in browser via Chrome DevTools MCP and take screenshot**
- [ ] **Step 3: Git commit task 7**

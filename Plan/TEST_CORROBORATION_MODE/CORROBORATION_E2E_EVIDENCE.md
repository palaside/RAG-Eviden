# CORROBORATION MODE: E2E SHIFT-LEFT & DATA-DRIVEN PIPELINE EVIDENCE
**ระบบทดสอบโหมดตรวจสอบความเชื่อมโยง (Corroboration & Linkage Verification System - 7 ขั้นตอน)**  
*อ้างอิงเอกสารข้อกำหนด:* `ความเชื่อมโยง.txt` (Intake Separation, Comparison Extraction, Candidate Matching, Dual-Sided Links, Non-Forced User Verification, and Reversible SSOT)

---

## 1. ภาพหลักฐานผลลัพธ์การประมวลผล (Visual Proof of Execution)

หลักฐานภาพถ่ายการรัน Data-Driven Workflow Pipeline ที่เชื่อมโยงระหว่าง **ข้อความสั่งโอนเงินในหน้าแชท (Chat Node)** และ **สลิปโอนเงินจริง (Slip Node)** พร้อมเรนเดอร์ UI ฝั่งซ้าย-ขวา (Dual Comparison View) แสดงสถานะ `USER_CONFIRMED` และความสามารถในการ Reversible สองทิศทาง:

![Corroboration Pipeline Visual Proof](file:///C:/Users/EVE/.gemini/antigravity/brain/c8211d09-030e-4b24-8837-3ce9589aa4a6/corroboration_pipeline_visual_proof.jpg)

---

## 2. ผลการทดสอบข้อ 1: E2E SHIFT-LEFT TESTING & CONTRACT VALIDATION PROTOCOL

ทดสอบผ่านสคริปต์ [run_corroboration_shift_left.py](file:///d:/Project/ชวกม.2/Plan/TEST_CORROBORATION_MODE/run_corroboration_shift_left.py) เพื่อคุมสัญญาข้อมูล (Data Contracts) 7 ขั้นตอน:

| ขั้นตอนตามข้อกำหนด | สัญญาข้อมูล (Contract Name) | ผลการทดสอบ (Status) | รายละเอียดการรับประกัน (Safeguards) |
| :--- | :--- | :--- | :--- |
| **ขั้นตอนที่ 1 & 2** | `ModeSeparationContract` | `[PASS] 100%` | ตรวจสอบ Intake แยกไฟล์ `MODE_CHAT` และ `MODE_SLIP` ชัดเจน ไม่ปะปนกัน |
| **ขั้นตอนที่ 3** | `ComparisonItemContract` | `[PASS] 100%` | สกัดเฉพาะข้อเท็จจริง (`is_raw_fact=True`) ห้าม AI อนุมานหรือสร้างข้อมูลเท็จ |
| **ขั้นตอนที่ 4 & 5** | `CandidateLinkageContract` | `[PASS] 100%` | ตรวจจับคู่ความเชื่อมโยงเป็น "จุดที่ควรเปิดดู" (`REVIEW_REQUIRED`) พร้อม Trap ป้องกัน Auto-confirm |
| **Boundary Trap** | `Boundary Limit Interceptor` | `[PASS (TRAPPED)]` | ดักจับกรณีจำลองโมเดล AI พยายาม Confirm เองโดยไม่ผ่านมนุษย์ ล็อกเป็น Error ทันที |
| **ขั้นตอนที่ 6** | `UserVerificationContract` | `[PASS] 100%` | ตรวจสอบการตัดสินใจของมนุษย์ รองรับ `KEEP_REVIEW_REQUIRED` ไม่บังคับเลือก |
| **ขั้นตอนที่ 7** | `DualSidedReversibilityContract` | `[PASS] 100%` | พิสูจน์การย้อนกลับได้ 2 ฝั่ง (Reversible) ทั้งฝั่งแชทและสลิป อิง BBox + SHA-256 |

---

## 3. ผลการทดลองข้อ 2: DATA-DRIVEN WORKFLOW PIPELINES

ทดสอบผ่านสคริปต์ [run_corroboration_data_driven_pipeline.py](file:///d:/Project/ชวกม.2/Plan/TEST_CORROBORATION_MODE/run_corroboration_data_driven_pipeline.py) รันข้อมูลพยานหลักฐานจริงจาก `แชทที่ 3`:

### 3.1 บันทึกสายพานข้อมูล (Pipeline Step-by-Step Trajectory)
1. **Intake & Hashing:**
   - Chat Source: `chatv3 (1).jpg` | SHA-256: `38bb247ba1f36402484439c4456956799042a9b40023a1f94537160cb7ce1464` | Laplacian: `681.00`
   - Slip Source: `slip_1500_kbank.jpg` | SHA-256: `54a638fca69cd4e073c66da6696fa049b49fce8fcae74ad05fb25b119a0a19fa` | Ref ID: `N006728230107019953913698`
2. **Extraction & Node Mapping:**
   - Chat Node (`CHAT_NODE_01`): สกัดข้อความ *"โอนเข้าบัญชีนี้นะ 1,500 บาท"* เวลา 13:53 น.
   - Slip Node (`SLIP_NODE_01`): สกัดยอดเงิน `1,500.00 THB` เวลา 14:15:22 น.
3. **Candidate Matching (จุดที่ควรเปิดดู):**
   - ตรวจพบความสัมพันธ์: ยอดเงินตรงกัน (1,500 บาท) และเวลาห่างกัน 22 นาที (อยู่ในหน้าต่าง 60 นาที)
   - สถานะเริ่มต้น: `REVIEW_REQUIRED` (ห้ามระบบสรุปเอง)
4. **Human-in-the-Loop Verification:**
   - มนุษย์ตรวจสอบหน้าต่างเปรียบเทียบซ้าย-ขวา และกดบันทึกยืนยันความเชื่อมโยง
   - สถานะเปลี่ยนเป็น: `USER_CONFIRMED`
5. **Reversible SSOT & Provenance Ledger Generation:**
   - บันทึกเข้า [CORROBORATION_LEAN_SSOT.json](file:///d:/Project/ชวกม.2/Plan/TEST_CORROBORATION_MODE/CORROBORATION_LEAN_SSOT.json)
   - บันทึกห่วงโซ่พยานเข้า [CORROBORATION_PROVENANCE_LEDGER.json](file:///d:/Project/ชวกม.2/Plan/TEST_CORROBORATION_MODE/CORROBORATION_PROVENANCE_LEDGER.json)

---

## 4. ตารางพิสูจน์การย้อนกลับได้แบบสองฝั่ง 100% (Dual-Sided Reversibility Traceability Matrix)

| Entity / Node ID | ด้านที่ 1: พิกัดแชทย้อนกลับ (Chat Traceability) | ด้านที่ 2: พิกัดสลิปย้อนกลับ (Slip Traceability) | สถานะความถูกต้อง |
| :--- | :--- | :--- | :---: |
| **CORROB_LINK_001** | **File:** `chatv3 (1).jpg`<br>**SHA-256:** `38bb247ba1f3...`<br>**Y-Range:** `[1420 - 1650]` px<br>**Text:** *"โอนเข้าบัญชีนี้นะ 1,500 บาท"* | **File:** `slip_1500_kbank.jpg`<br>**SHA-256:** `54a638fc...`<br>**Ref ID:** `N006728230107019953913698`<br>**Amount:** `1,500.00 THB` | `VERIFIED 100% REVERSIBLE` |

---

## 5. แหล่งไฟล์ที่สร้างขึ้นและเครื่องมือ Interactive Viewer
- **Interactive UI Dashboard:** [CORROBORATION_DATA_DRIVEN_VIEWER.html](file:///d:/Project/ชวกม.2/Plan/TEST_CORROBORATION_MODE/CORROBORATION_DATA_DRIVEN_VIEWER.html)
- **สัญญาระบบ (Contracts):** [CORROBORATION_CONTRACTS.py](file:///d:/Project/ชวกม.2/Plan/TEST_CORROBORATION_MODE/CORROBORATION_CONTRACTS.py)
- **Shift-Left Test Suite:** [run_corroboration_shift_left.py](file:///d:/Project/ชวกม.2/Plan/TEST_CORROBORATION_MODE/run_corroboration_shift_left.py)
- **Data-Driven Pipeline Runner:** [run_corroboration_data_driven_pipeline.py](file:///d:/Project/ชวกม.2/Plan/TEST_CORROBORATION_MODE/run_corroboration_data_driven_pipeline.py)
- **Lean SSOT Database:** [CORROBORATION_LEAN_SSOT.json](file:///d:/Project/ชวกม.2/Plan/TEST_CORROBORATION_MODE/CORROBORATION_LEAN_SSOT.json)

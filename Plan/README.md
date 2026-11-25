# 📋 ศูนย์บัญชาการแผนงาน (Plan Management Hub)

โฟลเดอร์นี้จัดทำขึ้นเพื่อเก็บรวบรวม **"แผนงาน (Plans)"** อย่างเป็นระบบตามลำดับเหตุการณ์และหัวข้อที่ผู้ใช้ชี้นำ 
โดยจะไม่มีการแตะต้องหรือกระทบกับระบบ **AGENTS 1 - 6** ที่ถูกฟรีซไว้เด็ดขาด

---

## 📌 กฎเกณฑ์และข้อตกลงในการทำงาน (Protocol)

1. **คำสั่งกระตุ้น (Trigger):**
   * เมื่อผู้ใช้พิมพ์คำว่า **"สร้างแผน"** หรือระบุหัวข้อที่ต้องการวางแผน
   * ระบบจะสร้างไฟล์แผนงานใหม่ตามลำดับเลข เช่น:
     * `PLAN_001_<ชื่อเรื่อง>.md`
     * `PLAN_002_<ชื่อเรื่อง>.md`

2. **โครงสร้างภายในของแต่ละไฟล์แผน (Plan Structure):**
   * **เป้าหมายหลัก (Objective):** วัตถุประสงค์ของงาน
   * **ขอบเขตและข้อจำกัด (Scope & Constraints):** สิ่งที่ต้องทำ และสิ่งที่ไม่ต้องทำ
   * **รายการงานที่ต้องทำ (To-Do List / Progress Tracking):**
     * `[ ]` งานที่รอดำเนินการ (Pending)
     * `[x]` ✅ งานที่ทำเสร็จแล้ว (Completed)
   * **บันทึกผลการปฏิบัติและการตรวจสอบ (Verification Log):** หลักฐานหรือบันทึกเมื่อทำงานเสร็จ

---

## 📑 สารบัญแผนงานทั้งหมด (Plan Index)

| รหัสแผน | ชื่อแผนงาน | วันที่สร้าง | สถานะ | ความคืบหน้า | ลิงก์ไฟล์ |
| :---: | :--- | :---: | :---: | :---: | :---: |
| `PLAN-001` | สถาปัตยกรรมการแสดงผลภาพผสมผสาน 2 เลเยอร์ (WebP + Vector Overlay) | 22 พ.ย. 2026 | 🟡 วางสเปกแล้ว | 2/9 (22%) | [PLAN_001_HYBRID_TWO_LAYER_ARCHITECTURE.md](file:///d:/Project/ชวกม.2/Plan/PLAN_001_HYBRID_TWO_LAYER_ARCHITECTURE.md) |
| `PLAN-002` | มาตรการตรวจจับและคัดกรองหลักฐานซ้ำซ้อน 4 ชั้น (4-Tier Forensic Deduplication) | 22 พ.ย. 2026 | 🟡 วางสเปกแล้ว | 1/8 (12%) | [PLAN_002_4_TIER_DEDUPLICATION_ENGINE.md](file:///d:/Project/ชวกม.2/Plan/PLAN_002_4_TIER_DEDUPLICATION_ENGINE.md) |
| `PLAN-003` | สถาปัตยกรรมไฮบริดปะติดปะต่อภาพแชทเส้นเดียว 4 ขั้นตอน (Unified Hybrid Long-Scroll) | 22 พ.ย. 2026 | 🟡 วางสเปกแล้ว | 1/10 (10%) | [PLAN_003_HYBRID_STITCH_ENGINE_4_STAGES.md](file:///d:/Project/ชวกม.2/Plan/PLAN_003_HYBRID_STITCH_ENGINE_4_STAGES.md) |
| `PLAN-004` | ระบบตรวจสอบและคัดกรองคุณภาพภาพพยานหลักฐาน (Image Quality Gatekeeper) | 22 พ.ย. 2026 | 🟡 วางสเปกแล้ว | 1/7 (14%) | [PLAN_004_IMAGE_QUALITY_GATEKEEPER.md](file:///d:/Project/ชวกม.2/Plan/PLAN_004_IMAGE_QUALITY_GATEKEEPER.md) |
| `PLAN-005` | แคชผลลัพธ์ OCR ถาวรผูกกับค่าแฮช SHA-256 (Immutable SHA-256 OCR Cache Engine) | 22 พ.ย. 2026 | 🟡 วางสเปกแล้ว | 1/7 (14%) | [PLAN_005_IMMUTABLE_SHA256_OCR_CACHE.md](file:///d:/Project/ชวกม.2/Plan/PLAN_005_IMMUTABLE_SHA256_OCR_CACHE.md) |
| `PLAN-006` | ดัชนีค้นหาด่วนบนหน้าเว็บ (Client-Side Inverted Index & Instant Search) | 22 พ.ย. 2026 | 🟡 วางสเปกแล้ว | 1/7 (14%) | [PLAN_006_CLIENT_SIDE_INSTANT_SEARCH_INDEX.md](file:///d:/Project/ชวกม.2/Plan/PLAN_006_CLIENT_SIDE_INSTANT_SEARCH_INDEX.md) |
| `PLAN-007` | โครงสร้างข้อมูลไม่บวมระดับศูนย์กลาง (Normalized Lean SSOT Data Model) | 22 พ.ย. 2026 | 🟡 วางสเปกแล้ว | 1/7 (14%) | [PLAN_007_NORMALIZED_LEAN_SSOT_DATA_MODEL.md](file:///d:/Project/ชวกม.2/Plan/PLAN_007_NORMALIZED_LEAN_SSOT_DATA_MODEL.md) |
| `PLAN-008` | ระบบพกพาเปิดในชั้นศาลแบบออฟไลน์ 100% (Offline-First Court Standalone Bundle) | 22 พ.ย. 2026 | 🟡 วางสเปกแล้ว | 1/7 (14%) | [PLAN_008_OFFLINE_FIRST_COURT_STANDALONE.md](file:///d:/Project/ชวกม.2/Plan/PLAN_008_OFFLINE_FIRST_COURT_STANDALONE.md) |
| `PLAN-009` | กลไกพิสูจน์การเชื่อมต่อภาพแชทไร้ข้อผิดพลาด 4 ชั้น และระบบจัดเรียง DAG อัตโนมัติ | 22 พ.ย. 2026 | 🟡 วางสเปกแล้ว | 1/9 (11%) | [PLAN_009_ZERO_ERROR_CHAT_STITCH_ALIGNMENT.md](file:///d:/Project/ชวกม.2/Plan/PLAN_009_ZERO_ERROR_CHAT_STITCH_ALIGNMENT.md) |
| `PLAN-010` | มาตรฐานนิติวิทยาศาสตร์สากลในการตรวจสอบชื่อไฟล์และไทม์แสตมป์ (Zero-Trust Metadata) | 22 พ.ย. 2026 | 🟡 วางสเปกแล้ว | 1/8 (12%) | [PLAN_010_ZERO_TRUST_METADATA_FORENSIC_STANDARDS.md](file:///d:/Project/ชวกม.2/Plan/PLAN_010_ZERO_TRUST_METADATA_FORENSIC_STANDARDS.md) |

---

## 🧪 การทดสอบ E2E Shift-Left Testing & Data Contract Validation

สายพานข้อมูลทั้ง 5 Phase (10 แผน) ได้รับการทดสอบรับรองสัญญาข้อมูลและประกอบชิ้นส่วนแบบ Shift-Left เรียบร้อยแล้ว 100%:
- 📄 **รายงานผลการทดสอบอย่างเป็นทางการ:** [SHIFT_LEFT_E2E_VERIFICATION_REPORT.md](file:///d:/Project/ชวกม.2/Plan/E2E_SHIFT_LEFT_TESTING/SHIFT_LEFT_E2E_VERIFICATION_REPORT.md)
- 📝 **บันทึกเหตุการณ์กลาง (Centralized Events):** [centralized_events.jsonl](file:///d:/Project/ชวกม.2/Plan/E2E_SHIFT_LEFT_TESTING/centralized_events.jsonl)
- ⚙️ **รหัสสัญญาและตัวตรวจจับ (Contracts & Harness):** [CONTRACTS.py](file:///d:/Project/ชวกม.2/Plan/E2E_SHIFT_LEFT_TESTING/CONTRACTS.py) / [run_shift_left_e2e.py](file:///d:/Project/ชวกม.2/Plan/E2E_SHIFT_LEFT_TESTING/run_shift_left_e2e.py)
- **สถานะ:** 🟢 **ALL 9 TEST GATES PASSED (100% PRODUCTION READY)**

---

## 🚀 การทดลองรันสายพานข้อมูลจริง (Data-Driven Workflow Pipeline Execution)

ระบบสายพานข้อมูล Phase 1 ถึง Phase 5 ถูกจำลองและรันประมวลผลจริงแบบ End-to-End ครบวงจร:
- 📄 **รายงานผลการรันไปป์ไลน์:** [PIPELINE_EXECUTION_REPORT.md](file:///d:/Project/ชวกม.2/Plan/DATA_DRIVEN_PIPELINE/PIPELINE_EXECUTION_REPORT.md)
- 🖥️ **หน้าจอรีวิวศาล (Interactive Preview):** [output_court_preview.html](file:///d:/Project/ชวกม.2/Plan/DATA_DRIVEN_PIPELINE/output_court_preview.html)
- 🗄️ **ฐานข้อมูล Lean SSOT (1.7KB):** [output_lean_ssot.json](file:///d:/Project/ชวกม.2/Plan/DATA_DRIVEN_PIPELINE/output_lean_ssot.json)
- 🔍 **สารบัญดัชนีคำค้น (Inverted Index):** [output_inverted_index.json](file:///d:/Project/ชวกม.2/Plan/DATA_DRIVEN_PIPELINE/output_inverted_index.json)
- 📄 **พิมพ์เขียวรอยต่อภาพ (Stitch Manifest):** [output_stitch_manifest.json](file:///d:/Project/ชวกม.2/Plan/DATA_DRIVEN_PIPELINE/output_stitch_manifest.json)
- ⚙️ **สคริปต์ไปป์ไลน์:** [pipeline_runner.py](file:///d:/Project/ชวกม.2/Plan/DATA_DRIVEN_PIPELINE/pipeline_runner.py)

---

## 🎴 การทดสอบชุดใหม่: กระบวนการนำเข้าสู่การ์ดทั้ง 4 (4-Cards Workflow)

ทดสอบขั้นตอน 1 ถึง 10 ตามสเปกผู้ใช้ (อัปโหลด ➔ แยกโหมด ➔ ตรวจจับ ➔ เก็บผลพร้อมที่มา ➔ การ์ด 4 ใบ ➔ ตรวจสอบย้อนกลับ):
- 📄 **รายงานผลการรันไปป์ไลน์การ์ดทั้ง 4 ใบ (พร้อมภาพ):** [FOUR_CARDS_DATA_DRIVEN_PIPELINE_EVIDENCE.md](file:///C:/Users/EVE/.gemini/antigravity/brain/c8211d09-030e-4b24-8837-3ce9589aa4a6/FOUR_CARDS_DATA_DRIVEN_PIPELINE_EVIDENCE.md)
- 🖥️ **หน้าจอแดชบอร์ดรีวิวศาล (Data-Driven 4 Cards):** [FOUR_CARDS_DATA_DRIVEN_VIEWER.html](file:///d:/Project/ชวกม.2/Plan/DATA_DRIVEN_PIPELINE/FOUR_CARDS_DATA_DRIVEN_VIEWER.html)
- 🗄️ **ฐานข้อมูล Lean SSOT (4.1 KB):** [FOUR_CARDS_LEAN_SSOT.json](file:///d:/Project/ชวกม.2/Plan/DATA_DRIVEN_PIPELINE/FOUR_CARDS_LEAN_SSOT.json)
- 📑 **บัญชีตามรอยย้อนกลับ (Provenance Ledger):** [FOUR_CARDS_PROVENANCE_LEDGER.json](file:///d:/Project/ชวกม.2/Plan/DATA_DRIVEN_PIPELINE/FOUR_CARDS_PROVENANCE_LEDGER.json)
- 📸 **ภาพผลลัพธ์การ์ดทั้ง 4 ใบพร้อมหลักฐานจริง:** [four_cards_pipeline_visual_proof.jpg](file:///C:/Users/EVE/.gemini/antigravity/brain/c8211d09-030e-4b24-8837-3ce9589aa4a6/four_cards_pipeline_visual_proof.jpg)
- ⚙️ **สคริปต์ไปป์ไลน์:** [run_4_cards_data_driven_pipeline.py](file:///d:/Project/ชวกม.2/Plan/DATA_DRIVEN_PIPELINE/run_4_cards_data_driven_pipeline.py)

---

## 🏛️ การทดสอบ Shift-Left กับชุดข้อมูลจริง (แชทที่ 3)

นำไฟล์ภาพพยานหลักฐานจริงจากโฟลเดอร์ `FOR TEST In EDOK_NUI\แชทที่ 3` มาเข้าสู่กระบวนการ Phase 1 - 5 ครบวงจร พร้อมตารางตามรอยย้อนกลับ (Provenance Traceability) และหลักฐานภาพจริง:
- 📄 **รายงานผลการทดสอบพยานหลักฐานจริง (พร้อมภาพ):** [CHAT_V3_E2E_SHIFT_LEFT_EVIDENCE.md](file:///C:/Users/EVE/.gemini/antigravity/brain/c8211d09-030e-4b24-8837-3ce9589aa4a6/CHAT_V3_E2E_SHIFT_LEFT_EVIDENCE.md)
- 🖥️ **หน้าจอแดชบอร์ดรีวิวศาล (แชทที่ 3):** [CHAT_V3_COURT_DASHBOARD.html](file:///d:/Project/ชวกม.2/Plan/E2E_SHIFT_LEFT_TESTING/CHAT_V3_COURT_DASHBOARD.html)
- 🗄️ **ฐานข้อมูล Lean SSOT (แชทที่ 3):** [CHATV3_LEAN_SSOT.json](file:///d:/Project/ชวกม.2/Plan/E2E_SHIFT_LEFT_TESTING/CHATV3_LEAN_SSOT.json)
- 📸 **ภาพพยานหลักฐานจริงพร้อมกรอบสีแดง:** [chatv3_1_visual_proof.jpg](file:///C:/Users/EVE/.gemini/antigravity/brain/c8211d09-030e-4b24-8837-3ce9589aa4a6/chatv3_1_visual_proof.jpg)
- ⚙️ **สคริปต์รันการทดสอบแชทที่ 3:** [run_test_chat_v3.py](file:///d:/Project/ชวกม.2/Plan/E2E_SHIFT_LEFT_TESTING/run_test_chat_v3.py)

---
*หมายเหตุ: เมื่อใดที่งานใน To-Do List ได้รับการปฏิบัติเสร็จสิ้น ระบบจะทำการอัปเดตเครื่องหมาย `[x]` และ `✅` พร้อมระบุวันเวลาที่แล้วเสร็จโดยอัตโนมัติ*

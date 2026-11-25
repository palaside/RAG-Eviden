---
name: Driven_Workflow_Pipelines
description: สกิลขับเคลื่อนและควบคุมสายพานข้อมูลพยานหลักฐาน 5 ขั้นตอน (5-Phase Data-Driven Workflow Pipelines Engine) จัดการการไหลของข้อมูลหลักฐานดิจิทัลคดีอาญาอย่างเป็นระบบ ตั้งแต่คัดกรองภาพ, แคช OCR ถาวร, คำนวณพิกัดสะสม Y_cumulative, สรุป Lean SSOT, จนถึงสร้างแพ็กเกจออฟไลน์ส่งศาล พร้อมคุมกฎเหล็ก Strict Grounding และ Dual-Sided Reversibility 100%
---

# ⚡ DRIVEN WORKFLOW PIPELINES (Data-Driven Workflow Execution Engine)
## สกิลควบคุมและขับเคลื่อนสายพานข้อมูลพยานหลักฐานดิจิทัลคดีอาญา 5 เฟส

> **Role & Core Mandate:**  
> คุณคือ **Chief Data Pipeline Architect & Forensic Workflow Lead**  
> ภารกิจของคุณคือขับเคลื่อนและควบคุม **Data-Driven Workflow Pipelines (5-Phase Pipeline)** เพื่อเปลี่ยนกองพยานหลักฐานดิจิทัลดิบ (ภาพแชทขนาดยาวนับพันภาพ และสลิปการเงิน) ให้ไหลผ่านสายพานข้อมูลที่ทำงานบน **ข้อมูลจริง (Data-Driven Determinism)** ทุกย่างก้าวต้องถูกขับเคลื่อนด้วยพยานหลักฐาน ไร้การคาดเดา ไร้ความหลอน (Zero Hallucination) และย้อนกลับได้สองทิศทาง 100%

---

## 🔄 สถาปัตยกรรมสายพานข้อมูล 5 เฟส (The 5-Phase Data-Driven Pipeline)

```mermaid
flowchart TD
    subgraph Phase1["PHASE 1: Intake & Forensic Gatekeeping"]
        RAW["ภาพหลักฐานดิบ (แชท / สลิป)"] --> G1["Quality Gate: Laplacian Blur Check (Var >= 100)"]
        G1 --> G2["4-Tier Deduplication: SHA-256 / pHash / Slip Ref"]
        G2 --> G3["Zero-Trust Intake: Temporal Anchor & ELA Integrity"]
    end

    subgraph Phase2["PHASE 2: Single-Pass Processing & Immutable Caching"]
        G3 --> P1["Immutable OCR Cache: {sha256}.json (ดึงผลใน 0.001s)"]
        P1 --> P2["DAG Flow & Quiet Zone Slicing (ห้ามผ่าบับเบิ้ล)"]
    end

    subgraph Phase3["PHASE 3: Spatial Alignment & Coordinate Math"]
        P2 --> S1["Continuous Strip: คำนวณพิกัดสะสม Y_cumulative"]
        S1 --> S2["Dual-Layer Canvas: WebP Base + SVG Vector Overlay"]
    end

    subgraph Phase4["PHASE 4: Lean SSOT Normalization & Search Indexing"]
        S2 --> N1["Relational Lean SSOT: Persons / Accounts / Slips (1-2MB)"]
        N1 --> N2["Client-Side Inverted Search Index (< 5ms Query)"]
    end

    subgraph Phase5["PHASE 5: Air-Gapped Packaging & Court Presentation"]
        N2 --> C1["Single-File Standalone HTML Bundle (ไร้ CDN ไร้เน็ต)"]
        C1 --> C2["Print-to-Court A4 Engine & Dual-Sided Provenance Ledger"]
        C2 --> COURT["สำนวนพยานหลักฐานมาตรฐานศาล (Court Dossier)"]
    end
```

---

## 🛠️ รายละเอียดการทำงานของแต่ละเฟส (Phase-by-Phase Mechanics)

### เฟสที่ 1: Intake & Forensic Gatekeeping (คัดกรองและรักษาความบริสุทธิ์ของพยาน)
* **กลไก:**
  1. สแกนความคมชัดภาพด้วย **Laplacian Variance**: ค่าความแปรปรวนต้อง $\ge 100$ หากต่ำกว่าจะถูกดักจับและแจ้งเตือนภาพมัว/เสียทันที
  2. กรองไฟล์ซ้ำ **4 ระดับ**: Binary SHA-256 ➔ pHash ➔ Semantic Slip Key (ธนาคาร + วันเวลา + Ref ID) ➔ Chat Visual Overlap
  3. ปลดการพึ่งพาชื่อไฟล์ Windows โดยแปลงเป็น **Vault ID ผูกแฮช SHA-256** ถาวร

### เฟสที่ 2: Single-Pass Processing & Immutable Caching (ถอดรหัสและแคชถาวร)
* **กลไก:**
  1. รัน OCR แบบรอบเดียว (Single-Pass) และบันทึกผลลงแคชดิสก์ `{sha256}.json` ตัดวงจรการรันซ้ำซ้อน ประหยัดเวลา 99.9%
  2. วิเคราะห์ทิศทางการสนทนาด้วย **DAG (Directed Acyclic Graph)** เพื่อเรียงลำดับเวลาการคุยก่อน-หลัง
  3. ค้นหา **Quiet Zone (ช่องว่างสีพื้นหลัง)** เพื่อกรีดตัดแบ่งหน้าแชท ห้ามผ่ากลางบับเบิ้ลข้อความหรือสติกเกอร์เด็ดขาด

### เฟสที่ 3: Spatial Alignment & Coordinate Math (จัดวางพิกัดพื้นที่ 2 มิติ)
* **กลไก:**
  1. ปะติดปะต่อแชทขนาดยาวแบบ Virtual Scrolling โดยคำนวณพิกัดสะสมแนวดิ่ง:
     $$Y_{cumulative}^{(i)} = Y_{cumulative}^{(i-1)} + H_i - Overlap_i$$
  2. แยกการแสดงผลเป็น **Dual-Layer Architecture**:
     - *Layer 0 (Canvas Base):* ภาพ WebP แท้ ความละเอียดสูง ไม่ถูกแก้ไข
     - *Layer 1 (Vector Layer):* SVG Bounding Boxes (`pointer-events: none`) ซูมไม่แตก ไม่แย่งโฟกัสเมาส์

### เฟสที่ 4: Lean SSOT Normalization & Search Indexing (จัดโครงสร้างฐานข้อมูลและดัชนีสืบค้น)
* **กลไก:**
  1. ลดขนาดโครงสร้างข้อมูลจาก 50MB เหลือ 1–2MB ด้วย **Relational Lean SSOT** โดยแยกตารางความจริง:
     - `Persons`: บัญชีม้า, ตัวการหลัก, ผู้เสียหาย
     - `Accounts`: ธนาคาร, เลขบัญชี, พร้อมเพย์
     - `Slips`: สลิปโอนเงินจริง, ยอดเงิน, วันเวลา, Ref ID
     - `ChatNodes`: บับเบิ้ลข้อความสั่งโอนที่เชื่อมโยง
  2. สร้าง **Client-Side Inverted Search Index (50KB)** ทำงานใน RAM เบราว์เซอร์ ค้นหายอดเงินและคำสำคัญได้ใน $\le 5$ มิลลิวินาที

### เฟสที่ 5: Air-Gapped Packaging & Court Presentation (แพ็กเกจส่งมอบมาตรฐานศาล)
* **กลไก:**
  1. รวมโค้ด HTML, CSS, JavaScript และฐานข้อมูล JSON ให้เป็น **Single Standalone HTML Bundle** เปิดใช้งานบน Flash Drive ได้ 100% แม้อยู่ในโหมดเครื่องบิน (Air-Gapped)
  2. บังคับใช้ **Print-to-Court A4 Engine**: จัดสมดุลกึ่งกลางแนวดิ่ง (Vertical Middle Balance) รองรับวรรณยุกต์ไทยและตัวเลขไม่ตกขอบ
  3. ออก **Provenance Ledger**: ตารางห่วงโซ่พยานที่พิสูจน์การย้อนกลับได้แบบสองทิศทาง (Dual-Sided Reversibility) 100%

---

## ⚖️ กฎเหล็กควบคุมสายพาน (Pipeline Operational Safeguards)

1. **Zero-Mock Enforcement (ห้ามใช้ข้อมูลจำลอง):**
   - ทุกตัวเลข ทุกยอดเงิน ทุกเลขบัญชี ต้องถูกผลักดันจากข้อมูลจริงในภาพ (Data-Driven Only)
   - หากภาพใดไม่มีคำสั่งโอนเงิน ให้บันทึกเป็น `transfer_amount: null (NOT_FOUND)` และคงสถานะเป็น `UNMATCHED`
2. **Dual-Sided Reversibility Guarantee:**
   - ทุกสรุปรายการทางการเงิน (Financial Cards 1-4) หรือข้อต่อสู้ในศาล ต้องสามารถคลิกเพื่อกระโดดกลับไปยังพิกัดจริงบนภาพต้นฉบับได้ทันที
3. **Production Parity Compliance:**
   - สายพานต้องผ่านการทดสอบด้วยชุดทดสอบ E2E และออกภาพหลักฐานผลลัพธ์ (Composite Visual Proof) ทุกครั้งที่มีการประมวลผล

---

## 🚀 คำสั่งกระตุ้นการทำงาน (Skill Triggers)
* `"รัน Driven Workflow Pipelines บน [โฟลเดอร์]"`
* `"ประมวลผลข้อมูลผ่านสายพาน 5 เฟส"`
* `"สร้าง Lean SSOT และออกแพ็กเกจศาลด้วย Driven Workflow Pipelines"`

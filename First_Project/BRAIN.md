# 🧠 BRAIN.md — The Sovereign Cognitive Orchestrator & 7-Step Workflow Engine

> **System Authority:** Sovereign Cognitive Core & Master Orchestration Engine  
> **Operational Status:** ACTIVE — Bounded Execution & Zero-Drift Pipeline  
> **Cognitive Mindset:** God-Mode Analytic Reasoning & Forensic Critical Thinking  
> **Master Rule:** ทุกการทำงานของ AI ต้องเริ่มต้นและเดินตามสายพานในไฟล์นี้อย่างเคร่งครัด 100% ห้ามข้ามขั้นตอน ห้ามมโนออกนอกกรอบ

---

## 🗺️ แผนที่ระบบสมองกลรวม (The Cognitive Master Map)

ระบบสมองกลนี้ผูกโยง **4 คลังวิศวกรรมแม่บท** เข้าสู่ **สายพานการปฏิบัติการ 7 สเต็ป**:

```mermaid
flowchart TD
    subgraph Vaults["🏛️ 4 คลังวิศวกรรมแม่บท (The 4 Knowledge Vaults)"]
        V1["1. นโยบายและเกราะป้องกัน\n[ENGINEERING EXECUTION POLICY/]\n(Scope Lock, 4-Tier Evidence, Anti-Hallucination)"]
        V2["2. กลไกความคิดและการวนลูป\n[Framework Architecture/]\n(5 Pillars: Prompt, Context, Harness, Loop, Graph)"]
        V3["3. ดีไซน์และแม่พิมพ์หน้าจอ\n[SPECIFICATION TEMPLATE/]\n(360° Studio, Dual-Track <60ms, Tactical Tokens)"]
        V4["4. สถาปัตยกรรมและวงจรระบบ\n[structure/]\n(SDLC 5-in-1, Modular Monolith, DB Optimistic Lock)"]
    end

    subgraph Circuit["⚡ สายพาน 7 สเต็ป (The 7-Step Cognitive Circuit)"]
        S1["Step 1: Reverse Prompting (Grill-Me)\n🎯 สกิล: grilling"]
        S2["Step 2: Architecture Blueprint\n🧠 สกิล: brainstorming + SDD"]
        S3["Step 3: Task Breakdown & Lock\n📝 สกิล: writing-plans -> STATE.md"]
        S4["Step 4: Vertical Slice Execution\n💻 สกิล: TDD (1 Test : 1 Code)"]
        S5["Step 5: Self-Healing 5-Whys\n🩺 สกิล: systematic-debugging (Max 3 Loops)"]
        S6["Step 6: Integration Verification\n🔬 สกิล: verification + audit script"]
        S7["Step 7: Immortal State Freeze\n💾 สกิล: save-project-state"]

        S1 --> S2 --> S3 --> S4 --> S6 --> S7
        S4 -.->|Test Fails| S5 -.->|Surgical Fix| S4
    end

    V1 -.->|Enforce Rules| Circuit
    V2 -.->|Drive ReAct Loop| Circuit
    V3 -.->|Style & Layout Spec| Circuit
    V4 -.->|Architectural Foundation| Circuit
```

---

## 🚦 กฎเหล็กแห่งการเปลี่ยนสถานะ (Strict State Transition Gates)

> **คำสั่งบังคับสูงสุด:** AI ห้ามกระโดดข้ามสเต็ปใดสเต็ปหนึ่งโดยเด็ดขาด การจะผ่านจากสเต็ปหนึ่งไปสู่อีกสเต็ปหนึ่ง ต้องผ่านเกณฑ์ของ **Gate** นั้นๆ เสมอ

```text
GATE 1: ปิดการซักถามได้ก็ต่อเมื่อ "อุดรูรั่วครบ 4 มิติ" (Core, Data Flow, Tech Stack, Edge Cases)
GATE 2: เริ่มแตก Task ได้ก็ต่อเมื่อ "พิมพ์เขียวสถาปัตยกรรมผ่านการเห็นชอบร่วมกัน"
GATE 3: เริ่มเขียนโค้ดได้ก็ต่อเมื่อ "เซฟแผนลง STATE.md และล็อก Single Active Task แล้ว"
GATE 4: ส่งมอบโมดูลเดี่ยวได้ก็ต่อเมื่อ "Unit Test สีเขียว 100% (Exit Code 0)"
GATE 5: ปิดข้อผิดพลาดได้ก็ต่อเมื่อ "ขุดพบ Root Cause 5-Whys และวนลูปไม่เกิน 3 ครั้ง"
GATE 6: รวมระบบได้ก็ต่อเมื่อ "รัน npm run audit และ tsc --noEmit ผ่าน 100%"
GATE 7: จบเซสชันได้ก็ต่อเมื่อ "บันทึก LATEST_CHECKPOINT.md ครบถ้วน"
```

---

## 🔄 เจาะลึกสายพาน 7 สเต็ป (Step-by-Step Cognitive Execution)

### Step 1: Reverse Prompting (Grill-Me Mode)
* **Trigger:** เมื่อผู้ใช้บอกความต้องการสั้นๆ หรือไอเดียเริ่มต้น
* **Action:** สวมบทบาทเป็น **Lead Architect Interviewer (Grill-Me)** ซักถามผู้ใช้แบบเจาะลึก 4 เสาหลักตายตัว:
  1. **Core Functions & Out of Scope:** ระบบนี้แก้ปัญหาอะไร มีฟังก์ชันหลักอะไร และ**สิ่งใดที่ไม่ต้องมีเด็ดขาด** (เพื่อตัดโค้ดขยะ)
  2. **Workflow & Data Structure:** ลำดับการประมวลผล, ข้อมูลนำเข้า (Input), ข้อมูลส่งออก (Output รูปแบบไหน ขนาด A4 หรือ ZIP) และเงื่อนไขพิเศษ
  3. **Tech Stack & Security:** เลือกภาษา/เครื่องมืออะไร, มีฐานข้อมูลไหม (Neon Postgres), มี Cloud Storage ไหม (R2), ความปลอดภัยระดับใด
  4. **Error Handling & Edge Cases:** กรณีพิเศษรับมืออย่างไร, วนลูปไม่ผ่าน 3 ครั้งให้ทำอย่างไร, เกณฑ์วัดผลสมบูรณ์คืออะไร
* **Exit Criteria:** สรุปรายการคำตอบของผู้ใช้และขอการยืนยันก่อนก้าวไป Step 2

### Step 2: Architecture Blueprint Synthesis
* **Action:** นำข้อมูลจาก Step 1 มาจับคู่กับคลังความรู้แม่บท:
  - ใช้ **[structure/02_MODULAR_ARCHITECTURE.md](file:///d:/iAMor%20Family/structure/02_MODULAR_ARCHITECTURE.md)** กำหนดโครงสร้างโฟลเดอร์โมดูลแบบ Modular Monolith
  - ใช้ **[structure/05_GOD_MODE_DATABASE.md](file:///d:/iAMor%20Family/structure/05_GOD_MODE_DATABASE.md)** ออกแบบตาราง DB พร้อมเกราะ Optimistic Lock (`version`)
  - ใช้ **[SPECIFICATION TEMPLATE/](file:///d:/iAMor%20Family/SPECIFICATION%20TEMPLATE)** ออกแบบ UI Tokens (Radius $\le 4\text{px}$, 8-Point Spacing)
* **Exit Criteria:** ออกเอกสารพิมพ์เขียว `SYSTEM_BLUEPRINT.md` พร้อมผัง Mermaid ที่ชัดเจน

### Step 3: Task Decomposition & Scope Lock
* **Action:** แตกงานสถาปัตยกรรมออกเป็น **Atomic Vertical Slices**:
  - กำหนด `IN_SCOPE` และ `OUT_OF_SCOPE` ตามกฎของ **[ENGINEERING EXECUTION POLICY/](file:///d:/iAMor%20Family/ENGINEERING%20EXECUTION%20POLICY)**
  - ห้ามเขียนทับ Root Entry Points (`/`, `layout.tsx`, `middleware.ts`) โดยไม่ได้รับคำสั่ง
  - บันทึกงานทั้งหมดลงใน `STATE.md` และล็อกสถานะ **Single Active Task Lock** ทำทีละ 1 งาน

### Step 4: Vertical Slice Implementation (TDD)
* **Action:** ลงมือพัฒนาโค้ดตามวงจร `red_green`:
  - พัฒนาแบบ **`1 Test : 1 Implementation`** เสมอ
  - เขียนโค้ดกระชับ สั้น ตรงจุดที่สุดตามหลัก YAGNI (Minimal Surgical Diff)
  - ห้ามมีชนิดข้อมูล `any` เด็ดขาด (Strict Zero-Any Contract)
  - เมื่อดำเนินการถึง **50% ของแผนงาน** ต้องหยุดพักครึ่งทางเพื่อบีบอัดและคลีนโค้ดก่อนทำต่อ

### Step 5: Self-Healing Telemetry & Root Cause Analysis
* **Action:** เมื่อรันคำสั่งแล้วเกิดข้อผิดพลาด (Exit Code $\ne 0$):
  - ห้ามผลักภาระให้ผู้ใช้ (Failure Responsibility Invariant: Agent ต้องหา HOW แก้เอง 100%)
  - รันกระบวนการ **5-Whys RCA** ขุดหารากเหง้า ไม่แก้ปัญหาแบบปะผุตามอาการ (No Symptom Patching)
  - **Max 3 Loops Circuit Breaker:** หากพยายามแก้จุดเดิมครบ 3 รอบแล้วยังไม่ผ่าน **ต้องหยุดทำงานทันที (Halt Execution)** และส่งต่อให้ผู้ใช้ (`ESCALATE_HUMAN`) พร้อมรายงานสาเหตุเชิงลึกเพื่อป้องกัน Token Burn

### Step 6: Cross-Module Integration Verification
* **Action:** เมื่อทุกโมดูลเดี่ยวเสร็จสิ้น ให้รันการทดสอบสายพานเชื่อมโยง:
  - รันสคริปต์ตรวจนโยบาย: `npm run audit` (ตรวจ Dead Code & Scope Violations)
  - รันการตรวจสอบ Type: `npx tsc --noEmit` (ต้องได้ Exit Code 0)
  - รัน E2E Smoke Test เพื่อพิสูจน์ว่า Data Flow ตั้งแต่ต้นน้ำสู่ปลายน้ำส่งต่อข้อมูลกันได้สนิท ไร้ Handshake Gap

### Step 7: Immortal State Persistence
* **Action:** เมื่อผ่านการทดสอบ 100%:
  - อัปเดตเช็กลิสต์ใน `STATE.md` เป็น Complete
  - สรุปผลงานและประวัติศาสตร์การตัดสินใจลงใน `LATEST_CHECKPOINT.md`
  - พร้อมสำหรับการฟื้นคืนชีพในเซสชันถัดไปอย่างไร้รอยต่อ

---

## 🚫 บัญชีดำข้อห้ามขั้นวิกฤต (The Cognitive Blacklist)
1. **ห้ามออกไฟล์เกินขอบเขต:** ออกเฉพาะไฟล์ที่จำเป็นตามที่ตกลงใน Step 1 เท่านั้น ไม่แอบยัดไฟล์ตัวอย่างหรือไลบรารีส่วนเกิน
2. **ห้ามมโนพาทไฟล์:** ต้องสำรวจคลังโค้ดจริงก่อนเสมอ (`INSPECT BEFORE ACT`)
3. **ห้ามแสร้งทำเทสต์เขียว (No Test Theater):** ผลการทดสอบต้องมาจาก Terminal Execution ที่มี Exit Code 0 เท่านั้น
4. **ห้ามเออออตามผู้ใช้หากผิดหลักวิศวกรรม (Zero Sycophancy):** กล้าค้านและชี้แจงด้วยหลักฐานทางเทคนิคเสมอตามจิตวิญญาณของ [SOVEREIGN.md](file:///d:/iAMor%20Family/SOVEREIGN.md)


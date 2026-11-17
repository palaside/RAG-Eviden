# 🛡️ First_Project — Universal Production-Ready Full-Stack & AI Governance Framework

> **Standard:** Enterprise Production-Ready Universal Suite (Full-Stack + Agentic Governance)  
> **Tech Stack:** Next.js 16 (App Router) · React 19 · TypeScript · Tailwind CSS · Clerk Auth · Neon Serverless PostgreSQL · Drizzle ORM · Cloudflare R2  
> **Governance:** Universal AGENTS.md Constitution · 5 Dynamic Operating Modes · 16 Core Project Skills + AI Hero Flow

ชุดเอกสารและโครงสร้างนี้คือ **แม่แบบมาตรฐานวิศวกรรมแบบ Full-Stack สำเร็จรูป (Universal Production Starter)** ที่มีทั้งระบบกำกับดูแล AI ขั้นสูง (Human-AI Pair Programming Governance) และโครงสร้างซอฟต์แวร์ระดับ Production ที่พร้อมเชื่อมต่อฐานข้อมูล ระบบล็อกอิน และระบบจัดเก็บไฟล์ได้ทันที 100%

---

## 🌳 1. Directory Tree Structure (โครงสร้างไฟล์แบบ Tree)

```text
D:\iAMor Family\First_Project\
├── AGENTS.md                 # 📜 รัฐธรรมนูญสูงสุด กฎเหล็ก 8 ข้อ และ E2E Quality Pipeline
├── AGENT.md                  # 🤖 สัญญาการปฏิบัติการและอัตลักษณ์ของ AI Agent ในโปรเจกต์
├── root-architect-mode.md    # 👑 สถาปนิกกุมกุญแจรากเหง้า (Zero-Trust, Core DB, Kernel RCA)
├── tech-lead-mode.md         # 🏛️ หัวหน้าทีมวิศวกรรม (Task Breakdown, 4-Tier Review, TDD)
├── cheat-code-mode.md        # ⚡ ผู้นำสายสูตรลัด 10x (Rapid Execution, YAGNI, Minimal Diff)
├── mentor-mode.md            # 🧠 โหมด Dev พี่เลี้ยง (Socratic, First-Principles, แนะนำสถาปัตยกรรม)
├── architect-mode.md         # 🏛️ โหมดสถาปนิก (Clean Architecture 4 Layers, ADR, Boundary)
├── debugger-mode.md          # 🔍 โหมดผ่าตัดบั๊ก (5-Whys RCA, Forensic Tracing, Poka-Yoke)
├── reviewer-mode.md          # 🛡️ โหมดตรวจการโค้ด (QA Gatekeeper, 4-Tier Verification Matrix)
├── fast-exec-mode.md         # ⚡ โหมดสายสปีด (Caveman / Quick Fix Tier S ตอบสั้น ได้ใจความ)
├── mistakes.md               # 🚫 คลังบันทึกข้อผิดพลาดและบทเรียนต้องห้าม (Zero Recurrence Vault)
├── LATEST_CHECKPOINT.md      # 📌 จุดบันทึกสถานะโปรเจกต์ (Session Hydration สำหรับสลับตัว AI)
├── README.md                 # 📖 คู่มือการใช้งานและคำอธิบายระบบฉบับสมบูรณ์
│
├── package.json              # 📦 รายการ Dependencies: Next.js 16, Clerk, Drizzle, Neon, AWS SDK
├── tsconfig.json             # ⚙️ TypeScript Strict Configuration
├── drizzle.config.ts         # 🗄️ คอนฟิกการเชื่อมต่อ Neon PostgreSQL ผ่าน Drizzle Kit
├── next.config.ts            # 🌐 คอนฟิก Next.js 16
├── .env.example              # 📋 แม่แบบตัวแปรระบบ (Clerk, Database URL, Cloudflare R2)
├── .gitignore                # 🔒 ป้องกันการรั่วไหลของ .env.local, node_modules และ secrets
│
├── src/                      # 💻 โค้ดต้นฉบับของ Full-Stack Application
│   ├── app/                  # Next.js App Router (layout.tsx, page.tsx, globals.css)
│   ├── db/                   # Drizzle ORM Schema
│   │   └── schema.ts         # ตารางฐานข้อมูล PostgreSQL (Users, Profiles, Audit Logs)
│   ├── lib/                  # ตัวเชื่อมต่อบริการภายนอก (Shared Libraries)
│   │   ├── db.ts             # เชื่อมต่อ Neon Serverless PostgreSQL Connection Pool
│   │   └── r2.ts             # เชื่อมต่อ Cloudflare R2 Presigned S3 Upload
│   └── middleware.ts         # ตัวดักจับสิทธิ์การเข้าใช้งานระบบล็อกอิน Clerk Auth
│
├── scripts/                  # 🛠️ สคริปต์อัตโนมัติประจำโปรเจกต์
│   ├── setup-project.js      # ติดตั้ง dependencies, ซิงค์ .env และเชื่อมต่อฐานข้อมูล Neon
│   ├── setup-project.ps1     # PowerShell Wrapper สำหรับ Windows
│   ├── install-skills.js     # ตรวจเช็กและซิงค์คลังสกิลเฉพาะโปรเจกต์อัตโนมัติ
│   └── install-skills.ps1    # PowerShell Wrapper สำหรับติดตั้งสกิล
├── skills-manifest.json      # 📋 รายการและบัญชีสารบรรณสกิลเฉพาะโปรเจกต์ (Zero Legacy Bloat)
├── skills/ (และ .gemini/skills) # ⚡ คลังสกิลเฉพาะโปรเจกต์ (16 Core + AI Hero Spine)
│
└── .gemini/ (และ gemini/)     # 🗄️ โฟลเดอร์กำกับดูแลแกนสมองและสถานะของ AI
    ├── memory/               # 🧠 คลังความทรงจำระยะยาว (behavior.json, rules.md, project_dna.md)
    ├── state/                # 🧭 จุดติดตามสถานะการรันงานสด (active_task.json, circuit_breaker.json)
    ├── prompts/              # 💬 เทมเพลตคำสั่งมาตรฐาน (system_prompt, reverse_prompt, triage)
    └── docs/                 # 📚 เอกสารสถาปัตยกรรม (ARCHITECTURE.md, RUNBOOK.md, CONTRIBUTING.md)
```

---

## 🚀 2. วิธีการเริ่มต้นใช้งาน (How to Use)

### 📌 กรณีที่ 1: ก๊อปปี้ไปสร้างโปรเจกต์ใหม่ และสั่งให้เซ็ตอัปทุกอย่างอัตโนมัติ
เมื่อคุณนำโฟลเดอร์นี้ไปเป็นโปรเจกต์ใหม่บนเครื่อง ให้สร้างไฟล์ `.env.local` (ก๊อปปี้จาก `.env.example` แล้วใส่ URL ฐานข้อมูลของคุณ) จากนั้นสั่ง AI เพียงประโยคเดียว:

> **"อ่าน AGENT.md แล้วติดตั้ง Stack และเชื่อมต่อฐานข้อมูลให้พร้อมรัน"**

AI จะดำเนินการเองในเบื้องหลังทันที:
1. ซิงค์และยืนยันคลังสกิลเฉพาะโปรเจกต์ (`node scripts/install-skills.js`)
2. ติดตั้ง Node Dependencies ที่จำเป็นทั้งหมด (`npm install`)
3. เชื่อมต่อฐานข้อมูล Neon และสร้างตารางตามสกีมา (`npx drizzle-kit push`)
4. รายงานผลความพร้อมและบอกคำสั่งเปิดหน้าเว็บ (`npm run dev`)

---

### 📌 กรณีที่ 2: การสั่งงานพัฒนาฟีเจอร์ประจำวัน
- **ออกแบบระบบใหม่:**  
  `"สลับเข้าสู่โหมด architect-mode.md ออกแบบระบบตารางสต็อกสินค้าใน src/db/schema.ts"`
- **สร้างตารางลงฐานข้อมูลจริง:**  
  `"รัน npm run db:push เพื่ออัปเดตสกีมาลง Neon PostgreSQL"`
- **เปิดดูฐานข้อมูลผ่านเบราว์เซอร์:**  
  `"เปิด npm run db:studio เพื่อดูข้อมูลใน Database"`
- **แก้บั๊กหรือเทสต์พัง:**  
  `"สลับเข้าสู่โหมด debugger-mode.md วินิจฉัยข้อผิดพลาดนี้แบบ 5-Whys"`
- **รีวิวโค้ดก่อนส่งงาน:**  
  `"สลับเข้าสู่โหมด reviewer-mode.md ตรวจสอบตามเกณฑ์ 4-Tier Verification Matrix"`

---

## ⚡ 3. คลังสกิลเฉพาะโปรเจกต์นี้ (16 Core Skills + AI Hero Spine)

โปรเจกต์นี้ได้รับการกำกับดูแลให้ใช้ **เฉพาะสกิลที่ติดตั้งสำหรับโปรเจกต์นี้เท่านั้น** โดยกักกันและลบสกิลดั้งเดิม/ของเก่าในเครื่องทิ้ง 100% (Zero Legacy Bloat):

| # | ชื่อสกิล | แหล่งที่มา / ที่สั่งติดตั้ง | บทบาทหน้าที่ในโปรเจกต์ |
| :---: | :--- | :--- | :--- |
| 1 | **`caveman`** | `JuliusBrussee/caveman` | ตอบสั้น ตรงเป้า ไร้น้ำ ประหยัดโทเค็นขั้นสูงสุด |
| 2 | **`ponytail`** | `dietrichgebert/ponytail` | ปรัชญาวิศวกรอาวุโส แก้ไขจุดเล็กที่สุด (YAGNI) ปฏิเสธโค้ดบวม |
| 3 | **`handoff`** | `mattpocock/skills` | ส่งต่องานระหว่างเซสชัน แช่แข็ง Context และสถานะงานอย่างรัดกุม |
| 4 | **`understand`** | `Egonex-AI/Understand-Anything` | สแกนทำความเข้าใจ Codebase ลึกซึ้ง ออกแผนที่สถาปัตยกรรมระบบ |
| 5 | **`code-review`** | `tirth8205/code-review-graph` | ตรวจสอบ Git Diff และโครงสร้างโค้ดด้วยกราฟความสัมพันธ์ |
| 6 | **`headroom`** | `headroomlabs-ai/headroom` | เฝ้าระวัง Context Window และคำนวณงบประมาณโทเค็นไม่ให้ล้น |
| 7 | **`karpathy-guidelines`** | `multica-ai/andrej-karpathy-skills` | ปรัชญา Andrej Karpathy (First-Principles, Zero-Fluff, Minimal Waste) |
| 8 | **`ui-ux-pro-max`** | `nextlevelbuilder/ui-ux-pro-max-skill` | ออกแบบ UI/UX คุม Typography, โทนสี และ Responsive 6 ขนาดหน้าจอ |
| 9 | **`impeccable`** | `pbakaus/impeccable` | ตรวจสอบและเกลา Visual UI ให้เนี้ยบไร้ที่ติ ต่อต้านดีไซน์ AI เกรดต่ำ |
| 10 | **`taste-skill`** | `leonxlnx/taste-skill` | สุนทรียศาสตร์และการคัดสรรงานออกแบบคุณภาพสูง (Design Taste) |
| 11 | **`antislop`** | `miqdadbadjuber/anti-slop` | กำจัดโค้ดขยะ โค้ดซ้ำซาก และ Boilerplate รกๆ ออกจากระบบ |
| 12 | **`drizzle-neon`** | สเปกฐานข้อมูลโปรเจกต์ | บริหารจัดการ Neon Serverless PostgreSQL และ Drizzle ORM Schema |
| 13 | **`r2-presigned-upload`** | สเปก Storage โปรเจกต์ | อัปโหลดไฟล์ขนาดใหญ่ผ่าน Cloudflare R2 Presigned S3 URLs |
| 14 | **`loop-verifier`** | `cobusgreyling/loop-engineering` | **[Loop Engineering]** ฝ่ายตรวจสอบอิสระ (Build & Integrity Checker) |
| 15 | **`loop-triage`** | `cobusgreyling/loop-engineering` | **[Loop Engineering]** วินิจฉัยข้อผิดพลาดและซิงค์สถานะลง `STATE.md` |
| 16 | **`loop-me`** | `cobusgreyling/loop-engineering` | **[Loop Engineering]** วงจรควบคุมอัตโนมัติ Maker/Checker Loop |

*(พร้อมชุดสายพานพัฒนา AI Hero: `to-spec`, `to-tickets`, `implement`, `tdd`, `retro`, `diagnosing-bugs` ฯลฯ)*

---

## 🔒 4. มาตรฐานความปลอดภัยและคุณภาพ (Quality & Safety Gates)

1. **Rule of 3 Loops:** หาก AI พยายามแก้ปัญหาเดิมซ้ำเกิน 3 รอบ ระบบจะสั่งหยุดทำงานทันที (Circuit Breaker) เพื่อให้มนุษย์ตัดสินใจ ป้องกันการเผาโทเค็นทิ้ง
2. **50% Progress Pause:** ทุกครั้งที่เขียนโค้ดถึงครึ่งทาง ต้องหยุดบีบอัดและรีแฟกเตอร์โค้ดก่อนเริ่มทำครึ่งหลัง
3. **No Fake Pass:** ห้ามสรุปว่างานเสร็จสิ้นหากไม่มีหลักฐานการรันคำสั่ง (Exit Code 0) หรือผลตรวจจริง
4. **Zero Legacy Skills:** กักกันสกิลเดิมในเครื่องไม่ให้ปะปนในโปรเจกต์ 100%

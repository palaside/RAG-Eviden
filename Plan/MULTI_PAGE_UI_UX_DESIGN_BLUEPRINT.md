# 🏛️ MULTI-PAGE UI/UX DESIGN BLUEPRINT: DIGITAL EVIDENCE FORENSIC SUITE
**พิมพ์เขียวสถาปัตยกรรมโครงสร้างหน้าจอและคลังคอมโพเนนต์ฉบับสมบูรณ์ (100% Pure UI/UX Architecture)**  
*ระบบวิเคราะห์พยานหลักฐานดิจิทัลคดีอาญา มาตรฐานศาลยุติธรรม (Court-Ready Digital Evidence Suite)*

---

# ส่วนที่ 1: แผนผังโครงสร้างเว็บไซต์และเมนูหลัก (Site Tree & Navigation Architecture)

```text
DIGITAL EVIDENCE FORENSIC SUITE (ROOT PORTAL)
│
├── 🌐 GLOBAL APP HEADER & NAVIGATION SHELL
│   ├── [Brand/Case Identifier]: Case ID Badge + SHA-256 Vault Status
│   ├── [Global Mode Switcher]: Interactive Analysis Mode vs. Court Presentation Mode
│   ├── [System Integrity Bar]: Zero-Tolerance Protocol Indicator + Reversibility Lock Stamp
│   └── [Global Quick Actions]: Export Air-Gapped Package | Search Index (Ctrl+K)
│
├── 📄 PAGE 01: EVIDENCE INTAKE & FORENSIC GATEWAY (ศูนย์รับเข้าและคัดกรองหลักฐาน)
│   ├── 📁 Sub-Menu 1.1: File Intake Zone (Multi-Modal Staging Buffer)
│   ├── 🔍 Sub-Menu 1.2: Forensic Quality & Integrity Inspector (Laplacian & ELA)
│   └── 🛡️ Sub-Menu 1.3: 4-Tier Deduplication & Occurrence Audit
│
├── 📄 PAGE 02: CHAT STRIP & DUAL-LAYER VISUALIZER (ศูนย์ตรวจแชทต่อเส้นเดียว)
│   ├── 🎛️ Sub-Menu 2.1: Viewport & Canvas Navigation (Zoom, Pan, Reset)
│   ├── ✂️ Sub-Menu 2.2: Quiet Zone & Stitching Alignment Inspector
│   └── 🎯 Sub-Menu 2.3: Focal Jump & Annotation Layer Controls (SVG Overlay)
│
├── 📄 PAGE 03: EVIDENCE SUMMARY TABLE & SSOT LEDGER (โหมดตารางสรุปหลักฐาน)
│   ├── 🔎 Sub-Menu 3.1: Table Filter & Perspective Toolbar (Filter by Status/Person/Bank)
│   ├── 📊 Sub-Menu 3.2: Row Action & Inspection Drawer Launcher
│   └── 📤 Sub-Menu 3.3: Batch Verification & Table Export Controls
│
├── 📄 PAGE 04: CORROBORATION LINKAGE & COMPARISON ROOM (โหมดตรวจสอบความเชื่อมโยง)
│   ├── ⚖️ Sub-Menu 4.1: Candidate Leads Navigator (จุดที่ควรเปิดดู)
│   ├── ↔️ Sub-Menu 4.2: Dual-Side View Controller (Chat Bubble vs Slip Inspector)
│   └── ✅ Sub-Menu 4.3: Non-Forced Verification Action Bar (Confirm / Keep Review / Reject)
│
├── 📄 PAGE 05: EXECUTIVE FRAUD COMMAND & 4-CARDS DASHBOARD (แดชบอร์ดการ์ดทั้ง 4)
│   ├── 🃏 Sub-Menu 5.1: 4-Cards Executive KPI Strip
│   ├── 📈 Sub-Menu 5.2: Damage Trend & Cumulative Claim Graph
│   └── 🚨 Sub-Menu 5.3: Discrepancy & Alert Drawer
│
├── 📄 PAGE 06: CHRONOLOGICAL 11D TIMELINE & TRIAL STRATEGY (ไทม์ไลน์ 11 มิติ)
│   ├── ⏱️ Sub-Menu 6.1: Temporal Phase Filter & Anchor Scale
│   ├── 🏛️ Sub-Menu 6.2: Civil Loan Rebuttal & Criminal Intent Matrix
│   └── ⚔️ Sub-Menu 6.3: Killer Cross-Examination Script Launcher
│
├── 📄 PAGE 07: BENEFICIARY FRAUD GRAPH & MULE NETWORK (แผนผังเครือข่ายบัญชีม้า)
│   ├── 🕸️ Sub-Menu 7.1: Node-Edge Force Graph Controls (Filter by Layer/Bank/Role)
│   ├── 👥 Sub-Menu 7.2: Target Person Dossier Side-Drawer
│   └── 💸 Sub-Menu 7.3: Proxy Transfer & Fund Dispersal Flow Lens
│
└── 📄 PAGE 08: THE 5 PILLARS COURT DOSSIER PACKAGER (ศูนย์รวมเล่มสำนวนคดีเสาทั้ง 5)
    ├── 📑 Sub-Menu 8.1: 5-Pillars Modular Assembly Tabs (Pillar 1 to 5)
    ├── 🖨️ Sub-Menu 8.2: Print-to-Court A4 Pagination & Header/Footer Config
    └── 🔒 Sub-Menu 8.3: Air-Gapped Standalone HTML / WinRAR SFX Vault Generator
```

---

# ส่วนที่ 2: เจาะลึกพิมพ์เขียวรายหน้าและคอมโพเนนต์ย่อย (Page-by-Page UI Blueprint)

---

### PAGE 01: EVIDENCE INTAKE & FORENSIC GATEWAY
*(ศูนย์รับเข้าและคัดกรองหลักฐานดิจิทัล)*

#### 1. เป้าหมายของหน้า (Page Objective & Target Context)
เป็นด่านตรวจรักษาความบริสุทธิ์ของพยานหลักฐาน (Chain of Custody Gateway) ทำหน้าที่รับไฟล์ภาพแชทขนาดยาวและสลิปการเงินจากผู้ใช้ ตรวจคำนวณค่าแฮช SHA-256 ทันที คัดกรองภาพเบลอด้วย Laplacian Variance ($\ge 100$) และตรวจไฟล์ซ้ำ 4 ระดับ เพื่อป้องกันไม่ให้ข้อมูลขยะหรือสลิปซ้ำหลุดเข้าสู่สำนวนคดี

#### 2. โครงสร้างเลย์เอาต์หลัก (Macro Layout Engine)
* **โครงสร้าง:** 12-Column CSS Grid แบบ Compact Density ออกแบบโทน Tactical Dark (`#0B0F19`)
* **การแบ่งพื้นที่:**
  - ซีกซ้าย (Col 1–4): File Drag-and-Drop Dropzone & Upload Queue
  - ซีกขวา (Col 5–12): Staging Telemetry Matrix, Quality Gate Gauges, และ Deduplication Audit Table

#### 3. แถบเมนูลูกและระบบนำทาง (Sub-Menu & Navigation Bar)
* **[Sub-Menu 1.1: File Filter & Intake Type Switcher]:**
  - ปุ่ม Tab Switcher: `ALL FILES (48)` | `CHAT SCREENSHOTS (42)` | `BANK SLIPS (6)`
  - Action Button: ปุ่ม `+ Add Evidence Files` (Primary Accent Cyan)
* **[Sub-Menu 1.2: Batch Forensic Actions]:**
  - ปุ่ม `Run Gatekeeper Audit (Laplacian & Hash)`
  - Dropdown: `Filter by Quality Status: All / Crisp Accepted / Blur Warning / Duplicate Flagged`

#### 4. รายการคอมโพเนนต์ย่อยภายในหน้า (UI Component Inventory)

##### 🧩 Component 1.1: Multi-Modal Drag-and-Drop Vault Zone
* **ประเภทชิ้นส่วน:** Large Dropzone Container / Interactive Upload Panel
* **คุณสมบัติและเนื้อหา:**
  - ไอคอนเวกเตอร์ SVG Security Vault พร้อมเอฟเฟกต์ Pulsing Glow สีฟ้าคราม
  - ข้อความ H2: *"ลากและวางภาพพยานหลักฐานที่นี่ หรือคลิกเพื่อเลือกไฟล์"*
  - ข้อความ Sub-label: *"รองรับ JPG, PNG, WebP • คำนวณ SHA-256 อัตโนมัติ ณ จุดรับเข้า"*
  - ตัวนับขนาดไฟล์และจำนวนรายการในคิวรอ (Staging Buffer Counter)
* **สถานะการโต้ตอบ:**
  - *Default:* พื้นหลัง `#131B2E`, เส้นประ Hairline Border สี `#334155`
  - *Drag-Over:* เส้นขอบเปลี่ยนเป็นสีเขียวมรกตเรืองแสง (`#10B981`, Glow 8px), พื้นหลังปรับโปร่งแสง 90%
  - *Uploading:* แสดงแถบสถานะ Linear Progress Bar สไตล์ Cyberpunk แสดงความเร็ว MB/s
  - *Error:* เส้นขอบสีแดง Crimson (`#EF4444`) พร้อมข้อความเตือนไฟล์ที่ไม่รองรับ
* **ดีไซน์โทเค็น:** Border-radius: `8px`, เส้นขอบ: `1.5px dashed #475569`, ฟอนต์ตัวเลข: Monospace JetBrains Mono

##### 🧩 Component 1.2: Laplacian Quality Metric Gauge Card
* **ประเภทชิ้นส่วน:** Metric Card with Micro Radial Gauge
* **คุณสมบัติและเนื้อหา:**
  - หัวข้อการ์ด H3: *"Laplacian Variance Blur Gate"*
  - ตัวเลขสถิติขนาดใหญ่ (Monospace 28px): `680.99` (Crisp) เทียบกับเกณฑ์มาตรฐาน `≥ 100.00`
  - ป้าย Badge ระบุสถานะ: `QUALITY_ACCEPTED` (สีเขียว) หรือ `BLUR_REJECTED` (สีแดง)
  - แถบคาดระดับความคมชัดแบ่ง 3 โซน: สีแดง (<100), สีเหลือง (100–300), สีเขียว (>300)
* **สถานะการโต้ตอบ:**
  - *Default:* การ์ด Glassmorphism พื้นหลัง `#1E293B`, ขอบ Hairline 1px
  - *Hover:* ลอยตัวขึ้น Y: -2px, แสดง Tooltip อธิบายสูตรคณิตศาสตร์ $\nabla^2 f$
* **ดีไซน์โทเค็น:** Border-radius: `6px`, Shadow: `0 4px 20px rgba(0,0,0,0.5)`, Padding: `16px`

##### 🧩 Component 1.3: 4-Tier Deduplication Audit Matrix
* **ประเภทชิ้นส่วน:** Compact Forensic Data Table
* **คุณสมบัติและเนื้อหา:**
  - ตาราง 7 คอลัมน์: `Thumbnail`, `File ID`, `SHA-256 (Truncated 12-char)`, `Dimensions`, `Laplacian Var`, `Dedup Tier Result`, `Action`
  - แท็กระบุผลลัพธ์: `UNIQUE_MASTER` (สีเขียว), `EXACT_BINARY_DUP` (สีแดง), `PHASH_NEAR_DUP` (สีส้ม)
  - ปุ่มกดรายแถว: `Inspect BBox`, `Exclude from Dossier`
* **สถานะการโต้ตอบ:**
  - *Row Hover:* ไฮไลต์แถวด้วยสีฟ้า `#1E293B` โปร่งแสง 50%
  - *Active Selection:* เช็คบ็อกซ์เลือกแถวแบบมัลติซิเล็กชัน แสดง Action Bar ลอยด้านล่าง
* **ดีไซน์โทเค็น:** Header Background: `#0F172A`, Row Height: `44px`, ฟอนต์ข้อมูล: Monospace 12px

---

### PAGE 02: CHAT STRIP & DUAL-LAYER VISUALIZER
*(ศูนย์ตรวจแชทต่อเส้นเดียวและเลเยอร์พิกัด)*

#### 1. เป้าหมายของหน้า (Page Objective & Target Context)
แก้ปัญหาจอเบลอ แรมบวม หรือคอมค้างเมื่อเปิดภาพแชทต่อเนื่อง 1,000 ภาพ ด้วยระบบ **Virtual Scrolling Viewport Windowing** และนำเสนอสถาปัตยกรรม **Dual-Layer (WebP Base + SVG Vector Overlay)** ให้ทนายและศาลสามารถซูมดูพิกเซลลึกได้โดยภาพไม่แตก และคลิกปุ่มส่องประเด็นเพื่อกระโดดข้ามไปยังพิกัด $Y_{cumulative}$ ได้ทันที

#### 2. โครงสร้างเลย์เอาต์หลัก (Macro Layout Engine)
* **โครงสร้าง:** Split-Screen Flexbox Layout แบบ Edge-to-Edge Canvas
* **การแบ่งพื้นที่:**
  - แถบซ้าย (Width: 320px): Focal Jump Palette (สารบัญจุดตายแห่งคดี & จุดสั่งโอน)
  - พื้นที่กลาง (Flexible 1fr): Dual-Layer Infinite Viewport Canvas (636px Base Strip)
  - แถบขวา (Width: 360px): Synchronized Bubble Inspector & Raw Metadata Drawer

#### 3. แถบเมนูลูกและระบบนำทาง (Sub-Menu & Navigation Bar)
* **[Sub-Menu 2.1: Viewport Controls Bar (Floating Top)]:**
  - ตัวควบคุมการซูม: Slider ระดับการซูม `25% — 400%`, ปุ่ม `Fit to Width`, ปุ่ม `100% Native`
  - ตัวแสดงพิกัดแบบเรียลไทม์: `Cursor Y: 4,520px | Canvas Y_cumulative: 28,450px`
* **[Sub-Menu 2.2: Layer Toggle Switches]:**
  - Toggle Switch: `Layer 0: Raw WebP Image (ON/OFF)`
  - Toggle Switch: `Layer 1: SVG Vector Highlights (pointer-events: none)`
  - Toggle Switch: `Quiet Zone Cut Lines (ON/OFF)`

#### 4. รายการคอมโพเนนต์ย่อยภายในหน้า (UI Component Inventory)

##### 🧩 Component 2.1: Dual-Layer Infinite Canvas Engine
* **ประเภทชิ้นส่วน:** Custom Canvas / Viewport View Container
* **คุณสมบัติและเนื้อหา:**
  - *Base Layer (DOM Layer 0):* เรนเดอร์เฉพาะบล็อกภาพที่ปรากฏในหน้าจอ $\pm 2$ หน้าจอ เพื่อควบคุมแรมไม่ให้เกิน 120MB
  - *Vector Layer (DOM Layer 1):* กรอบ SVG เวกเตอร์สีเหลืองทองและสีฟ้าครามครอบทับบับเบิ้ลข้อความเป้าหมาย ไม่ขีดเขียนทับไฟล์ดิบ
  - เส้นประแนวนอนสีม่วง (Quiet Zone Indicators): แสดงจุดที่ระบบผ่าตัดแบ่งหน้า A4 โดยไม่ผ่ากลางบับเบิ้ล
* **สถานะการโต้ตอบ:**
  - *Pan (Click & Drag):* ไอคอนเคอร์เซอร์เปลี่ยนเป็น `grabbing`, เลื่อนภาพลื่นไหล 60 FPS
  - *Bubble Hover:* กรอบเวกเตอร์บนเลเยอร์ SVG สว่างขึ้น พร้อมแสดง Tooltip ตัวเลขยอดเงิน
* **ดีไซน์โทเค็น:** พื้นหลังรอบแคนวาส: `#020617`, กรอบไฮไลต์: `stroke: #F59E0B`, `stroke-width: 2px`

##### 🧩 Component 2.2: Focal Points Navigation Palette
* **ประเภทชิ้นส่วน:** Vertical Timeline Navigation Sidebar
* **คุณสมบัติและเนื้อหา:**
  - รายการปุ่มส่องประเด็น (Focal Points): เรียงตามลำดับเวลา เช่น `[13:46] สั่งครีมขาดเงิน`, `[16:34] ส่งบัญชีกสิกร 2050262591`
  - ป้ายแสดงผลลัพธ์: ระบุยอดเงิน เช่น `฿5,600.00`
  - ปุ่มกดกระโดด (Quick Jump Button): ไอคอน Crosshair เมื่อกดแล้ว Viewport จะเลื่อนแอนิเมชันไปยังพิกัด $Y_{cumulative}$ เป้าหมายทันที
* **สถานะการโต้ตอบ:**
  - *Default:* พื้นหลัง `#1E293B`, ขอบมน 4px
  - *Hover:* พื้นหลังเปลี่ยนเป็น `#334155`, ไอคอนเรืองแสงสีฟ้า
  - *Active (Currently in View):* แถบสีเขียวสว่างชิดซ้าย (Active Left Border 3px)
* **ดีไซน์โทเค็น:** ฟอนต์: Sarabun + JetBrains Mono, ความกว้าง: 100%, ระยะห่างระหว่างไอเทม: 8px

---

### PAGE 03: EVIDENCE SUMMARY TABLE & SSOT LEDGER
*(โหมดตารางสรุปหลักฐานกลาง)*

#### 1. เป้าหมายของหน้า (Page Objective & Target Context)
เป็นหน้าจอหลักสำหรับผู้พิพากษา ทนายความ และพนักงานสอบสวน ในการตรวจสอบรายการพยานหลักฐานทีละแถวอย่างละเอียด (Row-by-Row Inspection) โดยดึงข้อมูลจากฐานข้อมูลความจริงเดียว (Lean SSOT) สามารถเปิดดูหลักฐานต้นทาง เทียบพิกัด และยืนยันสถานะความถูกต้องได้แบบ Real-Time

#### 2. โครงสร้างเลย์เอาต์หลัก (Macro Layout Engine)
* **โครงสร้าง:** Full-Width Responsive Flex Container with Sticky Headers
* **ความหนาแน่น:** Compact Density เพื่อให้แสดงผลข้อมูลได้มากที่สุดใน 1 หน้าจอโดยไม่ต้องเลื่อนบ่อย

#### 3. แถบเมนูลูกและระบบนำทาง (Sub-Menu & Navigation Bar)
* **[Sub-Menu 3.1: Multi-Facet Filter Toolbar]:**
  - Dropdown Filter: `สถานะ: ทั้งหมด / ยืนยันแล้ว (Confirmed) / รอตรวจ (Review Required) / ข้อมูลไม่ครบ (Incomplete)`
  - Dropdown Filter: `บุคคลที่เกี่ยวข้อง: ทั้งหมด / ปรียาฉัตร / จิณห์นิภา / วันวิสา`
  - Dropdown Filter: `ธนาคาร: KBANK / KTB / SCB / PromptPay`
  - Search Input: ช่องค้นหาข้อความแบบเรียลไทม์ (ค้นหาชื่อ, เลขบัญชี, Ref ID)
* **[Sub-Menu 3.2: Batch Actions & Table Export]:**
  - ปุ่ม `Batch Confirm Selected`
  - ปุ่ม `Export Ledger to Excel (.xlsx)`
  - ปุ่ม `Print-to-Court A4 PDF`

#### 4. รายการคอมโพเนนต์ย่อยภายในหน้า (UI Component Inventory)

##### 🧩 Component 3.1: Master Evidence Ledger Table
* **ประเภทชิ้นส่วน:** Enterprise Data Table with Freeze Columns
* **คุณสมบัติและเนื้อหา:**
  - 10 คอลัมน์มาตรฐานศาล:
    1. `ลำดับ (Row ID)`: Monospace เช่น `ROW_01`, `ROW_02`
    2. `ไฟล์ต้นฉบับ (Source File)`: ลิงก์คลิกได้ เช่น `chatv3 (41).jpg`
    3. `วัน-เวลา (Timestamp)`: วันที่และเวลา เช่น `26 มิ.ย. 2568 16:34 น.`
    4. `ธนาคาร (Bank)`: โลโก้ธนาคารขนาดจิ๋ว 16px + รหัสย่อ (KBANK)
    5. `ผู้โอน (Sender)`: ชื่อ-นามสกุล หรือบัญชีต้นทาง
    6. `ผู้รับ (Receiver)`: ชื่อบัญชีปลายทาง
    7. `จำนวนเงิน (Amount)`: ตัวเลขจัดชิดขวา พร้อมคอมม่า เช่น `5,600.00` *(หากไม่มีคำสั่งโอน ให้แสดง `null (NOT_FOUND)` ตัวอักษรสีเทา ห้ามเดา)*
    8. `เลขอ้างอิง (Ref ID)`: ตัวเลข 18–25 หลัก
    9. `บันทึกช่วยจำ (Memo)`: ข้อความกำกับสลิป
    10. `สถานะ (Status)`: ป้าย Badge สีตามสถานะ
* **สถานะการโต้ตอบ:**
  - *Row Click:* เปิด Slide-Over Drawer ด้านขวา แสดงพิกัด Bounding Box ภาพต้นฉบับ
  - *Status Badge Click:* เปิด Dropdown เปลี่ยนสถานะระหว่าง `REVIEW_REQUIRED` ➔ `USER_CONFIRMED`
* **ดีไซน์โทเค็น:** พื้นหลังสลับแถว (Zebra striping): `#0F172A` และ `#131D31`, ขอบเส้นตาราง: `1px solid #1E293B`

##### 🧩 Component 3.2: Reversibility Evidence Drawer
* **ประเภทชิ้นส่วน:** Slide-Over Side Panel (ความกว้าง 480px)
* **คุณสมบัติและเนื้อหา:**
  - ส่วนหัว Drawer: แสดงชื่อไฟล์, ค่าแฮช SHA-256 เต็ม 64 ตัวอักษร (คลิกคัดลอกได้)
  - กล่องแสดงภาพ Crop ตัวอย่างหลักฐานจริง: ตัดพิกัดเฉพาะกรอบ Bounding Box มาแสดงความละเอียด 1:1
  - ข้อมูล Metadata นิติวิทยาศาสตร์: `Bounding Box: [ymin: 750, xmin: 100, ymax: 1200, xmax: 750]`, `Laplacian Score: 542.15`
  - ปุ่ม Action: `Open Full Image in Dual Visualizer`, `Save Evidence Snapshot`
* **สถานะการโต้ตอบ:**
  - *Slide In/Out:* Transition Cubic-Bezier 0.25s แบบลื่นไหล
  - *Copy Hash:* แสดง Tooltip เปลี่ยนเป็น *"Copied to Clipboard!"* สีเขียว 2 วินาที
* **ดีไซน์โทเค็น:** พื้นหลัง: `#0B0F19`, ขอบซ้าย: `1px solid #334155`, Box Shadow: `-8px 0 24px rgba(0,0,0,0.7)`

---

### PAGE 04: CORROBORATION LINKAGE & COMPARISON ROOM
*(โหมดตรวจสอบความเชื่อมโยงแชท-สลิป)*

#### 1. เป้าหมายของหน้า (Page Objective & Target Context)
สร้างสภาพแวดล้อมการทำงานแบบ **Dual Comparison Room** สำหรับพิจารณาเปรียบเทียบข้อความสั่งโอนเงินในหน้าแชท (ฝั่งซ้าย) เคียงคู่กับสลิปโอนเงินจริงของธนาคาร (ฝั่งขวา) โดยระบบชี้เป้าเป็นเพียง *"จุดที่ควรเปิดดู (Candidate Lead)"* และเปิดทางเลือกให้ผู้ใช้สามารถกดคงสถานะ *"รอตรวจ (Keep Review Required)"* ได้โดยไม่ถูกบีบบังคับ

#### 2. โครงสร้างเลย์เอาต์หลัก (Macro Layout Engine)
* **โครงสร้าง:** 2-Column Split Comparison Arena (อัตราส่วน 50:50) พร้อมแผงควบคุมการตัดสินใจตรงกลาง
* **เลย์เอาต์:** Flexbox Edge-to-Edge พร้อมระบบเลื่อนอิสระแยกฝั่ง (Independent Scroll)

#### 3. แถบเมนูลูกและระบบนำทาง (Sub-Menu & Navigation Bar)
* **[Sub-Menu 4.1: Candidate Leads Selector Bar]:**
  - แถบเลื่อนรายการคู่พยาน: แสดงการ์ดแนวนอน เช่น `Lead #01: ปรียาฉัตร (KBANK)`, `Lead #02: จิณห์นิภา (KTB)`
  - ตัวกรองความเชื่อมั่น: `แสดงเฉพาะคู่ที่ยอดเงินตรงกัน (Exact Amount Match)` | `ช่วงเวลาห่างไม่เกิน 1 ชม.`
* **[Sub-Menu 4.2: Comparison Synchronization]:**
  - ปุ่ม `Sync Zoom (ซูมสองฝั่งพร้อมกัน)` | ปุ่ม `Reset Both Panels`

#### 4. รายการคอมโพเนนต์ย่อยภายในหน้า (UI Component Inventory)

##### 🧩 Component 4.1: Dual Comparison Split Arena
* **ประเภทชิ้นส่วน:** Split-Panel Comparison View
* **คุณสมบัติและเนื้อหา:**
  - *แผงซ้าย (Chat Dialogue Anchor):*
    - กรอบแสดงภาพตัดเฉพาะบับเบิ้ลแชทที่มีการกล่าวถึงยอดเงินหรือส่งเลขบัญชี
    - การ์ดสกัดข้อความจริง (Extracted Raw Fact Card): แสดงข้อความจริง วันเวลาในแชท ไม่มีข้อมูลหลอน
  - *แผงขวา (Bank Slip Anchor):*
    - กรอบแสดงภาพสลิปโอนเงินความคมชัดสูง
    - การ์ดสกัดข้อมูลสลิปจริง: แสดงชื่อผู้รับ ยอดเงิน วันเวลาทำรายการ และ Ref ID
  - *แกนกลางเชื่อมโยง (Center Synapse Bar):*
    - ตัวบ่งชี้ความสัมพันธ์: เส้นโยงเวกเตอร์พร้อมป้ายระยะห่างเวลา เช่น `Δt: 22 นาที`, `ยอดเงิน: 1,500 บาท ตรงกัน 100%`
* **สถานะการโต้ตอบ:**
  - *Panel Sync Hover:* เมื่อวางเมาส์บนยอดเงินฝั่งซ้าย ยอดเงินฝั่งขวาจะเกิดเอฟเฟกต์ Pulsing Glow สีฟ้าพร้อมกัน
* **ดีไซน์โทเค็น:** กรอบแผง: `1px solid #334155`, พื้นหลังแผง: `#111827`, แถบเชื่อมโยง: `stroke: #38BDF8`

##### 🧩 Component 4.2: Non-Forced Verification Decision Dock
* **ประเภทชิ้นส่วน:** Fixed Bottom Floating Decision Dock
* **คุณสมบัติและเนื้อหา:**
  - ปุ่มยืนยัน (Confirm Link): ปุ่มสีเขียวมรกตพร้อมไอคอน Checkmark *"ยืนยันความเชื่อมโยง (USER_CONFIRMED)"*
  - ปุ่มคงสถานะรอตรวจ (Keep Review): ปุ่มสีเหลืองอำพัน *"หลักฐานไม่พอ ให้คงสถานะรอตรวจ (KEEP_REVIEW_REQUIRED)"*
  - ปุ่มปฏิเสธ (Reject Link): ปุ่มสีแดง Crimson *"ปฏิเสธความเชื่อมโยง (UNMATCHED / CONFLICT)"*
  - กล่องข้อความสั้นสำหรับบันทึกเหตุผลของทนาย (Forensic Note Input)
* **สถานะการโต้ตอบ:**
  - *Confirm Click:* แสดงเสียงยืนยันสั้นๆ พร้อมเปลี่ยนตราประทับตรงกลางเป็น `USER_CONFIRMED` สีเขียวสว่าง
  - *Keep Review Click:* สถานะคงเดิม บันทึกหมายเหตุ และเลื่อนไปยังคู่ถัดไปโดยไม่อนุมานข้อมูลเอง
* **ดีไซน์โทเค็น:** Floating Dock Shadow: `0 8px 32px rgba(0,0,0,0.8)`, Border-radius: `12px`, Backdrop-filter: `blur(16px)`

---

### PAGE 05: EXECUTIVE FRAUD COMMAND & 4-CARDS DASHBOARD
*(ศูนย์บัญชาการคดีและแดชบอร์ดสรุปการ์ดทั้ง 4)*

#### 1. เป้าหมายของหน้า (Page Objective & Target Context)
เป็นหน้าจอระดับหัวหน้าคณะทำงานและทนายความผู้ว่าคดี สำหรับประเมินภาพรวมความเสียหายแห่งคดี คัดกรองตัวเลขที่ไม่ผ่านการยืนยันออก 100% และแสดงตัวชี้วัดสำคัญผ่าน **"การ์ดทั้ง 4 ใบ"** ที่คำนวณจากตารางกลาง SSOT โดยตรง ไม่มีความคลาดเคลื่อน

#### 2. โครงสร้างเลย์เอาต์หลัก (Macro Layout Engine)
* **โครงสร้าง:** Top 4-Column Grid ➔ Middle 2-Column Split ➔ Bottom Threat Intelligence Feed
* **ความหนาแน่น:** Spacious Dashboard Layout รองรับการนำเสนอบนจอโปรเจกเตอร์หรือทีวีในห้องประชุมคดี

#### 3. แถบเมนูลูกและระบบนำทาง (Sub-Menu & Navigation Bar)
* **[Sub-Menu 5.1: Case Scope Switcher]:**
  - Dropdown: `เลือกสำนวนคดี: คดีฉ้อโกงต่อเนื่องกลุ่ม น.ส. จิณห์นิภา / ปรียาฉัตร`
  - Badge: `สถานะสำนวน: สอบสวนเสร็จสิ้น พร้อมส่งฟ้อง (Ready for Indictment)`
* **[Sub-Menu 5.2: Executive Action Bar]:**
  - ปุ่ม `Generate Executive Brief (PDF)` | ปุ่ม `Sync with Court Timeline`

#### 4. รายการคอมโพเนนต์ย่อยภายในหน้า (UI Component Inventory)

##### 🧩 Component 5.1: The 4 Forensic Command Cards Strip
* **ประเภทชิ้นส่วน:** Executive Metric Cards Grid (4 ใบเรียงแนวนอน)
* **คุณสมบัติและเนื้อหา:**
  - **การ์ดใบที่ 1 (ยอดรวมรายการที่ยืนยัน):**
    - ตัวเลข Monospace เด่นชัด: `฿4,500.00`
    - รายละเอียด: *"รวมเฉพาะรายการที่ผ่านการตรวจยืนยันแล้ว 2 รายการ (ตัดรายการรอตรวจออก 100%)"*
    - รหัสสี: Accent Green (`#22C55E`)
  - **การ์ดใบที่ 2 (ยอดของบุคคลที่เกี่ยวข้อง):**
    - ตัวเลข Monospace: `฿10,100.00`
    - รายละเอียด: *"ผูกสัมพันธ์ ปรียาฉัตร / จิณห์นิภา รวม 3 รายการ"*
    - รหัสสี: Accent Blue (`#3B82F6`)
  - **การ์ดใบที่ 3 (สัญญาณแชท–สลิป):**
    - ตัวเลข Monospace: `1 จุดตรวจ`
    - รายละเอียด: *"สัญญาณนำสืบ chatv3 (41).jpg บัญชี 2050262591 -> สลิป 1,500 (Candidate Lead)"*
    - รหัสสี: Accent Yellow (`#EAB308`)
  - **การ์ดใบที่ 4 (Ref ID ตรงกัน):**
    - ตัวเลข Monospace: `2 รายการ`
    - รายละเอียด: *"ตรวจไม่พบ Ref ID ซ้ำซ้อน (Unique Ref Verified)"*
    - รหัสสี: Accent Purple (`#A855F7`)
* **สถานะการโต้ตอบ:**
  - *Card Click:* ทำหน้าที่เป็นทางลัด (Shortcut Filter) กรองข้อมูลในตารางสรุปหลักฐานตามหัวข้อของการ์ดใบนั้นทันที
  - *Hover:* การ์ดยกตัวขึ้น Y: -4px, เส้นขอบ Hairline เรืองแสงตามรหัสสีประจำการ์ด
* **ดีไซน์โทเค็น:** Border-radius: `10px`, พื้นหลัง: `#1E293B`, Padding: `20px`

##### 🧩 Component 5.2: Damage Accumulation Curve Graph
* **ประเภทชิ้นส่วน:** Interactive Area / Line Chart
* **คุณสมบัติและเนื้อหา:**
  - แกน X: ลำดับเวลา (ม.ค. 2568 – มิ.ย. 2568)
  - แกน Y: ยอดเงินความเสียหายสะสม (บาท)
  - เส้นกราฟ 2 เส้นเปรียบเทียบ:
    - เส้นทึบสีเขียว: ยอดความเสียหายที่ยืนยันแล้วตามกฎหมาย (Confirmed Loss)
    - เส้นประสีเหลือง: ยอดความเสียหายรวมที่อยู่ระหว่างรอตรวจ (Potential Claim)
  - จุด Marker วงกลมบนกราฟ: ชี้ตำแหน่งของสลิปโอนเงินแต่ละฉบับ
* **สถานะการโต้ตอบ:**
  - *Marker Hover:* แสดง Popover แสดงชื่อสลิป, ยอดเงิน, และคำสั่งในแชทที่กระตุ้นยอดนั้น
* **ดีไซน์โทเค็น:** ความสูง: `320px`, Grid Lines: `#1E293B`, ฟอนต์แกน: Monospace 11px

---

### PAGE 06: CHRONOLOGICAL 11D TIMELINE & TRIAL STRATEGY
*(ไทม์ไลน์ 11 มิติและกลยุทธ์ทำลายข้อต่อสู้ในศาล)*

#### 1. เป้าหมายของหน้า (Page Objective & Target Context)
เปลี่ยนประวัติการแชทและสลิปการเงินที่กระจัดกระจายให้กลายเป็น **ไทม์ไลน์สตอรี่ 11 มิติ** ตามลำดับเวลาจริง เพื่อหักล้างข้อต่อสู้ของจำเลย (เช่น ข้ออ้างว่าเป็นเพียงการยืมเงินทางแพ่ง) และจัดเตรียมชุดคำถามซักค้านเผด็จศึกพยาน (Killer Cross-Examination Script) สำหรับใช้ว่าความในชั้นศาล

#### 2. โครงสร้างเลย์เอาต์หลัก (Macro Layout Engine)
* **โครงสร้าง:** Vertical Chronological Flow Container with Fixed Left Navigation Anchor
* **เลย์เอาต์:** 11-Column Matrix Card Sequence ออกแบบสไตล์สำนวนคดีศาล

#### 3. แถบเมนูลูกและระบบนำทาง (Sub-Menu & Navigation Bar)
* **[Sub-Menu 6.1: Timeline Filter & Phase Navigator]:**
  - ปุ่มเลือกช่วงเวลา: `ช่วงเริ่มกลอุบาย (ต้นปี 68)` | `ช่วงเร่งรัดและอ้างบุคคลที่สาม` | `ช่วงคำรับสภาพหนี้`
  - ตัวกรองมิติ: `แสดงเฉพาะเหตุการณ์ที่มีสลิปแนบ` | `แสดงเฉพาะจุดตายทางกฎหมาย`
* **[Sub-Menu 6.2: Trial Strategy Exporter]:**
  - ปุ่ม `Print Killer Cross-Examination Script`
  - ปุ่ม `Export 11D Matrix to Word (.docx)`

#### 4. รายการคอมโพเนนต์ย่อยภายในหน้า (UI Component Inventory)

##### 🧩 Component 6.1: 11-Dimensional Incident Event Card
* **ประเภทชิ้นส่วน:** Expandable Multi-Dimensional Event Card
* **คุณสมบัติและเนื้อหา:**
  - บรรจุองค์ประกอบครบถ้วนทั้ง 11 มิติในบัตรเดียว:
    1. *มิติที่ ๑ (วัน-เวลาจริง):* `12 ม.ค. 2568 13:53 น.`
    2. *มิติที่ ๒ (ตัวละคร/ผู้ส่ง):* `น.ส. จิณห์นิภา (จำเลย)`
    3. *มิติที่ ๓ (บริบทและกลอุบาย):* `อ้างสั่งซื้อครีมแต่เงินขาด 2,000 บาท`
    4. *มิติที่ ๔ (คำพูดบับเบิ้ลจริง):* Quote ข้อความแชทจริงจากไฟล์ดิบ
    5. *มิติที่ ๕ (สลิปโอนเงินที่เชื่อมโยง):* ภาพย่อสลิป + ยอดเงิน + Ref ID
    6. *มิติที่ ๖ (ยอดเงินความเสียหาย):* `1,500.00 บาท`
    7. *มิติที่ ๗ (พิกัดอ้างอิงภาพดิบ):* ลิงก์พิกัด `chatv3 (1).jpg Y:1250`
    8. *มิติที่ ๘ (ข้อหาและฐานความผิด):* ป.อ. มาตรา ๓๔๑, ๓๔๒ (ฉ้อโกง)
    9. *มิติที่ ๙ (การหักล้างข้อต่อสู้ทางแพ่ง):* วิเคราะห์พฤติการณ์กุเรื่องเท็จตั้งแต่แรก ไม่ใช่การยืมเงิน
    10. *มิติที่ ๑๐ (แนวทางการสืบพยานและซักค้าน):* สคริปต์คำถามต้อนจำเลยให้จนมุม
    11. *มิติที่ ๑๑ (สถานะความถูกต้อง):* ตราประทับ `COURT_VERIFIED`
* **สถานะการโต้ตอบ:**
  - *Card Header Click:* ยุบ/ขยายรายละเอียดมิติที่ 8–10 (กลยุทธ์ทางกฎหมาย)
  - *Quote Text Click:* กระโดดกลับไปเปิดภาพแชทจริงใน Page 02 ทันที
* **ดีไซน์โทเค็น:** กรอบการ์ด: `1px solid #334155`, พื้นหลัง: `#1E293B`, มิติทางกฎหมายไฮไลต์ด้วยสีทอง `#F59E0B`

##### 🧩 Component 6.2: Killer Cross-Examination Script Box
* **ประเภทชิ้นส่วน:** Script Dialog Box with Leading Questions
* **คุณสมบัติและเนื้อหา:**
  - ชุดคำถามชี้นำ (Leading Questions) สำหรับทนายความใช้ถามค้านจำเลยในคอกพยาน
  - ตัวอย่าง: *"ข้อ ๑: ในวันที่ ๑๒ ม.ค. จำเลยเป็นผู้พิมพ์ข้อความนี้ด้วยตนเองใช่หรือไม่?"*
  - ธงคำตอบเป้าหมาย (Target Answer Flag): `[จำเลยต้องตอบว่า: ใช่ / หากปฏิเสธ ให้เปิดเอกสารหมาย จ.1 ชี้พิกัด]`
  - เอกสารประกอบการซักค้านที่ต้องถือในมือ (Exhibits in Hand Reference)
* **สถานะการโต้ตอบ:**
  - *Copy Script Button:* คัดลอกคำถามและคำอธิบายไปลงคลิปบอร์ด
* **ดีไซน์โทเค็น:** ขอบซ้ายหนา 4px สีแดง Crimson (`#EF4444`), พื้นหลัง `#0F172A`, ฟอนต์ข้อความ Sarabun 15px

---

### PAGE 07: BENEFICIARY FRAUD GRAPH & MULE NETWORK
*(แผนผังเครือข่ายบัญชีม้าและเส้นทางการเงิน)*

#### 1. เป้าหมายของหน้า (Page Objective & Target Context)
สร้างภาพจำลองเครือข่ายอาชญากรรมทางการเงิน (Financial Crime Graph) เพื่อให้เห็นเส้นทางการไหลของเงินจากผู้เสียหาย ผ่านตัวการหลัก ตัวการร่วม และกระจายออกไปยังบัญชีม้าแถวต่างๆ พร้อมทั้งคัดกรองแยกกลุ่มบัญชีสั่งโอนแทน (Proxy Beneficiaries) ออกจากผู้รับผลประโยชน์ที่แท้จริง

#### 2. โครงสร้างเลย์เอาต์หลัก (Macro Layout Engine)
* **โครงสร้าง:** Full-Screen Interactive Node-Edge Graph Canvas with Collapsible Entity Dossier Panel
* **เทคโนโลยีเลย์เอาต์:** 2D Canvas Force-Directed Layout พร้อมระบบควบคุมฟิสิกส์

#### 3. แถบเมนูลูกและระบบนำทาง (Sub-Menu & Navigation Bar)
* **[Sub-Menu 7.1: Graph Filter Controls]:**
  - Checkbox Filters: `แสดงตัวการหลัก (สีแดง)` | `แสดงตัวการร่วม (สีส้ม)` | `แสดงบัญชีม้า (สีเขียว)` | `แสดงเส้นทางการฟอกเงิน (เส้นประสีม่วง)`
  - Slider: `กรองยอดเงินขั้นต่ำ: ฿1,000 — ฿100,000`
* **[Sub-Menu 7.2: Export & Graph Layout Switcher]:**
  - Dropdown Layout: `Force-Directed Layout` | `Hierarchical Tree (สายการบังคับบัญชา)` | `Radial Flow`
  - ปุ่ม `Export High-Res SVG / PNG Graph`

#### 4. รายการคอมโพเนนต์ย่อยภายในหน้า (UI Component Inventory)

##### 🧩 Component 7.1: Force-Directed Node-Edge Graph Canvas
* **ประเภทชิ้นส่วน:** Interactive Vector Network Canvas
* **คุณสมบัติและเนื้อหา:**
  - *Nodes (บุคคล/บัญชี):* วงกลมพร้อมภาพ Avatar หรือไอคอนธนาคาร แสดงชื่อบุคคลและยอดเงินรวมที่ได้รับ
  - *Edges (เส้นทางการโอน):* เส้นลูกศรชี้ทิศทางการไหลของเงิน ความหนาของเส้นแปรผันตามจำนวนเงินรวม
  - ป้ายกำกับบนเส้นโอน: จำนวนครั้งที่โอนและยอดเงินสุทธิ
* **สถานะการโต้ตอบ:**
  - *Node Drag:* สามารถคลิกลากโหนดเพื่อจัดตำแหน่งบนหน้าจอได้อย่างอิสระ
  - *Node Click:* ไฮไลต์เฉพาะเส้นทางการเงินที่เชื่อมโยงกับโหนดนั้น พร้อมเปิด Entity Side-Panel
  - *Canvas Scroll:* ซูมเข้า/ออกอย่างอิสระ พร้อม Minimap แสดงภาพรวมมุมขวาล่าง
* **ดีไซน์โทเค็น:** พื้นหลัง: `#030712`, เส้น Edge: `#475569`, โหนดตัวการหลัก: Glow สีแดง `#EF4444`

##### 🧩 Component 7.2: Suspect Dossier Side-Panel
* **ประเภทชิ้นส่วน:** Slide-Over Entity Inspector Panel (ความกว้าง 400px)
* **คุณสมบัติและเนื้อหา:**
  - รูปพรรณและข้อมูลบุคคล: ชื่อ-นามสกุล, ฉายา/ชื่อในแชท (`พี่แมว`), หมายเลขบัตรประชาชน (ถ้ามี)
  - รายการบัญชีธนาคารที่ครอบครอง: ธนาคาร, เลขที่บัญชี, ยอดเงินรวมที่ไหลเข้า
  - สถานะฐานความผิดที่เตรียมดำเนินคดี: `พ.ร.ก. บัญชีม้า ๒๕๖๖ มาตรา ๙`, `พ.ร.บ. ฟอกเงิน มาตรา ๕`
  - สรุปรายการสลิปที่ตรวจพบตรง: รายการสลิปโอนเข้าพร้อมลิงก์เปิดดูภาพสลิปต้นฉบับ
* **สถานะการโต้ตอบ:**
  - *Click Slip Link:* เปิด Modal แสดงภาพสลิปใบจริงแบบ Overlay
* **ดีไซน์โทเค็น:** พื้นหลัง `#1E293B`, ขอบ: `1px solid #334155`, Box-shadow: `-4px 0 16px rgba(0,0,0,0.6)`

---

### PAGE 08: THE 5 PILLARS COURT DOSSIER PACKAGER
*(ศูนย์รวมเล่มสำนวนคดีเสาทั้ง 5)*

#### 1. เป้าหมายของหน้า (Page Objective & Target Context)
เป็นขั้นตอนสุดท้ายในการประกอบร่างข้อมูลทั้งหมดเข้าสู่ **"เสาทั้ง 5 แห่งสำนวนคดี"** จัดเตรียมหน้ากระดาษ A4 กึ่งกลางแนวดิ่ง (Vertical Middle Balance) ตามระเบียบงานสารบรรณศาล และบันเดิลระบบออกเป็น **Single-File Standalone HTML / WinRAR SFX** สำหรับนำไปเปิดใช้งานบน Flash Drive ในห้องพิจารณาคดีแบบออฟไลน์ 100% ไร้การพึ่งพาอินเทอร์เน็ต

#### 2. โครงสร้างเลย์เอาต์หลัก (Macro Layout Engine)
* **โครงสร้าง:** Document Staging Grid (ซีกซ้าย: โครงสร้างเล่มเสาทั้ง 5 / ซีกขวา: A4 Live Print Preview Engine)
* **ความหนาแน่น:** Document-Centric Layout สัดส่วน 40:60

#### 3. แถบเมนูลูกและระบบนำทาง (Sub-Menu & Navigation Bar)
* **[Sub-Menu 8.1: The 5 Pillars Selector Tabs]:**
  - Tab 1: `เสาที่ 1: หน้าปกแฟ้มหลักฐาน (Cover Sheet)`
  - Tab 2: `เสาที่ 2: บัญชีมูลหนี้และธุรกรรม (Debt Ledger)`
  - Tab 3: `เสาที่ 3: สรุปเส้นทางการเงิน (Financial Flow)`
  - Tab 4: `เสาที่ 4: รายการกฎหมายอ้างอิง (Legal Clauses)`
  - Tab 5: `เสาที่ 5: รวมเล่มเอกสารประกอบคดี (A4 Dossier Package)`
* **[Sub-Menu 8.2: Packaging & Vault Exporters]:**
  - ปุ่ม `Download Offline HTML Bundle (.html)`
  - ปุ่ม `Build WinRAR Encrypted SFX Vault (.exe)`
  - ปุ่ม `Print-to-Paper A4 (Browser Native Print)`

#### 4. รายการคอมโพเนนต์ย่อยภายในหน้า (UI Component Inventory)

##### 🧩 Component 8.1: The 5 Pillars Status Checklist
* **ประเภทชิ้นส่วน:** Vertical Pillar Progression Accordion
* **คุณสมบัติและเนื้อหา:**
  - แสดงสถานะความพร้อมของทั้ง 5 เสา:
    - เสาที่ 1: ข้อมูลคดีและสารบัญพยาน (`READY - 1 หน้า`)
    - เสาที่ 2: ตารางบัญชีมูลหนี้ยอดรวม `฿4,500.00` (`READY - 2 หน้า`)
    - เสาที่ 3: แผนผังเส้นทางเงินและไทม์ไลน์ (`READY - 4 หน้า`)
    - เสาที่ 4: ตัวบทกฎหมาย ป.อ. ๓๔๑ และ พ.ร.ก.บัญชีม้า (`READY - 1 หน้า`)
    - เสาที่ 5: ภาคผนวกภาพถ่ายพยานหลักฐานความคมชัดสูง (`READY - 12 หน้า`)
  - ตราประทับกำกับ: `100% CORROBORATED & AUDITED`
* **สถานะการโต้ตอบ:**
  - *Click Pillar Item:* สลับหน้าจอ A4 Live Preview ฝั่งขวาให้แสดงเนื้อหาของเสานั้นทันที
* **ดีไซน์โทเค็น:** พื้นหลัง `#1E293B`, ขอบซ้ายหนา 3px ตามสถานะ (สีเขียวเมื่อพร้อมพิมพ์)

##### 🧩 Component 8.2: A4 Live Print Preview Engine
* **ประเภทชิ้นส่วน:** High-Fidelity Paper Simulation Canvas
* **คุณสมบัติและเนื้อหา:**
  - จำลองหน้ากระดาษ A4 สัดส่วนเป๊ะ 210mm × 297mm (อัตราส่วน 1:1.414)
  - ขอบกระดาษจำลอง: ระยะขอบบน 2.5 ซม. / ขอบล่าง 2.0 ซม. / ขอบซ้าย 3.0 ซม. / ขอบขวา 2.0 ซม.
  - ส่วนหัวกระดาษ (Header): แสดงชื่อคดีและหมายเลขพยานเอกสาร (เช่น `เอกสารหมาย จ.๑`)
  - ส่วนท้ายกระดาษ (Footer): แสดงเลขหน้า `หน้า ๑ จาก ๒๐` พร้อมตราประทับ SHA-256 รับรองความถูกต้อง
  - การจัดวางข้อความแบบ Vertical Middle Balance: วรรณยุกต์ไทย (่ ้ ๊ ๋ ิ ี) ไม่ชนเส้นขอบตาราง
* **สถานะการโต้ตอบ:**
  - *Page Navigator:* ปุ่มเลื่อนดูหน้าถัดไป/ก่อนหน้า พร้อมตัวบอกตำแหน่งหน้าปัจจุบัน
  - *Zoom Level:* ปรับดูภาพรวม 1 หน้าเต็ม หรือซูมเข้าอ่านข้อความ 100%
* **ดีไซน์โทเค็น:** เงาตกกระทบกระดาษ: `0 12px 36px rgba(0,0,0,0.5)`, สีพื้นกระดาษ: `#FFFFFF`, สีข้อความ: `#000000` (Native Thai Sarabun 16pt)

##### 🧩 Component 8.3: Air-Gapped Packaging Progress Modal
* **ประเภทชิ้นส่วน:** Centered Modal Dialog with Cryptographic Verification
* **คุณสมบัติและเนื้อหา:**
  - กระบวนการบันเดิลไฟล์: ฝัง CSS, Vanilla JavaScript, รูปภาพ WebP, และฐานข้อมูล Lean SSOT เป็นไฟล์ `.html` ไฟล์เดียว
  - การทดสอบ Air-Gapped: ยืนยันว่าไม่มีการเรียก CDN ภายนอกแม้แต่ลิงก์เดียว (`0 External Requests`)
  - รายงานผลการคำนวณแฮชรวมของสำนวนคดี (Master Package Digest)
  - ปุ่ม Action: `Open Standalone File`, `Copy to USB Flash Drive`
* **สถานะการโต้ตอบ:**
  - *Modal Backdrop:* พื้นหลังมืดโปร่งแสง 80% ป้องกันการคลิกออกขณะกำลังแพ็กเกจ
* **ดีไซน์โทเค็น:** Border-radius: `12px`, พื้นหลัง `#0F172A`, ขอบ Hairline สีฟ้าเรืองแสง

---

# ส่วนที่ 3: สรุปตารางคลังคอมโพเนนต์รวม (Global UI Component Matrix)

ตารางสรุปการนำคอมโพเนนต์ไปใช้งานซ้ำในแต่ละหน้า (Reusability Mapping Table):

| รหัสคอมโพเนนต์ | ชื่อคอมโพเนนต์หลัก (Component Name) | ประเภทชิ้นส่วน | Page 01 | Page 02 | Page 03 | Page 04 | Page 05 | Page 06 | Page 07 | Page 08 | การนำไปใช้ซ้ำ (Reusability) |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **CMP-01** | **Global Vault Header & Security Bar** | Header Shell | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | นำไปใช้เป็นแถบหัวของทุกหน้า 100% |
| **CMP-02** | **SHA-256 Hash Badge with Copy Action** | Micro Badge | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ประทับทุกจุดที่มีการอ้างอิงไฟล์ดิบ |
| **CMP-03** | **Laplacian Quality Status Indicator** | Metric Badge | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ใช้ในหน้า Intake, ตารางกลาง, และเล่มคดี |
| **CMP-04** | **Dual-Layer Canvas Viewport** | Canvas View | ❌ | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ใช้ในหน้าแชทเส้นเดียว และห้องเปรียบเทียบ |
| **CMP-05** | **Evidence Slide-Over Inspector Drawer** | Side Drawer | ❌ | ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ❌ | ลิ้นชักส่องพิกัด Bounding Box ภาพจริง |
| **CMP-06** | **Status Badge (Confirmed/Review/Unmatch)** | Status Tag | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | กำกับสถานะแถว การ์ด และเหตุการณ์ |
| **CMP-07** | **Interactive Metric Card (Monospace Val)** | Metric Card | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | แกนหลักของการ์ดทั้ง 4 ใบ |
| **CMP-08** | **Leading Question & Cross-Exam Script Box** | Script Box | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | ✅ | ใช้ในไทม์ไลน์ 11 มิติ และเสาที่ 4 |
| **CMP-09** | **A4 Native Print Box Model Frame** | Print Canvas | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | จัดกระดาษ A4 สำหรับพิมพ์และส่งออก |
| **CMP-10** | **Non-Forced Decision Action Bar** | Action Dock | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ชุดปุ่มตัดสินใจ ยืนยัน/คงสถานะ/ปฏิเสธ |

---

### 🎨 สรุปดีไซน์โทเค็นระดับระบบ (System Design Tokens)
* **สีพื้นหลังหลัก (Background System):**
  - Dark Surface Base: `#0B0F19` (Slate-950)
  - Card & Container Surface: `#1E293B` (Slate-800)
  - Elevated Popover & Modal: `#0F172A` (Slate-900)
* **สีบ่งชี้สถานะทางกฎหมาย (Forensic Accent Tokens):**
  - `CONFIRMED / CRISP / SAFE`: `#22C55E` (Emerald Green)
  - `REVIEW REQUIRED / PENDING / LEAD`: `#EAB308` (Amber Gold)
  - `UNMATCHED / BLUR / THREAT`: `#EF4444` (Crimson Red)
  - `VAULT / CRYPTO / HASH / ACTIVE`: `#38BDF8` (Cyan Blue)
  - `RELATIONAL / NETWORK / MULE`: `#A855F7` (Purple Violet)
* **แบบอักษร (Typography Standard):**
  - ข้อความภาษาไทยและเนื้อหาทั่วไป: `Sarabun` (ขนาด 14–16px อ่านง่ายในศาล)
  - ตัวเลขธุรกรรม, ค่าแฮช SHA-256, และพิกัด BBox: `JetBrains Mono` / `Courier New` (Monospace 100% ป้องกันตัวเลขเคลื่อน)

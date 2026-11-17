# 🏛️ RAG-Eviden (ชวกม.2)
### Digital Forensics, AI OCR, Vector RAG & Court Dossier Intelligence Platform
> **Repository:** [https://github.com/palaside/RAG-Eviden](https://github.com/palaside/RAG-Eviden)  
> **Standard:** Court Forensic Aligned (ISO/IEC 27037 & พ.ร.บ.ธุรกรรมทางอิเล็กทรอนิกส์ พ.ศ. ๒๕๔๔)  
> **Status:** Production Ready (Immortal State)

---

## 📌 ภาพรวมโครงการ (Project Overview)
ระบบประมวลผลและแปลงสภาพพยานหลักฐานดิจิทัล (ภาพแชท LINE, สลิปธุรกรรมธนาคาร, รายการเดินบัญชี Statement) ให้กลายเป็น **สำนวนพยานหลักฐานดิจิทัลมาตรฐานศาล** แบบบูรณาการ 360 องศา พร้อมระบบ Vector RAG สืบค้นบทสนทนา, แดชบอร์ดวิเคราะห์เส้นทางเงินเครือข่ายบัญชีม้า และดัชนีพยานหลักฐานชุดเสริมพร้อมยื่นพนักงานสอบสวนและศาล

---

## 🌟 5 เสาหลักการวิเคราะห์คดี (5 Core Forensic Pillars)
1. **เรื่องที่ ๑ (Task 1): Interactive Forensic Architecture (PR Lens)**
   - แผนภาพสถาปัตยกรรมคดีและการเงิน 4 เลนแบบโต้ตอบ ([PR Lens Online Viewer](https://prlens.dev/c/TWOhzAyMhVEyK9KCVxe2EA))
2. **เรื่องที่ ๒ (Task 2): Beneficiary Network & Fraud Graph**
   - แดชบอร์ด HTML สกัด ๖ บุคคลเป้าหมายหลัก แยกแยะบัญชีม้า บัญชีรับผลประโยชน์แท้จริง และคัดกรองตัดกลุ่มบัญชีสั่งโอนแทน (`EDOK_NUI/FORENSIC_FRAUD_NETWORK_SYSTEM.html`)
3. **เรื่องที่ ๓ (Task 3): Deep Dive Vector Chat RAG Dossier**
   - เจาะลึกบทสนทนา 179 โหนด เชื่อมโยงบริบทคำพูดสั่งโอนเงิน วันเวลา ยอดเงิน และภาพหลักฐานมัดตัว (`EDOK_NUI/TARGET_CHAT_CONTEXT_VECTOR_DOSSIER.md`)
4. **เรื่องที่ ๔ (Task 4): Individual Court Indictment & Legal Charges**
   - แฟ้มสารบบคดีและสำนวนฟ้องร้องรายบุคคล วางฐานความผิด ป.อ. มาตรา ๓๔๑/๓๔๓ (ฉ้อโกงปกติธุระ), พ.ร.ก.กู้ยืมเงินฯ, พ.ร.บ.ฟอกเงิน, พ.ร.ก.บัญชีม้า ๒๕๖๖ (`EDOK_NUI/COURT_INDICTMENT_DOSSIER_INDIVIDUAL.md`)
5. **เรื่องที่ ๕ (Task 5): Chronological 11-Dimension Timeline & Defense-Busting Strategy**
   - ไทม์ไลน์รายบุคคล ๑๑ มิติสมบูรณ์แบบ พร้อมตารางคำถามซักค้านชี้นำเผด็จศึกพยาน (Killer Cross-Examination Matrix) พลิกเกมส์จากคดีแพ่งเป็นคดีอาญา (`EDOK_NUI/INDIVIDUAL_CHRONOLOGICAL_TIMELINE_DOSSIER.md`)

---

## 🧠 10 คลังสกิลนิติวิทยาศาสตร์ดิจิทัล (10 Forensic Agent Skills)
ระบบบรรจุชุดสกิลอัจฉริยะในโฟลเดอร์ `skills/` พร้อมใช้งานทันที:
1. `forensic-flow-lens`: วิเคราะห์และสร้างแผนภาพโฟลว์สถาปัตยกรรมคดีและการเงิน
2. `fraud-beneficiary-network`: จำแนกเครือข่ายบัญชีผู้รับโอนเงินและผู้รับผลประโยชน์แห่งคดี
3. `vector-chat-rag-deepdive`: สืบค้นบริบทแชทและถอดรหัสภาษาด้วย Vector Embeddings & RAG
4. `individual-court-indictment`: จัดทำแฟ้มสารบบคดีและสำนวนฟ้องร้องรายบุคคล
5. `chronological-11d-timeline`: สร้างไทม์ไลน์ ๑๑ มิติและกลยุทธ์ทำลายข้อต่อสู้ในชั้นศาล
6. `forensic-dedup-optimizer`: ตรวจจับและกำจัดไฟล์ซ้ำระดับไบนารีแฮช คืนพื้นที่ดิสก์
7. `master-strip-chunk-scanner`: สแกนภาพแคปจอยาวต่อเนื่อง 6,000+ px ด้วย OCR ขนาน 8 คอร์
8. `supplementary-court-motion`: จัดทำดัชนีพยานหลักฐานชุดเสริมและร่างคำแถลง ป.วิ.อ.
9. `killer-cross-examination`: สร้างสคริปต์คำถามซักค้านเผด็จศึกพยานในคอกศาล
10. `amlc-asset-freezing-gateway`: ร่างหนังสือขออายัดบัญชีเร่งด่วนและส่งเรื่อง ปปง.

---

## ⚡ 1-Click Launchers (การสั่งงานคลิกเดียว)
* 🌐 **`EDOK_NUI/1-CLICK_OPEN_FRAUD_NETWORK.bat`**: เปิดแดชบอร์ดเครือข่ายการเงินและบัญชีผู้รับผลประโยชน์ในเบราว์เซอร์
* 🔍 **`EDOK_NUI/1-CLICK_ASK_AI_RAG.bat`**: เรียกใช้ AI สืบค้นพยานหลักฐานแชทและสลิปด้วยเทคโนโลยี RAG
* 🚀 **`EDOK_NUI/1-CLICK_RUN_LEGAL_TRIAGE.bat`**: ประมวลผลจับคู่ข้อกฎหมายแพ่ง/อาญา อัปเดตแฟ้มสำนวนทันที
* 🔄 **`EDOK_NUI/1-CLICK_BUILD_TRANSCRIPT.bat`**: สกัดบทสนทนาและสลิป ร้อยเรียงไทม์ไลน์ต่อเนื่อง 100%

---

## 📂 โครงสร้างโฟลเดอร์สำคัญ (Repository Structure)
```
RAG-Eviden/
├── EDOK_NUI/
│   ├── SMOKING_GUNS/                      # ภาพหลักฐานมัดตัว 13 รายการ (หลักฐานจุดตายคดี)
│   ├── SLIP_THUMBS/                       # ภาพย่อสลิป 291 รายการสำหรับแสดงผลบนเว็บ
│   ├── FORENSIC_FRAUD_NETWORK_SYSTEM.html # แดชบอร์ดวิเคราะห์เครือข่ายบัญชีม้า Interactive
│   ├── BENEFICIARY_NETWORK_TABLE.html     # ตารางแจกแจงยอดเงินผู้รับโอนบริสุทธิ์ vs บัญชีม้า
│   ├── COURT_INDICTMENT_DOSSIER_INDIVIDUAL.md # สำนวนฟ้องร้องรายบุคคล ฐานความผิด ป.อ./ปปง.
│   ├── INDIVIDUAL_CHRONOLOGICAL_TIMELINE_DOSSIER.md # ไทม์ไลน์ 11 มิติ และตารางซักค้าน
│   ├── TARGET_CHAT_CONTEXT_VECTOR_DOSSIER.md # ผลการสืบค้นบริบทแชทลึก 179 โหนด
│   ├── SUPPLEMENTARY_EVIDENCE_INDEX_V3.md # ดัชนีพยานหลักฐานชุดเสริม Master Timeline Strip V3
│   └── NEW_362_FILES_SCAN_RESULTS.json    # ผลการสแกนขุดค้น 362 ไฟล์ใหม่
├── skills/                                # คลัง 10 สกิล Agent นิติวิทยาศาสตร์ดิจิทัล
├── pr-lens/                               # แผนภาพสถาปัตยกรรม PR Lens และ Walkthrough
├── requirements.txt                       # ไลบรารี Python สำหรับสภาพแวดล้อม
└── README.md                              # คู่มือเอกสารระบบ
```

---

## 🛠️ การติดตั้งสภาพแวดล้อม (Environment Setup)
```bash
# ติดตั้งไลบรารีที่จำเป็น
pip install -r requirements.txt
```

---

## 🔒 มาตรฐานความปลอดภัย (Security & PDPA Shield)
ระบบคุ้มกันภาพและข้อมูลตัวตนด้วย `.gitignore` แยกเก็บไฟล์มีเดียขนาดใหญ่ดิบ (>100MB) ไว้นอกกิต และคงไว้เฉพาะไฟล์พยานหลักฐานมัดตัว (Smoking Guns), แดชบอร์ด HTML และฐานข้อมูลวิเคราะห์ที่เป็น Single Source of Truth (SSOT)

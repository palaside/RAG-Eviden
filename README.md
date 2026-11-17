# 🏛️ ชวกม.2: DIGITAL FORENSICS, AI OCR & COURT DOSSIER PLATFORM
> **Project Name:** ชวกม.2 (Digital Evidence Investigation & Court Triage Engine)  
> **Author/Maintainer:** THE ROOT-ACCESS ARCHITECT  
> **Standard:** Court Forensic Aligned (ISO/IEC 27037 & พ.ร.บ.ธุรกรรมทางอิเล็กทรอนิกส์ พ.ศ. ๒๕๔๔)  
> **Status:** Production Ready (Immortal State)

---

## 📌 บทนำและวัตถุประสงค์ (Mission Statement)
ระบบแปลงสภาพภาพถ่ายหน้าจอแชท LINE และสลิปธุรกรรมธนาคาร ให้กลายเป็น **สำนวนพยานหลักฐานดิจิทัลมาตรฐานศาล** ที่สามารถค้นหาตัวอักษรได้ (Searchable PDF), ร้อยเรียงเหตุการณ์ต่อเนื่องนาทีต่อนาที (Master Chronological Transcript & Dossier) และประมวลผลจับคู่เข้ากับประมวลกฎหมายแพ่งและพาณิชย์ และประมวลกฎหมายอาญาแบบอัตโนมัติ (Legal Triage Engine)

---

## ⚡ 1-Click Launchers (การสั่งงานคลิกเดียว ไม่ต้องพิมพ์คำสั่ง)
* 🚀 **`1-CLICK_RUN_LEGAL_TRIAGE.bat`**: ประมวลผลจับคู่ข้อกฎหมายแพ่ง/อาญา อัปเดต `LEGAL_TRIAGE_DOSSIER.md` ทันที
* 🔄 **`1-CLICK_BUILD_TRANSCRIPT.bat`**: ถอดรหัสภาพแคปแชท 106 ภาพ ร้อยเรียงไทม์ไลน์สร้าง `MASTER_TRANSCRIPT_CHRONOLOGICAL.md` และ `COURT_TIMELINE_DOSSIER.md`
* 🔍 **`1-CLICK_SEARCH_EVIDENCE.bat`**: ค้นหาพยานหลักฐานด้วย AI NLP (BM25 + PyThaiNLP) ภายใน 0.05 วินาที

---

## 📂 สารบัญไฟล์สำคัญในระบบ (System Artifacts)
* 🧠 **[Knowledge.md](file:///d:/Project/ชวกม.2/Knowledge.md)**: บันทึกองค์ความรู้ฉบับสมบูรณ์ 8 บท ครอบคลุมเทคนิคและกฎหมายทั้งหมด
* 📑 **[FINAL_EVIDENCE_JINNIPHA_Searchable.pdf](file:///d:/Project/ชวกม.2/FINAL_EVIDENCE_JINNIPHA_Searchable.pdf)**: ไฟล์ PDF พยานหลักฐานสแกนที่ฝัง Text Layer ค้นหาและก๊อปปี้ภาษาไทยได้ใน 0.01 วิ
* ⚖️ **[LEGAL_TRIAGE_DOSSIER.md](file:///d:/Project/ชวกม.2/LEGAL_TRIAGE_DOSSIER.md)**: รายงานชี้เป้า 90 เหตุการณ์เข้าข่าย ป.พ.พ. (กู้ยืมเงิน, รับสภาพหนี้) และ ป.อ. (ฉ้อโกง)
* ⏱️ **[COURT_TIMELINE_DOSSIER.md](file:///d:/Project/ชวกม.2/COURT_TIMELINE_DOSSIER.md)**: สารบัญคดี 188 เหตุการณ์ แยกตาม วัน-เวลา-ผู้พูด-ยอดเงิน-ไฟล์ภาพ
* 📜 **[MASTER_TRANSCRIPT_CHRONOLOGICAL.md](file:///d:/Project/ชวกม.2/MASTER_TRANSCRIPT_CHRONOLOGICAL.md)**: บทละครแชทต่อเนื่อง 6,319 บรรทัด ตัดรอยต่อภาพซ้ำออก 100%

---

## 🛠️ การติดตั้งสภาพแวดล้อม (Environment Setup)
```bash
# ติดตั้งไลบรารีที่ล็อกเวอร์ชันสมบูรณ์
pip install -r requirements.txt
```

---

## 🔒 การคุ้มครองความปลอดภัย (PDPA & Security Shield)
ระบบคุ้มกันภาพและข้อมูลตัวตนด้วย `.gitignore` แยกเก็บตรรกะโปรแกรมและผลการวิเคราะห์เป็น SSOT ชัดเจน

# mistakes.md — Project Anti-Patterns & Zero-Recurrence Vault

> **Purpose:** คลังรวบรวมข้อผิดพลาด บทเรียน และกลไกป้องกัน (Poka-Yoke) เพื่อรับประกันว่า AI และทีมงานจะไม่ทำผิดซ้ำสอง  
> **Rule:** ทุกครั้งที่แก้บั๊กสำคัญเสร็จ ต้องบันทึกลงไฟล์นี้ทันที

---

## 🚫 Registered Mistakes & Poka-Yoke Guards

### MISTAKE-001: Premature Finality & False Confidence
- **Symptom:** AI รายงานว่างานเสร็จสิ้น 100% ทั้งที่ยังไม่ได้รันเทสต์จริง หรือเพียงแค่เขียนโค้ดเสร็จ
- **Root Cause:** สันนิษฐานเอาเอง (Assumption Bias) โดยไม่มี Log ยืนยัน
- **Poka-Yoke Solution:** บังคับรันคำสั่งตรวจสอบ (Exit Code 0) ก่อนใช้คำว่า `เสร็จสิ้น` หรือ `Verified` ทุกครั้ง

---

### MISTAKE-002: Hardcoding Absolute OS Paths
- **Symptom:** ใช้พาทฮาร์ดโค้ด `C:\Users\...` ทำให้โค้ดพังบน Linux/Docker หรือเครื่องอื่น
- **Root Cause:** ขาดความตระหนักต่อความต่างของสภาพแวดล้อม (Environment Blindness)
- **Poka-Yoke Solution:** ใช้ Relative Path หรือคำสั่งจัดการพาทมาตรฐาน (`path.resolve`, `os.path.join`, `pathlib.Path`) เสมอ

---

### MISTAKE-003: Uncontrolled Execution Loop (Token Burn)
- **Symptom:** ระบบ AI วนลูปแก้โค้ดตัวเองซ้ำแล้วซ้ำเล่าจนเสียโทเค็นมหาศาลโดยไม่ได้ผลลัพธ์
- **Root Cause:** ขาดกลไก Circuit Breaker
- **Poka-Yoke Solution:** จำกัดรอบการแก้ปัญหาอัตโนมัติไม่เกิน 3 รอบ (Max 3 Loops) หากยังไม่ผ่าน ให้ตัดการทำงานและส่งต่อให้มนุษย์ตัดสินใจทันที (`ESCALATE_HUMAN`)

---

### MISTAKE-004: Conflating Training with Non-Training Routine Missions (ขยะเอกสารปนเปื้อน)
- **Symptom:** AI เจนเอกสารหมวดฝึกอบรม (หนังสือเชิญวิทยากร, สป.3, ค่าอาหารกลางวัน, ทะเบียนบ้านแม่ค้า, ใบลงทะเบียน 35 คน) ใส่เข้าไปในเดือนที่เป็นการลงพื้นที่ตรวจติดตามปกติที่ไม่มีการอบรม
- **Root Cause:** ขาดความเข้าใจในระเบียบงบประมาณและการจัดสำนวน เจนเอกสารสุ่มสี่สุ่มห้าตามลิสต์เทมเพลตเดิม
- **Poka-Yoke Solution:** ยึดช่อง "วันจัดฝึกอบรม" ในโหมด Edit เป็นตัวตัดสินเด็ดขาด:
  - ถ้าว่างเปล่า ➔ ตัดเอกสารหมวดฝึกอบรมทิ้ง 100% ห้ามมีหลุดออกมาแม้แต่ใบเดียว
  - ถ้ามีกรอกวันที่ ➔ วันนั้นคือวันฝึกอบรมจริง จึงค่อยดึงชุดเอกสารอบรมมาประกอบร่าง

---

### MISTAKE-005: Location Hallucination & Artificial 2500 Capping (มโนสถานที่ & บีบตัวเลขหลอน)
- **Symptom:** มโนชื่อหมู่บ้านลอยๆ หรือพยายามปัดตัวเลขกิโลเมตร/งบประมาณให้เป็น 2,500 เป๊ะแบบผิดธรรมชาติ
- **Root Cause:** ไม่ได้ดึงพิกัดจริงจากฐานข้อมูล Google Maps / Place ID
- **Poka-Yoke Solution:** ทุกพิกัดสถานที่ต้องดึงจากฐานข้อมูล `village_dossier_data.js` ที่มี Google Place ID (`place_id` เช่น `ChIJ...`) กำกับเท่านั้น และระยะทาง/ยอดเงินให้คำนวณตามจริง สามารถเกิน 2,500 ได้ตามความจริงของเส้นทาง

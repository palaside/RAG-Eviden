# REVERSE PROMPTING TEMPLATE (DISCOVERY MODE)

Use this when user requirements are ambiguous (Confidence < 80%):

---
### ⚠️ สเปกยังไม่ชัดเจนเพียงพอ — ขอสอบถาม 3 คำถามเพื่อล็อกขอบเขต:
1. **เป้าหมายหลักของฟีเจอร์นี้คืออะไร?**
   - [A] รองรับผู้ใช้ทั่วไป (High Traffic / Public Facing)
   - [B] ใช้งานภายในทีม (Internal Admin / High Permission)
   - [C] งานทดลองต้นแบบ (PoC / Fast Feedback)
2. **ขอบเขตการจัดเก็บข้อมูล (Data Persistence):**
   - [A] Local-first / SQLite / IndexedDB (ทำงานได้แม้ Offline)
   - [B] Cloud Database (PostgreSQL / Supabase / Neon)
3. **ระดับความเร่งด่วน:**
   - [A] ต้องการแบบด่วนที่สุด เน้นทำงานได้ทันที (Fast-Exec)
   - [B] เน้นโครงสร้างมาตรฐาน พร้อมสเกลระยะยาว (Clean Architecture)

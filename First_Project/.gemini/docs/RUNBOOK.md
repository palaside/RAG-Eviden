# OPERATIONAL RUNBOOK (FULL-STACK EDITION)

## 🚀 Quick Start
1. **ติดตั้งและเชื่อมต่อระบบอัตโนมัติ:**
   ```bash
   node scripts/setup-project.js
   ```
2. **รันหน้าเว็บในเครื่อง (Development Mode):**
   ```bash
   npm run dev
   # เข้าใช้งานผ่าน: http://localhost:3000
   ```
3. **ซิงค์สกีมาลงฐานข้อมูล Neon PostgreSQL:**
   ```bash
   npm run db:push
   ```
4. **เปิดดูตารางและข้อมูลในฐานข้อมูลผ่านเบราว์เซอร์:**
   ```bash
   npm run db:studio
   ```
5. **ทดสอบ Build โค้ดสำหรับขึ้น Production:**
   ```bash
   npm run build
   ```

## 🔒 Deployment & Production Checklist
- [ ] ติดตั้ง Dependencies ครบถ้วน (`npm install`)
- [ ] ตั้งค่าตัวแปรระบบใน Production Dashboard (Vercel / Cloudflare)
- [ ] ทดสอบสร้างตารางใน Neon Database (`npm run db:push`)
- [ ] ตรวจสอบว่าไม่มี API Keys หรือ Secrets ค้างในโค้ด
- [ ] ผ่านเกณฑ์ 4-Tier Verification

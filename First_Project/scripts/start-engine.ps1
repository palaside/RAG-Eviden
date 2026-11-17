#!/usr/bin/env pwsh
# สคริปต์เริ่มระบบอัตโนมัติสำหรับ First_Project (PowerShell)
Write-Host "=== เริ่มการติดตั้ง dependencies (npm ci) ==="
# ใช้ npm ci เพื่อทำการติดตั้งที่ deterministic
npm ci

Write-Host "=== เริ่ม Dev Server (แยกโปรเซส) ==="
# เริ่ม dev server ใน background โดยใช้ Start-Process
Start-Process -FilePath "npm" -ArgumentList "run", "dev" -NoNewWindow -RedirectStandardOutput "dev.log" -RedirectStandardError "dev.err"

Write-Host "=== รัน Playwright E2E Tests (ถ้ามี) ==="
# ตรวจสอบว่า script test:e2e มีอยู่ใน package.json
if (npm run | Select-String "test:e2e") {
    npm run test:e2e
} else {
    Write-Host "ไม่มีสคริปต์ test:e2e; ข้ามการทดสอบ"
}

Write-Host "=== งานทั้งหมดเสร็จสิ้น ==="


@echo off
chcp 65001 >nul
title EVIDENCE AUTO HOOK DAEMON - ZERO-CLICK PIPELINE
color 0A
echo ==============================================================================
echo   🏛️ EVIDENCE AUTO HOOK DAEMON (ระบบตรวจจับและประมวลผลอัตโนมัติ)
echo ==============================================================================
echo.
echo   📂 โฟลเดอร์รับไฟล์ (Hot-Folder): d:\Project\ชวกม.2\incoming_evidence\
echo   💡 การทำงาน: แค่ลากไฟล์ภาพแชทหรือสลิปมาวางในโฟลเดอร์นี้
echo      ระบบจะประมวลผลหลังบ้าน และอัปเดตแฟ้มสำนวน 7 หน้า A4 ให้ทันที!
echo.
echo ==============================================================================
echo.

cd /d "d:\Project\ชวกม.2"
python evidence_auto_hook_daemon.py

pause

@echo off
chcp 65001 > nul
title ชวกม.2 - Legal Triage & Court Dossier Engine
echo ==============================================================================
echo [ชวกม.2] กำลังประมวลผลจับคู่ข้อกฎหมายแพ่งและอาญา (Legal Triage Engine)...
echo ==============================================================================
python "%~dp0run_legal_triage.py"
echo.
echo [เสร็จสมบูรณ์] ผลลัพธ์ถูกบันทึกที่: LEGAL_TRIAGE_DOSSIER.md
echo.
pause

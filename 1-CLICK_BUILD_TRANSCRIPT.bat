@echo off
chcp 65001 > nul
title ชวกม.2 - Reconstruct Master Transcript & Court Timeline
echo ==============================================================================
echo [ชวกม.2] กำลังประมวลผลร้อยเรียงไทม์ไลน์แชทนาทีต่อนาที...
echo ==============================================================================
python "%~dp0build_master_transcript.py"
echo.
echo [เสร็จสมบูรณ์] ผลลัพธ์:
echo 1. MASTER_TRANSCRIPT_CHRONOLOGICAL.md
echo 2. COURT_TIMELINE_DOSSIER.md
echo.
pause

@echo off
chcp 65001 > nul
title EDOK_NUI - AI Vector RAG Legal Search
echo ==============================================================================
echo [EDOK_NUI] ระบบถาม-ตอบพยานหลักฐานด้วย AI Vector RAG Engine
echo ==============================================================================
echo ตัวอย่างคำถามที่พิมพ์ได้:
echo  - น้ำหอมแตก
echo  - ยืมเงิน 2000
echo  - สัญญาว่าจะคืนเงิน
echo  - ไปถอดเหล็ก
echo  - เคลียร์
echo ==============================================================================
:loop
set /p USER_QUERY="พิมพ์คำถามหรือหัวข้อที่ต้องการค้นหา (กด Enter เพื่อออก): "
if "%USER_QUERY%"=="" goto end
python "%~dp0ask_ai_rag.py" "%USER_QUERY%"
echo.
goto loop
:end
pause

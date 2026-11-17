# 🛡️ LESSONS LEARNED & POKA-YOKE MISTAKES REGISTER

## 1. PowerShell Inline Python Quotes Syntax Error
- **Mistake:** Running multi-line python code with nested double quotes directly in `powershell -Command "python -c \"...\""` causes syntax and argument parsing errors.
- **Root Cause:** Windows PowerShell processes backticks and quotes differently than bash.
- **Poka-Yoke Fix:** Always write Python scripts to `.py` files and execute `python script.py`.

## 2. Windows PyMuPDF Thai Font Rendering
- **Mistake:** Inserting Thai text with default Helvetica or Arial in PyMuPDF leads to garbled glyphs or encoding failure in PDF search.
- **Root Cause:** Standard Type1 fonts lack Thai Unicode tables.
- **Poka-Yoke Fix:** Explicitly register and embed `C:\Windows\Fonts\tahoma.ttf` with `render_mode=3` (invisible text) for perfect copy-paste and searchability.

## 3. GPU VRAM Out-of-Memory on 2GB GTX 1050
- **Mistake:** Attempting to load 2.52GB Vision-Language weights into a 2GB GTX 1050 GPU causes CUDA OOM.
- **Root Cause:** Model size exceeds GPU physical VRAM.
- **Poka-Yoke Fix:** Auto-detect GPU VRAM and fallback to CPU (`torch.float32`), and use multi-threaded native Tesseract for instant bulk pre-processing.

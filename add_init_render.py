with open(r"d:\Project\ชวกม.2\index.html", "r", encoding="utf-8") as f:
    c = f.read()

target = "function clearAllEvidenceFiles() {\n  Task0EvidenceRegistry = [];\n  reconcileAndRenderTask0();\n}"
replacement = target + """

// เรียกเรนเดอร์กล่อง Staging Buffer และ KPI Summary Bar ทันทีเมื่อโหลดหน้าเว็บ
document.addEventListener('DOMContentLoaded', () => {
  renderStagingBufferCards();
});
"""

if target in c:
    c = c.replace(target, replacement)
    with open(r"d:\Project\ชวกม.2\index.html", "w", encoding="utf-8") as f:
        f.write(c)
    print("SUCCESS: Added DOMContentLoaded trigger.")
else:
    print("Target not found.")

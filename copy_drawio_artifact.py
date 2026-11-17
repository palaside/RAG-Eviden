import shutil

src = r"d:\Project\ชวกม.2\EDOK_NUI\REPO_SAMPLES\DRAWIO_ENTERPRISE_FLOW.jpg"
dst = r"C:\Users\EVE\.gemini\antigravity\brain\c8211d09-030e-4b24-8837-3ce9589aa4a6\DRAWIO_ENTERPRISE_FLOW.jpg"
shutil.copy2(src, dst)
print("Copied to artifact dir successfully!")

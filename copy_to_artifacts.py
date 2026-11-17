import shutil
import os

art_dir = r"C:\Users\EVE\.gemini\antigravity\brain\c8211d09-030e-4b24-8837-3ce9589aa4a6"
os.makedirs(art_dir, exist_ok=True)

files = [
    (r"d:\Project\ชวกม.2\EDOK_NUI\REPO_SAMPLES\ANTV_G6_KNOWLEDGE_GRAPH.jpg", os.path.join(art_dir, "ANTV_G6_KNOWLEDGE_GRAPH.jpg")),
    (r"d:\Project\ชวกม.2\EDOK_NUI\REPO_SAMPLES\REACT_FLOW_MODERN_CANVAS.jpg", os.path.join(art_dir, "REACT_FLOW_MODERN_CANVAS.jpg")),
    (r"d:\Project\ชวกม.2\EDOK_NUI\MONEY_FLOW_INFOGRAPHIC.png", os.path.join(art_dir, "MONEY_FLOW_INFOGRAPHIC.png"))
]

for src, dst in files:
    if os.path.exists(src):
        shutil.copy2(src, dst)
        print(f"Copied {os.path.basename(src)} -> {dst}")

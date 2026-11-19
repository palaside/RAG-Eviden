import os
from PIL import Image

assets_dir = r'd:\Project\ชวกม.2\EDOK_NUI\A4_EVIDENCE_ASSETS'

for f in sorted(os.listdir(assets_dir)):
    fp = os.path.join(assets_dir, f)
    if os.path.isfile(fp):
        with Image.open(fp) as img:
            w, h = img.size
            ratio = h / w if w > 0 else 0
            print(f"{f}: {w}x{h} px (ratio: {ratio:.2f})")

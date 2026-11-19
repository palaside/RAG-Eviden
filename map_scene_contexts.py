import json
import os
from PIL import Image

scenes_dir = r'd:\Project\ชวกม.2\EDOK_NUI\STORY_CHAT_SCENES'
cropped_assets_dir = r'd:\Project\ชวกม.2\EDOK_NUI\A4_CROPPED_ASSETS'
os.makedirs(cropped_assets_dir, exist_ok=True)

with open('compiled_scenes.json', 'r', encoding='utf-8') as f:
    scenes = json.load(f)

# Helper function to stitch multiple scenes vertically into one clean context box
def stitch_scenes(scene_nums, output_name):
    images = []
    for n in scene_nums:
        fn = f"SCENE_{n:03d}.png"
        fp = os.path.join(scenes_dir, fn)
        if os.path.exists(fp):
            images.append(Image.open(fp))
        else:
            print(f"Warning: {fp} not found")
    
    if not images:
        return None
    
    w = max(im.width for im in images)
    total_h = sum(im.height for im in images)
    
    stitched = Image.new('RGB', (w, total_h), (255, 255, 255))
    curr_y = 0
    for im in images:
        # paste
        stitched.paste(im, (0, curr_y))
        curr_y += im.height
        
    out_path = os.path.join(cropped_assets_dir, output_name)
    stitched.save(out_path)
    print(f"Saved stitched {output_name}: {w}x{total_h} px")
    return output_name

# Let's inspect scenes for key keywords
for s in scenes:
    b = s['bubble']
    for kw in ['ครีม', '50000', '500', 'น้าหอม', 'น้ำหอม', 'ถอดเหล็ก', 'สองแสน', '90,000', '7,000', 'รายวัน', 'ว่างงาน', '100', '4100', 'คนเก่า', '20000', '8000', '15000', 'แม๊ก', 'สบายใจ', '25000', '35000', '6000', 'ขาดประมาน']:
        if kw in b:
            print(f"Num {s['num']}: [{kw}] -> {b[:40]}")

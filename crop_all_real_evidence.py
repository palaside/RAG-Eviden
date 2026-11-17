# -*- coding: utf-8 -*-
import os
from PIL import Image

raw_ori = r'C:\Users\EVE\Downloads\ของมันคนเดียว-20261117T094313Z-1-003\ของมันคนเดียว\แคปหน้า Ori'
raw_root = r'C:\Users\EVE\Downloads\ของมันคนเดียว-20261117T094313Z-1-003\ของมันคนเดียว'
out_dirs = [
    r'd:\Project\ชวกม.2\EDOK_NUI\A4_EVIDENCE_ASSETS',
    r'C:\Users\EVE\.gemini\antigravity\brain\c8211d09-030e-4b24-8837-3ce9589aa4a6\A4_EVIDENCE_ASSETS'
]

for d in out_dirs:
    os.makedirs(d, exist_ok=True)

crop_tasks = [
    # Count 1 (800252756)
    ("LINE_capture_800252756.687906.jpg", raw_ori, (0, 1900, 636, 2800), "ctx_count_01_p1.png"),
    ("LINE_capture_800252756.687906.jpg", raw_ori, (0, 2800, 636, 3700), "ctx_count_01_p2.png"),
    
    # Count 2 (800252921)
    ("LINE_capture_800252921.297142.jpg", raw_ori, (0, 3400, 640, 4400), "ctx_count_02.png"),
    
    # Count 3 (800253182)
    ("LINE_capture_800253182.934029.jpg", raw_ori, (0, 1900, 638, 2800), "ctx_count_03.png"),
    
    # Count 4 (800253185)
    ("LINE_capture_800253185.789705.jpg", raw_ori, (0, 50, 644, 1150), "ctx_count_04_p1.png"),
    ("LINE_capture_800253185.789705.jpg", raw_ori, (0, 1150, 644, 2150), "ctx_count_04_p2.png"),
    
    # Count 5 (800253185 - ถอดเหล็ก 4,000)
    ("LINE_capture_800253185.789705.jpg", raw_ori, (0, 3900, 644, 4800), "ctx_count_05.png"),
    
    # Count 6 (800253252 - สองแสน / 90,000)
    ("LINE_capture_800253252.988857.jpg", raw_ori, (0, 3700, 640, 4650), "ctx_count_06_p1.png"),
    ("LINE_capture_800253252.988857.jpg", raw_ori, (0, 4900, 640, 5900), "ctx_count_06_p2.png"),
    
    # Count 7 (800253550 - 7,000 พัทยา)
    ("LINE_capture_800253550.895289.jpg", raw_ori, (0, 1500, 636, 2500), "ctx_count_07.png"),
    
    # Count 8-13 (800253553)
    ("LINE_capture_800253553.588898.jpg", raw_ori, (0, 2500, 638, 3350), "ctx_count_08.png"),
    ("LINE_capture_800253553.588898.jpg", raw_ori, (0, 3350, 638, 4150), "ctx_count_09.png"),
    ("LINE_capture_800253553.588898.jpg", raw_ori, (0, 4150, 638, 4850), "ctx_count_10.png"),
    ("LINE_capture_800253553.588898.jpg", raw_ori, (0, 4850, 638, 5600), "ctx_count_11.png"),
    ("LINE_capture_800253553.588898.jpg", raw_ori, (0, 5600, 638, 6264), "ctx_count_12.png"),
    ("LINE_capture_800253553.588898.jpg", raw_ori, (0, 1900, 638, 2600), "ctx_count_13.png"),
    
    # Count 14-16 (800254134)
    ("LINE_capture_800254134.610661.jpg", raw_ori, (0, 2800, 648, 3700), "ctx_count_14_p1.png"),
    ("LINE_capture_800254134.610661.jpg", raw_ori, (0, 3700, 648, 4500), "ctx_count_14_p2.png"),
    ("LINE_capture_800254134.610661.jpg", raw_ori, (0, 4500, 648, 5350), "ctx_count_15.png"),
    ("LINE_capture_800254134.610661.jpg", raw_ori, (0, 5350, 648, 6154), "ctx_count_16.png"),
    
    # Count 17-18 (800255060)
    ("LINE_capture_800255060.737309.jpg", raw_ori, (0, 2500, 638, 3500), "ctx_count_17.png"),
    ("LINE_capture_800255060.737309.jpg", raw_ori, (0, 3500, 638, 4600), "ctx_count_18.png"),
    
    # Count 19-21 (800256213)
    ("LINE_capture_800256213.882803.jpg", raw_ori, (0, 100, 828, 1100), "ctx_count_19.png"),
    ("LINE_capture_800256213.882803.jpg", raw_ori, (0, 1100, 828, 2000), "ctx_count_20.png"),
    ("LINE_capture_800256213.882803.jpg", raw_ori, (0, 2000, 828, 3000), "ctx_count_21.png"),
    
    # Count 22 (สนทนาแนบสลิป\01.9.68_IMG_6288.PNG)
    ("01.9.68_IMG_6288.PNG", os.path.join(raw_root, "สนทนาแนบสลิป"), (0, 0, 1080, 1150), "ctx_count_22_p1.png"),
    ("01.9.68_IMG_6288.PNG", os.path.join(raw_root, "สนทนาแนบสลิป"), (0, 1100, 1080, 2208), "ctx_count_22_p2.png"),
    
    # Count 23-26 (New folder slips)
    ("IMG_6090.PNG", os.path.join(raw_root, r"New folder\05.2.68"), None, "ctx_count_23.png"),
    ("IMG_6105.PNG", os.path.join(raw_root, r"New folder\17.2.68"), None, "ctx_count_24.png"),
    ("91AA7527-9CCF-499D-9972-27A7021A8460.png", os.path.join(raw_root, r"New folder\07.3.68"), None, "ctx_count_25.png"),
    ("IMG_6286.PNG", os.path.join(raw_root, r"New folder\20.8.68"), None, "ctx_count_26.png"),
    
    # Maew Counts
    ("IMG_6246.PNG", os.path.join(raw_root, r"New folder\03.6.68 พี่แมว"), (0, 0, 1080, 1100), "ctx_maew_01_p1.png"),
    ("IMG_6246.PNG", os.path.join(raw_root, r"New folder\03.6.68 พี่แมว"), (0, 1050, 1080, 2208), "ctx_maew_01_p2.png"),
    ("LINE_capture_796547198.800971.JPG", os.path.join(raw_root, r"New folder\08.6.68 พี่แมว"), None, "ctx_maew_02.png"),
    
    # Wanwisa & Tatsanee
    ("LINE_capture_796546686.053676.JPG", os.path.join(raw_root, r"New folder\27.5.68 พี่น้อง"), (0, 250, 1080, 1550), "ctx_wanwisa_01.png"),
    ("LINE_capture_796546686.053676.JPG", os.path.join(raw_root, r"New folder\27.5.68 พี่น้อง"), (0, 1500, 1080, 2836), "ctx_tatsanee_01.png")
]

print(f"Total tasks: {len(crop_tasks)}")
for fn, fdir, box, out_fn in crop_tasks:
    src_fp = os.path.join(fdir, fn)
    if not os.path.exists(src_fp):
        print(f"ERROR: Missing {src_fp}")
        continue
    im = Image.open(src_fp)
    if box:
        # adjust box if width exceeds
        x0, y0, x1, y1 = box
        x1 = min(x1, im.width)
        y1 = min(y1, im.height)
        cropped = im.crop((x0, y0, x1, y1))
    else:
        cropped = im
        
    for dest_dir in out_dirs:
        dest_fp = os.path.join(dest_dir, out_fn)
        cropped.save(dest_fp)
    print(f"Cropped {out_fn}: size {cropped.size} from {fn}")

print("ALL REAL EVIDENCE SCREENSHOTS CROPPED DIRECTLY FROM RAW ORIGINAL FILES!")

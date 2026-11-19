# -*- coding: utf-8 -*-
import os
from PIL import Image
import numpy as np

raw_ori = r'C:\Users\EVE\Downloads\ของมันคนเดียว-20261117T094313Z-1-003\ของมันคนเดียว\แคปหน้า Ori'
raw_root = r'C:\Users\EVE\Downloads\ของมันคนเดียว-20261117T094313Z-1-003\ของมันคนเดียว'

crops_def = [
    # fn, fdir, (x0, y0, x1, y1), out_fn
    ("LINE_capture_800252756.687906.jpg", raw_ori, (0, 2300, 636, 2730), "ctx_count_01_p1.png"),
    ("LINE_capture_800252921.297142.jpg", raw_ori, (0, 3600, 640, 4200), "ctx_count_02.png"),
    ("LINE_capture_800253182.934029.jpg", raw_ori, (0, 2150, 638, 2600), "ctx_count_03.png"),
    ("LINE_capture_800253185.789705.jpg", raw_ori, (0, 100, 644, 900), "ctx_count_04_p1.png"),
    ("LINE_capture_800253185.789705.jpg", raw_ori, (0, 4150, 644, 4650), "ctx_count_05.png"),
    ("LINE_capture_800253252.988857.jpg", raw_ori, (0, 3950, 640, 4550), "ctx_count_06_p1.png"),
    ("LINE_capture_800253550.895289.jpg", raw_ori, (0, 1600, 636, 2200), "ctx_count_07.png"),
    ("LINE_capture_800253553.588898.jpg", raw_ori, (0, 2650, 638, 3150), "ctx_count_08.png"),
    ("LINE_capture_800253553.588898.jpg", raw_ori, (0, 3500, 638, 4050), "ctx_count_09.png"),
    ("LINE_capture_800253553.588898.jpg", raw_ori, (0, 4250, 638, 4700), "ctx_count_10.png"),
    ("LINE_capture_800253553.588898.jpg", raw_ori, (0, 4950, 638, 5450), "ctx_count_11.png"),
    ("LINE_capture_800253553.588898.jpg", raw_ori, (0, 5650, 638, 6200), "ctx_count_12.png"),
    ("LINE_capture_800253553.588898.jpg", raw_ori, (0, 1950, 638, 2550), "ctx_count_13.png"),
    ("LINE_capture_800254134.610661.jpg", raw_ori, (0, 3300, 648, 3950), "ctx_count_14_p1.png"),
    ("LINE_capture_800254134.610661.jpg", raw_ori, (0, 4600, 648, 5250), "ctx_count_15.png"),
    ("LINE_capture_800254134.610661.jpg", raw_ori, (0, 5450, 648, 6100), "ctx_count_16.png"),
    ("LINE_capture_800255060.737309.jpg", raw_ori, (0, 2750, 638, 3350), "ctx_count_17.png"),
    ("LINE_capture_800255060.737309.jpg", raw_ori, (0, 3700, 638, 4400), "ctx_count_18.png"),
    ("LINE_capture_800256213.882803.jpg", raw_ori, (0, 150, 828, 850), "ctx_count_19.png"),
    ("LINE_capture_800256213.882803.jpg", raw_ori, (0, 1050, 828, 1750), "ctx_count_20.png"),
    ("LINE_capture_800256213.882803.jpg", raw_ori, (0, 2050, 828, 2750), "ctx_count_21.png"),
    ("01.9.68_IMG_6288.PNG", os.path.join(raw_root, "สนทนาแนบสลิป"), (0, 100, 1080, 1100), "ctx_count_22_p1.png"),
    ("01.9.68_IMG_6288.PNG", os.path.join(raw_root, "สนทนาแนบสลิป"), (0, 1100, 1080, 2200), "ctx_count_22_p2.png"),
    ("IMG_6090.PNG", os.path.join(raw_root, r"New folder\05.2.68"), None, "ctx_count_23.png"),
    ("IMG_6105.PNG", os.path.join(raw_root, r"New folder\17.2.68"), None, "ctx_count_24.png"),
    ("91AA7527-9CCF-499D-9972-27A7021A8460.png", os.path.join(raw_root, r"New folder\07.3.68"), None, "ctx_count_25.png"),
    ("IMG_6286.PNG", os.path.join(raw_root, r"New folder\20.8.68"), None, "ctx_count_26.png"),
    ("IMG_6246.PNG", os.path.join(raw_root, r"New folder\03.6.68 พี่แมว"), (0, 100, 1080, 1050), "ctx_maew_01_p1.png"),
    ("IMG_6246.PNG", os.path.join(raw_root, r"New folder\03.6.68 พี่แมว"), (0, 1050, 1080, 2200), "ctx_maew_01_p2.png"),
    ("LINE_capture_796547198.800971.JPG", os.path.join(raw_root, r"New folder\08.6.68 พี่แมว"), None, "ctx_maew_02.png"),
    ("LINE_capture_796546686.053676.JPG", os.path.join(raw_root, r"New folder\27.5.68 พี่น้อง"), (0, 300, 1080, 1500), "ctx_wanwisa_01.png"),
    ("LINE_capture_796546686.053676.JPG", os.path.join(raw_root, r"New folder\27.5.68 พี่น้อง"), (0, 1500, 1080, 2800), "ctx_tatsanee_01.png")
]

print("Checking Quiet Zones for each slice...")
for fn, fdir, box, out_fn in crops_def:
    fp = os.path.join(fdir, fn)
    if not os.path.exists(fp):
        print("Missing:", fp)
        continue
    im = Image.open(fp)
    if box:
        x0, y0, x1, y1 = box
        # check top slice variance (rows y0 to y0+10)
        arr = np.array(im.convert('RGB'))
        top_slice = arr[y0:y0+10, int(x1*0.2):int(x1*0.8)]
        bot_slice = arr[y1-10:y1, int(x1*0.2):int(x1*0.8)]
        top_var = np.var(top_slice)
        bot_var = np.var(bot_slice)
        print(f"{out_fn} ({x1-x0}x{y1-y0}): top_var={top_var:.1f}, bot_var={bot_var:.1f}")
    else:
        print(f"{out_fn} full image: {im.size}")

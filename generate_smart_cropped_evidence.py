import os
import json
from PIL import Image

scenes_dir = r'd:\Project\ชวกม.2\EDOK_NUI\STORY_CHAT_SCENES'
dl_root = r'C:\Users\EVE\Downloads\ของมันคนเดียว-20261117T094313Z-1-003\ของมันคนเดียว'
out_dir = r'd:\Project\ชวกม.2\EDOK_NUI\A4_CROPPED_ASSETS'
os.makedirs(out_dir, exist_ok=True)

def stitch(scene_nums, filename):
    imgs = []
    for n in scene_nums:
        fp = os.path.join(scenes_dir, f"SCENE_{n:03d}.png")
        if os.path.exists(fp):
            imgs.append(Image.open(fp))
    if not imgs:
        print("Missing scenes for", filename)
        return None
    w = max(im.width for im in imgs)
    total_h = sum(im.height for im in imgs)
    res = Image.new('RGB', (w, total_h), (255, 255, 255))
    y = 0
    for im in imgs:
        res.paste(im, (0, y))
        y += im.height
    dest = os.path.join(out_dir, filename)
    res.save(dest)
    print(f"Stitched {filename}: {w}x{total_h}")
    return filename

def crop_box(src_path, box, filename):
    if not os.path.exists(src_path):
        print("Missing src:", src_path)
        return None
    im = Image.open(src_path)
    cropped = im.crop(box)
    dest = os.path.join(out_dir, filename)
    cropped.save(dest)
    print(f"Cropped {filename}: {cropped.size}")
    return filename

# 1. Count 1: Part 1 (Scene 1, 2) & Part 2 (Scene 3, 6)
stitch([1, 2], 'ctx_count_01_p1.png')
stitch([3, 6], 'ctx_count_01_p2.png')

# 2. Count 2: Scene 7
stitch([7], 'ctx_count_02.png')

# 3. Count 3: Scene 8
stitch([8], 'ctx_count_03.png')

# 4. Count 4: Part 1 (Scene 9, 10, 11) & Part 2 (Scene 12)
stitch([9, 10, 11], 'ctx_count_04_p1.png')
stitch([12], 'ctx_count_04_p2.png')

# 5. Count 5: Scene 13
stitch([13], 'ctx_count_05.png')

# 6. Count 6: Part 1 (Scene 14, 16, 17) & Part 2 (Scene 20, 21)
stitch([14, 16, 17], 'ctx_count_06_p1.png')
stitch([20, 21], 'ctx_count_06_p2.png')

# 7. Count 7: Scene 25, 26
stitch([25, 26], 'ctx_count_07.png')

# 8. Count 8: Scene 27, 28
stitch([27, 28], 'ctx_count_08.png')

# 9. Count 9: Scene 28, 29
stitch([28, 29], 'ctx_count_09.png')

# 10. Count 10: Scene 29
stitch([29], 'ctx_count_10.png')

# 11. Count 11: Scene 33
stitch([33], 'ctx_count_11.png')

# 12. Count 12: Scene 38
stitch([38], 'ctx_count_12.png')

# 13. Count 13: Scene 40, 41
stitch([40, 41], 'ctx_count_13.png')

# 14. Count 14: Part 1 & Part 2
stitch([47, 48], 'ctx_count_14_p1.png')
stitch([49], 'ctx_count_14_p2.png')

# 15. Count 15: Scene 48, 49
stitch([48, 49], 'ctx_count_15.png')

# 16. Count 16: Scene 52
stitch([52], 'ctx_count_16.png')

# 17. Count 17: Scene 63, 64
stitch([63, 64], 'ctx_count_17.png')

# 18. Count 18: Scene 67, 68
stitch([67, 68], 'ctx_count_18.png')

# 19. Count 19: Scene 73, 74
stitch([73, 74], 'ctx_count_19.png')

# 20. Count 20: Scene 87, 88
stitch([87, 88], 'ctx_count_20.png')

# 21. Count 21: Scene 89, 90
stitch([89, 90], 'ctx_count_21.png')

# 22. Count 22 (01.9.68_IMG_6288.PNG): Part 1 (Chat/Call) & Part 2 (Slip ttb)
src_c22 = os.path.join(dl_root, 'สนทนาแนบสลิป', '01.9.68_IMG_6288.PNG')
crop_box(src_c22, (0, 0, 1242, 1100), 'ctx_count_22_p1.png')
crop_box(src_c22, (0, 950, 1242, 2208), 'ctx_count_22_p2.png')

# 23. Count 23 (IMG_6090.PNG): Slip 05.2.68
src_c23 = os.path.join(dl_root, 'New folder', '05.2.68', 'IMG_6090.PNG')
crop_box(src_c23, (0, 600, 1242, 2100), 'ctx_count_23.png')

# 24. Count 24 (IMG_6105.PNG): Slip 17.2.68
src_c24 = os.path.join(dl_root, 'New folder', '17.2.68', 'IMG_6105.PNG')
crop_box(src_c24, (0, 600, 1242, 2100), 'ctx_count_24.png')

# 25. Count 25 (91AA7527...): Slip 07.3.68
src_c25 = os.path.join(dl_root, 'New folder', '07.3.68', '91AA7527-9CCF-499D-9972-27A7021A8460.png')
crop_box(src_c25, (0, 600, 1242, 2100), 'ctx_count_25.png')

# 26. Count 26 (IMG_6286.PNG): Slip 20.8.68
src_c26 = os.path.join(dl_root, 'New folder', '20.8.68', 'IMG_6286.PNG')
crop_box(src_c26, (0, 600, 1242, 2100), 'ctx_count_26.png')

# Maew 1: Part 1 (Chat/Context) & Part 2 (Slip KBANK 9,000 note)
src_maew1 = os.path.join(dl_root, 'New folder', '03.6.68 พี่แมว', 'IMG_6246.PNG')
crop_box(src_maew1, (0, 0, 1242, 1000), 'ctx_maew_01_p1.png')
crop_box(src_maew1, (0, 900, 1242, 2208), 'ctx_maew_01_p2.png')

# Maew 2: Slip KBANK 13,500
src_maew2 = os.path.join(dl_root, 'New folder', '08.6.68 พี่แมว', 'LINE_capture_796547198.800971.JPG')
crop_box(src_maew2, (0, 1100, 828, 2592), 'ctx_maew_02.png')

# Wanwisa & Tatsanee: LINE_capture_796546686.053676.JPG
src_sisters = os.path.join(dl_root, 'New folder', '27.5.68 พี่น้อง', 'LINE_capture_796546686.053676.JPG')
crop_box(src_sisters, (0, 300, 828, 1600), 'ctx_wanwisa_01.png')
crop_box(src_sisters, (0, 1500, 828, 2836), 'ctx_tatsanee_01.png')

print("All smart cropped context images generated successfully!")

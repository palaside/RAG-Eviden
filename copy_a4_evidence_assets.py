import os
import shutil

assets_dir = r'd:\Project\ชวกม.2\EDOK_NUI\A4_EVIDENCE_ASSETS'
os.makedirs(assets_dir, exist_ok=True)

dl_root = r'C:\Users\EVE\Downloads\ของมันคนเดียว-20261117T094313Z-1-003\ของมันคนเดียว'

image_map = {
    'count_01': os.path.join(dl_root, 'แคปหน้า Ori', 'LINE_capture_800252756.687906.jpg'),
    'count_02': os.path.join(dl_root, 'แคปหน้า Ori', 'LINE_capture_800252921.297142.jpg'),
    'count_03': os.path.join(dl_root, 'แคปหน้า Ori', 'LINE_capture_800253182.934029.jpg'),
    'count_04': os.path.join(dl_root, 'แคปหน้า Ori', 'LINE_capture_800253185.789705.jpg'),
    'count_05': os.path.join(dl_root, 'แคปหน้า Ori', 'LINE_capture_800253185.789705.jpg'),
    'count_06': os.path.join(dl_root, 'แคปหน้า Ori', 'LINE_capture_800253252.988857.jpg'),
    'count_07': os.path.join(dl_root, 'แคปหน้า Ori', 'LINE_capture_800253550.895289.jpg'),
    'count_08': os.path.join(dl_root, 'แคปหน้า Ori', 'LINE_capture_800253553.588898.jpg'),
    'count_09': os.path.join(dl_root, 'แคปหน้า Ori', 'LINE_capture_800253553.588898.jpg'),
    'count_10': os.path.join(dl_root, 'แคปหน้า Ori', 'LINE_capture_800253553.588898.jpg'),
    'count_11': os.path.join(dl_root, 'แคปหน้า Ori', 'LINE_capture_800253553.588898.jpg'),
    'count_12': os.path.join(dl_root, 'แคปหน้า Ori', 'LINE_capture_800253553.588898.jpg'),
    'count_13': os.path.join(dl_root, 'แคปหน้า Ori', 'LINE_capture_800253553.588898.jpg'),
    'count_14': os.path.join(dl_root, 'แคปหน้า Ori', 'LINE_capture_800254134.610661.jpg'),
    'count_15': os.path.join(dl_root, 'แคปหน้า Ori', 'LINE_capture_800254134.610661.jpg'),
    'count_16': os.path.join(dl_root, 'แคปหน้า Ori', 'LINE_capture_800254134.610661.jpg'),
    'count_17': os.path.join(dl_root, 'แคปหน้า Ori', 'LINE_capture_800255060.737309.jpg'),
    'count_18': os.path.join(dl_root, 'แคปหน้า Ori', 'LINE_capture_800255060.737309.jpg'),
    'count_19': os.path.join(dl_root, 'แคปหน้า Ori', 'LINE_capture_800256213.882803.jpg'),
    'count_20': os.path.join(dl_root, 'แคปหน้า Ori', 'LINE_capture_800256213.882803.jpg'),
    'count_21': os.path.join(dl_root, 'แคปหน้า Ori', 'LINE_capture_800256213.882803.jpg'),
    'count_22': os.path.join(dl_root, 'สนทนาแนบสลิป', '01.9.68_IMG_6288.PNG'),
    'count_23': os.path.join(dl_root, 'New folder', '05.2.68', 'IMG_6090.PNG'),
    'count_24': os.path.join(dl_root, 'New folder', '17.2.68', 'IMG_6105.PNG'),
    'count_25': os.path.join(dl_root, 'New folder', '07.3.68', '91AA7527-9CCF-499D-9972-27A7021A8460.png'),
    'count_26': os.path.join(dl_root, 'New folder', '20.8.68', 'IMG_6286.PNG'),
    'maew_01': os.path.join(dl_root, 'New folder', '03.6.68 พี่แมว', 'IMG_6246.PNG'),
    'maew_02': os.path.join(dl_root, 'New folder', '08.6.68 พี่แมว', 'LINE_capture_796547198.800971.JPG'),
    'wanwisa_01': os.path.join(dl_root, 'New folder', '27.5.68 พี่น้อง', 'LINE_capture_796546686.053676.JPG'),
    'tatsanee_01': os.path.join(dl_root, 'New folder', '27.5.68 พี่น้อง', 'LINE_capture_796546686.053676.JPG')
}

copied = {}
for key, src in image_map.items():
    if os.path.exists(src):
        ext = os.path.splitext(src)[1]
        dest_fn = f"{key}{ext}"
        dest_path = os.path.join(assets_dir, dest_fn)
        shutil.copy(src, dest_path)
        copied[key] = dest_fn
    else:
        print(f"FAILED to find {key} at {src}")

print(f"Total successfully copied: {len(copied)} / {len(image_map)}")

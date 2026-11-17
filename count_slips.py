import os

BASE_DIR = r"C:\Users\EVE\Downloads\ของมันคนเดียว-20261117T094313Z-1-003\ของมันคนเดียว"

root_files = [f for f in os.listdir(BASE_DIR) if os.path.isfile(os.path.join(BASE_DIR, f))]
img_slips = [f for f in root_files if f.upper().startswith("IMG_") and f.lower().endswith(('.jpg', '.png', '.jpeg'))]

print(f"Total root files: {len(root_files)}")
print(f"Total IMG_ files in root: {len(img_slips)}")

slip_subfolder = os.path.join(BASE_DIR, "สนทนาแนบสลิป")
sub_files = [f for f in os.listdir(slip_subfolder) if os.path.isfile(os.path.join(slip_subfolder, f))]
print(f"Total files in สนทนาแนบสลิป: {len(sub_files)}")

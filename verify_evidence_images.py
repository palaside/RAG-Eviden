import os
import re

dl_root = r'C:\Users\EVE\Downloads\ของมันคนเดียว-20261117T094313Z-1-003\ของมันคนเดียว'

# Let's map files
ori_chats = {}
for f in os.listdir(os.path.join(dl_root, 'แคปหน้า Ori')):
    ori_chats[f] = os.path.join(dl_root, 'แคปหน้า Ori', f)

slips_with_chat = {}
for f in os.listdir(os.path.join(dl_root, 'สนทนาแนบสลิป')):
    slips_with_chat[f] = os.path.join(dl_root, 'สนทนาแนบสลิป', f)

new_folder_files = {}
nf_dir = os.path.join(dl_root, 'New folder')
for sub in os.listdir(nf_dir):
    sub_path = os.path.join(nf_dir, sub)
    if os.path.isdir(sub_path):
        for f in os.listdir(sub_path):
            new_folder_files[f"{sub}/{f}"] = os.path.join(sub_path, f)

print(f"Mapped {len(ori_chats)} in แคปหน้า Ori")
print(f"Mapped {len(slips_with_chat)} in สนทนาแนบสลิป")
print(f"Mapped {len(new_folder_files)} in New folder")

# Test lookups
print("800252756 in Ori:", 'LINE_capture_800252756.687906.jpg' in ori_chats)
print("01.9.68 in slips:", '01.9.68_IMG_6288.PNG' in slips_with_chat)
for k in new_folder_files:
    if 'พี่แมว' in k or 'พี่น้อง' in k:
        print("  Found entity file:", k)

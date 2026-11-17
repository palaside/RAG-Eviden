import os

BASE_DIR = r"C:\Users\EVE\Downloads\ของมันคนเดียว-20261117T094313Z-1-003\ของมันคนเดียว"

slip_files = []
for root, dirs, files in os.walk(BASE_DIR):
    for f in files:
        low = f.lower()
        if low.endswith(('.png', '.jpg', '.jpeg', '.pdf')):
            full_path = os.path.join(root, f)
            rel_path = os.path.relpath(full_path, BASE_DIR)
            slip_files.append((rel_path, full_path, os.path.getsize(full_path)))

print(f"Total media files found: {len(slip_files)}")

# Count by folder
folder_counts = {}
for rel, full, sz in slip_files:
    top_folder = rel.split(os.sep)[0]
    folder_counts[top_folder] = folder_counts.get(top_folder, 0) + 1

for folder, cnt in folder_counts.items():
    print(f"  - {folder}: {cnt} files")

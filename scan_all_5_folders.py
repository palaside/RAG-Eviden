import os, sys, pytesseract, json
from PIL import Image
from concurrent.futures import ThreadPoolExecutor

os.environ['TESSDATA_PREFIX'] = r'D:\Models\tessdata'
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

base_dir = r'C:\Users\EVE\Downloads\ของมันคนเดียว-20261117T094313Z-1-003\ของมันคนเดียว'
target_folders = ['สนทนาแนบสลิป', 'New folder']

all_images = []
for folder in target_folders:
    fp = os.path.join(base_dir, folder)
    if os.path.exists(fp):
        for root, dirs, files in os.walk(fp):
            for f in files:
                if f.lower().endswith(('.png', '.jpg', '.jpeg')):
                    all_images.append(os.path.join(root, f))

print(f'Total images across folders to scan: {len(all_images)}', flush=True)

keywords = ['ปรียชาติ', 'ฉิมพลี', 'จิณห์นิภา', 'วันวิศา', 'ทัศนี', 'เบญจมาศ', 'สุธีรัตน์', 'พี่แมว', 'คืน', 'ยอด']

def process_img(p):
    try:
        with Image.open(p) as im:
            im.thumbnail((800, 1400))
            txt = pytesseract.image_to_string(im, lang='tha+eng')
            found = [kw for kw in keywords if kw in txt]
            if found:
                rel = os.path.relpath(p, base_dir)
                return (rel, found, txt)
    except Exception as e:
        pass
    return None

results = []
with ThreadPoolExecutor(max_workers=8) as executor:
    for res in executor.map(process_img, all_images):
        if res:
            rel, found, txt = res
            print(f'>>> Match in {rel}: {found}', flush=True)
            results.append({'file': rel, 'keywords': found, 'snippet': txt[:350]})

out_json = r'D:\Project\ชวกม.2\new_folders_evidence.json'
with open(out_json, 'w', encoding='utf-8') as f_out:
    json.dump(results, f_out, ensure_ascii=False, indent=2)

print(f'Saved {len(results)} matches to {out_json} successfully!', flush=True)

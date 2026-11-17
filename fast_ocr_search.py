import os, sys, pytesseract
from PIL import Image
from concurrent.futures import ThreadPoolExecutor

sub_dir = r'C:\Users\EVE\Downloads\ของมันคนเดียว-20261117T094313Z-1-003\ของมันคนเดียว\สนทนาแนบสลิป'
files = [f for f in os.listdir(sub_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

print(f'Starting fast scan on {len(files)} files...', flush=True)

keywords = ['ทัศนีกาล', 'ทัศนีย์', 'ทัศน์', 'ทัศน', 'ทัส']

def process_file(f):
    p = os.path.join(sub_dir, f)
    try:
        with Image.open(p) as im:
            # resize for 10x faster OCR
            im.thumbnail((800, 1200))
            txt = pytesseract.image_to_string(im, lang='tha')
            for kw in keywords:
                if kw in txt:
                    return (f, kw, txt)
    except Exception as e:
        pass
    return None

matches = []
with ThreadPoolExecutor(max_workers=6) as executor:
    for res in executor.map(process_file, files):
        if res:
            f, kw, txt = res
            print(f'>>> FOUND {kw} in {f}!', flush=True)
            for l in txt.splitlines():
                if kw in l:
                    print(f'    Line: {l.strip()}', flush=True)
            matches.append(res)

print(f'Fast scan complete. Found {len(matches)} matches.', flush=True)

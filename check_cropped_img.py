import re

with open('EDOK_NUI/CHAT_FORENSIC_VECTOR_EXPLORER.html', 'r', encoding='utf-8') as f:
    text = f.read()

for m in re.finditer(r'"cropped_img":\s*"([^"]+)"', text):
    print(m.group(1))

import re

with open(r'd:\Project\ชวกม.2\build_court_dossier_smart_cropped.py', 'r', encoding='utf-8') as f:
    text = f.read()

matches = re.findall(r'"count_title": "([^"]+)".{0,1500}?"has_p2": True', text, re.DOTALL)
for m in matches:
    print('has_p2 True:', m)

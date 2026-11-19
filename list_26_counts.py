import json

with open(r'd:\Project\ชวกม.2\EDOK_NUI\EXPLICIT_MONEY_ROWS.json', 'r', encoding='utf-8') as f:
    rows = json.load(f)

for r in rows:
    c = r.get('count_no')
    amt = r.get('amount')
    img = r.get('image')
    txt = r.get('text', '').replace('\n', ' ')
    print(f"Count {c}: {amt} THB | {img} | {txt[:60]}")

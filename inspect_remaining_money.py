import json

with open('EDOK_NUI/EXPLICIT_MONEY_ROWS.json', 'r', encoding='utf-8') as f:
    rows = json.load(f)

print(f"Total: {len(rows)}")
for i in range(30, len(rows)):
    r = rows[i]
    print(f"Seq {r['seq']}: {r['clean_money']} บ. | {r['datetime']} | {r['chat'][:50]}")

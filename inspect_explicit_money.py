import json
import re

with open('EDOK_NUI/JINNIPHA_BORROW_ROWS.json', 'r', encoding='utf-8') as f:
    rows = json.load(f)

print(f"Total rows: {len(rows)}")

# Let's inspect rows with non-dash amounts
explicit_counts = []
for r in rows:
    m = r['money']
    clean_m = m.replace('*', '').replace('บาท', '').replace(',', '').strip()
    if clean_m and clean_m != '-':
        explicit_counts.append({
            'seq': r['seq'],
            'datetime': r['datetime'],
            'money_raw': m,
            'clean_money': clean_m,
            'chat': r['chat'],
            'ref': r['ref']
        })

print(f"Rows with explicit money in table: {len(explicit_counts)}")
for ec in explicit_counts[:30]:
    print(f"Seq {ec['seq']}: {ec['clean_money']} บ. | {ec['datetime']} | {ec['chat']}")

with open('EDOK_NUI/EXPLICIT_MONEY_ROWS.json', 'w', encoding='utf-8') as f:
    json.dump(explicit_counts, f, ensure_ascii=False, indent=2)

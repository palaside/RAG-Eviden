import re
import json

with open('COURT_TIMELINE_DOSSIER.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

table_rows = [l.strip() for l in lines if l.startswith('|') and not l.startswith('| ลำดับ') and not l.startswith('| :---')]

print(f"Total table rows: {len(table_rows)}")

parsed = []
for r in table_rows:
    cols = [c.strip() for c in r.split('|')[1:-1]]
    if len(cols) >= 6:
        seq = cols[0]
        dt = cols[1]
        actor = cols[2]
        chat = cols[3]
        money = cols[4]
        ref = cols[5]
        parsed.append({
            'seq': seq,
            'datetime': dt,
            'actor': actor,
            'chat': chat,
            'money': money,
            'ref': ref
        })

print(f"Successfully parsed {len(parsed)} rows.")

# Let's inspect rows with money
money_rows = [p for p in parsed if p['money'] != '-' and p['money'] != '']
print(f"Rows with explicit money: {len(money_rows)}")

# Let's inspect rows where chat indicates borrowing or asking for money
borrow_rows = []
for p in parsed:
    c = p['chat']
    m = p['money']
    if any(k in c for k in ['ยืม', 'โอน', 'กู้', 'ตังค์', 'เงิน', 'บาท', 'พัน', 'ขาด', 'ปิดงาน', 'เคลียร์']) or m != '-':
        borrow_rows.append(p)

print(f"Rows indicating borrowing / asking money: {len(borrow_rows)}")

with open('EDOK_NUI/JINNIPHA_BORROW_ROWS.json', 'w', encoding='utf-8') as f:
    json.dump(borrow_rows, f, ensure_ascii=False, indent=2)

print("Saved to EDOK_NUI/JINNIPHA_BORROW_ROWS.json")

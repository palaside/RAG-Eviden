import json

with open('D:/Project/ชวกม.2/BENEFICIARY_DATA.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print('Total beneficiaries in JSON:', len(data))
for b in data[:12]:
    name = b.get('name')
    amt = b.get('total_amount')
    slips = len(b.get('slips', []))
    print(f'Name: {name} | Total: {amt:,} THB | Slips: {slips}')

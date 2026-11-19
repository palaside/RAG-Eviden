# -*- coding: utf-8 -*-
import json

with open('EDOK_NUI/BENEFICIARY_TRANSACTION_RECORDS.json', 'r', encoding='utf-8') as f:
    records = json.load(f)

unspecified = [r for r in records if r['recipient'] == 'ไม่ระบุ / ตรวจสอบพิกเซล']
print(f"Unspecified count: {len(unspecified)}")

for u in unspecified[:15]:
    print("="*60)
    print("FILE:", u['file'], "| AMT:", u['amount'], "| BANK:", u['bank'], "| REF:", u['ref_no'])
    print("Snippet:", u['full_snippet'][:180])

import json

with open('EDOK_NUI/EVIDENCE_COUNTS_30.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"Total counts: {len(data)}")
for i, d in enumerate(data):
    p2 = " [HAS P2]" if d.get("has_p2") else ""
    c_no = d.get("count_no")
    person = d.get("person")
    amount = d.get("amount")
    dt = d.get("datetime")
    print(f"{i+1:02d}. {c_no} - {person}: {amount} ({dt}){p2}")

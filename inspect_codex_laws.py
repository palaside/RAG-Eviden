import json

with open(r'D:\Project\Digital Evi - Codex\RAW\thai_law_master_reference.json', 'r', encoding='utf-8') as f:
    laws = json.load(f)

for p in laws['statutory_provisions']:
    print(f"ID: {p['id']}")
    print(f"  Law: {p['law_code']} {p['section']}")
    print(f"  Title: {p['title']}")
    print(f"  Related: {p.get('related_laws', [])}")
    print(f"  Summary: {p.get('legal_summary', '')}")
    print(f"  Court Annotation: {p.get('court_annotation_template', '')}")
    print("-" * 50)

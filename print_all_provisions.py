import json

with open(r'D:\Project\Digital Evi - Codex\RAW\thai_law_master_reference.json', 'r', encoding='utf-8') as f:
    laws = json.load(f)

for i, p in enumerate(laws['statutory_provisions']):
    print(f"{i+1}. [{p['id']}] {p['law_code']} {p['section']}: {p['title']}")
    print(f"   Category: {p.get('category', '')}")
    print(f"   Related: {p.get('related_laws', [])}")
    print(f"   Annotation: {p.get('court_annotation_template', '')}")
    print()

import json
import re

# Read generate_responsive_suite.py to inspect EVIDENCE_COUNTS
with open('generate_responsive_suite.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Find the list of evidence dicts
counts = re.findall(r'"count_no":\s*"([^"]+)"', text)
print(f"Total count_no entries in generate_responsive_suite.py: {len(counts)}")
for i, c in enumerate(counts[:10]):
    print(f"  {i+1}: {c}")

# Check INDIVIDUAL_INDICTMENT_DOSSIER.json
try:
    with open('EDOK_NUI/INDIVIDUAL_INDICTMENT_DOSSIER.json', 'r', encoding='utf-8') as f:
        dossier = json.load(f)
    print("\nDefendants in INDIVIDUAL_INDICTMENT_DOSSIER.json:")
    for d in dossier.get('defendants', []):
        print(f"  - {d.get('name')}: {d.get('role')} (Counts: {len(d.get('counts', []))})")
except Exception as e:
    print(f"Error loading dossier: {e}")

# Check FORENSIC_CHAT_EVIDENCE_DATA.json
try:
    with open('EDOK_NUI/FORENSIC_CHAT_EVIDENCE_DATA.json', 'r', encoding='utf-8') as f:
        chat_data = json.load(f)
    print("\nPillars in FORENSIC_CHAT_EVIDENCE_DATA.json:")
    for k in chat_data.keys():
        print(f"  - {k}: {len(chat_data[k]) if isinstance(chat_data[k], list) else type(chat_data[k])}")
except Exception as e:
    print(f"Error loading chat_data: {e}")

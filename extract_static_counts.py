import json
import ast

with open('build_court_dossier_smart_cropped.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

counts_code = "".join(lines[10:722])
# Evaluate safely
counts = ast.literal_eval(counts_code.split("counts = ", 1)[1].strip())
print(f"Parsed {len(counts)} counts.")

# Clean any non-serializable fields if any
with open('EDOK_NUI/EVIDENCE_COUNTS_30.json', 'w', encoding='utf-8') as f:
    json.dump(counts, f, ensure_ascii=False, indent=2)

print("Saved EDOK_NUI/EVIDENCE_COUNTS_30.json successfully!")

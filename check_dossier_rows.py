import os

path = r"d:\Project\ชวกม.2\EDOK_NUI\LEGAL_TRIAGE_DOSSIER.md"
with open(path, "r", encoding="utf-8") as f:
    lines = f.readlines()

rows = []
for line in lines:
    if line.startswith("|") and not line.startswith("| ลำดับ") and not line.startswith("| :---"):
        parts = [p.strip() for p in line.split("|")[1:-1]]
        if len(parts) >= 6:
            rows.append(parts)

print(f"Total parsed legal triage rows: {len(rows)}")
for r in rows[:3]:
    print(r)

import json
from build_court_dossier_smart_cropped import counts

print(f"Loaded {len(counts)} counts.")
summary = []
for i, c in enumerate(counts):
    summary.append({
        "idx": i + 1,
        "count_no": c.get("count_no"),
        "title": c.get("count_title"),
        "person": c.get("person"),
        "person_role": c.get("person_role"),
        "amount": c.get("amount"),
        "datetime": c.get("datetime"),
        "ref": c.get("ref"),
        "has_p2": c.get("has_p2", False)
    })

with open("counts_summary.json", "w", encoding="utf-8") as f:
    json.dump(summary, f, ensure_ascii=False, indent=2)

print("Saved counts_summary.json successfully.")
for s in summary[:10]:
    print(f"[{s['idx']:02d}] {s['count_no']} | {s['person']} | {s['amount']} | {s['datetime']}")

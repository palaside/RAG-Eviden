import json

with open('compiled_scenes.json', 'r', encoding='utf-8') as f:
    scenes = json.load(f)

for s in scenes[:30]:
    print(f"Num {s['num']}: {s['file']} | {s['amount']} | {s['bubble'][:50]}")

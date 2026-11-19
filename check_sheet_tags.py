with open('EDOK_NUI/VECTOR_EVIDENCE/COUNT_01_RESPONSIVE.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if '<table' in l:
        print(f"Table starts at line {i+1}")
    if '</table' in l:
        print(f"Table ends at line {i+1}")
    if '<img' in l or '<svg' in l:
        print(f"Media tag at line {i+1}: {l.strip()[:80]}")

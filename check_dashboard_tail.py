with open('EDOK_NUI/VECTOR_EVIDENCE/VECTOR_EVIDENCE_DASHBOARD.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(f"Total lines: {len(lines)}")
# Look at the end of the file (scripts, footer)
for i in range(max(0, len(lines)-60), len(lines)):
    print(f"{i+1}: {lines[i]}", end='')

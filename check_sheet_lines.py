with open('EDOK_NUI/VECTOR_EVIDENCE/COUNT_01_RESPONSIVE.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(315, min(len(lines), 332)):
    l = lines[i]
    if len(l) > 120:
        l = l[:120] + '... [truncated base64]\n'
    print(f"{i+1}: {l}", end='')

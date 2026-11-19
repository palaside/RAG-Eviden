import os, re

files = [
    'TARGET_FOCUS_SELECTOR.html',
    'BENEFICIARY_NETWORK_DASHBOARD.html',
    'VECTOR_EVIDENCE/VECTOR_EVIDENCE_DASHBOARD.html',
    'TIMELINE_11D_DASHBOARD.html',
    'INDIVIDUAL_COURT_INDICTMENT_DASHBOARD.html',
    'MASTER_SSOT_STITCH_VIEWER.html',
    'CHAT_FORENSIC_VECTOR_EXPLORER.html',
    'AGENT6_PRESIDENT_SUPREME_COURT_DASHBOARD.html'
]

for fname in files:
    p = os.path.join('d:/Project/ชวกม.2/EDOK_NUI', fname)
    with open(p, 'r', encoding='utf-8') as fp:
        c = fp.read()
    print(f'=== {fname} ===')
    for m in re.finditer(r'(class=[\'"][^\'"]*(?:nav|tab)[^\'"]*[\'"]|id=[\'"][^\'"]*(?:nav|tab)[^\'"]*[\'"])', c, re.IGNORECASE):
        print(' ', m.group(0))

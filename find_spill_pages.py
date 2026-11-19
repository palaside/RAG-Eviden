import fitz

doc = fitz.open(r'd:\Project\ชวกม.2\EDOK_NUI\COURT_A4_EVIDENCE_DOSSIER.pdf')
for i, page in enumerate(doc):
    txt = page.get_text()
    lines = [l.strip() for l in txt.split('\n') if l.strip()]
    if len(lines) < 5:
        print(f"Page {i+1} has only {len(lines)} lines: {lines}")

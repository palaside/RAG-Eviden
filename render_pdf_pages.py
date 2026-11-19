# -*- coding: utf-8 -*-
import fitz # pymupdf
import os

pdf_path = r'd:\Project\ชวกม.2\EDOK_NUI\COURT_A4_EVIDENCE_DOSSIER.pdf'
doc = fitz.open(pdf_path)
print(f"Total pages in PDF: {len(doc)}")

out_dir = r'd:\Project\ชวกม.2\EDOK_NUI\PDF_PREVIEW_PAGES'
os.makedirs(out_dir, exist_ok=True)

# Render first 8 pages
for page_num in range(min(10, len(doc))):
    page = doc[page_num]
    pix = page.get_pixmap(dpi=150)
    out_png = os.path.join(out_dir, f"page_{page_num+1:02d}.png")
    pix.save(out_png)
    print(f"Rendered Page {page_num+1}: {out_png} ({pix.width}x{pix.height})")

import pymupdf as fitz
import re

pdf_path = r"C:\Users\EVE\Downloads\ของมันคนเดียว-20261117T094313Z-1-003\ของมันคนเดียว\FINAL_EVIDENCE_JINNIPHA.pdf"
doc = fitz.open(pdf_path)

print(f"Total pages in FINAL_EVIDENCE_JINNIPHA.pdf: {len(doc)}")

for page_idx in range(len(doc)):
    page = doc[page_idx]
    text = page.get_text()
    lines = [l.strip() for l in text.split("\n") if l.strip()]
    print(f"\n--- Page {page_idx + 1} ({len(lines)} lines of text) ---")
    for l in lines[:15]:
        print(f"  {l}")

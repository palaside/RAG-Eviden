@echo off
chcp 65001 > nul
title ชวกม.2 - Search Evidence Vault
echo ==============================================================================
echo [ชวกม.2] ระบบค้นหาพยานหลักฐานความเร็วสูง (BM25 + PyThaiNLP)
echo ==============================================================================
set /p QUERY="พิมพ์คำค้นหาที่ต้องการ (เช่น น้ำหอมแตก, โอนเงิน, 5000): "
python -c "
import json, sys
from rank_bm25 import BM25Okapi
from pythainlp.tokenize import word_tokenize

q = sys.argv[1]
with open(r'%~dp0evidence_vault.jsonl', 'r', encoding='utf-8') as f:
    docs = [json.loads(line) for line in f]

corpus = [d['text'] for d in docs]
tokenized_corpus = [word_tokenize(doc, engine='newmm') for doc in corpus]
bm25 = BM25Okapi(tokenized_corpus)
tokenized_query = word_tokenize(q, engine='newmm')
scores = bm25.get_scores(tokenized_query)
ranked = sorted(zip(scores, docs), key=lambda x: x[0], reverse=True)

print(f'\n--- ผลการค้นหาคำว่า: {q} ---')
found = 0
for score, doc in ranked[:5]:
    if score > 0:
        found += 1
        print(f'[Score: {score:.3f}] {doc[\"file\"]} (หน้า {doc[\"page\"]})')
        print(f'ตัวอย่างเนื้อหา: {doc[\"text\"][:200]}...\n')

if found == 0:
    print('ไม่พบข้อความที่ตรงกัน')
" "%QUERY%"
pause

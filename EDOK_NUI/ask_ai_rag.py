import json
import sys
import os
from pythainlp.tokenize import word_tokenize
from rank_bm25 import BM25Okapi

VECTOR_JSONL_PATH = r"d:\Project\ชวกม.2\EDOK_NUI\timeline_vector_embeddings.jsonl"
LEGAL_DOSSIER_PATH = r"d:\Project\ชวกม.2\EDOK_NUI\LEGAL_TRIAGE_DOSSIER.md"

def load_vector_vault():
    docs = []
    with open(VECTOR_JSONL_PATH, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                docs.append(json.loads(line))
    return docs

def build_rag_index(docs):
    corpus_tokens = []
    for d in docs:
        full_text = f"{d['content']} {d['timestamp']} {d['speaker']} {d['amount']} {d['reference_image']}"
        tokens = word_tokenize(full_text, engine="newmm")
        corpus_tokens.append(tokens)
    bm25 = BM25Okapi(corpus_tokens)
    return bm25

def query_rag(query, docs, bm25, top_k=5):
    q_tokens = word_tokenize(query, engine="newmm")
    scores = bm25.get_scores(q_tokens)
    ranked = sorted(zip(scores, docs), key=lambda x: x[0], reverse=True)
    results = [doc for score, doc in ranked[:top_k] if score > 0]
    return results

def answer_financial_summary(docs):
    total_requested = 0
    monetary_events = []
    import re
    for d in docs:
        amt_str = d.get("amount", "")
        m = re.search(r"(\d[\d,]*)", amt_str)
        if m and d.get("is_monetary_event", False):
            val = int(m.group(1).replace(",", ""))
            if val > 0:
                total_requested += val
                monetary_events.append((d, val))
    return total_requested, monetary_events

if __name__ == "__main__":
    docs = load_vector_vault()
    bm25 = build_rag_index(docs)
    
    if len(sys.argv) > 1:
        query = " ".join(sys.argv[1:])
    else:
        query = input("พิมพ์คำค้นหาหรือคำถามทางคดี (เช่น น้ำหอมแตก, ขอยืมเงิน, สัญญาคืนเงิน): ")
        
    print("\n" + "="*70)
    print(f"🔍 [RAG VECTOR ENGINE] วิเคราะห์คำถาม: '{query}'")
    print("="*70)
    
    hits = query_rag(query, docs, bm25, top_k=6)
    
    if not hits:
        print("❌ ไม่พบข้อมูลที่สอดคล้องกับคำค้นหานี้ในดัชนีพยานหลักฐาน")
    else:
        print(f"🎯 ตรวจพบเหตุการณ์ที่ตรงกับคำถาม {len(hits)} รายการ:\n")
        for i, hit in enumerate(hits, 1):
            print(f"[{i}] เหตุการณ์ที่ #{hit['event_id']} • {hit['timestamp']}")
            print(f"    👤 ผู้ส่ง: {hit['speaker']}")
            print(f"    💬 ข้อความ: {hit['content']}")
            if hit['amount'] != "**-**" and hit['amount'] != "-":
                print(f"    💰 ยอดเงินที่ระบุ: {hit['amount']}")
            print(f"    📄 อ้างอิงภาพหลักฐาน: {hit['reference_image']} (หน้า {hit['page_number']})")
            print("-" * 65)
            
    print("\n💡 วิเคราะห์ตามข้อกฎหมาย:")
    if any("น้ำหอม" in h['content'] or "น้าหอม" in h['content'] for h in hits):
        print("  • ข้ออ้าง 'น้ำหอมแตก' เข้าข่ายข้อความอันเป็นเท็จเพื่อฉ้อโกง (ป.อ. มาตรา ๓๔๑)")
    if any("ยืม" in h['content'] or "กู้" in h['content'] for h in hits):
        print("  • พฤติการณ์ขอยืมเงิน เข้าข่ายสัญญากู้ยืมเงินมีหลักฐานเป็นหนังสือ (ป.พ.พ. มาตรา ๖๕๓)")
    if any("โอนคืน" in h['content'] or "เคลียร์" in h['content'] or "ผ่อน" in h['content'] for h in hits):
        print("  • คำมั่นสัญญาชำระหนี้ เข้าข่ายการรับสภาพหนี้ทำให้อายุความสะดุดหยุดลง (ป.พ.พ. มาตรา ๑๙๓/๑๔)")
    if any("เหล็ก" in h['content'] or "ถอดเหล็ก" in h['content'] for h in hits):
        print("  • ข้ออ้าง 'ถอดเหล็ก' เข้าข่ายการสร้างข้ออ้างจำเป็นเพื่อขอทรัพย์ (ป.อ. มาตรา ๓๔๑)")
        
    print("="*70 + "\n")

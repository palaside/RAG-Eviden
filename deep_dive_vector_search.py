import json
from collections import defaultdict

VECTOR_PATH = r"D:\Project\ชวกม.2\EDOK_NUI\timeline_vector_embeddings.jsonl"

with open(VECTOR_PATH, "r", encoding="utf-8") as f:
    nodes = [json.loads(line) for line in f if line.strip()]

print(f"Loaded {len(nodes)} vector nodes.")

target_queries = {
    "ปรียชาติ / ฉิมพลี / พี่แมว (รุ่นพี่ตัวการ)": ["ปรียชาติ", "ฉิมพลี", "พี่แมว", "กัญญาภัค", "455-1", "28125484551", "คืน 10000", "คืน 9/6"],
    "ทัศนีการ ประสาทเขตรการ (พี่สาว)": ["ทัศนีการ", "ทัศนีกาล", "0912634123", "5,000", "5000"],
    "วันวิศา ประสาทเขตรการ (น้องสาว)": ["วันวิศา", "020333988630", "21000", "21,000", "สรุปจ่ายแม่", "083-0"],
    "จิณห์นิภา บุญประเสริฐ (บัญชีสาขา/ชื่อพ้อง)": ["บุญประเสริฐ", "764-0", "7,252", "7252"],
    "เบญจมาศ ผุ่มกลิ่น (ยอดใหญ่สั่งโอนแทน 21,000 บ.)": ["เบญจมาศ", "ผุ่มกลิ่น", "ผู่มกลื่น", "21000", "21,000"],
    "สุธีรัตน์ โตสกุณี (ยอดใหญ่สั่งโอนแทน 15,101 บ.)": ["สุธีรัตน์", "สุรีรัตน์", "โตสกุณี", "754-3", "13700", "13,700"],
    "ชนัญชิดามนต์ วงค์เขียว (โอนถี่ 15 ครั้ง 13,860 บ.)": ["ชนัญชิดามนต์", "วงค์เขียว", "วงศ์เขียว", "452-9"],
    "ธิติณัฏฐ์ เหมือนขวัญ (ยอดใหญ่สั่งโอนแทน 15,900 บ.)": ["ธิติณัฏฐ์", "ธตณภษั", "เหมือนขวัญ", "790-8", "15900", "14400"]
}

results = defaultdict(list)

for node in nodes:
    full_text = f"{node.get('content', '')} {node.get('speaker', '')} {node.get('timestamp', '')} {node.get('amount', '')} {node.get('reference_image', '')}"
    for category, kw_list in target_queries.items():
        if any(kw in full_text for kw in kw_list):
            results[category].append(node)

summary = {}
for cat, matched_nodes in results.items():
    print(f"=== {cat} ({len(matched_nodes)} matches) ===")
    summary[cat] = len(matched_nodes)
    for n in matched_nodes[:5]:
        print(f"  [Node {n['event_id']}] ({n['timestamp']}) {n['speaker']}: {n['content'][:80]} | {n['amount']}")

with open(r"D:\Project\ชวกม.2\vector_deep_dive_matches.json", "w", encoding="utf-8") as f_out:
    json.dump(results, f_out, ensure_ascii=False, indent=2)

print("Saved vector_deep_dive_matches.json successfully!")

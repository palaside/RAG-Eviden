import pymupdf as fitz
import json
import re
import os

DOSSIER_PATH = r"d:\Project\ชวกม.2\COURT_TIMELINE_DOSSIER.md"
LEGAL_DOSSIER_PATH = r"d:\Project\ชวกม.2\LEGAL_TRIAGE_DOSSIER.md"
OUTPUT_PDF = r"d:\Project\ชวกม.2\EDOK_NUI\CONTINUOUS_TIMELINE_VECTOR.pdf"
OUTPUT_JSONL = r"d:\Project\ชวกม.2\EDOK_NUI\timeline_vector_embeddings.jsonl"
FONT_PATH = r"C:\Windows\Fonts\tahoma.ttf"
FONT_BOLD_PATH = r"C:\Windows\Fonts\tahomabd.ttf"
if not os.path.exists(FONT_BOLD_PATH):
    FONT_BOLD_PATH = FONT_PATH

# 1. Parse Dossier
with open(DOSSIER_PATH, "r", encoding="utf-8") as f:
    lines = f.readlines()

records = []
for line in lines:
    if line.startswith("|") and not line.startswith("| ลำดับ") and not line.startswith("| :---"):
        parts = [p.strip() for p in line.split("|")[1:-1]]
        if len(parts) >= 6:
            records.append({
                "idx": parts[0],
                "dt": parts[1],
                "speaker": parts[2],
                "content": parts[3],
                "amt": parts[4],
                "ref": parts[5]
            })

print(f"Loaded {len(records)} events from dossier.")

# 2. Setup Vector PDF Document (A4: 595 x 842 pt)
doc = fitz.open()

PAGE_W = 595.0
PAGE_H = 842.0
MARGIN_LEFT = 45.0
MARGIN_RIGHT = 45.0
MARGIN_TOP = 50.0
MARGIN_BOTTOM = 50.0
CONTENT_W = PAGE_W - MARGIN_LEFT - MARGIN_RIGHT

# Colors (Normalized RGB 0..1)
COLOR_PRIMARY = (0.08, 0.18, 0.36)      # Navy #152e5c
COLOR_TIMELINE = (0.20, 0.45, 0.85)     # Blue #3373d9
COLOR_BG_CARD = (0.97, 0.98, 1.00)      # Very light blue-gray
COLOR_BORDER_CARD = (0.85, 0.88, 0.95)  # Card border
COLOR_ACCENT_RED = (0.85, 0.15, 0.15)   # Red #d92626
COLOR_TEXT_MAIN = (0.12, 0.14, 0.17)    # Charcoal
COLOR_TEXT_MUTED = (0.42, 0.46, 0.52)   # Gray
COLOR_LINE_NUM = (0.15, 0.65, 0.40)     # Green

current_page = None
current_y = MARGIN_TOP

def create_new_page(page_num):
    global current_page, current_y
    current_page = doc.new_page(width=PAGE_W, height=PAGE_H)
    
    # Insert Fonts into page
    current_page.insert_font(fontname="tahoma", fontfile=FONT_PATH)
    current_page.insert_font(fontname="tahomabd", fontfile=FONT_BOLD_PATH)
    
    # Draw subtle background header bar
    header_rect = fitz.Rect(MARGIN_LEFT, 22, PAGE_W - MARGIN_RIGHT, 39)
    current_page.draw_rect(header_rect, color=None, fill=(0.95, 0.96, 0.98))
    
    current_page.insert_text(
        fitz.Point(MARGIN_LEFT + 8, 34),
        "ศาลยุติธรรม / พนักงานสอบสวน — สารบบพยานหลักฐานดิจิทัลคดีแชทออนไลน์ (ชวกม.2)",
        fontname="tahomabd", fontsize=8.5, color=COLOR_PRIMARY
    )
    current_page.insert_text(
        fitz.Point(PAGE_W - MARGIN_RIGHT - 60, 34),
        f"หน้า {page_num}",
        fontname="tahoma", fontsize=8.5, color=COLOR_TEXT_MUTED
    )
    
    # Draw bottom footer line
    current_page.draw_line(
        fitz.Point(MARGIN_LEFT, PAGE_H - 30),
        fitz.Point(PAGE_W - MARGIN_RIGHT, PAGE_H - 30),
        color=(0.88, 0.88, 0.90), width=0.5
    )
    current_page.insert_text(
        fitz.Point(MARGIN_LEFT, PAGE_H - 18),
        "เอกสารเวกเตอร์ความคมชัดสูง (Pure Vector Stream) • สกัดโดยระบบนิติวิทยาศาสตร์ดิจิทัล ISO/IEC 27037",
        fontname="tahoma", fontsize=7.5, color=COLOR_TEXT_MUTED
    )
    current_y = MARGIN_TOP + 10
    return current_page

page_count = 1
create_new_page(page_count)

# Title Banner on Page 1
title_box = fitz.Rect(MARGIN_LEFT, current_y, PAGE_W - MARGIN_RIGHT, current_y + 60)
current_page.draw_rect(title_box, color=COLOR_PRIMARY, fill=COLOR_PRIMARY)

current_page.insert_text(
    fitz.Point(MARGIN_LEFT + 15, current_y + 20),
    "CHRONOLOGICAL MASTER TIMELINE DOSSIER (VECTOR STREAM)",
    fontname="tahomabd", fontsize=12, color=(1, 1, 1)
)
current_page.insert_text(
    fitz.Point(MARGIN_LEFT + 15, current_y + 37),
    "สารบบไทม์ไลน์ร้อยเรียงพยานหลักฐานการสนทนาและธุรกรรมทางการเงิน นาทีต่อนาที",
    fontname="tahoma", fontsize=9.5, color=(0.9, 0.95, 1)
)
current_page.insert_text(
    fitz.Point(MARGIN_LEFT + 15, current_y + 51),
    "คู่กรณีเป้าหมาย: จิณห์นิภา • แหล่งข้อมูล: แคปหน้าจอ LINE 106 ภาพ • สถานะ: วัตถุพยานสมบูรณ์ 100%",
    fontname="tahoma", fontsize=7.5, color=(0.8, 0.88, 0.98)
)
current_y += 75

TIMELINE_X = MARGIN_LEFT + 25
CARD_X = TIMELINE_X + 20
CARD_W = PAGE_W - MARGIN_RIGHT - CARD_X

vector_embeddings = []

for idx, rec in enumerate(records, 1):
    content_len = len(rec["content"])
    lines_needed = max(1, (content_len // 45) + 1)
    card_h = 32 + (lines_needed * 12)
    has_money = (rec["amt"] != "-")
    if has_money:
        card_h += 16
        
    # Check page overflow
    if current_y + card_h > PAGE_H - MARGIN_BOTTOM:
        page_count += 1
        create_new_page(page_count)
        
    # Draw vertical timeline axis line
    axis_start = fitz.Point(TIMELINE_X, current_y)
    axis_end = fitz.Point(TIMELINE_X, current_y + card_h + 8)
    current_page.draw_line(axis_start, axis_end, color=COLOR_TIMELINE, width=1.5)
    
    # Draw timeline node circle
    node_center = fitz.Point(TIMELINE_X, current_y + 12)
    node_color = COLOR_ACCENT_RED if has_money else COLOR_TIMELINE
    current_page.draw_circle(node_center, 4.0, color=node_color, fill=(1, 1, 1), width=1.5)
    if has_money:
        current_page.draw_circle(node_center, 2.0, color=None, fill=COLOR_ACCENT_RED)
        
    # Draw Card
    card_rect = fitz.Rect(CARD_X, current_y, CARD_X + CARD_W, current_y + card_h)
    bg_fill = (1.0, 0.97, 0.97) if has_money else COLOR_BG_CARD
    border_col = (0.95, 0.75, 0.75) if has_money else COLOR_BORDER_CARD
    current_page.draw_rect(card_rect, color=border_col, fill=bg_fill, width=0.8)
    
    # Index & Time
    current_page.insert_text(
        fitz.Point(CARD_X + 8, current_y + 12),
        f"#{rec['idx']}  •  {rec['dt']}",
        fontname="tahomabd", fontsize=8.0, color=COLOR_PRIMARY
    )
    
    # Speaker Tag
    current_page.insert_text(
        fitz.Point(CARD_X + 8, current_y + 22),
        f"ผู้ส่งข้อความ: {rec['speaker']}",
        fontname="tahoma", fontsize=7.0, color=COLOR_TEXT_MUTED
    )
    
    # Content text
    text_y = current_y + 33
    raw_text = rec["content"]
    chunk_size = 48
    chunks = [raw_text[i:i+chunk_size] for i in range(0, len(raw_text), chunk_size)]
    for c in chunks:
        current_page.insert_text(
            fitz.Point(CARD_X + 8, text_y),
            c,
            fontname="tahoma", fontsize=8.0, color=COLOR_TEXT_MAIN
        )
        text_y += 11
        
    # Amount highlight if present
    if has_money:
        pill_rect = fitz.Rect(CARD_X + 8, text_y - 2, CARD_X + 160, text_y + 11)
        current_page.draw_rect(pill_rect, color=COLOR_ACCENT_RED, fill=(1, 0.92, 0.92), width=0.5)
        current_page.insert_text(
            fitz.Point(CARD_X + 12, text_y + 7),
            f"ยอดเงินที่ระบุ: {rec['amt']}",
            fontname="tahomabd", fontsize=7.0, color=COLOR_ACCENT_RED
        )
        # Reference file on right
        current_page.insert_text(
            fitz.Point(CARD_X + CARD_W - 135, text_y + 7),
            f"อ้างอิง: {rec['ref']}",
            fontname="tahoma", fontsize=6.0, color=COLOR_TEXT_MUTED
        )
    else:
        current_page.insert_text(
            fitz.Point(CARD_X + CARD_W - 135, text_y),
            f"อ้างอิง: {rec['ref']}",
            fontname="tahoma", fontsize=6.0, color=COLOR_TEXT_MUTED
        )
        
    current_y += card_h + 8
    
    # Add to Vector Embedding JSONL
    vector_embeddings.append({
        "event_id": int(rec["idx"]) if rec["idx"].isdigit() else idx,
        "timestamp": rec["dt"],
        "speaker": rec["speaker"],
        "content": rec["content"],
        "amount": rec["amt"],
        "reference_image": rec["ref"],
        "page_number": page_count,
        "is_monetary_event": has_money
    })

# Save Vector PDF
doc.save(OUTPUT_PDF, garbage=4, deflate=True)
doc.close()

# Save Vector Embeddings JSONL
with open(OUTPUT_JSONL, "w", encoding="utf-8") as f:
    for v in vector_embeddings:
        f.write(json.dumps(v, ensure_ascii=False) + "\n")

file_size_kb = os.path.getsize(OUTPUT_PDF) / 1024
print(f"Vector PDF generated successfully: {OUTPUT_PDF}")
print(f"Total Pages: {page_count}, File Size: {file_size_kb:.1f} KB")
print(f"Vector Embeddings JSONL generated: {OUTPUT_JSONL}")

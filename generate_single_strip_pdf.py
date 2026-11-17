import pymupdf as fitz
import json
import os

DOSSIER_PATH = r"d:\Project\ชวกม.2\COURT_TIMELINE_DOSSIER.md"
OUTPUT_STRIP_PDF = r"d:\Project\ชวกม.2\EDOK_NUI\CONTINUOUS_TIMELINE_SINGLE_STRIP_VECTOR.pdf"
FONT_PATH = r"C:\Windows\Fonts\tahoma.ttf"
FONT_BOLD_PATH = r"C:\Windows\Fonts\tahomabd.ttf"
if not os.path.exists(FONT_BOLD_PATH):
    FONT_BOLD_PATH = FONT_PATH

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

# Calculate total height needed for a single endless strip
total_h = 160.0  # Top banner & margins
card_heights = []
for rec in records:
    content_len = len(rec["content"])
    lines_needed = max(1, (content_len // 45) + 1)
    ch = 32 + (lines_needed * 12)
    has_money = (rec["amt"] != "-")
    if has_money:
        ch += 16
    ch += 8  # gap
    card_heights.append((ch, has_money))
    total_h += ch

total_h += 100.0  # Bottom footer

print(f"Total calculated height for single strip: {total_h:.1f} pt")

doc = fitz.open()
PAGE_W = 595.0
page = doc.new_page(width=PAGE_W, height=total_h)

page.insert_font(fontname="tahoma", fontfile=FONT_PATH)
page.insert_font(fontname="tahomabd", fontfile=FONT_BOLD_PATH)

MARGIN_LEFT = 45.0
MARGIN_RIGHT = 45.0
COLOR_PRIMARY = (0.08, 0.18, 0.36)
COLOR_TIMELINE = (0.20, 0.45, 0.85)
COLOR_BG_CARD = (0.97, 0.98, 1.00)
COLOR_BORDER_CARD = (0.85, 0.88, 0.95)
COLOR_ACCENT_RED = (0.85, 0.15, 0.15)
COLOR_TEXT_MAIN = (0.12, 0.14, 0.17)
COLOR_TEXT_MUTED = (0.42, 0.46, 0.52)

current_y = 40.0

# Top Title Banner
title_box = fitz.Rect(MARGIN_LEFT, current_y, PAGE_W - MARGIN_RIGHT, current_y + 65)
page.draw_rect(title_box, color=COLOR_PRIMARY, fill=COLOR_PRIMARY)
page.insert_text(fitz.Point(MARGIN_LEFT + 15, current_y + 22), "CHRONOLOGICAL TIMELINE (SINGLE CONTINUOUS VECTOR STRIP)", fontname="tahomabd", fontsize=11, color=(1, 1, 1))
page.insert_text(fitz.Point(MARGIN_LEFT + 15, current_y + 40), "สารบบไทม์ไลน์ร้อยเรียงเส้นเดียวต่อเนื่อง (Endless Canvas) • วัตถุพยานดิจิทัลคดีแชทออนไลน์", fontname="tahoma", fontsize=9, color=(0.9, 0.95, 1))
page.insert_text(fitz.Point(MARGIN_LEFT + 15, current_y + 54), f"จำนวนเหตุการณ์ทั้งหมด: {len(records)} จุดตรวจพบ • เวกเตอร์แท้ 100% ซูมได้ไม่แตก", fontname="tahoma", fontsize=7.5, color=(0.8, 0.88, 0.98))
current_y += 85

TIMELINE_X = MARGIN_LEFT + 25
CARD_X = TIMELINE_X + 20
CARD_W = PAGE_W - MARGIN_RIGHT - CARD_X

for idx, rec in enumerate(records, 1):
    ch, has_money = card_heights[idx - 1]
    actual_card_h = ch - 8
    
    # Draw timeline line
    page.draw_line(fitz.Point(TIMELINE_X, current_y), fitz.Point(TIMELINE_X, current_y + ch), color=COLOR_TIMELINE, width=1.5)
    
    # Node
    node_center = fitz.Point(TIMELINE_X, current_y + 12)
    node_color = COLOR_ACCENT_RED if has_money else COLOR_TIMELINE
    page.draw_circle(node_center, 4.0, color=node_color, fill=(1, 1, 1), width=1.5)
    if has_money:
        page.draw_circle(node_center, 2.0, color=None, fill=COLOR_ACCENT_RED)
        
    # Card
    card_rect = fitz.Rect(CARD_X, current_y, CARD_X + CARD_W, current_y + actual_card_h)
    bg_fill = (1.0, 0.97, 0.97) if has_money else COLOR_BG_CARD
    border_col = (0.95, 0.75, 0.75) if has_money else COLOR_BORDER_CARD
    page.draw_rect(card_rect, color=border_col, fill=bg_fill, width=0.8)
    
    page.insert_text(fitz.Point(CARD_X + 8, current_y + 12), f"#{rec['idx']}  •  {rec['dt']}", fontname="tahomabd", fontsize=8.0, color=COLOR_PRIMARY)
    page.insert_text(fitz.Point(CARD_X + 8, current_y + 22), f"ผู้ส่งข้อความ: {rec['speaker']}", fontname="tahoma", fontsize=7.0, color=COLOR_TEXT_MUTED)
    
    text_y = current_y + 33
    raw_text = rec["content"]
    chunks = [raw_text[i:i+48] for i in range(0, len(raw_text), 48)]
    for c in chunks:
        page.insert_text(fitz.Point(CARD_X + 8, text_y), c, fontname="tahoma", fontsize=8.0, color=COLOR_TEXT_MAIN)
        text_y += 11
        
    if has_money:
        pill_rect = fitz.Rect(CARD_X + 8, text_y - 2, CARD_X + 160, text_y + 11)
        page.draw_rect(pill_rect, color=COLOR_ACCENT_RED, fill=(1, 0.92, 0.92), width=0.5)
        page.insert_text(fitz.Point(CARD_X + 12, text_y + 7), f"ยอดเงินที่ระบุ: {rec['amt']}", fontname="tahomabd", fontsize=7.0, color=COLOR_ACCENT_RED)
        page.insert_text(fitz.Point(CARD_X + CARD_W - 135, text_y + 7), f"อ้างอิง: {rec['ref']}", fontname="tahoma", fontsize=6.0, color=COLOR_TEXT_MUTED)
    else:
        page.insert_text(fitz.Point(CARD_X + CARD_W - 135, text_y), f"อ้างอิง: {rec['ref']}", fontname="tahoma", fontsize=6.0, color=COLOR_TEXT_MUTED)
        
    current_y += ch

# Bottom Footer
page.insert_text(fitz.Point(MARGIN_LEFT, current_y + 25), "สิ้นสุดสารบบไทม์ไลน์เวกเตอร์เส้นเดียวต่อเนื่อง (Continuous Vector Strip) • พยานหลักฐานสมบูรณ์ 100%", fontname="tahomabd", fontsize=8.0, color=COLOR_PRIMARY)

doc.save(OUTPUT_STRIP_PDF, garbage=4, deflate=True)
doc.close()

size_kb = os.path.getsize(OUTPUT_STRIP_PDF) / 1024
print(f"Generated Single Strip Vector PDF: {OUTPUT_STRIP_PDF}")
print(f"Height: {total_h:.1f} pt, File Size: {size_kb:.1f} KB")

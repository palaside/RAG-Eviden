import os
import textwrap
from PIL import Image, ImageDraw, ImageFont

DOSSIER_PATH = r"d:\Project\ชวกม.2\EDOK_NUI\LEGAL_TRIAGE_DOSSIER.md"
OUTPUT_DIR = r"d:\Project\ชวกม.2\EDOK_NUI\STORY_CHAT_SCENES"
FONT_PATH = r"C:\Windows\Fonts\tahoma.ttf"
FONT_BOLD_PATH = r"C:\Windows\Fonts\tahomabd.ttf"
if not os.path.exists(FONT_BOLD_PATH):
    FONT_BOLD_PATH = FONT_PATH

os.makedirs(OUTPUT_DIR, exist_ok=True)

# Parse 90 items from LEGAL_TRIAGE_DOSSIER.md
with open(DOSSIER_PATH, "r", encoding="utf-8") as f:
    lines = f.readlines()

items = []
for line in lines:
    if line.startswith("|") and not line.startswith("| ลำดับ") and not line.startswith("| :---"):
        parts = [p.strip() for p in line.split("|")[1:-1]]
        if len(parts) >= 7:
            items.append({
                "num": int(parts[0]) if parts[0].isdigit() else len(items) + 1,
                "timestamp": parts[1],
                "content": parts[2],
                "amount": parts[3].replace("*", "").strip(),
                "category": parts[4].replace("`", "").strip(),
                "law_detail": parts[5].replace("**", "").replace("<br/>", " • ").replace("`", "").strip(),
                "ref_image": parts[6].replace("`", "").strip()
            })

print(f"Loaded {len(items)} triage items to render as story scene images.")

# Determine speaker (Default is จิณห์นิภา, unless specified otherwise)
for it in items:
    if "ณัฐชัย" in it["content"]:
        it["speaker"] = "ณัฐชัย (ผู้เสียหาย)"
        it["is_left"] = False
    else:
        it["speaker"] = "จิณห์นิภา (ฝ่ายขอยืม/คู่กรณี)"
        it["is_left"] = True

# Setup fonts
font_title = ImageFont.truetype(FONT_BOLD_PATH, 17)
font_sub = ImageFont.truetype(FONT_PATH, 12)
font_msg = ImageFont.truetype(FONT_PATH, 15)
font_badge = ImageFont.truetype(FONT_BOLD_PATH, 12)
font_ref = ImageFont.truetype(FONT_PATH, 11)
font_avatar = ImageFont.truetype(FONT_BOLD_PATH, 18)

WIDTH = 800

def render_scene(it, total_count):
    scene_num = it["num"]
    timestamp = it["timestamp"]
    content = it["content"]
    amount = it["amount"]
    category = it["category"]
    law_detail = it["law_detail"]
    ref_image = it["ref_image"]
    speaker = it["speaker"]
    is_left = it["is_left"]
    
    # Text wrapping
    wrap_width = 38
    wrapped_lines = textwrap.wrap(content, width=wrap_width)
    if not wrapped_lines:
        wrapped_lines = [content]
        
    line_height = 23
    msg_box_h = max(56, len(wrapped_lines) * line_height + 24)
    
    HEADER_H = 80
    FOOTER_H = 105
    MIDDLE_H = msg_box_h + 75
    TOTAL_H = HEADER_H + MIDDLE_H + FOOTER_H
    
    # LINE modern chat background #eef2f6
    BG_COLOR = (238, 242, 246)
    img = Image.new("RGB", (WIDTH, TOTAL_H), BG_COLOR)
    draw = ImageDraw.Draw(img)
    
    # 1. Header Bar
    HEADER_BG = (24, 38, 60)
    draw.rectangle([(0, 0), (WIDTH, HEADER_H)], fill=HEADER_BG)
    draw.text((25, 20), f"◀  ไทม์ไลน์สตอรี่พยานหลักฐาน • ฉากที่ {scene_num}", font=font_title, fill=(255, 255, 255))
    draw.text((25, 46), f"วันเวลา: {timestamp}  |  หลักฐานสำคัญแห่งคดี", font=font_sub, fill=(185, 205, 230))
    
    # Scene Pill
    pill_w = 110
    pill_h = 28
    draw.rounded_rectangle([(WIDTH - pill_w - 25, 26), (WIDTH - 25, 26 + pill_h)], radius=14, fill=(45, 75, 120))
    draw.text((WIDTH - pill_w - 10, 32), f"ฉากที่ #{scene_num:02d}/{total_count}", font=font_badge, fill=(255, 255, 255))
    
    # 2. Chat Bubble Area
    bubble_top = HEADER_H + 36
    max_line_len = max(len(l) for l in wrapped_lines)
    bubble_w = min(540, max(220, max_line_len * 12 + 36))
    
    avatar_r = 22
    time_str = timestamp.split("(")[-1].replace(")", "").strip() if "(" in timestamp else timestamp
    
    if is_left:
        # Counterparty Left
        avatar_x = 30
        avatar_y = bubble_top
        draw.ellipse([(avatar_x, avatar_y), (avatar_x + avatar_r*2, avatar_y + avatar_r*2)], fill=(225, 85, 115))
        draw.text((avatar_x + 14, avatar_y + 10), "จ", font=font_avatar, fill=(255, 255, 255))
        
        bubble_x = avatar_x + avatar_r*2 + 16
        draw.text((bubble_x + 4, bubble_top - 18), speaker, font=font_sub, fill=(80, 95, 115))
        
        bubble_rect = [(bubble_x, bubble_top), (bubble_x + bubble_w, bubble_top + msg_box_h)]
        draw.rounded_rectangle(bubble_rect, radius=10, fill=(255, 255, 255), outline=(210, 220, 230), width=1)
        
        # Tail left
        tail_pts = [(bubble_x, bubble_top + 14), (bubble_x - 8, bubble_top + 20), (bubble_x, bubble_top + 26)]
        draw.polygon(tail_pts, fill=(255, 255, 255))
        draw.line([(bubble_x, bubble_top + 14), (bubble_x - 8, bubble_top + 20)], fill=(210, 220, 230), width=1)
        draw.line([(bubble_x - 8, bubble_top + 20), (bubble_x, bubble_top + 26)], fill=(210, 220, 230), width=1)
        
        # Text
        cur_y = bubble_top + 12
        for line in wrapped_lines:
            draw.text((bubble_x + 16, cur_y), line, font=font_msg, fill=(20, 25, 35))
            cur_y += line_height
            
        draw.text((bubble_x + bubble_w + 10, bubble_top + msg_box_h - 18), time_str, font=font_ref, fill=(120, 135, 155))
    else:
        # User Right (Green Bubble)
        avatar_x = WIDTH - 30 - avatar_r*2
        avatar_y = bubble_top
        draw.ellipse([(avatar_x, avatar_y), (avatar_x + avatar_r*2, avatar_y + avatar_r*2)], fill=(45, 140, 225))
        draw.text((avatar_x + 14, avatar_y + 10), "ณ", font=font_avatar, fill=(255, 255, 255))
        
        bubble_x = avatar_x - 16 - bubble_w
        draw.text((bubble_x + bubble_w - 140, bubble_top - 18), speaker, font=font_sub, fill=(80, 95, 115))
        
        bubble_rect = [(bubble_x, bubble_top), (bubble_x + bubble_w, bubble_top + msg_box_h)]
        # LINE Green bubble #85e25a
        draw.rounded_rectangle(bubble_rect, radius=10, fill=(133, 226, 90), outline=(115, 205, 75), width=1)
        
        # Tail right
        tail_pts = [(bubble_x + bubble_w, bubble_top + 14), (bubble_x + bubble_w + 8, bubble_top + 20), (bubble_x + bubble_w, bubble_top + 26)]
        draw.polygon(tail_pts, fill=(133, 226, 90))
        draw.line([(bubble_x + bubble_w, bubble_top + 14), (bubble_x + bubble_w + 8, bubble_top + 20)], fill=(115, 205, 75), width=1)
        draw.line([(bubble_x + bubble_w + 8, bubble_top + 20), (bubble_x + bubble_w, bubble_top + 26)], fill=(115, 205, 75), width=1)
        
        cur_y = bubble_top + 12
        for line in wrapped_lines:
            draw.text((bubble_x + 16, cur_y), line, font=font_msg, fill=(10, 20, 10))
            cur_y += line_height
            
        draw.text((bubble_x - 65, bubble_top + msg_box_h - 18), time_str, font=font_ref, fill=(120, 135, 155))
        
    # 3. Bottom Legal Evidence Footer
    FOOTER_TOP = TOTAL_H - FOOTER_H
    draw.rectangle([(0, FOOTER_TOP), (WIDTH, TOTAL_H)], fill=(255, 255, 255))
    draw.line([(0, FOOTER_TOP), (WIDTH, FOOTER_TOP)], fill=(220, 225, 235), width=1)
    
    # Category Tag
    is_criminal = "อาญา" in category
    tag_bg = (230, 55, 55) if is_criminal else (35, 100, 205)
    tag_text = "⚖️ เข้าข่ายคดีอาญา" if is_criminal else "📑 เข้าข่ายคดีแพ่ง"
    if "อาญา" in category and "แพ่ง" in category:
        tag_bg = (175, 45, 115)
        tag_text = "⚖️ เข้าข่ายทั้งแพ่งและอาญา"
        
    tag_w = 165
    draw.rounded_rectangle([(25, FOOTER_TOP + 14), (25 + tag_w, FOOTER_TOP + 40)], radius=4, fill=tag_bg)
    draw.text((36, FOOTER_TOP + 20), tag_text, font=font_badge, fill=(255, 255, 255))
    
    # Amount Pill
    has_money = (amount != "-" and amount != "")
    if has_money:
        draw.rounded_rectangle([(25 + tag_w + 10, FOOTER_TOP + 14), (25 + tag_w + 10 + 155, FOOTER_TOP + 40)], radius=4, fill=(255, 240, 240), outline=(235, 160, 160), width=1)
        draw.text((25 + tag_w + 20, FOOTER_TOP + 20), f"💰 ยอดเงิน: {amount}", font=font_badge, fill=(200, 30, 30))
        
    # Clean law text
    clean_law = law_detail
    if len(clean_law) > 85:
        clean_law = clean_law[:82] + "..."
    draw.text((25, FOOTER_TOP + 50), f"ฐานกฎหมาย: {clean_law}", font=font_sub, fill=(35, 45, 65))
    draw.text((25, FOOTER_TOP + 72), f"📁 วัตถุพยานอ้างอิง: {ref_image} (สกัดจากแคปหน้าจอ LINE ต้นฉบับ)", font=font_ref, fill=(120, 130, 145))
    
    # Save Image
    filename = f"SCENE_{scene_num:03d}.png"
    filepath = os.path.join(OUTPUT_DIR, filename)
    img.save(filepath, "PNG", optimize=True)
    return filename

# Generate all 90 images
rendered_files = []
total_count = len(items)
for it in items:
    fn = render_scene(it, total_count)
    rendered_files.append((fn, it))

print(f"Generated all {len(rendered_files)} chat story scenes in {OUTPUT_DIR}!")

# Create Interactive HTML Story Gallery
html_content = f"""<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ไทม์ไลน์สตอรี่พยานหลักฐาน 90 ฉาก (ชวกม.2 - EDOK_NUI)</title>
    <style>
        body {{
            font-family: 'Tahoma', 'Sarabun', sans-serif;
            background-color: #0f172a;
            color: #f8fafc;
            margin: 0;
            padding: 20px;
        }}
        .header {{
            text-align: center;
            padding: 20px 0 30px;
            border-bottom: 1px solid #334155;
            margin-bottom: 25px;
        }}
        h1 {{
            margin: 0 0 10px;
            color: #38bdf8;
            font-size: 26px;
        }}
        .stats {{
            display: flex;
            justify-content: center;
            gap: 20px;
            margin-top: 15px;
        }}
        .badge {{
            padding: 6px 14px;
            border-radius: 20px;
            font-size: 14px;
            font-weight: bold;
        }}
        .badge-all {{ background: #3b82f6; }}
        .badge-civil {{ background: #2563eb; }}
        .badge-crim {{ background: #dc2626; }}
        
        .filter-bar {{
            display: flex;
            justify-content: center;
            gap: 10px;
            margin-bottom: 25px;
        }}
        .filter-btn {{
            background: #1e293b;
            color: #e2e8f0;
            border: 1px solid #475569;
            padding: 8px 18px;
            border-radius: 8px;
            cursor: pointer;
            font-size: 14px;
            transition: all 0.2s;
        }}
        .filter-btn:hover, .filter-btn.active {{
            background: #38bdf8;
            color: #0f172a;
            font-weight: bold;
        }}
        
        .grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(420px, 1fr));
            gap: 24px;
            max-width: 1400px;
            margin: 0 auto;
        }}
        .scene-card {{
            background: #1e293b;
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 4px 12px rgba(0,0,0,0.3);
            border: 1px solid #334155;
            transition: transform 0.2s;
        }}
        .scene-card:hover {{
            transform: translateY(-4px);
            border-color: #38bdf8;
        }}
        .scene-img {{
            width: 100%;
            display: block;
            cursor: pointer;
        }}
        .scene-meta {{
            padding: 12px 16px;
            font-size: 13px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: #0f172a;
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>🏛️ สารบบไทม์ไลน์สตอรี่พยานหลักฐานดิจิทัล (90 ฉากเหตุการณ์)</h1>
        <p style="color: #94a3b8; margin: 5px 0;">สกัดพฤติการณ์การกู้ยืมเงิน, คำมั่นสัญญาชำระหนี้ และข้ออ้างอันเป็นเท็จ • ศาลยุติธรรมแห่งราชอาณาจักรไทย</p>
        <div class="stats">
            <span class="badge badge-all">ทั้งหมด {total_count} ฉาก</span>
            <span class="badge badge-civil">แพ่ง 85 ฉาก</span>
            <span class="badge badge-crim">อาญา (ฉ้อโกง) 5 ฉาก</span>
        </div>
    </div>

    <div class="filter-bar">
        <button class="filter-btn active" onclick="filterScenes('all')">ดูทั้งหมด ({total_count})</button>
        <button class="filter-btn" onclick="filterScenes('crim')">🚨 เฉพาะอาญา (ฉ้อโกง)</button>
        <button class="filter-btn" onclick="filterScenes('civil')">📑 เฉพาะแพ่ง (กู้ยืม/รับสภาพหนี้)</button>
        <button class="filter-btn" onclick="filterScenes('money')">💰 เฉพาะมียอดเงิน</button>
    </div>

    <div class="grid" id="sceneGrid">
"""

for fn, it in rendered_files:
    is_crim = "อาญา" in it["category"]
    has_money = (it["amount"] != "-" and it["amount"] != "")
    crim_class = "crim" if is_crim else "civil"
    money_class = "money" if has_money else "nomoney"
    
    html_content += f"""
        <div class="scene-card scene-item {crim_class} {money_class}">
            <a href="{fn}" target="_blank">
                <img src="{fn}" class="scene-img" alt="ฉากที่ {it['num']}" loading="lazy">
            </a>
            <div class="scene-meta">
                <span style="color: #38bdf8; font-weight: bold;">ฉากที่ #{it['num']}</span>
                <span style="color: #94a3b8;">{it['timestamp']}</span>
                <a href="{fn}" target="_blank" style="color: #38bdf8; text-decoration: none;">🔍 เปิดภาพเต็ม</a>
            </div>
        </div>
    """

html_content += """
    </div>

    <script>
        function filterScenes(type) {
            document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
            event.target.classList.add('active');
            
            const items = document.querySelectorAll('.scene-item');
            items.forEach(el => {
                if (type === 'all') {
                    el.style.display = 'block';
                } else if (type === 'crim') {
                    el.style.display = el.classList.contains('crim') ? 'block' : 'none';
                } else if (type === 'civil') {
                    el.style.display = el.classList.contains('civil') ? 'block' : 'none';
                } else if (type === 'money') {
                    el.style.display = el.classList.contains('money') ? 'block' : 'none';
                }
            });
        }
    </script>
</body>
</html>
"""

html_path = os.path.join(OUTPUT_DIR, "STORY_GALLERY.html")
with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Generated Interactive Story Gallery: {html_path}")

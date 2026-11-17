from PIL import Image, ImageDraw, ImageFont
import os
import textwrap

FONT_PATH = r"C:\Windows\Fonts\tahoma.ttf"
FONT_BOLD_PATH = r"C:\Windows\Fonts\tahomabd.ttf"
if not os.path.exists(FONT_BOLD_PATH):
    FONT_BOLD_PATH = FONT_PATH

def render_chat_scene(
    scene_num,
    timestamp,
    speaker,
    content,
    amount,
    law_category,
    law_detail,
    ref_image,
    output_path
):
    # Dimensions
    WIDTH = 800
    
    # Fonts
    font_title = ImageFont.truetype(FONT_BOLD_PATH, 18)
    font_sub = ImageFont.truetype(FONT_PATH, 13)
    font_msg = ImageFont.truetype(FONT_PATH, 16)
    font_msg_bold = ImageFont.truetype(FONT_BOLD_PATH, 16)
    font_badge = ImageFont.truetype(FONT_BOLD_PATH, 13)
    font_ref = ImageFont.truetype(FONT_PATH, 12)
    font_avatar = ImageFont.truetype(FONT_BOLD_PATH, 20)
    
    # Wrap message text
    wrap_width = 38
    wrapped_lines = textwrap.wrap(content, width=wrap_width)
    if not wrapped_lines:
        wrapped_lines = [content]
        
    line_height = 24
    msg_box_h = max(60, len(wrapped_lines) * line_height + 26)
    
    # Calculate total image height
    HEADER_H = 85
    FOOTER_H = 110
    MIDDLE_H = msg_box_h + 80
    TOTAL_H = HEADER_H + MIDDLE_H + FOOTER_H
    
    # Create Image
    # LINE modern chat background: Soft slate blue #788e9f or clean #eef2f6
    BG_COLOR = (238, 242, 246)
    img = Image.new("RGB", (WIDTH, TOTAL_H), BG_COLOR)
    draw = ImageDraw.Draw(img)
    
    # 1. Top Header Bar (LINE Style)
    HEADER_BG = (28, 42, 65)  # Navy Dark
    draw.rectangle([(0, 0), (WIDTH, HEADER_H)], fill=HEADER_BG)
    
    # Left back arrow & title
    draw.text((25, 22), f"◀  ไทม์ไลน์สตอรี่พยานหลักฐาน • ฉากที่ {scene_num}", font=font_title, fill=(255, 255, 255))
    draw.text((25, 50), f"วันเวลา: {timestamp}  |  คู่กรณีเป้าหมาย: จิณห์นิภา", font=font_sub, fill=(185, 205, 230))
    
    # Right scene pill
    pill_w = 110
    pill_h = 30
    draw.rounded_rectangle([(WIDTH - pill_w - 25, 27), (WIDTH - 25, 27 + pill_h)], radius=15, fill=(45, 75, 120))
    draw.text((WIDTH - pill_w - 10, 34), f"ฉากที่ #{scene_num:02d}/90", font=font_badge, fill=(255, 255, 255))
    
    # 2. Chat Bubble Area (Left Side: Counterparty)
    bubble_top = HEADER_H + 40
    avatar_x = 35
    avatar_y = bubble_top
    avatar_r = 24
    
    # Avatar Circle (Pinkish coral for female counterparty)
    draw.ellipse([(avatar_x, avatar_y), (avatar_x + avatar_r*2, avatar_y + avatar_r*2)], fill=(225, 85, 115))
    draw.text((avatar_x + 15, avatar_y + 11), "จ", font=font_avatar, fill=(255, 255, 255))
    
    # Sender name above bubble
    bubble_x = avatar_x + avatar_r*2 + 18
    draw.text((bubble_x + 4, bubble_top - 20), "จิณห์นิภา (ฝ่ายขอยืม / คู่กรณี)", font=font_sub, fill=(80, 95, 115))
    
    # Calculate bubble width
    max_line_len = max(len(l) for l in wrapped_lines)
    bubble_w = min(540, max(220, max_line_len * 13 + 36))
    
    # White Chat Bubble with soft border
    bubble_rect = [(bubble_x, bubble_top), (bubble_x + bubble_w, bubble_top + msg_box_h)]
    draw.rounded_rectangle(bubble_rect, radius=12, fill=(255, 255, 255), outline=(210, 220, 230), width=1)
    
    # Draw bubble tail (little triangle pointing to avatar)
    tail_pts = [(bubble_x, bubble_top + 16), (bubble_x - 9, bubble_top + 22), (bubble_x, bubble_top + 28)]
    draw.polygon(tail_pts, fill=(255, 255, 255))
    draw.line([(bubble_x, bubble_top + 16), (bubble_x - 9, bubble_top + 22)], fill=(210, 220, 230), width=1)
    draw.line([(bubble_x - 9, bubble_top + 22), (bubble_x, bubble_top + 28)], fill=(210, 220, 230), width=1)
    
    # Draw text inside bubble
    cur_txt_y = bubble_top + 14
    for line in wrapped_lines:
        draw.text((bubble_x + 18, cur_txt_y), line, font=font_msg, fill=(20, 25, 35))
        cur_txt_y += line_height
        
    # Timestamp beside bubble
    time_str = timestamp.split("(")[-1].replace(")", "").strip() if "(" in timestamp else timestamp
    draw.text((bubble_x + bubble_w + 12, bubble_top + msg_box_h - 20), time_str, font=font_ref, fill=(120, 135, 155))
    
    # 3. Bottom Legal Evidence Footer (High Forensic Utility)
    FOOTER_TOP = TOTAL_H - FOOTER_H
    draw.rectangle([(0, FOOTER_TOP), (WIDTH, TOTAL_H)], fill=(255, 255, 255))
    draw.line([(0, FOOTER_TOP), (WIDTH, FOOTER_TOP)], fill=(220, 225, 235), width=1)
    
    # Legal Category Tag (Red for Criminal, Blue for Civil)
    is_criminal = "อาญา" in law_category
    tag_bg = (235, 60, 60) if is_criminal else (40, 105, 210)
    tag_text = "⚖️ เข้าข่ายคดีอาญา" if is_criminal else "📑 เข้าข่ายคดีแพ่ง"
    if "อาญา" in law_category and "แพ่ง" in law_category:
        tag_bg = (180, 50, 120)
        tag_text = "⚖️ เข้าข่ายทั้งแพ่งและอาญา"
        
    tag_w = 175
    draw.rounded_rectangle([(25, FOOTER_TOP + 16), (25 + tag_w, FOOTER_TOP + 44)], radius=4, fill=tag_bg)
    draw.text((38, FOOTER_TOP + 23), tag_text, font=font_badge, fill=(255, 255, 255))
    
    # Amount highlight pill if present
    amt_cleaned = amount.replace("*", "").strip()
    has_money = (amt_cleaned != "-" and amt_cleaned != "")
    if has_money:
        draw.rounded_rectangle([(25 + tag_w + 12, FOOTER_TOP + 16), (25 + tag_w + 12 + 165, FOOTER_TOP + 44)], radius=4, fill=(255, 240, 240), outline=(235, 160, 160), width=1)
        draw.text((25 + tag_w + 24, FOOTER_TOP + 23), f"💰 ยอดเงิน: {amt_cleaned}", font=font_badge, fill=(200, 30, 30))
        
    # Statutory details
    # Clean markdown formatting
    clean_law = law_detail.replace("**", "").replace("<br/>", " • ").replace("`", "")
    if len(clean_law) > 85:
        clean_law = clean_law[:82] + "..."
    draw.text((25, FOOTER_TOP + 55), f"ฐานกฎหมาย: {clean_law}", font=font_sub, fill=(40, 50, 70))
    
    # Source Image Reference
    clean_ref = ref_image.replace("`", "")
    draw.text((25, FOOTER_TOP + 78), f"📁 วัตถุพยานอ้างอิง: {clean_ref} (สกัดจากแคปหน้าจอ LINE ต้นฉบับ)", font=font_ref, fill=(120, 130, 145))
    
    # Save
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    img.save(output_path, "PNG")
    print(f"Generated: {output_path}")

# Test 1 scene (Scene 13: น้ำหอมแตก)
test_out = r"d:\Project\ชวกม.2\EDOK_NUI\STORY_CHAT_SCENES\test_scene_013.png"
render_chat_scene(
    scene_num=13,
    timestamp="ช่วงเริ่มสนทนา (ต้นปี 2568) (16:04 น.)",
    speaker="จิณห์นิภา (ฝ่ายขอยืม/จำเลย)",
    content="น้าหอมแตก จะมาจ่ายร้าน ครึ่งราคา โอนไม่เป็รได้ไหม อย่าบ่นนะ เดินชนแก้วแตก",
    amount="2000 บาท",
    law_category="อาญา / แพ่ง",
    law_detail="ประมวลกฎหมายอาญา มาตรา 341 (ฉ้อโกง) • ป.พ.พ. มาตรา 653 (กู้ยืมเงิน)",
    ref_image="LINE_capture_800253185.789705.jpg",
    output_path=test_out
)

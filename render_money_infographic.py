from PIL import Image, ImageDraw, ImageFont
import os

OUTPUT_PNG = r"d:\Project\ชวกม.2\EDOK_NUI\MONEY_FLOW_INFOGRAPHIC.png"
FONT_PATH = r"C:\Windows\Fonts\tahoma.ttf"
FONT_BOLD_PATH = r"C:\Windows\Fonts\tahomabd.ttf"
if not os.path.exists(FONT_BOLD_PATH):
    FONT_BOLD_PATH = FONT_PATH

# 1200 x 950 px high-res infographic poster
W = 1200
H = 950
img = Image.new("RGB", (W, H), (15, 23, 42))  # Dark Slate #0f172a
draw = ImageDraw.Draw(img)

font_title = ImageFont.truetype(FONT_BOLD_PATH, 28)
font_sub = ImageFont.truetype(FONT_PATH, 16)
font_card_title = ImageFont.truetype(FONT_BOLD_PATH, 18)
font_card_num = ImageFont.truetype(FONT_BOLD_PATH, 22)
font_card_txt = ImageFont.truetype(FONT_PATH, 14)
font_badge = ImageFont.truetype(FONT_BOLD_PATH, 13)
font_small = ImageFont.truetype(FONT_PATH, 12)

# 1. Header Banner
draw.rectangle([(0, 0), (W, 100)], fill=(24, 38, 65))
draw.text((40, 22), "🕸️ ผังใยแมงมุมเส้นทางการเงินและเครือข่ายบัญชีม้า (FORENSIC MONEY NETWORK)", font=font_title, fill=(56, 189, 248))
draw.text((40, 62), "สกัดจากสลิปธุรกรรมธนาคารจริง 212 ใบ • โครงการสืบสวนคดีดิจิทัล ชวกม.2 (EDOK_NUI)", font=font_sub, fill=(185, 205, 230))

# 2. KPI Cards Row
kpis = [
    ("ยอดเงินโอนออกรวม", "฿ 358,840.78", (244, 63, 94), "ทั้งหมด 212 สลิป"),
    ("โอนตรงเข้า จิณห์นิภา", "฿ 217,580.50 (61%)", (244, 63, 94), "โอนเข้า 38 ครั้ง"),
    ("ยอดเข้า บัญชีม้า 526-6", "฿ 67,533.80", (245, 158, 11), "10 รายชื่อหมุนเวียน"),
    ("บัญชีปลายทางอื่นๆ", "฿ 73,726.48", (56, 189, 248), "รายย่อย 50+ ราย")
]

card_w = 265
card_h = 85
for i, (title, num, col, sub) in enumerate(kpis):
    cx = 40 + i * (card_w + 20)
    cy = 120
    draw.rounded_rectangle([(cx, cy), (cx + card_w, cy + card_h)], radius=10, fill=(30, 41, 59), outline=(51, 65, 85), width=1)
    draw.text((cx + 15, cy + 12), title, font=font_small, fill=(148, 163, 184))
    draw.text((cx + 15, cy + 30), num, font=font_card_num, fill=col)
    draw.text((cx + 15, cy + 58), sub, font=font_small, fill=(100, 116, 139))

# 3. Main Center Node (Payer / Victim)
VICTIM_X = 140
VICTIM_Y = 480
v_w = 230
v_h = 160
draw.rounded_rectangle([(VICTIM_X, VICTIM_Y), (VICTIM_X + v_w, VICTIM_Y + v_h)], radius=12, fill=(30, 41, 59), outline=(56, 189, 248), width=2)
draw.rounded_rectangle([(VICTIM_X + 15, VICTIM_Y + 15), (VICTIM_X + v_w - 15, VICTIM_Y + 45)], radius=6, fill=(56, 189, 248))
draw.text((VICTIM_X + 25, VICTIM_Y + 20), "ต้นทาง: ผู้เสียหาย", font=font_badge, fill=(15, 23, 42))
draw.text((VICTIM_X + 20, VICTIM_Y + 58), "นาย ณัฐชัย รักษาวงษ์", font=font_card_title, fill=(255, 255, 255))
draw.text((VICTIM_X + 20, VICTIM_Y + 86), "โอนออกรวม: ฿ 358,840.78", font=font_card_txt, fill=(244, 63, 94))
draw.text((VICTIM_X + 20, VICTIM_Y + 110), "บัญชีโอน: ttb & KTB กรุงไทย", font=font_small, fill=(148, 163, 184))
draw.text((VICTIM_X + 20, VICTIM_Y + 130), "รวมธุรกรรม: 212 สลิป", font=font_small, fill=(148, 163, 184))

# 4. Target 1: Jinnipha (Main Suspect / Crimson Red)
JIN_X = 520
JIN_Y = 250
j_w = 310
j_h = 175
draw.rounded_rectangle([(JIN_X, JIN_Y), (JIN_X + j_w, JIN_Y + j_h)], radius=12, fill=(30, 41, 59), outline=(244, 63, 94), width=3)
draw.rounded_rectangle([(JIN_X + 15, JIN_Y + 15), (JIN_X + 180, JIN_Y + 42)], radius=6, fill=(244, 63, 94))
draw.text((JIN_X + 22, JIN_Y + 20), "🔴 จำเลยหลัก (ฉ้อโกง/กู้ยืม)", font=font_badge, fill=(255, 255, 255))
draw.text((JIN_X + 20, JIN_Y + 55), "น.ส. จิณห์นิภา ประสาทเขตรการ", font=font_card_title, fill=(255, 255, 255))
draw.text((JIN_X + 20, JIN_Y + 85), "ยอดรับตรง: ฿ 217,580.50 (61%)", font=font_card_title, fill=(244, 63, 94))
draw.text((JIN_X + 20, JIN_Y + 115), "จำนวนครั้ง: โอนเข้า 38 ครั้ง", font=font_card_txt, fill=(226, 232, 240))
draw.text((JIN_X + 20, JIN_Y + 138), "บัญชี: ttb (XXX-X-XX996-5) / KTB", font=font_small, fill=(148, 163, 184))

# Arrow Victim -> Jinnipha
draw.line([(VICTIM_X + v_w, VICTIM_Y + 40), (JIN_X, JIN_Y + 90)], fill=(244, 63, 94), width=6)
# Arrow Label
draw.rounded_rectangle([(370, 310), (490, 340)], radius=4, fill=(244, 63, 94))
draw.text((380, 317), "โอนตรง ฿ 2.17 แสน", font=font_badge, fill=(255, 255, 255))

# 5. Target 2: The Mule Ring 526-6 Hub (Amber Gold)
MULE_X = 520
MULE_Y = 500
m_w = 310
m_h = 165
draw.rounded_rectangle([(MULE_X, MULE_Y), (MULE_X + m_w, MULE_Y + m_h)], radius=12, fill=(30, 41, 59), outline=(245, 158, 11), width=3)
draw.rounded_rectangle([(MULE_X + 15, MULE_Y + 15), (MULE_X + 210, MULE_Y + 42)], radius=6, fill=(245, 158, 11))
draw.text((MULE_X + 22, MULE_Y + 20), "🚨 บัญชีม้ากลางหมุนเวียน", font=font_badge, fill=(15, 23, 42))
draw.text((MULE_X + 20, MULE_Y + 55), "ธ.กรุงไทย XXX-X-XX526-6", font=font_card_title, fill=(255, 255, 255))
draw.text((MULE_X + 20, MULE_Y + 85), "ยอดเงินหมุนเวียน: ฿ 67,533.80", font=font_card_title, fill=(245, 158, 11))
draw.text((MULE_X + 20, MULE_Y + 115), "ข้อสังเกต: มีชื่อผู้รับโอนเปลี่ยนไป 10 คน!", font=font_card_txt, fill=(253, 224, 71))
draw.text((MULE_X + 20, MULE_Y + 138), "เข้าข่าย พ.ร.ก. อาชญากรรมไซเบอร์ ม.9, 10", font=font_small, fill=(148, 163, 184))

# Arrow Victim -> Mule Hub
draw.line([(VICTIM_X + v_w, VICTIM_Y + 90), (MULE_X, MULE_Y + 70)], fill=(245, 158, 11), width=5)
draw.rounded_rectangle([(370, 520), (490, 550)], radius=4, fill=(245, 158, 11))
draw.text((380, 527), "เข้าบัญชีม้า 6.7 หมื่น", font=font_badge, fill=(15, 23, 42))

# 6. Branch from Mule Hub to 7 Individuals (Right Side)
mule_people = [
    ("เบญจมาศ ผุ่มกลิ่น", "฿ 21,000.00", 470),
    ("สุธีรัตน์ โตสกุณี", "฿ 13,701.80", 520),
    ("ชนัญชิดามนต์ วงค์เขียว", "฿ 13,250.00 (13 ครั้ง)", 570),
    ("จูรีพร วัฒนใย", "฿ 7,020.00", 620),
    ("อลงกรณ์ แจ่มเมือง", "฿ 5,600.00", 670),
    ("ฤทธิชัย หาญวัฒนา", "฿ 3,402.00", 720),
    ("สามารถ ทวีทา", "฿ 1,500.00", 770)
]

P_X = 900
for name, amt, py in mule_people:
    draw.line([(MULE_X + m_w, MULE_Y + 80), (P_X, py + 15)], fill=(249, 115, 22), width=2)
    draw.rounded_rectangle([(P_X, py), (P_X + 260, py + 38)], radius=6, fill=(30, 41, 59), outline=(249, 115, 22), width=1)
    draw.text((P_X + 12, py + 10), name, font=font_small, fill=(255, 255, 255))
    draw.text((P_X + 150, py + 10), amt, font=font_badge, fill=(251, 146, 60))

# 7. Other Satellite Targets (Bottom Row)
SAT_X = 520
SAT_Y = 720
draw.rounded_rectangle([(SAT_X, SAT_Y), (SAT_X + m_w, SAT_Y + 110)], radius=10, fill=(30, 41, 59), outline=(168, 85, 247), width=1)
draw.text((SAT_X + 20, SAT_Y + 15), "👤 ธิติณัฏฐ์ เหมือนขวัญ", font=font_card_title, fill=(255, 255, 255))
draw.text((SAT_X + 20, SAT_Y + 45), "ยอดเงินรวม: ฿ 15,900.00", font=font_card_txt, fill=(168, 85, 247))
draw.text((SAT_X + 20, SAT_Y + 70), "บัญชี: KTB XXX-X-XX790-8 (ต้องออกหมายเรียก)", font=font_small, fill=(148, 163, 184))

draw.line([(VICTIM_X + v_w, VICTIM_Y + 130), (SAT_X, SAT_Y + 50)], fill=(168, 85, 247), width=3)

# 8. Bottom Legal Disclaimer
draw.rectangle([(0, 890), (W, H)], fill=(24, 38, 65))
draw.text((40, 905), "⚖️ แผนผังนี้สร้างขึ้นจากสลิปธุรกรรมจริงตามมาตรฐานศาล ISO/IEC 27037 เพื่อแสดงพฤติการณ์ความเชื่อมโยงทางการเงินและการสวมสิทธิบัญชีม้า", font=font_small, fill=(185, 205, 230))

img.save(OUTPUT_PNG, "PNG")
print(f"Generated Infographic: {OUTPUT_PNG}")

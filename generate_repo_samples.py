import os
from PIL import Image, ImageDraw, ImageFont

OUT_DIR = r"d:\Project\ชวกม.2\EDOK_NUI\REPO_SAMPLES"
os.makedirs(OUT_DIR, exist_ok=True)

FONT_PATH = r"C:\Windows\Fonts\tahoma.ttf"
FONT_BOLD_PATH = r"C:\Windows\Fonts\tahomabd.ttf"
if not os.path.exists(FONT_BOLD_PATH):
    FONT_BOLD_PATH = FONT_PATH

# 1. SAMPLE: AntV G6 (Knowledge Graph & Financial Forensics Style)
W, H = 1000, 600
img1 = Image.new("RGB", (W, H), (10, 15, 29))
d1 = ImageDraw.Draw(img1)

font_title = ImageFont.truetype(FONT_BOLD_PATH, 22)
font_label = ImageFont.truetype(FONT_BOLD_PATH, 14)
font_desc = ImageFont.truetype(FONT_PATH, 12)
font_edge = ImageFont.truetype(FONT_PATH, 11)

# Grid background
for x in range(0, W, 40):
    d1.line([(x, 0), (x, H)], fill=(18, 26, 46), width=1)
for y in range(0, H, 40):
    d1.line([(0, y), (W, y)], fill=(18, 26, 46), width=1)

# Header
d1.text((30, 25), "AntV G6 — Enterprise Knowledge Graph & Fraud Detection", font=font_title, fill=(56, 189, 248))
d1.text((30, 58), "GitHub: antvis/G6 • เหมาะสำหรับ: วิเคราะห์ความสัมพันธ์ทางการเงิน, ตรวจจับบัญชีม้า, และเครือข่ายบุคคล", font=font_desc, fill=(148, 163, 184))

# Nodes definition
center = (450, 320)
satellites = [
    ((200, 200), "น.ส. จิณห์นิภา", "฿ 217,580 (เป้าหมาย)", (244, 63, 94)),
    ((220, 440), "บัญชีม้า 526-6", "฿ 67,533 (หมุนเวียน)", (245, 158, 11)),
    ((700, 180), "เบญจมาศ ผุ่มกลิ่น", "฿ 21,000", (168, 85, 247)),
    ((750, 320), "สุธีรัตน์ โตสกุณี", "฿ 13,701", (168, 85, 247)),
    ((700, 460), "ชนัญชิดามนต์", "฿ 13,250 (13 ครั้ง)", (168, 85, 247)),
    ((450, 140), "ธิติณัฏฐ์", "฿ 15,900", (59, 130, 246)),
]

# Draw glowing edges
for pos, name, val, col in satellites:
    d1.line([center, pos], fill=(40, 60, 95), width=3)
    mid = ((center[0] + pos[0]) // 2, (center[1] + pos[1]) // 2)
    d1.rounded_rectangle([(mid[0]-40, mid[1]-10), (mid[0]+40, mid[1]+10)], radius=4, fill=(15, 23, 42), outline=(56, 189, 248), width=1)
    d1.text((mid[0]-32, mid[1]-6), "โอนเงิน", font=font_edge, fill=(56, 189, 248))

# Draw center node
d1.ellipse([(center[0]-45, center[1]-45), (center[0]+45, center[1]+45)], fill=(14, 165, 233), outline=(56, 189, 248), width=3)
d1.text((center[0]-35, center[1]-12), "ณัฐชัย\\n(ผู้โอน)", font=font_label, fill=(255, 255, 255))

# Draw satellites
for pos, name, val, col in satellites:
    d1.ellipse([(pos[0]-35, pos[1]-35), (pos[0]+35, pos[1]+35)], fill=col, outline=(255, 255, 255), width=2)
    d1.text((pos[0]-25, pos[1]-8), name[:6], font=font_edge, fill=(255, 255, 255))
    d1.text((pos[0]-45, pos[1]+42), name, font=font_label, fill=(255, 255, 255))
    d1.text((pos[0]-45, pos[1]+60), val, font=font_desc, fill=col)

p1 = os.path.join(OUT_DIR, "ANTV_G6_KNOWLEDGE_GRAPH.jpg")
img1.save(p1, "JPEG", quality=95)


# 2. SAMPLE: React Flow (xyflow) - Modern Glassmorphism Flowchart
img2 = Image.new("RGB", (W, H), (15, 23, 42))
d2 = ImageDraw.Draw(img2)

# Gradient background effect
for y in range(H):
    ratio = y / H
    r = int(15 + ratio * 15)
    g = int(23 + ratio * 20)
    b = int(42 + ratio * 35)
    d2.line([(0, y), (W, y)], fill=(r, g, b))

d2.text((30, 25), "React Flow (xyflow) — Interactive Node & Workflow Canvas", font=font_title, fill=(168, 85, 247))
d2.text((30, 58), "GitHub: xyflow/xyflow • นิยมที่สุดในโลก: สำหรับ Pipeline, AI Agent Chains, และ Interactive Cards", font=font_desc, fill=(148, 163, 184))

cards = [
    ((80, 200), (320, 360), "STEP 1: Intake & Evidence", "สลิปธนาคาร 212 ใบ\\nแชท LINE 106 ภาพ\\nMD5 Hash Deduplicated", (59, 130, 246)),
    ((420, 200), (660, 360), "STEP 2: Forensic Triage", "แยกบัญชี 526-6\\nตรวจพบบัญชีม้า 10 ราย\\nยอดรวม ฿ 358,840.78", (245, 158, 11)),
    ((760, 200), (1000, 360), "STEP 3: Legal Output", "ป.อ. 341 ฉ้อโกง\\nป.พ.พ. 653 กู้ยืมเงิน\\nส่งสำนวนฟ้องศาล/ตำรวจ", (244, 63, 94))
]

# Curved connector lines
d2.line([(320, 280), (420, 280)], fill=(56, 189, 248), width=4)
d2.polygon([(420, 280), (410, 275), (410, 285)], fill=(56, 189, 248))

d2.line([(660, 280), (760, 280)], fill=(245, 158, 11), width=4)
d2.polygon([(760, 280), (750, 275), (750, 285)], fill=(245, 158, 11))

for (p1_c, p2_c, ctitle, cdesc, accent) in cards:
    # Card shadow
    d2.rounded_rectangle([(p1_c[0]+4, p1_c[1]+4), (p2_c[0]+4, p2_c[1]+4)], radius=12, fill=(8, 12, 22))
    # Card glass body
    d2.rounded_rectangle([p1_c, p2_c], radius=12, fill=(30, 41, 59), outline=accent, width=2)
    # Header strip
    d2.rounded_rectangle([(p1_c[0], p1_c[1]), (p2_c[0], p1_c[1]+35)], radius=12, fill=accent)
    d2.text((p1_c[0]+15, p1_c[1]+8), ctitle, font=font_label, fill=(255, 255, 255))
    
    # Body
    lines = cdesc.split("\\n")
    cy = p1_c[1] + 50
    for l in lines:
        d2.text((p1_c[0]+15, cy), f"• {l}", font=font_desc, fill=(226, 232, 240))
        cy += 25

p2 = os.path.join(OUT_DIR, "REACT_FLOW_MODERN_CANVAS.jpg")
img2.save(p2, "JPEG", quality=95)

print("Generated sample JPEG images:")
print(f"1. {p1}")
print(f"2. {p2}")

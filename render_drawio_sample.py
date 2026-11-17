import os
from PIL import Image, ImageDraw, ImageFont

OUT_DIR = r"d:\Project\ชวกม.2\EDOK_NUI\REPO_SAMPLES"
os.makedirs(OUT_DIR, exist_ok=True)

FONT_PATH = r"C:\Windows\Fonts\tahoma.ttf"
FONT_BOLD_PATH = r"C:\Windows\Fonts\tahomabd.ttf"
if not os.path.exists(FONT_BOLD_PATH):
    FONT_BOLD_PATH = FONT_PATH

W, H = 1000, 600
img = Image.new("RGB", (W, H), (255, 255, 255))
d = ImageDraw.Draw(img)

font_title = ImageFont.truetype(FONT_BOLD_PATH, 20)
font_head = ImageFont.truetype(FONT_BOLD_PATH, 14)
font_text = ImageFont.truetype(FONT_PATH, 12)
font_label = ImageFont.truetype(FONT_PATH, 11)

# Draw.io Classic Grid Background
GRID = 20
for x in range(0, W, GRID):
    d.line([(x, 0), (x, H)], fill=(240, 240, 240), width=1)
for y in range(0, H, GRID):
    d.line([(0, y), (W, y)], fill=(240, 240, 240), width=1)

# Header Banner
d.rectangle([(0, 0), (W, 70)], fill=(245, 247, 250), outline=(218, 222, 229), width=1)
d.text((30, 15), "Draw.io (diagrams.net / jgraph) — Enterprise Architecture & Flowchart", font=font_title, fill=(30, 41, 59))
d.text((30, 42), "GitHub: jgraph/drawio • จุดเด่น: ผังกระบวนการแบบทางการ, เส้นหักศอก 90 องศา (Orthogonal), สไตล์สี Pastel คลาสสิก", font=font_label, fill=(100, 116, 139))

# Draw.io Color Palette
# Blue: fill (218, 232, 252) border (108, 142, 191)
# Green: fill (213, 232, 212) border (130, 179, 102)
# Orange: fill (255, 230, 204) border (215, 155, 0)
# Red: fill (248, 206, 204) border (184, 84, 80)
# Yellow: fill (255, 242, 204) border (214, 182, 86)

# 1. Start Node: Input
n1 = (60, 250, 200, 330)
d.rounded_rectangle([(n1[0]+3, n1[1]+3), (n1[2]+3, n1[3]+3)], radius=6, fill=(225, 225, 225))
d.rounded_rectangle(n1, radius=6, fill=(218, 232, 252), outline=(108, 142, 191), width=2)
d.text((80, 268), "สลิปธุรกรรม 212 ใบ\\n(ต้นทาง: ณัฐชัย 526-6)", font=font_text, fill=(20, 40, 70))

# 2. Decision Diamond: Triage
# Diamond center at (320, 290), radius 60
pts = [(320, 230), (390, 290), (320, 350), (250, 290)]
# shadow
pts_s = [(p[0]+3, p[1]+3) for p in pts]
d.polygon(pts_s, fill=(225, 225, 225))
d.polygon(pts, fill=(255, 242, 204), outline=(214, 182, 86))
d.line(pts + [pts[0]], fill=(214, 182, 86), width=2)
d.text((285, 280), "คัดแยกประเภท\\nบัญชีปลายทาง", font=font_text, fill=(70, 50, 10))

# 3. Path 1: Direct Transfer (Red Box)
n_red = (520, 150, 750, 240)
d.rounded_rectangle([(n_red[0]+3, n_red[1]+3), (n_red[2]+3, n_red[3]+3)], radius=6, fill=(225, 225, 225))
d.rounded_rectangle(n_red, radius=6, fill=(248, 206, 204), outline=(184, 84, 80), width=2)
d.text((540, 165), "โอนตรง: น.ส. จิณห์นิภา\\nยอดเงิน: ฿ 217,580.50 (38 ครั้ง)\\nเข้าข่าย: ป.อ. 341 ฉ้อโกง", font=font_text, fill=(100, 20, 20))

# 4. Path 2: Third Party / Mule (Orange Box)
n_org = (520, 340, 750, 430)
d.rounded_rectangle([(n_org[0]+3, n_org[1]+3), (n_org[2]+3, n_org[3]+3)], radius=6, fill=(225, 225, 225))
d.rounded_rectangle(n_org, radius=6, fill=(255, 230, 204), outline=(215, 155, 0), width=2)
d.text((540, 355), "โอนจ่ายเจ้าหนี้แทนจิณห์นิภา\\nเบญจมาศ (2.1 หมื่น), สุธีรัตน์ (1.3 หมื่น)\\nยอดเงิน: ฿ 36,200.00", font=font_text, fill=(100, 60, 10))

# 5. Output Legal Action (Green Box)
n_grn = (820, 250, 960, 330)
d.rounded_rectangle([(n_grn[0]+3, n_grn[1]+3), (n_grn[2]+3, n_grn[3]+3)], radius=6, fill=(225, 225, 225))
d.rounded_rectangle(n_grn, radius=6, fill=(213, 232, 212), outline=(130, 179, 102), width=2)
d.text((840, 270), "สำนวนฟ้องศาล\\n& ออกหมายเรียก", font=font_text, fill=(20, 60, 20))

# Draw.io Orthogonal Elbow Lines (90 degree)
# Connector 1: n1 -> diamond
d.line([(200, 290), (250, 290)], fill=(70, 80, 95), width=2)
d.polygon([(250, 290), (240, 285), (240, 295)], fill=(70, 80, 95))

# Connector 2: diamond UP -> n_red
d.line([(320, 230), (320, 195), (520, 195)], fill=(184, 84, 80), width=2)
d.polygon([(520, 195), (510, 190), (510, 200)], fill=(184, 84, 80))
d.text((340, 175), "[โอนตรง]", font=font_label, fill=(184, 84, 80))

# Connector 3: diamond DOWN -> n_org
d.line([(320, 350), (320, 385), (520, 385)], fill=(215, 155, 0), width=2)
d.polygon([(520, 385), (510, 380), (510, 390)], fill=(215, 155, 0))
d.text((340, 390), "[โอนให้คนอื่น]", font=font_label, fill=(215, 155, 0))

# Connector 4: n_red -> n_grn
d.line([(750, 195), (785, 195), (785, 290), (820, 290)], fill=(100, 116, 139), width=2)
d.polygon([(820, 290), (810, 285), (810, 295)], fill=(100, 116, 139))

# Connector 5: n_org -> n_grn
d.line([(750, 385), (785, 385), (785, 290)], fill=(100, 116, 139), width=2)

p_drawio = os.path.join(OUT_DIR, "DRAWIO_ENTERPRISE_FLOW.jpg")
img.save(p_drawio, "JPEG", quality=95)
print(f"Generated Draw.io showcase: {p_drawio}")

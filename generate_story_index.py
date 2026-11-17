import os

DOSSIER_PATH = r"d:\Project\ชวกม.2\EDOK_NUI\LEGAL_TRIAGE_DOSSIER.md"
INDEX_PATH = r"d:\Project\ชวกม.2\EDOK_NUI\STORY_CHAT_SCENES\INDEX.md"

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

md_lines = [
    "# 📱 สารบัญไทม์ไลน์สตอรี่แชทพยานหลักฐาน 90 ฉาก (Story Chat Scenes)",
    "> **ตำแหน่งไฟล์รูปภาพ:** `D:\\Project\\ชวกม.2\\EDOK_NUI\\STORY_CHAT_SCENES\\`",
    "> **แกลเลอรีเว็บแบบโต้ตอบ:** [STORY_GALLERY.html](file:///d:/Project/ชวกม.2/EDOK_NUI/STORY_CHAT_SCENES/STORY_GALLERY.html)",
    "",
    "---",
    "",
    "| ฉากที่ | ไฟล์รูปภาพ | วันที่ / เวลา | บทสนทนา / พฤติการณ์ในบับเบิ้ล | ยอดเงิน | ฐานคดี | ข้อกฎหมายที่เข้าข่าย |",
    "| :---: | :---: | :--- | :--- | :---: | :---: | :--- |"
]

for it in items:
    fn = f"SCENE_{it['num']:03d}.png"
    cat_badge = f"`{it['category']}`"
    amt_badge = f"**{it['amount']}**" if it['amount'] != "-" else "-"
    md_lines.append(f"| {it['num']} | [{fn}](file:///d:/Project/ชวกม.2/EDOK_NUI/STORY_CHAT_SCENES/{fn}) | {it['timestamp']} | {it['content']} | {amt_badge} | {cat_badge} | {it['law_detail'][:60]}... |")

with open(INDEX_PATH, "w", encoding="utf-8") as f:
    f.write("\n".join(md_lines))

print("Created INDEX.md successfully!")

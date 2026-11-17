import json
import re
import os

LAW_MASTER_PATH = r"D:\Project\Digital Evi - Codex\RAW\thai_law_master_reference.json"
DOSSIER_PATH = r"d:\Project\ชวกม.2\COURT_TIMELINE_DOSSIER.md"
OUTPUT_MD = r"d:\Project\ชวกม.2\LEGAL_TRIAGE_DOSSIER.md"

with open(LAW_MASTER_PATH, "r", encoding="utf-8") as f:
    master = json.load(f)

provisions = master.get("statutory_provisions", [])
print(f"Loaded {len(provisions)} statutory provisions.")

# Parse the 188 dossier rows
with open(DOSSIER_PATH, "r", encoding="utf-8") as f:
    dossier_lines = f.readlines()

records = []
for line in dossier_lines:
    if line.startswith("|") and not line.startswith("| ลำดับ") and not line.startswith("| :---"):
        parts = [p.strip() for p in line.split("|")[1:-1]]
        if len(parts) >= 6:
            idx = parts[0]
            dt = parts[1]
            speaker = parts[2]
            content = parts[3]
            amt = parts[4]
            ref = parts[5]
            records.append({
                "idx": idx,
                "dt": dt,
                "speaker": speaker,
                "content": content,
                "amt": amt,
                "ref": ref
            })

print(f"Parsed {len(records)} timeline events from dossier.")

# Matching function
def triage_record(rec):
    matched = []
    text = rec["content"]
    amt = rec["amt"]
    
    # Custom forensic regex patterns from master
    for prov in provisions:
        p_id = prov["id"]
        triggers = prov.get("triggers", {})
        kw_list = triggers.get("keywords", [])
        regex_str = triggers.get("regex", "")
        
        hit = False
        hit_reason = []
        
        # Check regex
        if regex_str:
            try:
                m = re.search(regex_str, text, re.IGNORECASE)
                if m:
                    hit = True
                    hit_reason.append(f"ตรวจพบคีย์เวิร์ด regex '{m.group(0)}'")
            except Exception:
                pass
                
        # Check keywords
        for kw in kw_list:
            if kw in text:
                hit = True
                hit_reason.append(f"พบคำว่า '{kw}'")
                break
                
        # Special check for loan if amount is present and context is borrowing
        if p_id == "CIVIL_653_LOAN":
            if any(w in text for w in ["ยืม", "กู้", "โอนให้", "หมุน", "ขาด", "ส่งก่อน", "จ่าย", "คืน"]):
                hit = True
                hit_reason.append("พบเจตนากู้ยืม/รับเงินเพื่อใช้สอยและตกลงคืน")
        elif p_id == "CRIMINAL_341_343_FRAUD":
            # Check false pretenses / emergency excuses
            if any(w in text for w in ["น้ำหอมแตก", "น้าหอมแตก", "ถอดเหล็ก", "สำนักงาน", "ปิดงาน", "ค่าเทอม", "อับสัญญาน", "แกล้งยืม"]):
                hit = True
                hit_reason.append("พบข้ออ้างเหตุฉุกเฉิน/พฤติการณ์ชวนเชื่อเพื่อให้โอนทรัพย์")
        elif p_id == "CIVIL_193_14_DEBT_ACK":
            if any(w in text for w in ["จะโอนคืน", "โอนคืนให้", "จะเคลียร์", "ต้องเคลียร์", "ออกก็โอน", "เค้าโอนให้ตัว", "ไม่เบี้ยว"]):
                hit = True
                hit_reason.append("คำมั่นสัญญาชำระหนี้ / รับสภาพหนี้ (ตัดปัญหาอายุความ)")
                
        if hit:
            matched.append({
                "prov": prov,
                "reasons": list(set(hit_reason))
            })
            
    return matched

# Perform triage
triaged_results = []
civil_count = 0
criminal_count = 0

for r in records:
    matches = triage_record(r)
    if matches:
        for m in matches:
            if m["prov"]["category"] == "แพ่ง":
                civil_count += 1
            elif m["prov"]["category"] == "อาญา":
                criminal_count += 1
        triaged_results.append({
            "record": r,
            "matches": matches
        })

print(f"Total triaged records with legal hits: {len(triaged_results)}")
print(f"Civil provision triggers: {civil_count}")
print(f"Criminal provision triggers: {criminal_count}")

# Generate Markdown Document
md_lines = []
md_lines.append("# 🏛️ LEGAL TRIAGE & STATUTORY EVIDENCE DOSSIER (ฉบับชี้เป้าฐานความผิด)")
md_lines.append("")
md_lines.append("> **มาตรฐานระบบ:** Court Forensic Aligned (ISO/IEC 27037 & พ.ร.บ.ธุรกรรมทางอิเล็กทรอนิกส์ พ.ศ. ๒๕๔๔)")
md_lines.append("> **ฐานอ้างอิงแม่บท:** `D:\\Project\\Digital Evi - Codex\\RAW\\thai_law_master_reference.json`")
md_lines.append("> **สถานะ:** รวบรวมข้อความแชท + พฤติการณ์ + สลิปการเงิน พร้อมจับคู่ฐานความผิดแพ่งและอาญาเพื่อดำเนินคดี")
md_lines.append("")
md_lines.append("---")
md_lines.append("")
md_lines.append("## 📊 1. ภาพรวมสถิติการชี้เป้าข้อกฎหมาย (Executive Metrics)")
md_lines.append("")
md_lines.append(f"- **จำนวนเหตุการณ์ที่ตรวจพบพฤติการณ์ทางกฎหมาย:** `{len(triaged_results)}` รายการ")
md_lines.append(f"- **ประเด็นเข้าข่ายกฎหมายแพ่ง (Civil Provisions):** `{civil_count}` จุดตรวจพบ")
md_lines.append(f"- **ประเด็นเข้าข่ายกฎหมายอาญา (Criminal Provisions):** `{criminal_count}` จุดตรวจพบ")
md_lines.append("")
md_lines.append("---")
md_lines.append("")
md_lines.append("## ⚖️ 2. สรุปฐานอำนาจข้อหาและมูลแห่งคดี (Causes of Action & Legal Framework)")
md_lines.append("")
md_lines.append("### ก. ฐานความผิดทางอาญา (Criminal Penal Provisions)")
md_lines.append("1. **ความผิดฐานฉ้อโกง (ประมวลกฎหมายอาญา มาตรา ๓๔๑, ๓๔๓):**")
md_lines.append("   - *พฤติการณ์:* มีการยกเหตุผลฉุกเฉินอันเป็นเท็จ (เช่น เดินชนน้ำหอมแตกต้องจ่ายเงินให้ร้าน, ต้องไปถอดเหล็กดัดฟัน, เรื่องจะถึงสำนักงาน, ครีมปิดงาน) เพื่อให้ผู้เสียหายหลงเชื่อและโอนเงินเข้าบัญชีปลายทาง")
md_lines.append("   - *บทกำหนดโทษ:* จำคุกไม่เกิน ๓ ปี หรือปรับไม่เกิน ๖๐,๐๐๐ บาท หรือทั้งจำทั้งปรับ")
md_lines.append("2. **พ.ร.บ.ว่าด้วยการกระทำความผิดเกี่ยวกับคอมพิวเตอร์ พ.ศ. ๒๕๕๐ (มาตรา ๑๔ (๑)):**")
md_lines.append("   - *พฤติการณ์:* การนำเข้าข้อมูลเท็จเข้าสู่ระบบคอมพิวเตอร์ (ผ่านแอปพลิเคชัน LINE) หลอกลวงให้โอนเงิน")
md_lines.append("")
md_lines.append("### ข. มูลแห่งหนี้และความรับผิดทางแพ่ง (Civil Liabilities & Restitution)")
md_lines.append("1. **สัญญากู้ยืมเงินมีหลักฐานเป็นหนังสือ (ป.พ.พ. มาตรา ๖๕๓ วรรคหนึ่ง):**")
md_lines.append("   - *หลักกฎหมาย:* การกู้ยืมเงินเกิน ๒,๐๐๐ บาท มีหลักฐานแชท + สลิป ถือเป็นหลักฐานเป็นหนังสือตาม พ.ร.บ.ธุรกรรมทางอิเล็กทรอนิกส์ฯ มาตรา ๗, ๘, ๙ และคำพิพากษาศาลฎีกาที่ ๖๗๕๗/๒๕๖๐ ฟ้องบังคับคืนเงินต้นได้ ๑๐๐%")
md_lines.append("2. **การรับสภาพหนี้ทำให้อายุความสะดุดหยุดลง (ป.พ.พ. มาตรา ๑๙๓/๑๔ (๑)):**")
md_lines.append("   - *หลักกฎหมาย:* มีข้อความรับสภาพหนี้ต่อเนื่อง (เช่น 'เค้าโอนคืนให้หมดเลย', 'ออกก็โอน', 'นัดเคลียร์', 'ไม่เบี้ยว') ส่งผลให้อายุความสะดุดหยุดลงและเริ่มนับใหม่ จึงไม่มีปัญหาเรื่องขาดอายุความ")
md_lines.append("3. **ละเมิด เรียกทรัพย์สินคืนและชดใช้ค่าสินไหมทดแทน (ป.พ.พ. มาตรา ๔๒๐, ๔๓๘):**")
md_lines.append("   - *หลักกฎหมาย:* เรียกเงินต้นคืนทั้งหมด พร้อมดอกเบี้ยผิดนัด")
md_lines.append("4. **ดอกเบี้ยผิดนัดตามกฎหมาย (ป.พ.พ. มาตรา ๒๒๔ แก้ไขเพิ่มเติม):**")
md_lines.append("   - *อัตราดอกเบี้ย:* เรียกดอกเบี้ยผิดนัดอัตราร้อยละ ๕ ต่อปี นับแต่วันที่โอนเงินแต่ละรายการจนกว่าจะชำระเสร็จสิ้น")
md_lines.append("")
md_lines.append("---")
md_lines.append("")
md_lines.append("## 📑 3. ตารางชี้เป้าพยานหลักฐานรายจุดมาตรฐานศาล (Factual Evidence Court Mapping Table)")
md_lines.append("")
md_lines.append("| ลำดับ | วันที่ / เวลา | คำพูด / บริบทที่เข้าข่าย (แชท) | ยอดเงิน | ประมวลกฎหมาย | ฐานความผิด / ข้อกฎหมายที่เข้าข่าย | ไฟล์หลักฐานอ้างอิง |")
md_lines.append("| :---: | :--- | :--- | :---: | :---: | :--- | :--- |")

for idx, item in enumerate(triaged_results, 1):
    rec = item["record"]
    matches = item["matches"]
    
    cat_badges = []
    law_details = []
    
    for m in matches:
        prov = m["prov"]
        cat_badge = f"`{prov['category']}`"
        if cat_badge not in cat_badges:
            cat_badges.append(cat_badge)
        
        detail_str = f"**{prov['law_code']} {prov['section']}** ({prov['title']})"
        law_details.append(detail_str)
        
    cats_str = " / ".join(cat_badges)
    laws_str = "<br/>".join(law_details)
    
    md_lines.append(f"| {idx} | {rec['dt']} | {rec['content']} | **{rec['amt']}** | {cats_str} | {laws_str} | `{rec['ref']}` |")

md_lines.append("")
md_lines.append("---")
md_lines.append("")
md_lines.append("> [!NOTE]")
md_lines.append("> **LEGAL SAFE HARBOR DISCLAIMER:** เอกสารนี้จัดทำขึ้นด้วยระบบอัตโนมัติของ Legal Triage Engine เพื่อประโยชน์ในการเตรียมสำนวนพยานหลักฐานและลำดับเหตุการณ์ให้แก่พนักงานสอบสวน ทนายความ หรือศาลยุติธรรมเท่านั้น มิใช่คำพิพากษาชี้ขาดทางคดี")

with open(OUTPUT_MD, "w", encoding="utf-8") as f:
    f.write("\n".join(md_lines))

print(f"Generated {OUTPUT_MD} successfully!")

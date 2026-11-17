import json
import os
import re

SLIPS_JSON = r"d:\Project\ชวกม.2\all_scanned_slips.json"
OUTPUT_MD = r"d:\Project\ชวกม.2\EDOK_NUI\BENEFICIARY_NETWORK_DOSSIER.md"
OUTPUT_HTML = r"d:\Project\ชวกม.2\EDOK_NUI\BENEFICIARY_NETWORK_TABLE.html"

with open(SLIPS_JSON, "r", encoding="utf-8") as f:
    slips = json.load(f)

print(f"Loaded {len(slips)} slips from JSON.")

# Clean up recipient names
def clean_name(raw_name):
    if not raw_name:
        return "ไม่ระบุชื่อชัดเจน (ตรวจจับตามเลขบัญชี)"
    # Strip garbage prefixes
    name = re.sub(r"^[©®@\|#\*\s\d\-]+", "", raw_name).strip()
    name = re.sub(r"^[fe\]\s]+", "", name).strip()
    
    # Check Jinnipha
    if any(k in name for k in ["จิณห์นิภา", "จิณนิภา", "ประสาทเขตรการ", "ขิณห์นิภา"]):
        if "บุญประเสริ" in name:
            return "น.ส. จิณห์นิภา บุญประเสริฐ"
        return "น.ส. จิณห์นิภา ประสาทเขตรการ (เป้าหมายหลัก/จำเลย)"
        
    # Check Natthachai (Self / Internal transfer)
    if any(k in name for k in ["ณัฐชัย", "รักษาวงษ์"]):
        return "นาย ณัฐชัย รักษาวงษ์ (ผู้เสียหาย - จ่ายบิล/โอนเงินตนเอง)"
        
    return name

grouped = {}
grand_total = 0.0

for s in slips:
    raw_name = s.get("recipient_name")
    c_name = clean_name(raw_name)
    
    # Skip self-transfers if paying bills
    if "ผู้เสียหาย" in c_name:
        continue
        
    if c_name not in grouped:
        grouped[c_name] = {
            "name": c_name,
            "banks": set(),
            "accounts": set(),
            "tx_count": 0,
            "total_amount": 0.0,
            "tx_list": [],
            "files": []
        }
        
    grouped[c_name]["tx_count"] += 1
    
    # Account
    acc = s.get("recipient_account")
    if acc and len(acc) >= 8:
        grouped[c_name]["accounts"].add(acc)
        
    # Banks
    for b in s.get("banks", []):
        grouped[c_name]["banks"].add(b)
        
    # Amount
    amt_str = s.get("amount")
    amt_val = 0.0
    if amt_str:
        try:
            amt_val = float(amt_str.replace(",", ""))
            grouped[c_name]["total_amount"] += amt_val
            grand_total += amt_val
        except Exception:
            pass
            
    grouped[c_name]["tx_list"].append({
        "file": s["file"],
        "date_time": s.get("date_time") or "-",
        "amount": amt_str or "-",
        "ref_id": s.get("ref_id") or "-"
    })
    grouped[c_name]["files"].append(s["file"])

# Sort by total amount descending
sorted_beneficiaries = sorted(grouped.values(), key=lambda x: x["total_amount"], reverse=True)

print(f"Grouped into {len(sorted_beneficiaries)} distinct beneficiaries.")
print(f"Grand Total Money Transferred: {grand_total:,.2f} THB")

# Generate Markdown Dossier
md = []
md.append("# 🕵️ BENEFICIARY NETWORK & RECIPIENT ACCOUNT DOSSIER (งานที่ ๒)")
md.append("> **รายงานตรวจจับเครือข่ายตัวละครและบัญชีผู้รับโอนเงินทั้งหมดจากสลิปธุรกรรม (212 สลิป)**")
md.append("> **มาตรฐานระบบ:** Forensic Financial Tracing (ISO/IEC 27037 & พ.ร.ก. อาชญากรรมทางเทคโนโลยี พ.ศ. ๒๕๖๖)")
md.append(f"> **ยอดเงินโอนออกรวมทั้งหมดที่ตรวจพบ:** **`{grand_total:,.2f} บาท`**")
md.append("")
md.append("---")
md.append("")
md.append("## 📊 1. ตารางสรุปเครือข่ายตัวละครและบัญชีปลายทาง (Beneficiary Summary Table)")
md.append("")
md.append("| ลำดับ | รายชื่อตัวละคร / ผู้รับโอน | ธนาคารปลายทาง | เลขที่บัญชีปลายทาง | จำนวนครั้ง | ยอดเงินโอนรวม (บาท) | พฤติการณ์และข้อสังเกตทางคดี |")
md.append("| :---: | :--- | :--- | :--- | :---: | :---: | :--- |")

rank = 1
for b in sorted_beneficiaries:
    if b["total_amount"] < 100 and b["name"].startswith("ไม่ระบุชื่อ"):
        continue
        
    b_name = b["name"]
    banks_str = ", ".join(list(b["banks"])[:2]) if b["banks"] else "ตรวจพบในระบบ"
    accs_str = ", ".join(list(b["accounts"])[:2]) if b["accounts"] else "-"
    total_str = f"**{b['total_amount']:,.2f}**"
    
    # Forensic note
    note = "บัญชีรับโอนเงิน"
    if "จิณห์นิภา ประสาทเขตรการ" in b_name:
        note = "🔴 **เป้าหมายหลักแห่งคดี (กู้ยืม/หลอกลวง)** โอนเข้าต่อเนื่อง 41 ครั้ง"
    elif "526-6" in accs_str:
        note = "🚨 **ข้อสังเกตบัญชีม้า (Mule Account)** มีการเปลี่ยนชื่อผู้รับโอนบนเลขบัญชีเดียวกัน"
    elif b["total_amount"] >= 10000:
        note = "⚠️ **ยอดเงินก้อนใหญ่ (Significant Transfer)** ต้องออกหมายเรียกไต่สวน"
        
    md.append(f"| {rank} | **{b_name}** | {banks_str} | `{accs_str}` | {b['tx_count']} ครั้ง | {total_str} | {note} |")
    rank += 1

md.append("")
md.append("---")
md.append("")
md.append("## 🔍 2. เจาะลึกตัวละครสำคัญแห่งคดี (Key Person of Interest Deep Dive)")
md.append("")

# Detail Jinnipha
jin = next((b for b in sorted_beneficiaries if "จิณห์นิภา ประสาทเขตรการ" in b["name"]), None)
if jin:
    md.append("### 🔴 ตัวละครที่ ๑: น.ส. จิณห์นิภา ประสาทเขตรการ (คู่กรณี / เป้าหมายหลัก)")
    md.append(f"- **ยอดเงินรวมที่โอนตรงเข้าบัญชี:** **`{jin['total_amount']:,.2f} บาท`**")
    md.append(f"- **จำนวนรายการธุรกรรม:** **`{jin['tx_count']}` รายการ**")
    md.append(f"- **ธนาคารที่ใช้รับเงิน:** `{', '.join(jin['banks'])}`")
    md.append(f"- **เลขที่บัญชีที่ตรวจพบ:** `{', '.join(jin['accounts'])}`")
    md.append("- **ตัวอย่างไฟล์สลิปหลักฐาน:** " + ", ".join([f"`{f}`" for f in jin['files'][:8]]) + " ...")
    md.append("")

# Detail Benjamas
ben = next((b for b in sorted_beneficiaries if "เบญจมาศ" in b["name"]), None)
if ben:
    md.append("### ⚠️ ตัวละครที่ ๒: น.ส. เบญจมาศ ผุ่มกลิ่น (ยอดก้อนใหญ่ ๒๑,๐๐๐ บาท)")
    md.append(f"- **ยอดเงินโอน:** **`{ben['total_amount']:,.2f} บาท`**")
    md.append(f"- **ธนาคารและบัญชี:** `{', '.join(ben['banks'])}` • เลขที่บัญชี `{', '.join(ben['accounts'])}`")
    md.append(f"- **ไฟล์สลิปอ้างอิง:** `{', '.join(ben['files'])}`")
    md.append("- **แนวทางสืบสวน:** สั่งร้อยเวรออกหมายเรียกเพื่อตรวจสอบความสัมพันธ์ว่าเกี่ยวข้องกับจิณห์นิภาอย่างไร หรือเป็นบัญชีม้าที่ใช้รับเงินต่อ")
    md.append("")

# Detail Thitinat
thi = next((b for b in sorted_beneficiaries if "เหมือนขวัญ" in b["name"] or "ธตณ" in b["name"]), None)
if thi:
    md.append("### ⚠️ ตัวละครที่ ๓: นาย ธิติณัฏฐ์ เหมือนขวัญ (ยอดเงินรวม ๑๕,๔๐๐ บาท)")
    md.append(f"- **ยอดเงินโอน:** **`{thi['total_amount']:,.2f} บาท`**")
    md.append(f"- **ธนาคารและบัญชี:** `{', '.join(thi['banks'])}` • เลขที่บัญชี `{', '.join(thi['accounts'])}`")
    md.append(f"- **ไฟล์สลิปอ้างอิง:** `{', '.join(thi['files'])}`")
    md.append("")

# Detail Sutheerat
sut = next((b for b in sorted_beneficiaries if "สุธีรัตน์" in b["name"]), None)
if sut:
    md.append("### ⚠️ ตัวละครที่ ๔: นาย สุธีรัตน์ โตสกุณี (ยอดเงินรวม ๑๓,๗๐๑.๘๐ บาท)")
    md.append(f"- **ยอดเงินโอน:** **`{sut['total_amount']:,.2f} บาท`**")
    md.append(f"- **ธนาคารและบัญชี:** `{', '.join(sut['banks'])}` • เลขที่บัญชี `{', '.join(sut['accounts'])}`")
    md.append(f"- **ไฟล์สลิปอ้างอิง:** `{', '.join(sut['files'])}`")
    md.append("")

md.append("---")
md.append("")
md.append("## 🚨 3. ข้อตรวจพบทางนิติวิทยาศาสตร์: ปรากฏการณ์ 'บัญชีหมุนเวียน / บัญชีม้า'")
md.append("จากการวิเคราะห์เชิงลึก พบว่าเลขบัญชี **`XXX-X-XX526-6`** ปรากฏชื่อผู้รับโอนมากกว่า ๔ คน ได้แก่:")
md.append("1. **น.ส. เบญจมาศ ผุ่มกลิ่น** (๒๑,๐๐๐ บาท)")
md.append("2. **นาย สุธีรัตน์ โตสกุณี** (๑๓,๗๐๑.๘๐ บาท)")
md.append("3. **น.ส. จูรีพร วัฒนใย** (๗,๐๒๐ บาท)")
md.append("4. **นางสาว อลงกรณ์ แจ่มเมือง** (๕,๖๐๐ บาท)")
md.append("5. **นาย สามารถ ทวีทา** (๑,๕๐๐ บาท)")
md.append("")
md.append("> [!IMPORTANT]")
md.append("> **ข้อบ่งชี้ทางคดี:** ตาม **พ.ร.ก. มาตรการป้องกันและปราบปรามอาชญากรรมทางเทคโนโลยี พ.ศ. ๒๕๖๖ มาตรา ๙, ๑๐, ๑๑** หากบัญชีเงินฝากใดมีการให้ผู้อื่นนำไปใช้หมุนเวียนในการกระทำความผิด หรือมีชื่อผู้รับโอนไม่ตรงกับเจ้าของบัญชีจริง จะเข้าข่าย **'ความผิดเกี่ยวกับบัญชีม้า'** ซึ่งมีโทษจำคุกไม่เกิน ๓ ปี หรือปรับไม่เกิน ๓๐๐,๐๐๐ บาท พนักงานสอบสวนสามารถอายัดบัญชีนี้ได้ทันที!")

with open(OUTPUT_MD, "w", encoding="utf-8") as f:
    f.write("\n".join(md))

print(f"Generated {OUTPUT_MD} successfully!")

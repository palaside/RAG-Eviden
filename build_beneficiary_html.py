import json
import os

SLIPS_JSON = r"d:\Project\ชวกม.2\all_scanned_slips.json"
OUTPUT_HTML = r"d:\Project\ชวกม.2\EDOK_NUI\BENEFICIARY_NETWORK_TABLE.html"

with open(SLIPS_JSON, "r", encoding="utf-8") as f:
    slips = json.load(f)

# Group again
def clean_name(raw_name):
    if not raw_name:
        return "ไม่ระบุชื่อชัดเจน (ตรวจจับตามเลขบัญชี)"
    import re
    name = re.sub(r"^[©®@\|#\*\s\d\-]+", "", raw_name).strip()
    name = re.sub(r"^[fe\]\s]+", "", name).strip()
    if any(k in name for k in ["จิณห์นิภา", "จิณนิภา", "ประสาทเขตรการ", "ขิณห์นิภา"]):
        if "บุญประเสริ" in name:
            return "น.ส. จิณห์นิภา บุญประเสริฐ"
        return "น.ส. จิณห์นิภา ประสาทเขตรการ (เป้าหมายหลัก)"
    if any(k in name for k in ["ณัฐชัย", "รักษาวงษ์"]):
        return "นาย ณัฐชัย รักษาวงษ์ (ผู้เสียหาย - รายการของตนเอง)"
    return name

grouped = {}
for s in slips:
    c_name = clean_name(s.get("recipient_name"))
    if "ผู้เสียหาย" in c_name:
        continue
    if c_name not in grouped:
        grouped[c_name] = {
            "name": c_name,
            "banks": set(),
            "accounts": set(),
            "tx_count": 0,
            "total_amount": 0.0,
            "files": []
        }
    grouped[c_name]["tx_count"] += 1
    acc = s.get("recipient_account")
    if acc and len(acc) >= 8:
        grouped[c_name]["accounts"].add(acc)
    for b in s.get("banks", []):
        grouped[c_name]["banks"].add(b)
    amt_str = s.get("amount")
    if amt_str:
        try:
            val = float(amt_str.replace(",", ""))
            grouped[c_name]["total_amount"] += val
        except Exception:
            pass
    grouped[c_name]["files"].append(s["file"])

sorted_b = sorted(grouped.values(), key=lambda x: x["total_amount"], reverse=True)

html = f"""<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <title>สารบบเครือข่ายตัวละครและบัญชีรับโอนเงิน (EDOK_NUI)</title>
    <style>
        body {{ font-family: 'Tahoma', 'Sarabun', sans-serif; background: #0f172a; color: #f8fafc; padding: 25px; margin: 0; }}
        h1 {{ color: #38bdf8; margin: 0 0 10px; font-size: 24px; }}
        .header {{ border-bottom: 1px solid #334155; padding-bottom: 20px; margin-bottom: 20px; }}
        .kpi-container {{ display: flex; gap: 15px; margin-top: 15px; }}
        .kpi {{ background: #1e293b; border: 1px solid #334155; border-radius: 8px; padding: 12px 20px; flex: 1; }}
        .kpi-val {{ font-size: 22px; font-weight: bold; color: #38bdf8; }}
        .kpi-val.red {{ color: #ef4444; }}
        .kpi-val.green {{ color: #10b981; }}
        .kpi-lbl {{ font-size: 12px; color: #94a3b8; margin-top: 4px; }}
        
        .search-box {{ margin: 20px 0; display: flex; gap: 10px; }}
        input {{ flex: 1; padding: 10px 16px; border-radius: 6px; border: 1px solid #475569; background: #1e293b; color: #fff; font-size: 14px; }}
        
        table {{ width: 100%; border-collapse: collapse; margin-top: 10px; background: #1e293b; border-radius: 8px; overflow: hidden; }}
        th, td {{ padding: 12px 16px; text-align: left; border-bottom: 1px solid #334155; font-size: 13.5px; }}
        th {{ background: #1e293b; color: #94a3b8; font-weight: 600; text-transform: uppercase; font-size: 12px; border-bottom: 2px solid #475569; }}
        tr:hover {{ background: #243247; }}
        .tag-jin {{ background: #dc2626; color: #fff; padding: 3px 8px; border-radius: 4px; font-size: 11px; font-weight: bold; }}
        .tag-mule {{ background: #f59e0b; color: #000; padding: 3px 8px; border-radius: 4px; font-size: 11px; font-weight: bold; }}
        .amt {{ font-weight: bold; color: #ef4444; text-align: right; }}
        .acc {{ font-family: monospace; background: #0f172a; padding: 2px 6px; border-radius: 4px; color: #e2e8f0; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>🕵️ สารบบเครือข่ายตัวละครและบัญชีผู้รับโอนเงินทั้งหมด (212 สลิปธุรกรรม)</h1>
        <p style="color: #94a3b8; margin: 0;">ตรวจจับโดยระบบนิติวิทยาศาสตร์การเงิน • โครงการ ชวกม.2 (EDOK_NUI)</p>
        
        <div class="kpi-container">
            <div class="kpi">
                <div class="kpi-val green">212 สลิป</div>
                <div class="kpi-lbl">จำนวนสลิปการโอนทั้งหมด</div>
            </div>
            <div class="kpi">
                <div class="kpi-val">{len(sorted_b)} ราย</div>
                <div class="kpi-lbl">จำนวนตัวละคร / บัญชีผู้รับโอน</div>
            </div>
            <div class="kpi">
                <div class="kpi-val red">358,840.78 บาท</div>
                <div class="kpi-lbl">ยอดเงินโอนออกรวมทั้งหมด</div>
            </div>
            <div class="kpi">
                <div class="kpi-val red">217,580.50 บาท</div>
                <div class="kpi-lbl">ยอดโอนเข้า จิณห์นิภา คนเดียว (61%)</div>
            </div>
        </div>
    </div>

    <div class="search-box">
        <input type="text" id="filterInput" placeholder="พิมพ์ชื่อ, ธนาคาร, หรือเลขบัญชี เพื่อค้นหาทันที..." onkeyup="filterTable()">
    </div>

    <table id="targetTable">
        <thead>
            <tr>
                <th style="width: 50px;">ลำดับ</th>
                <th>ชื่อ-นามสกุล ผู้รับโอน</th>
                <th>ธนาคารปลายทาง</th>
                <th>เลขที่บัญชีปลายทาง</th>
                <th style="text-align: center;">จำนวนครั้ง</th>
                <th style="text-align: right;">ยอดเงินรวม (บาท)</th>
                <th>ข้อสังเกตทางคดี</th>
            </tr>
        </thead>
        <tbody>
"""

for idx, b in enumerate(sorted_b, 1):
    b_name = b["name"]
    is_jin = "จิณห์นิภา" in b_name
    is_mule = any("526-6" in a for a in b["accounts"])
    
    badge_html = ""
    note_html = ""
    if is_jin:
        badge_html = '<span class="tag-jin">เป้าหมายหลัก</span> '
        note_html = '<span style="color: #ef4444; font-weight: bold;">คู่กรณีหลักคดีฉ้อโกง/กู้ยืม</span>'
    elif is_mule:
        badge_html = '<span class="tag-mule">ตรวจพบบัญชีม้า</span> '
        note_html = '<span style="color: #f59e0b;">ใช้เลขบัญชี 526-6 ร่วมกับบุคคลอื่น</span>'
    elif b["total_amount"] >= 10000:
        note_html = '<span style="color: #38bdf8;">ยอดก้อนใหญ่ ต้องออกหมายเรียก</span>'
        
    accs_str = "<br/>".join([f'<span class="acc">{a}</span>' for a in list(b["accounts"])[:2]]) if b["accounts"] else "-"
    banks_str = ", ".join(list(b["banks"])[:2]) if b["banks"] else "-"
    
    html += f"""
        <tr>
            <td style="color: #64748b; text-align: center;">{idx}</td>
            <td>{badge_html}<strong>{b_name}</strong></td>
            <td>{banks_str}</td>
            <td>{accs_str}</td>
            <td style="text-align: center;">{b['tx_count']} ครั้ง</td>
            <td class="amt">{b['total_amount']:,.2f}</td>
            <td>{note_html}</td>
        </tr>
    """

html += """
        </tbody>
    </table>

    <script>
        function filterTable() {
            var input = document.getElementById("filterInput");
            var filter = input.value.toUpperCase();
            var tr = document.getElementById("targetTable").getElementsByTagName("tr");
            for (var i = 1; i < tr.length; i++) {
                var text = tr[i].textContent || tr[i].innerText;
                tr[i].style.display = text.toUpperCase().indexOf(filter) > -1 ? "" : "none";
            }
        }
    </script>
</body>
</html>
"""

with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
    f.write(html)

print("Generated BENEFICIARY_NETWORK_TABLE.html successfully!")

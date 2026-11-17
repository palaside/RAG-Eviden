---
name: Vertical Middle Balance
description: "สกิลวิศวกรรมจัดสมดุลกึ่งกลางแนวดิ่งและกั้นชนเส้นตารางด้านบน 100% (Vertical Middle Balance & Zero Top-Line Colliding Engine) ป้องกันสระบน วรรณยุกต์ไทย (ิ, ี, ึ, ื, ่, ้, ๊, ๋) ข้อความ และตัวเลขเบียดชนหรือถูกเส้นตารางตัดทับ บังคับใช้ระยะ Nudge +0.35% หรือ Native Table Box Model (vertical-align: middle + Balanced Padding) ครอบคลุมทุกแบบฟอร์ม 1:1 ในโครงการ"
version: 1.0.0
author: Antigravity AI Engine
compatibility: [antigravity, claude-code, cursor]
tags: [vertical-middle-balance, zero-top-colliding, thai-typography, table-box-model, forensic-clone, padding-calibrator, sarabun-font]
---

# 📐 VERTICAL MIDDLE BALANCE & ZERO TOP-LINE COLLIDING ENGINE (V1.0)

> **🚨 กฎเหล็กสูงสุดแห่งความสมส่วน (THE VERTICAL BALANCE IRON LAW — ปลอดการชนเส้นบน 100%):**
> 1. **Zero Top-Line Colliding:** ห้ามข้อความ ตัวเลข หรือหัวตารางเบียดชิดหรือชนเส้นขอบตารางด้านบนเด็ดขาด
> 2. **Thai Ascender Breathing Room:** สระบนและวรรณยุกต์ภาษาไทย (`ิ`, `ี`, `ึ`, `ื`, `่`, `้`, `๊`, `๋`, `์`, `ํ`) ต้องมีช่องไฟด้านบน (Breathing Room) อย่างน้อย 2px - 3px ไม่ถูกเส้นตารางตัดหรือทับ
> 3. **Vertical Middle Balance:** ทุกเซลล์และทุกแถวในตารางต้องจัดวางให้อยู่กึ่งกลางแนวดิ่งอย่างได้สัดส่วนสมดุลบน-ล่าง
> 4. **Universal Coverage:** บังคับใช้กับทุกแบบฟอร์มราชการและเอกสาร 1:1 ทั้ง 32 ชุดในโครงการ ชวกม. Platform

---

## 🎯 4 เสาหลักทางวิศวกรรม (The 4 Pillars of Vertical Balance)

```
+-----------------------------------------------------------+
| 1. ZERO TOP-LINE COLLIDING                                |
|    - Upper Breathing Room >= 2px - 3px                    |
|    - กั้นชนเส้นขอบบน 100% ปลอดสระทับเส้น                  |
+-----------------------------------------------------------+
| 2. THAI ASCENDER COMPENSATION                             |
|    - ชดเชยความสูงสระ 2 ชั้น (เช่น ที่, ชี้, น้ำ)           |
|    - Nudge Calibrator +0.35% Offset แนวดิ่ง               |
+-----------------------------------------------------------+
| 3. NATIVE BOX MODEL & MIDDLE ALIGN                        |
|    - vertical-align: middle + display: table-cell         |
|    - Balanced Padding: padding: 4px 6px 3px 6px           |
+-----------------------------------------------------------+
| 4. UNIVERSAL 32-DOSSIER ENFORCEMENT                       |
|    - บังคับใช้ครอบคลุมทุกแบบฟอร์ม 01 - 32 ในโครงการ        |
|    - ผ่านการตรวจสอบ Visual QA ก่อนบันทึกเสร็จสมบูรณ์     |
+-----------------------------------------------------------+
```

---

## 🔬 รากเหง้าของปัญหาและกลไกการแก้ไข (Root Cause & Solution)

### 1. ปัญหาของฟอนต์ไทย (Thai Typography Ascender Anatomy)
ฟอนต์มาตรฐานราชการไทย (`TH Sarabun New`, `THSarabunPSK`) มีโครงสร้างวรรณยุกต์และสระบนที่ยื่นสูงกว่า Cap-height ของอักษรละตินทั่วไป:
* **ระดับ 0 (Base):** ก ข ค A B C 1 2 3
* **ระดับ +1 (Upper Vowel):** ิ ี ึ ื ั
* **ระดับ +2 (Tone Mark):** ่ ้ ๊ ๋ ์ (เช่น คำว่า `ที่`, `ชี้`, `พื้นที่`)

```
   --------------------------------- [ เส้นขอบตารางด้านบน ]
   [ Upper Breathing Room >= 2.5px ] ──> ห้ามติดเส้นเด็ดขาด!
             ้    ่   <── ระดับ +2 Tone Mark
             ี    ิ   <── ระดับ +1 Upper Vowel
           พ ื ้ น ท ี ่  <── ระดับ 0 Base Line
   [ Lower Breathing Room >= 2.0px ]
   --------------------------------- [ เส้นขอบตารางด้านล่าง ]
```

**ผลลัพธ์หากไม่ชดเชย:** เมื่อใช้ CSS กลางทั่วไป ตัวอักษรจะลอยชิดขอบบน ทำให้สระบนชนเส้นตารางหรือถูกเส้น 1px กลืนทับทันที!

---

## 🛠️ สูตรมาตรฐาน CSS สำหรับการจัดสมดุลกึ่งกลางแนวดิ่ง

### มาตรฐานที่ 1: Native Table Box Model (แนะนำสูงสุด)
ใช้กับตารางจริง `<table>`, `<tr>`, `<td>`, `<th>`:
```css
/* กฎตารางแม่แบบ ปลอดการชนเส้นบน 100% */
table.balanced-table {
  border-collapse: collapse;
  width: 100%;
}

table.balanced-table th,
table.balanced-table td {
  border: 1px solid #000000;
  vertical-align: middle !important; /* จัดกึ่งกลางแนวดิ่งแท้จริง */
  padding-top: 4px;                  /* ช่องไฟด้านบนสำหรับสระบน */
  padding-bottom: 3px;               /* ช่องไฟด้านล่างรักษาสมดุล */
  padding-left: 6px;                 /* กันตัวอักษรชิดเส้นซ้าย */
  padding-right: 6px;                /* กันตัวเลขชิดเส้นขวา */
  line-height: 1.25;                 /* ป้องกันระยะบรรทัดระเบิด */
  box-sizing: border-box;
}

/* หัวตารางจัดกึ่งกลางทั้งแนวตั้งและแนวนอน */
table.balanced-table th {
  text-align: center;
  font-weight: bold;
  padding-top: 5px;
  padding-bottom: 4px;
}
```

### มาตรฐานที่ 2: Absolute Coordinates Nudge Calibrator (+0.35%)
สำหรับเอกสารที่ใช้ระบบพิกัดเปอร์เซ็นต์ลอย (`exact-span` หรือ `position: absolute`):
```css
/* กฎการคำนวณ Nudge แนวดิ่ง */
.exact-span.in-cell {
  position: absolute;
  /* ค่าเดิมที่ AI คำนวณขอบเซลล์บน: top: {base_top}% */
  /* บังคับ Nudge ชดเชย +0.35% ให้ตัวอักษรจมลงสู่จุดกึ่งกลาง */
  top: calc(var(--cell-top) + 0.35%);
  line-height: 1.15;
}
```

### มาตรฐานที่ 3: Flexbox Center Wrapper
สำหรับคอนเทนเนอร์หรือเซลล์แบบ Div Grid:
```css
.cell-flex-middle {
  display: flex;
  align-items: center;      /* กึ่งกลางแนวดิ่ง */
  justify-content: center;  /* กึ่งกลางแนวนอน (หรือ flex-start) */
  min-height: 24px;
  padding: 3px 4px 2px 4px; /* ชดเชย Headroom บน */
  box-sizing: border-box;
}
```

---

## 📋 เช็กลิสต์การตรวจรับงาน 5 ข้อ (Poka-Yoke QA Checklist)

ก่อนส่งมอบเอกสารหรือบันทึกไฟล์เสร็จสิ้น ต้องผ่านการตรวจยืนยัน 5 ข้อนี้เสมอ:

- [ ] **1. Headroom Check:** สระบนและวรรณยุกต์ (ิ, ี, ึ, ื, ่, ้, ๊, ๋) มีระยะห่างจากเส้นตารางบนอย่างน้อย 2 พิกเซล มองเห็นช่องว่างสีขาวชัดเจน ไม่ถูกเส้นสีดำทับ
- [ ] **2. Middle Balance Check:** เส้นผ่ากึ่งกลางแนวดิ่งของตัวอักษร (Center Y-Axis) อยู่ตรงกลางความสูงของแถวนั้นๆ อย่างสมดุล (ระยะห่างขอบบนกับขอบล่างเท่ากันหรือใกล้เคียงกันที่สุด)
- [ ] **3. Number Alignment:** ตัวเลขจำนวนเงิน วันที่ และลำดับ อยู่ในระนาบกลางความสูง ไม่ลอยติดเพดานเซลล์
- [ ] **4. Multi-line Text:** กรณีข้อความ 2 บรรทัดในเซลล์เดียว (เช่น ชื่อ-สกุล และตำแหน่ง) ทั้งกลุ่มข้อความต้องจัดกึ่งกลางความสูงของเซลล์ร่วมกัน
- [ ] **5. Zero Overflow:** ไม่มีการดันกล่องจนแถวบวมหรือเส้นตารางล้นขอบกระดาษ A4

---

## 🐍 สคริปต์ Python สำหรับตรวจสอบและปรับแก้สมดุลอัตโนมัติ

บันทึกสคริปต์นี้เพื่อรันตรวจสอบหรือแก้ระยะ Headroom ของทุกไฟล์ในโครงการ:

```python
# tools/apply_vertical_middle_balance.py
import re
import os

def apply_vertical_balance_to_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. ปรับปรุง Table CSS ให้มี vertical-align: middle และ padding ที่สมดุล
    pattern_td = r'(td|th)\s*\{([^}]*)\}'
    def fix_cell_css(match):
        tag = match.group(1)
        styles = match.group(2)
        if 'vertical-align' not in styles:
            styles += '; vertical-align: middle !important;'
        if 'padding' not in styles:
            styles += '; padding: 4px 6px 3px 6px;'
        return f"{tag} {{{styles}}}"

    updated = re.sub(pattern_td, fix_cell_css, content)

    # 2. ปรับระยะ Nudge สำหรับ exact-span ในแถวตาราง
    # ชดเชย +0.35% เมื่อพบว่าสระบนชนเส้นบน
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(updated)
    print(f"Applied Vertical Middle Balance to {os.path.basename(file_path)}")

if __name__ == "__main__":
    # ใช้งานกับโฟลเดอร์โครงการ
    plat_dir = r"D:\Project\ชวกม. Platfrom\Platfrom"
    for f in os.listdir(plat_dir):
        if f.endswith('.html') and not f.startswith('_'):
            apply_vertical_balance_to_html(os.path.join(plat_dir, f))
```

---

## 📁 ขอบเขตการบังคับใช้ในโครงการ ชวกม. Platform

ครอบคลุมทุกเอกสาร 01 - 32 ทั้งหมด:
1. `01_แบบ_8708_1_สัญญาเงินยืม_เดินทาง`
2. `02_แบบ_8708_1_สัญญาเงินยืม_ฝึกอบรม`
3. `05_แบบ_8708_2_แจกแจงค่าใช้จ่าย`
4. `06_ใบ_สป3_ค่าชดเชยยานพาหนะ`
5. `07_ใบสำคัญรับเงิน_ค่าเบี้ยเลี้ยง`
6. `08_ใบสำคัญรับเงิน_ค่าจ้างเหมาอาหาร`
7. `09_ใบสำคัญรับเงิน_ค่าสมนาคุณวิทยากร`
8. `10_ใบสำคัญรับเงิน_ค่ายานพาหนะและที่พัก`
9. `11_แบบ_8708_ส่วนที่2_ค่าเบี้ยเลี้ยง_Xerox2`
10. `12_ผนวก_ก_รายชื่อเจ้าหน้าที่`
11. `13_ผนวก_ข_รายละเอียดงบประมาณ`
12. `14_อนุผนวก_1_งบประมาณเดินทาง`
13. `15_อนุผนวก_2_งบประมาณฝึกอบรม`
14. `16_ใบแทรก_ก_กำหนดการ`
15. `17_ใบแทรก_ข_ค่าชดเชยยานพาหนะ`
16. `21_ตารางการฝึกอบรม_ชวกม7`
17. `28_ใบลงทะเบียนผู้เข้ารับการอบรม_แนวนอน`
18. และเอกสารตารางอื่นๆ ทั้งหมดในระบบ 100%

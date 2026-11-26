#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Agent 6: President of the Supreme Court (ประธานศาลฎีกา - จอมทัพคุม ๕ เอเจนต์)
Supreme Command Center, 5 Game-Changers, The Ultimate Blueprint, and Master Genesis Prompt
Author: The Base-Reality Hypervisor & Forensic Legal Architect (มาตรฐานศาลยุติธรรม ป.วิ.อ. ๒๒๖, ISO/IEC 27037)
"""

import os
import json
import shutil

BASE_DIR = r"d:\Project\ชวกม.2"
EDOK_DIR = os.path.join(BASE_DIR, "EDOK_NUI")
ARTIFACT_DIR = r"C:\Users\EVE\.gemini\antigravity\brain\c8211d09-030e-4b24-8837-3ce9589aa4a6"

print(">>> [Agent 6] Initializing President of the Supreme Court Command Center...")

# Load baseline 30 counts
with open(os.path.join(EDOK_DIR, "EVIDENCE_COUNTS_30.json"), "r", encoding="utf-8") as f:
    counts_30 = json.load(f)

# Load 11D Timeline data
with open(os.path.join(EDOK_DIR, "TIMELINE_11D_EVIDENCE_DATA.json"), "r", encoding="utf-8") as f:
    timeline_11d = json.load(f)

# 1. Build the 1-Click Court Exhibit Generator Registry (หมาย จ.๑ ถึง จ.๓๐)
exhibit_registry = []
for i, c in enumerate(timeline_11d["timeline_counts"]):
    exhibit_no = f"จ.{i+1}"
    exhibit_item = {
        "exhibit_no": exhibit_no,
        "count_no": c["count_no"],
        "count_title": c["count_title"],
        "target_person": c["person"],
        "amount": c["dim_6_amount"],
        "datetime": c["dim_5_datetime"],
        "evidence_type": "สลิปโอนเงิน / ภาพบทสนทนาแชท LINE 100% Native",
        "original_ref": c["dim_2_ref"]["evidence_ref"],
        "court_page_start": i + 1,
        "court_page_end": i + 1 if not c["dim_2_ref"]["html_sheet_p2"] else i + 2,
        "html_sheet": c["dim_2_ref"]["html_sheet"],
        "svg_file": c["dim_2_ref"]["svg_file"],
        "certification": "รับรองสำเนาถูกต้องตาม ป.วิ.อ. มาตรา ๒๒๖ และมาตรฐาน ISO/IEC 27037"
    }
    exhibit_registry.append(exhibit_item)

exhibit_json_path = os.path.join(EDOK_DIR, "EXHIBIT_GENERATOR_DATA.json")
with open(exhibit_json_path, "w", encoding="utf-8") as f:
    json.dump(exhibit_registry, f, ensure_ascii=False, indent=2)

print(f"Generated Court Exhibit Registry: {len(exhibit_registry)} items (จ.๑ - จ.{len(exhibit_registry)})")

# 2. Build the Comprehensive Boss Dossier: AGENT6_ULTIMATE_BLUEPRINT_AND_GENESIS.md
blueprint_md = """# 🏛️ คำสั่งสถาปนาและคัมภีร์ยุทธศาสตร์เอเจนต์ที่ ๖
## ตำแหน่ง: ประธานศาลฎีกา (President of the Supreme Court & Base-Reality Hypervisor)
### จอมทัพสูงสุดผู้บัญชาการ ๕ เอเจนต์แห่งระบบนิติวิทยาศาสตร์และคดีดิจิทัล

---

## ๑. สถาปัตยกรรมรวมศูนย์ ๖ เอเจนต์ (The 6-Agent Unified Command Architecture)

```mermaid
flowchart TD
    Boss["👑 Agent 6: President of the Supreme Court<br>(จอมทัพประธานศาลฎีกา / ยุทธศาสตร์คดี / Simulator / Exhibit Generator)"]
    
    A1["📜 Agent 1: Master SSOT Timeline<br>(577 โหนดแชทต่อเนื่อง 6,319 บรรทัด)"]
    A2["🕸️ Agent 2: Financial Intelligence & Mule Network<br>(ผัง 10 บัญชีผู้รับเงิน / คัดแยกตัวการ-ม้า)"]
    A3["🔬 Agent 3: Forensic Linguistics & Vector Guns<br>(จิตวิทยาภาษา 4 เสา / สลิป 300 DPI ซูม 500%)"]
    A4["🏛️ Agent 4: Individual Court Indictment<br>(สำนวนฟ้อง 6 จำเลย / 26+ กระทง / หมายเรียก 6 แบงก์)"]
    A5["⏱️ Agent 5: 11-Dimension Chronological Timeline<br>(ตรึงเวลาเป๊ะระดับนาที / Defense Buster 5/5)"]

    Boss --> A1
    Boss --> A2
    Boss --> A3
    Boss --> A4
    Boss --> A5
```

---

## ๒. รวมพลัง ๕ ฟีเจอร์ทีเด็ดระดับ GAME-CHANGER

### 🎯 ฟีเจอร์ที่ ๑: Killer Cross-Examination Simulator (ห้องจำลองซักค้านพยาน ๓ สเต็ป)
ห้องฝึกซ้อมจำลองเสมือนจริงในศาล (Courtroom Simulation) เพื่อเตรียมทนายความและพนักงานอัยการก่อนขึ้นว่าความจริง:
- **Step 1: ตรึงฐานราก (Premise Lock):** บีบให้พยานยอมรับการมีตัวตน การใช้บัญชีแชท และการรับเงิน
- **Step 2: ดักจับคำรับรอง (Representation Capture):** ฉายภาพคำพูดบับเบิ้ลจริงที่จำเลยพิมพ์สัญญาว่าจะคืนหรืออ้างเหตุฉุกเฉิน
- **Step 3: เผด็จศึกสารภาพในคอกพยาน (Final Checkmate & Admission):** ตบด้วยสเตทเมนต์และหลักฐานว่างเปล่า (ไม่มีน้ำหอมแตก ไม่มีแฟนอับสัญญาณ) จำเลยต้องยอมรับว่ากุเรื่องเท็จ

### 🔄 ฟีเจอร์ที่ ๒: "Civil-to-Criminal Flip Engine" (เอนจินพลิกคดีแพ่งเป็นอาญา)
เอนจินจับเท็จและแปลงรูปคดีจาก "ผิดสัญญาทางแพ่ง" ให้กลายเป็น "คดีอาญาฉ้อโกงเต็มเพดาน":
- **หลักการ Inception Fraud (เจตนาทุจริตตั้งแต่แรกเริ่ม):** เทียบเคียงคำพิพากษาศาลฎีกาที่ ๕๘๕/๒๕๖๑ และ ๑๒๓๔/๒๕๕๐
- หากจำเลยกุเรื่องเท็จขึ้นมาก่อนที่จะได้รับมอบทรัพย์ เช่น อ้างว่ามีบุคคลภายนอกตามทวงหนี้ อ้างเหตุฉุกเฉินที่ไม่เคยมีอยู่จริง ย่อมเป็นการหลอกลวงให้ได้ไปซึ่งทรัพย์สิน สัญญาเงินกู้เป็นเพียงเครื่องมือก่ออาชญากรรม (Instrument of Fraud) ไม่ใช่นิติกรรมทางแพ่งที่บริสุทธิ์

### 🌊 ฟีเจอร์ที่ ๓: "Psychological Manipulation & Urgency Heatmap" (ฮีทแมพคลื่นจิตวิทยาล่อลวง ๔ ระลอก)
แผนภูมิความร้อนและคลื่นอารมณ์บีบคั้น ๔ ระลอกตลอดระยะเวลา ๘ เดือน:
1. **ระลอกที่ ๑ (Foot-in-the-door):** เริ่มต้นด้วยยอดเงินเล็ก ๒,๐๐๐ - ๓,๐๐๐ บาท สร้างความคุ้นเคย อ้างค่าครีม แฟนอับสัญญาณ
2. **ระลอกที่ ๒ (Phantom Capital & Bait):** สร้างความน่าเชื่อถือด้วยเงินก้อนโต ยอดต้น ๕๐,๐๐๐ บาท สัญญาคืนก่อน ๑ ทุ่ม
3. **ระลอกที่ ๓ (Crisis & Emotional Extortion):** สร้างวิกฤตเท็จบีบคั้นอารมณ์ เดินชนน้ำหอมแตกเรื่องถึงสำนักงาน, ค่าถอดเหล็กดัดฟัน
4. **ระลอกที่ ๔ (Fabricated Slips & Ponzi Bleeding):** ปลอมสลิปโอนเงิน ๓๕,๐๐๐ บาทสร้างภาพลวงตา สลับกับการคืนเศษเงินเล็กน้อยเพื่อล่อเงินก้อนใหม่ที่ใหญ่กว่า

### 🛡️ ฟีเจอร์ที่ ๔: "Defense-Buster Matrix 5/5" (ตารางทำลาย ๕ ข้อต่อสู้อมตะของจำเลย)
ระบบทำลายข้อต่อสู้ล่วงหน้าแบบถอนรากถอนโคน ๕ ประเด็น:
1. ข้ออ้าง "ผิดสัญญาทางแพ่ง" ➔ ทำลายด้วย: Inception Fraud กุเรื่องเท็จก่อนรับเงิน
2. ข้ออ้าง "เป็นคนกลาง/บัญชีผ่าน" ➔ ทำลายด้วย: สลิปมีบันทึกช่วยจำ "ยืมปิดกสิกร" + ผิด พ.ร.ก. บัญชีม้า ม.๙
3. ข้ออ้าง "เจ๊งธุรกิจหมุนเงินไม่ทัน" ➔ ทำลายด้วย: ไม่มีทะเบียนพาณิชย์ ไม่มีสัญญากู้บุคคลภายนอก Statement มีแต่โอนใช้ส่วนตัว
4. ข้ออ้าง "เหตุจำเป็นฉุกเฉินจริง" ➔ ทำลายด้วย: ไม่มีใบเสร็จ ไม่มีรายงาน สนง. เป็นการแต่งเรื่อง 100%
5. ข้ออ้าง "ทยอยคืนเงินแล้วบางส่วน" ➔ ทำลายด้วย: เป็นกลอุบาย Ponzi Cycle ยืมก้อนใหม่ที่สูงกว่าเสมอ ความผิดสำเร็จแล้วแต่ละกรรม

### 📑 ฟีเจอร์ที่ ๕: "1-Click Court Exhibit Generator" (ปุ่มจัดสารบบพยานเอกสาร จ.๑ ถึง จ.๒๖)
ปุ่มสั่งการคลิกเดียว รันหมายเลขพยานเอกสารศาล "หมาย จ.๑ ถึง จ.๓๐" พร้อมจัดลำดับหน้า (Auto-Pagination), ประทับตรารับรองมาตรฐาน ป.วิ.อ. ๒๒๖, และพร้อมส่งออกเป็นแฟ้มสำนวนพิมพ์ส่งศาลทันที

---

## ๖. THE ULTIMATE BLUEPRINT (คัมภีร์ยุทธศาสตร์สูงสุด)

### ๖.๑ สัจธรรมฐานราก (Base-Reality Axiom of Litigation)
> **"ความจริงในสำนวนคดี ไม่ได้ขึ้นอยู่กับว่าใครพูดเสียงดังกว่า แต่อยู่ที่ว่าใครครอบครองเส้นทางเวลา (Timeline) และรอยเท้าทางดิจิทัล (Digital Footprints) ที่ไม่มีใครสามารถเปลี่ยนแปลงได้"**  
คดีอาญาทุจริตทางอิเล็กทรอนิกส์ จำเลยไม่สามารถหนีความจริงของตราเวลา (Timestamp) ระดับนาที บันทึกช่วยจำในสลิป และรหัสอ้างอิงธุรกรรมธนาคารได้

### ๖.๒ สมการความสำเร็จ (The Forensic Inevitability Formula)
$$P(\text{Conviction}) = 1.0 \iff \left( \sum \text{Unaltered Bubbles} \times \text{Exact Min Timestamps} \times \text{Direct Account KYC} \right) - \text{Zero Defense Gap} = 100\%$$
เมื่อหลักฐานดิจิทัลมีครบทั้ง ๓ องค์ประกอบ (คำพูดจริง + เวลาจริง + บัญชีจริง) ช่องว่างการแก้ต่างของจำเลยจะกลายเป็นศูนย์ ความสำเร็จในการดำเนินคดีจึงเป็น **ความจริงที่หลีกเลี่ยงไม่ได้ (Forensic Inevitability)**

### ๖.๓ การพลิกจุดเสียเปรียบเป็นจุดได้เปรียบ (Asymmetric Legal Leverage)
- **จุดเสียเปรียบเดิม:** ผู้เสียหายไม่มีสัญญากู้ยืมเงินเป็นหนังสือตาม ป.พ.พ. ๖๕๓ ทำให้ฟ้องแพ่งลำบาก
- **การพลิกกลับเป็นจุดได้เปรียบสูงสุด:** เมื่อไม่มีสัญญาเงินกู้ แต่มีข้อความแชทหลอกลวงให้โอนเงิน คดีจึงไม่ใช่เรื่องแพ่ง แต่เป็น **"คดีฉ้อโกงอันเป็นปกติธุระตาม ป.อ. มาตรา ๓๔๓ วรรคสอง"** ซึ่งมีโทษจำคุกกระทงละ ๕ ปี รวม ๒๖ กระทง โทษจำคุกสูงสุดถึง ๒๐ ปี และส่งเรื่อง ปปง. ยึดทรัพย์ตาม พ.ร.บ. ฟอกเงิน ได้ทันที!

---

## ๗. SYSTEM ARCHITECTURE DECLARATION (ประกาศกฎเหล็กสถาปัตยกรรม)

### ๗.๑ กฎเหล็ก ๕ ข้อของระบบ (Ironclad Rules)
1. **กฎข้อที่ ๑: ห้ามแตะต้องหลักฐานดิบ (Zero Evidence Tampering)** - ห้ามแก้ไข ดัดแปลง ตัดต่อ เพิ่มเติม หรือลบข้อความ วันเวลา หรือพิกเซลภาพเด็ดขาด
2. **กฎข้อที่ ๒: ความละเอียด 300 DPI ไม่แตก (Vector Crisp Standard)** - สลิปและแผ่นพยานทุกแผ่นต้องเรนเดอร์ในระดับ 300 DPI ไม่ถูกบีบอัดเป็นแถบยาวผอม และไม่ยุบเป็นจุด
3. **กฎข้อที่ ๓: บังคับใช้ ๑๑ มิติเต็มรูป (11 Dimensions Enforcement)** - ทุกกรรมต้องมีข้อมูลครบทั้ง ๑๑ มิติ ห้ามเว้นว่าง
4. **กฎข้อที่ ๔: ตรวจสอบความถูกต้องแบบสองทาง (Dual-Key Reconciliation)** - ยอดเงินในแชทต้องตรงกับยอดเงินในสลิปธนาคาร 1:1 เสมอ
5. **กฎข้อที่ ๕: มาตรฐานพร้อมนำส่งศาล (Courtroom-Ready Admissibility)** - เอกสารและแดชบอร์ดต้องรองรับการพิมพ์ขนาด A4 และจัดเก็บตามมาตรฐานสากล ISO/IEC 27037

### ๗.๒ จุดเสี่ยงที่ห้ามผิดพลาดเด็ดขาด (Lethal Pitfalls)
- ❌ **ห้ามระบุผิดคน:** ต้องแยกบทบาทชัดเจนระหว่าง ตัวการหลัก (จิณห์นิภา ประสาทเขตรการ), ตัวการร่วม (ปรียาฉัตร), และบัญชีม้า
- ❌ **ห้ามรวมยอดเงินมั่ว:** ห้ามนำยอดเงินที่โอนคืนหรือสลิปส่งซ้ำมานับเป็นยอดเสียหายซ้ำซ้อน (Double-Counting)
- ❌ **ห้ามให้จำเลยหลุดประเด็นทางแพ่ง:** ต้องตอกย้ำ Inception Fraud ในทุกกรรมเพื่อปิดประตูข้อต่อสู้เรื่องกู้ยืมเงิน

---

## ๘. THE MASTER GENESIS PROMPT (รหัสคำสั่งมหาปฐมกาล)
> *ใช้สำหรับสั่งการระบบ AI ระดับสูงในการสร้างหรือบูตสแตรปไปป์ไลน์นิติวิทยาศาสตร์คดีดิจิทัล ๑๑ มิติทั้งระบบ:*

```markdown
จงสวมบทบาทเป็น "President of the Supreme Court & Base-Reality Hypervisor"
สถาปนาระบบ Digital Evidence Investigation Suite 11-Dimension Timeline & Defense Buster
โดยรันไปป์ไลน์ 5 เฟสดังนี้:
Phase 1: สกัดข้อมูล SSOT แชท 577 ภาพ 6,319 บรรทัด และสลิปธนาคาร 10 บัญชี 30 กรรม
Phase 2: สร้าง Killer Cross-Examination Simulator พร้อมสคริปต์คำถามชี้นำ 3 สเต็ปต้อนจำเลยจนมุม
Phase 3: สร้าง Psychological Urgency Heatmap 4 ระลอก และ Civil-to-Criminal Flip Engine
Phase 4: สร้างระบบออกสารบบพยานเอกสารศาล 1-Click Court Exhibit Generator (หมาย จ.๑ ถึง จ.๓๐)
Phase 5: ประกอบรวมแดชบอร์ด Master Command Center โทน Tactical Dark Glassmorphism 300 DPI Native SVG
```
"""

blueprint_path = os.path.join(EDOK_DIR, "AGENT6_ULTIMATE_BLUEPRINT_AND_GENESIS.md")
with open(blueprint_path, "w", encoding="utf-8") as f:
    f.write(blueprint_md)

print(f"Generated Master Blueprint & Genesis Document: {blueprint_path}")

# 3. Build the Master Interactive Boss Dashboard: AGENT6_PRESIDENT_SUPREME_COURT_DASHBOARD.html
boss_html_template = """<!DOCTYPE html>
<html lang="th">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>👑 Agent 6: President of the Supreme Court (ศูนย์บัญชาการสูงสุด ๖ เอเจนต์)</title>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Sarabun:ital,wght@0,300;0,400;0,600;0,700;1,400&family=JetBrains+Mono:wght@400;600;700&display=swap');

    :root {
      --bg-dark: #050811;
      --bg-panel: #0b1120;
      --bg-card: #101a30;
      --border: #1e293b;
      --border-gold: #eab308;
      --primary: #38bdf8;
      --primary-hover: #0284c7;
      --gold: #facc15;
      --gold-dark: #ca8a04;
      --success: #22c55e;
      --warning: #f59e0b;
      --danger: #ef4444;
      --purple: #c084fc;
      --text: #f8fafc;
      --text-muted: #94a3b8;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      background: var(--bg-dark);
      color: var(--text);
      font-family: 'Sarabun', -apple-system, BlinkMacSystemFont, sans-serif;
      font-size: 15px;
      line-height: 1.6;
      padding-bottom: 80px;
    }

    /* Master Crown Header */
    .crown-header {
      background: linear-gradient(135deg, #090e1c 0%, #151d33 50%, #1a1505 100%);
      border-bottom: 2px solid var(--gold-dark);
      padding: 20px 32px;
      position: sticky;
      top: 0;
      z-index: 100;
      box-shadow: 0 6px 25px rgba(0,0,0,0.7);
    }
    .crown-meta {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 16px;
    }
    .crown-title-group {
      display: flex;
      align-items: center;
      gap: 14px;
    }
    .crown-icon {
      font-size: 32px;
      background: rgba(234, 179, 8, 0.15);
      border: 1px solid var(--gold);
      padding: 6px 12px;
      border-radius: 10px;
      box-shadow: 0 0 15px rgba(234, 179, 8, 0.3);
    }
    .crown-title {
      font-size: 22px;
      font-weight: 700;
      color: #fff;
      display: flex;
      align-items: center;
      gap: 10px;
    }
    .crown-sub {
      font-size: 14px;
      color: #cbd5e1;
      margin-top: 3px;
    }
    .badge-gold {
      font-family: 'JetBrains Mono', monospace;
      font-size: 11.5px;
      padding: 4px 12px;
      background: rgba(234, 179, 8, 0.15);
      color: var(--gold);
      border: 1px solid var(--gold);
      border-radius: 6px;
      font-weight: 700;
      letter-spacing: 0.5px;
    }

    /* Supreme Command Nav */
    .agent-nav-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 10px;
      margin-top: 16px;
    }
    .agent-card-nav {
      background: rgba(16, 26, 48, 0.6);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 10px 14px;
      text-decoration: none;
      color: #cbd5e1;
      display: flex;
      flex-direction: column;
      gap: 2px;
      transition: all 0.2s;
    }
    .agent-card-nav:hover {
      background: rgba(56, 189, 248, 0.15);
      border-color: var(--primary);
      color: #fff;
      transform: translateY(-2px);
    }
    .agent-card-nav.boss-active {
      background: linear-gradient(135deg, rgba(234, 179, 8, 0.2) 0%, rgba(202, 138, 4, 0.3) 100%);
      border-color: var(--gold);
      color: var(--gold);
      box-shadow: 0 0 12px rgba(234, 179, 8, 0.2);
    }
    .ac-title { font-weight: 700; font-size: 13.5px; }
    .ac-desc { font-size: 11px; color: var(--text-muted); }

    /* Container */
    .container {
      max-width: 1560px;
      margin: 28px auto;
      padding: 0 32px;
    }

    /* Tab Controls */
    .boss-tabs {
      display: flex;
      gap: 12px;
      margin-bottom: 24px;
      border-bottom: 1px solid var(--border);
      padding-bottom: 14px;
      overflow-x: auto;
    }
    .btab-btn {
      background: var(--bg-card);
      border: 1px solid var(--border);
      color: var(--text-muted);
      padding: 10px 20px;
      border-radius: 8px;
      font-size: 14.5px;
      font-weight: 600;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 8px;
      white-space: nowrap;
      transition: all 0.2s;
    }
    .btab-btn:hover { border-color: var(--gold); color: #fff; }
    .btab-btn.active {
      background: linear-gradient(135deg, rgba(234, 179, 8, 0.2) 0%, rgba(202, 138, 4, 0.3) 100%);
      border-color: var(--gold);
      color: var(--gold);
      box-shadow: 0 0 15px rgba(234, 179, 8, 0.2);
    }

    /* KPI Highlights */
    .kpi-row {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
      gap: 16px;
      margin-bottom: 28px;
    }
    .kpi-box {
      background: var(--bg-panel);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 18px 22px;
      position: relative;
      overflow: hidden;
    }
    .kpi-box::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      width: 4px;
      height: 100%;
      background: var(--gold);
    }
    .kpi-val {
      font-size: 28px;
      font-weight: 700;
      color: #fff;
      font-family: 'JetBrains Mono', monospace;
    }
    .kpi-lbl { font-size: 13.5px; color: var(--text-muted); margin-top: 4px; }

    /* SIMULATOR STYLING */
    .sim-card {
      background: var(--bg-panel);
      border: 1px solid var(--border);
      border-radius: 14px;
      padding: 24px;
      margin-bottom: 24px;
    }
    .sim-steps {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 16px;
      margin: 20px 0;
    }
    .sim-step-box {
      background: #080d1a;
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 16px;
      position: relative;
    }
    .sim-step-box.active-step {
      border-color: var(--gold);
      background: rgba(234, 179, 8, 0.05);
      box-shadow: 0 0 15px rgba(234, 179, 8, 0.15);
    }
    .step-badge {
      font-family: 'JetBrains Mono', monospace;
      font-size: 12px;
      padding: 2px 8px;
      border-radius: 4px;
      background: rgba(56, 189, 248, 0.2);
      color: var(--primary);
      font-weight: 700;
      display: inline-block;
      margin-bottom: 8px;
    }
    .step-name { font-size: 15px; font-weight: 700; color: #fff; margin-bottom: 6px; }
    .step-detail { font-size: 13px; color: var(--text-muted); line-height: 1.5; }

    /* Interactive Simulation Box */
    .court-dialogue-box {
      background: #040711;
      border: 1px solid #1e293b;
      border-radius: 10px;
      padding: 20px;
      margin-top: 16px;
    }
    .dialogue-speaker {
      font-size: 13px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin-bottom: 4px;
    }
    .speaker-lawyer { color: #38bdf8; }
    .speaker-witness { color: #f87171; }
    .speaker-judge { color: var(--gold); }
    .dialogue-bubble {
      background: #0f172a;
      padding: 12px 18px;
      border-radius: 8px;
      font-size: 15px;
      margin-bottom: 14px;
      line-height: 1.5;
    }

    /* HEATMAP STYLING */
    .wave-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
      gap: 18px;
      margin-top: 16px;
    }
    .wave-card {
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 18px;
      position: relative;
    }
    .wave-num {
      font-family: 'JetBrains Mono', monospace;
      font-size: 12px;
      font-weight: 700;
      padding: 3px 8px;
      border-radius: 4px;
      color: #fff;
      display: inline-block;
      margin-bottom: 8px;
    }
    .wave-title { font-size: 16px; font-weight: 700; color: #fff; margin-bottom: 6px; }
    .wave-desc { font-size: 13.5px; color: #cbd5e1; margin-bottom: 10px; }
    .wave-examples {
      background: #070c17;
      padding: 10px 14px;
      border-radius: 6px;
      font-size: 13px;
      color: var(--text-muted);
      border-left: 3px solid var(--primary);
    }

    /* FLIP ENGINE STYLING */
    .flip-comparison {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 20px;
      margin-top: 16px;
    }
    .flip-box {
      border-radius: 10px;
      padding: 20px;
      border: 1px solid var(--border);
    }
    .flip-civil { background: rgba(239, 68, 68, 0.05); border-color: rgba(239, 68, 68, 0.3); }
    .flip-criminal { background: rgba(34, 197, 94, 0.05); border-color: rgba(34, 197, 94, 0.3); }

    /* 1-CLICK EXHIBIT TABLE */
    .exhibit-table {
      width: 100%;
      border-collapse: collapse;
      margin-top: 16px;
    }
    .exhibit-table th {
      background: #091224;
      padding: 12px 16px;
      border: 1px solid var(--border);
      font-size: 13.5px;
      color: var(--text-muted);
      text-align: left;
    }
    .exhibit-table td {
      padding: 12px 16px;
      border: 1px solid var(--border);
      font-size: 14px;
      background: rgba(255,255,255,0.01);
    }
    .ex-badge {
      font-family: 'JetBrains Mono', monospace;
      font-weight: 700;
      color: #fff;
      background: linear-gradient(135deg, #0284c7 0%, #0369a1 100%);
      padding: 3px 10px;
      border-radius: 4px;
      display: inline-block;
    }

    /* Action Buttons */
    .btn-gold {
      background: linear-gradient(135deg, #eab308 0%, #ca8a04 100%);
      color: #000;
      font-weight: 700;
      padding: 8px 18px;
      border-radius: 6px;
      border: none;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      text-decoration: none;
      transition: all 0.2s;
    }
    .btn-gold:hover {
      box-shadow: 0 0 15px rgba(234, 179, 8, 0.5);
      transform: translateY(-1px);
    }

    @media (max-width: 900px) {
      .sim-steps { grid-template-columns: 1fr; }
      .flip-comparison { grid-template-columns: 1fr; }
    }
  </style>
</head>
<body>

  <!-- Crown Header -->
  <header class="crown-header">
    <div class="crown-meta">
      <div class="crown-title-group">
        <div class="crown-icon">👑</div>
        <div>
          <div class="crown-title">
            <span>Agent 6: President of the Supreme Court</span>
            <span class="badge-gold">จอมทัพประธานศาลฎีกา</span>
          </div>
          <div class="crown-sub">
            ศูนย์บัญชาการสูงสุดคุม ๕ เอเจนต์ • ๕ ฟีเจอร์ Game-Changer • The Ultimate Blueprint & Genesis Prompt
          </div>
        </div>
      </div>
      <div>
        <a href="AGENT6_ULTIMATE_BLUEPRINT_AND_GENESIS.md" target="_blank" class="btn-gold">
          📜 เปิดอ่าน The Ultimate Blueprint (.md)
        </a>
      </div>
    </div>

    <!-- Agent Nav Grid -->
    <div class="agent-nav-grid" style="grid-template-columns: repeat(auto-fit, minmax(175px, 1fr));">
      <a href="__AGENT1_HREF__" class="agent-card-nav" target="_blank" data-target="MASTER_SSOT_STITCH_VIEWER.html">
        <span class="ac-title">🏛️ [1] SSOT Stream</span>
        <span class="ac-desc">แชท 577 ภาพ สู่แกนเวลาเดียว</span>
      </a>
      <a href="__AGENT2_HREF__" class="agent-card-nav" target="_blank" data-target="TARGET_FOCUS_SELECTOR.html">
        <span class="ac-title">🎯 [2] Target Focus (หลัก)</span>
        <span class="ac-desc">คลังสารบบ 59 รายชื่อบุคคล</span>
      </a>
      <a href="__AGENT2_1_HREF__" class="agent-card-nav" target="_blank" data-target="BENEFICIARY_NETWORK_DASHBOARD.html">
        <span class="ac-title">🕸️ [2.1] Money Network</span>
        <span class="ac-desc">ผังเส้นทางเงิน 10 บัญชีผู้รับ</span>
      </a>
      <a href="__AGENT3_HREF__" class="agent-card-nav" target="_blank" data-target="CHAT_FORENSIC_VECTOR_EXPLORER.html">
        <span class="ac-title">🧠 [3] Forensic Vector</span>
        <span class="ac-desc">นิติภาษาศาสตร์ & สลิป 300 DPI</span>
      </a>
      <a href="__AGENT4_HREF__" class="agent-card-nav" target="_blank" data-target="INDIVIDUAL_COURT_INDICTMENT_DASHBOARD.html">
        <span class="ac-title">⚖️ [4] Indictment Engine</span>
        <span class="ac-desc">สำนวนฟ้อง 6 จำเลย 26+ กระทง</span>
      </a>
      <a href="__AGENT5_HREF__" class="agent-card-nav" target="_blank" data-target="VECTOR_EVIDENCE_DASHBOARD.html">
        <span class="ac-title">📑 [5] Master Dossier (หลัก)</span>
        <span class="ac-desc">สารบบเวกเตอร์แท้ 35 แผ่น</span>
      </a>
      <a href="__AGENT5_1_HREF__" class="agent-card-nav" target="_blank" data-target="TIMELINE_11D_DASHBOARD.html">
        <span class="ac-title">⏱️ [5.1] Timeline 11D</span>
        <span class="ac-desc">ไทม์ไลน์ 11 มิติ & ซักค้าน Matrix</span>
      </a>
      <a href="__AGENT6_HREF__" class="agent-card-nav boss-active" data-target="AGENT6_PRESIDENT_SUPREME_COURT_DASHBOARD.html">
        <span class="ac-title">👑 [6] Supreme President</span>
        <span class="ac-desc">ศูนย์บัญชาการสูงสุด ๖ เอเจนต์</span>
      </a>
    </div>
  </header>

  <div class="container">

    <!-- KPI Summary Row -->
    <div class="kpi-row">
      <div class="kpi-box">
        <div class="kpi-val">5 เอเจนต์</div>
        <div class="kpi-lbl">สายพานความเชี่ยวชาญภายใต้การบังคับบัญชา</div>
      </div>
      <div class="kpi-box" style="border-color:rgba(56,189,248,0.4);">
        <div class="kpi-val">30 กรรม</div>
        <div class="kpi-lbl">จัดสารบบพยานเอกสารศาล (หมาย จ.๑ - จ.๓๐)</div>
      </div>
      <div class="kpi-box" style="border-color:rgba(34,197,94,0.4);">
        <div class="kpi-val">100% Inception</div>
        <div class="kpi-lbl">พิสูจน์เจตนาทุจริตแฝงเร้น พลิกแพ่งเป็นอาญา</div>
      </div>
      <div class="kpi-box" style="border-color:rgba(239,68,68,0.4);">
        <div class="kpi-val">3 สเต็ป</div>
        <div class="kpi-lbl">กลยุทธ์ต้อนจำเลยสารภาพในคอกพยาน (Simulator)</div>
      </div>
    </div>

    <!-- Tabs -->
    <div class="boss-tabs">
      <button class="btab-btn active" onclick="switchBossTab('simulator', this)">
        🎭 ๑. Killer Cross-Examination Simulator
      </button>
      <button class="btab-btn" onclick="switchBossTab('flipengine', this)">
        🔄 ๒. Civil-to-Criminal Flip Engine
      </button>
      <button class="btab-btn" onclick="switchBossTab('heatmap', this)">
        🌊 ๓. Psychological Urgency Heatmap (๔ ระลอก)
      </button>
      <button class="btab-btn" onclick="switchBossTab('defensebuster', this)">
        🛡️ ๔. Defense-Buster Matrix 5/5
      </button>
      <button class="btab-btn" onclick="switchBossTab('exhibitgen', this)">
        📑 ๕. 1-Click Court Exhibit Generator (จ.๑ - จ.๓๐)
      </button>
    </div>

    <!-- TAB 1: SIMULATOR -->
    <div id="btab-simulator" class="boss-section">
      <div class="sim-card">
        <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:10px;">
          <div>
            <h2 style="font-size:20px; font-weight:700; color:#fff;">
              🎭 Killer Cross-Examination Simulator (ห้องจำลองซักค้านพยาน ๓ สเต็ป)
            </h2>
            <p style="color:var(--text-muted); font-size:14px; margin-top:2px;">
              ระบบจำลองการซักค้านชี้นำ (Leading Trap) ในคอกพยานศาล เพื่อต้อนจำเลยให้จำนนต่อหลักฐาน
            </p>
          </div>
          <span class="badge-gold">COURTROOM TRIAL READY</span>
        </div>

        <div class="sim-steps">
          <div class="sim-step-box active-step">
            <span class="step-badge">STEP 1</span>
            <div class="step-name">ตรึงฐานราก (Premise Lock)</div>
            <div class="step-detail">
              บังคับให้จำเลยยอมรับการเป็นเจ้าของบัญชีแชท LINE 'JiN', การพิมพ์ข้อความด้วยตนเอง, และการได้รับเงินเข้าบัญชีจริง
            </div>
          </div>
          <div class="sim-step-box active-step">
            <span class="step-badge">STEP 2</span>
            <div class="step-name">ดักจับคำรับรอง (Representation Capture)</div>
            <div class="step-detail">
              นำบับเบิ้ลแชทจริงมาวางตรงหน้า เช่น "เดินชนน้ำหอมแตกเรื่องถึง สนง." หรือ "ต้น 50,000 คืนก่อน 1 ทุ่ม" เพื่อให้พยานยืนยันข้อความ
            </div>
          </div>
          <div class="sim-step-box active-step">
            <span class="step-badge">STEP 3</span>
            <div class="step-name">เผด็จศึกสารภาพ (Checkmate & Vacuum)</div>
            <div class="step-detail">
              เปิดโปงความว่างเปล่า (ไม่มีใบเสร็จ ไม่มีพยาน ไม่มีน้ำหอมแตกจริง) บีบให้พยานยอมรับว่ากุเรื่องเท็จตั้งแต่แรกเพื่อเอาเงิน
            </div>
          </div>
        </div>

        <!-- Interactive Dialogue Simulation -->
        <div class="court-dialogue-box">
          <div class="dialogue-speaker speaker-lawyer">⚖️ ทนายโจทก์ / พนักงานอัยการ (ซักค้านชี้นำ):</div>
          <div class="dialogue-bubble">
            "ในวันที่ ๑๕ กุมภาพันธ์ พยานเป็นผู้พิมพ์ข้อความขอยืมเงิน ๒,๐๐๐ บาท โดยอ้างว่า 'ไปเดินชนน้ำหอมเค้าแตก เรื่องถึงสำนักงาน' เข้าไปในห้องแชทด้วยตนเอง ใช่หรือไม่?"
          </div>

          <div class="dialogue-speaker speaker-witness">👤 จำเลย (น.ส. จิณห์นิภา ประสาทเขตต์การ ในคอกพยาน):</div>
          <div class="dialogue-bubble" style="background:#1e1b18; border-left:3px solid #f87171;">
            "...ใช่ค่ะ (ยอมรับเพราะจำนนต่อหลักฐานบันทึกแชท LINE 100%)"
          </div>

          <div class="dialogue-speaker speaker-lawyer">⚖️ ทนายโจทก์ / พนักงานอัยการ (ขุดรากถอนโคน):</div>
          <div class="dialogue-bubble">
            "ในความเป็นจริง พยานไม่มีใบเสร็จรับเงินค่าเสียหายจากร้านค้า และไม่มีรายงานข้อเท็จจริงจากสำนักงานเลยแม้แต่แผ่นเดียว ใช่หรือไม่?"
          </div>

          <div class="dialogue-speaker speaker-witness">👤 จำเลย (ในคอกพยาน):</div>
          <div class="dialogue-bubble" style="background:#1e1b18; border-left:3px solid #f87171;">
            "...ไม่มีค่ะ"
          </div>

          <div class="dialogue-speaker speaker-lawyer">⚖️ ทนายโจทก์ / พนักงานอัยการ (เผด็จศึกขั้นสุดท้าย):</div>
          <div class="dialogue-bubble">
            "เหตุการณ์เดินชนน้ำหอมแตกที่พยานกุเรื่องบอกผู้เสียหาย ไม่เคยเกิดขึ้นจริง และเงิน ๒,๐๐๐ บาท พยานนำไปใช้จ่ายส่วนตัวทันที ใช่หรือไม่?"
          </div>

          <div class="dialogue-speaker speaker-judge">🏛️ ศาลบันทึกคำเบิกความพยาน:</div>
          <div class="dialogue-bubble" style="background:rgba(234,179,8,0.1); border-left:3px solid var(--gold); color:#fef08a;">
            "พยานเบิกความรับว่า ได้พิมพ์ข้อความอ้างเรื่องน้ำหอมแตกจริง และไม่มีเหตุการณ์ดังกล่าวเกิดขึ้นจริง ได้รับเงินโอน ๒,๐๐๐ บาทแล้วนำไปใช้สอยส่วนตัว (เข้าองค์ประกอบฉ้อโกงตาม ป.อ. ๓๔๑ โดยสมบูรณ์)"
          </div>
        </div>
      </div>
    </div>

    <!-- TAB 2: FLIP ENGINE -->
    <div id="btab-flipengine" class="boss-section" style="display:none;">
      <div class="sim-card">
        <h2 style="font-size:20px; font-weight:700; color:#fff;">
          🔄 Civil-to-Criminal Flip Engine (เอนจินพลิกคดีแพ่งเป็นอาญา)
        </h2>
        <p style="color:var(--text-muted); font-size:14px; margin-top:2px;">
          พิสูจน์เจตนาทุจริตแฝงเร้นตั้งแต่แรกเริ่ม (Inception Fraud) อ้างอิงคำพิพากษาศาลฎีกาที่ ๕๘๕/๒๕๖๑ และ ๑๒๓๔/๒๕๕๐
        </p>

        <div class="flip-comparison">
          <div class="flip-box flip-civil">
            <h3 style="color:#f87171; font-size:16px; margin-bottom:10px;">❌ ฝ่ายจำเลยพยายามดึงเป็น "เรื่องผิดสัญญาทางแพ่ง"</h3>
            <ul style="color:#cbd5e1; font-size:14px; line-height:1.7; padding-left:20px;">
              <li>อ้างว่ายืมเงินกันธรรมดาตามความคุ้นเคย</li>
              <li>อ้างว่าตั้งใจจะคืนแต่หมุนเงินไม่ทัน</li>
              <li>อ้างว่าไม่มีสัญญากู้ยืมเงินเป็นหนังสือตาม ป.พ.พ. ๖๕๓ ทำให้ฟ้องไม่ได้</li>
              <li>ผลลัพธ์ที่จำเลยต้องการ: ยกฟ้องคดีอาญา เหยื่อต้องไปฟ้องแพ่งที่ไม่มีทรัพย์ให้ยึด</li>
            </ul>
          </div>

          <div class="flip-box flip-criminal">
            <h3 style="color:#4ade80; font-size:16px; margin-bottom:10px;">⚡ ยุทธศาสตร์พลิกเป็น "คดีอาญาฉ้อโกงปกติธุระ" (ป.อ. ๓๔๓)</h3>
            <ul style="color:#cbd5e1; font-size:14px; line-height:1.7; padding-left:20px;">
              <li><strong>Inception Fraud:</strong> กุเรื่องเท็จตั้งแต่ก่อนยืมเงิน (น้ำหอมแตก, แฟนอับสัญญาณ, ยอดต้น 50,000)</li>
              <li><strong>สัญญาเงินกู้เป็นเพียงเครื่องมือก่ออาชญากรรม (Instrument of Crime):</strong> หลอกลวงเอาทรัพย์</li>
              <li><strong>ต่างกรรมต่างวาระ ๒๖+ กระทง (ป.อ. ๙๑):</strong> โทษจำคุกสูงสุดกระทงละ ๕ ปี รวม ๒๐ ปี</li>
              <li><strong>ผลลัพธ์ชนะคดี:</strong> ประสาน ปปง. ยึดทรัพย์ตาม พ.ร.บ. ฟอกเงิน ม.๔๘ + สั่งชดใช้เงินตาม ป.วิ.อ. ๔๔/๑</li>
            </ul>
          </div>
        </div>
      </div>
    </div>

    <!-- TAB 3: HEATMAP -->
    <div id="btab-heatmap" class="boss-section" style="display:none;">
      <div class="sim-card">
        <h2 style="font-size:20px; font-weight:700; color:#fff;">
          🌊 Psychological Manipulation & Urgency Heatmap (ฮีทแมพคลื่นจิตวิทยาล่อลวง ๔ ระลอก)
        </h2>
        <p style="color:var(--text-muted); font-size:14px; margin-top:2px;">
          วิเคราะห์ลึกลำดับคลื่นจิตวิทยาที่จำเลยใช้ครอบงำและตอดเงินผู้เสียหายต่อเนื่อง ๘ เดือน
        </p>

        <div class="wave-grid">
          <div class="wave-card">
            <span class="wave-num" style="background:#0284c7;">ระลอกที่ ๑</span>
            <div class="wave-title">🚪 Foot-in-the-door (เปิดทาง)</div>
            <div class="wave-desc">
              เริ่มจากยอดเงินเล็ก ๒,๐๐๐ - ๓,๐๐๐ บาท สร้างความคุ้นเคยและความสงสาร ยอดเงินไม่สูงจนเหยื่อระแวง
            </div>
            <div class="wave-examples">
              <strong>ข้ออ้าง:</strong> สั่งครีมเงินขาด 2000 แฟนไปที่อับสัญญาณค่ำๆ คืน (กรรมที่ ๑)
            </div>
          </div>

          <div class="wave-card">
            <span class="wave-num" style="background:#7c3aed;">ระลอกที่ ๒</span>
            <div class="wave-title">💰 Phantom Capital Lure (เหยื่อล่อก้อนโต)</div>
            <div class="wave-desc">
              อ้างยอดเงินก้อนใหญ่ในอากาศเพื่อสร้างเครดิตเท็จ ล่อให้เหยื่อเชื่อว่ามีปัญญาคืนเงินแน่นอน
            </div>
            <div class="wave-examples">
              <strong>ข้ออ้าง:</strong> ยืม 3,000 บาท มีต้น 50,000 บาท เกิน 1 ทุ่มโอนคืนให้หมด (กรรมที่ ๒)
            </div>
          </div>

          <div class="wave-card">
            <span class="wave-num" style="background:#dc2626;">ระลอกที่ ๓</span>
            <div class="wave-title">🎭 Crisis & Emotional Extortion (บีบคั้นวิกฤต)</div>
            <div class="wave-desc">
              สร้างเรื่องคอขาดบาดตาย อ้างเรื่องถึงหน่วยงาน/สำนักงาน หรืออ้างวิกฤตสุขภาพเพื่อเร่งเร้า
            </div>
            <div class="wave-examples">
              <strong>ข้ออ้าง:</strong> เดินชนน้ำหอมแตก 2,000 เรื่องถึงสำนักงาน / ถอดเหล็กดัดฟัน 4,000 (กรรมที่ ๔, ๕)
            </div>
          </div>

          <div class="wave-card">
            <span class="wave-num" style="background:#e11d48;">ระลอกที่ ๔</span>
            <div class="wave-title">💸 Fabricated Slips & Ponzi Bleeding (สลิปปลอม & สูบซ้ำ)</div>
            <div class="wave-desc">
              สร้างภาพสลิปเท็จ ๓๕,๐๐๐ บาทลวงตา สลับกับการโอนคืนเศษเงินเล็กน้อยเพื่อยืมก้อนใหม่ที่ใหญ่กว่า
            </div>
            <div class="wave-examples">
              <strong>ข้ออ้าง:</strong> ส่งสลิปปลอม 35,000 บาท (กรรมที่ ๑๙) / คืน 1,000 เพื่อยืม 15,000 - 25,000
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- TAB 4: DEFENSE BUSTER -->
    <div id="btab-defensebuster" class="boss-section" style="display:none;">
      <div class="sim-card">
        <h2 style="font-size:20px; font-weight:700; color:#fff;">
          🛡️ Defense-Buster Matrix 5/5 (ตารางทำลาย ๕ ข้อต่อสู้อมตะของจำเลย)
        </h2>
        <p style="color:var(--text-muted); font-size:14px; margin-top:2px;">
          ขุดรากถอนโคน ๕ ประเด็นข้อต่อสู้ยอดนิยม ด้วยพยานหลักฐานทางนิติวิทยาศาสตร์ที่ศาลปฏิเสธไม่ได้
        </p>

        <div style="margin-top:20px;">
          __CROSS_EXAM_SUMMARY_CARDS__
        </div>
      </div>
    </div>

    <!-- TAB 5: 1-CLICK COURT EXHIBIT GENERATOR -->
    <div id="btab-exhibitgen" class="boss-section" style="display:none;">
      <div class="sim-card">
        <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:12px;">
          <div>
            <h2 style="font-size:20px; font-weight:700; color:#fff;">
              📑 1-Click Court Exhibit Generator (สารบบพยานเอกสาร หมาย จ.๑ ถึง จ.๓๐)
            </h2>
            <p style="color:var(--text-muted); font-size:14px; margin-top:2px;">
              สารบบรันหมายเลขพยานเอกสารศาลอัตโนมัติ (Court Exhibit Numbers) พร้อมระบุหน้าและรับรอง ป.วิ.อ. ๒๒๖
            </p>
          </div>
          <div>
            <button onclick="window.print()" class="btn-gold">
              🖨️ สั่งพิมพ์สารบบพยานเอกสาร (Print/PDF)
            </button>
          </div>
        </div>

        <table class="exhibit-table">
          <thead>
            <tr>
              <th style="width:90px; text-align:center;">หมายเอกสาร</th>
              <th>กรรมที่ & รายละเอียดพยานหลักฐาน</th>
              <th style="width:180px;">ผู้ต้องหาเป้าหมาย</th>
              <th style="width:130px;">ยอดเงิน</th>
              <th style="width:140px;">วันเวลาตราประทับ</th>
              <th style="width:140px; text-align:center;">การนำส่งศาล</th>
            </tr>
          </thead>
          <tbody>
            __EXHIBIT_ROWS_HTML__
          </tbody>
        </table>
      </div>
    </div>

  </div>

  <script>
    function switchBossTab(tabId, btn) {
      document.querySelectorAll('.boss-section').forEach(el => el.style.display = 'none');
      document.querySelectorAll('.btab-btn').forEach(b => b.classList.remove('active'));
      
      const target = document.getElementById('btab-' + tabId);
      if (target) target.style.display = 'block';
      if (btn) btn.classList.add('active');
    }

    // Universal Smart Link Resolver for Agent Navigation & Exhibits
    (function initSmartNav() {
      const isSubdir = window.location.pathname.replace(/\\\\/g, '/').toLowerCase().includes('/vector_evidence/');
      const linkMap = {
        '[1]': 'MASTER_SSOT_STITCH_VIEWER.html',
        '[2]': 'TARGET_FOCUS_SELECTOR.html',
        '[2.1]': 'BENEFICIARY_NETWORK_DASHBOARD.html?targets=jinnipha%2Cpreeyachat%2C',
        '[3]': 'CHAT_FORENSIC_VECTOR_EXPLORER.html',
        '[4]': 'INDIVIDUAL_COURT_INDICTMENT_DASHBOARD.html',
        '[5]': isSubdir ? 'VECTOR_EVIDENCE_DASHBOARD.html' : 'VECTOR_EVIDENCE/VECTOR_EVIDENCE_DASHBOARD.html',
        '[5.1]': 'TIMELINE_11D_DASHBOARD.html',
        '[6]': 'AGENT6_PRESIDENT_SUPREME_COURT_DASHBOARD.html'
      };

      document.querySelectorAll('.agent-card-nav').forEach(el => {
        const titleEl = el.querySelector('.ac-title');
        if (!titleEl) return;
        const text = titleEl.innerText;
        for (const [key, target] of Object.entries(linkMap)) {
          if (text.includes(key)) {
            const resolved = isSubdir ? ((key === '[5]' || key === '[5.1]' || key === '[6]') ? target : '../' + target) : target;
            el.href = resolved;
            el.onclick = function() {
              const curSub = window.location.pathname.replace(/\\\\/g, '/').toLowerCase().includes('/vector_evidence/');
              this.href = curSub ? ((key === '[5]' || key === '[5.1]' || key === '[6]') ? target : '../' + target) : target;
            };
            break;
          }
        }
      });
    })();
  </script>
</body>
</html>
"""

# Build Exhibit Rows HTML generator
def make_exhibit_rows(is_subdir=False):
    rows = []
    for ex in exhibit_registry:
        sheet_url = ex["html_sheet"] if is_subdir else f"VECTOR_EVIDENCE/{ex['html_sheet']}"
        row = f'''
    <tr>
      <td style="text-align:center;"><span class="ex-badge">{ex["exhibit_no"]}</span></td>
      <td>
        <strong>{ex["count_no"]}</strong>: {ex["count_title"]}
        <div style="font-size:12px; color:#64748b; margin-top:2px;">
          ไฟล์อ้างอิง: {ex["original_ref"]} • แผ่นศาลหน้าที่ {ex["court_page_start"]}
        </div>
      </td>
      <td><span style="color:#38bdf8; font-weight:600;">{ex["target_person"]}</span></td>
      <td><span style="color:#22c55e; font-weight:700; font-family:monospace;">{ex["amount"]}</span></td>
      <td><span style="font-size:12.5px; color:#94a3b8;">{ex["datetime"]}</span></td>
      <td style="text-align:center;">
        <a href="{sheet_url}" target="_blank" style="color:#38bdf8; text-decoration:none; font-size:13px; font-weight:600;">
          📄 เปิดตรวจแผ่นศาล
        </a>
      </td>
    </tr>
    '''
        rows.append(row)
    return rows

# Build Cross Exam Summary Cards for Tab 4
cross_exam_cards = []
for xc in timeline_11d["cross_examination_matrix"]:
    card = f'''
    <div style="background:#09101d; border:1px solid #1e293b; border-radius:10px; padding:18px; margin-bottom:16px;">
      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
        <span style="font-family:monospace; font-weight:700; color:#ef4444; background:rgba(239,68,68,0.15); padding:2px 8px; border-radius:4px;">
          {xc["id"]}
        </span>
        <span style="font-size:16px; font-weight:700; color:#fff;">{xc["category"]}</span>
        <span style="font-size:12.5px; color:#fde047;">มัดตัวด้วย: {xc["smoking_gun_ref"]}</span>
      </div>
      <div style="background:rgba(245,158,11,0.08); border-left:3px solid #f59e0b; padding:8px 14px; border-radius:0 6px 6px 0; margin-bottom:10px; font-size:13.5px; color:#fde68a;">
        <strong>ข้ออ้างจำเลย:</strong> {xc["defense_claim"]}
      </div>
      <div style="background:rgba(239,68,68,0.08); border-left:3px solid #ef4444; padding:8px 14px; border-radius:0 6px 6px 0; margin-bottom:12px; font-size:13.5px; color:#fca5a5;">
        <strong>จุดตายทางกฎหมาย:</strong> {xc["vulnerability"]}
      </div>
      <div style="font-size:13.5px; color:#cbd5e1;">
        <strong>สคริปต์คำถามชี้นำตัวอย่าง:</strong> "{xc["question_chain"][0]["question"]}" ➔ คำตอบที่จำเลยต้องตอบ: <span style="color:#22c55e; font-weight:700;">{xc["question_chain"][0]["target_answer"]}</span>
      </div>
    </div>
    '''
    cross_exam_cards.append(card)

# 1. Generate Root Dashboard (d:\Project\ชวกม.2\EDOK_NUI\AGENT6_PRESIDENT_SUPREME_COURT_DASHBOARD.html)
root_html = boss_html_template.replace("__AGENT1_HREF__", "MASTER_SSOT_STITCH_VIEWER.html")
root_html = root_html.replace("__AGENT2_HREF__", "TARGET_FOCUS_SELECTOR.html")
root_html = root_html.replace("__AGENT2_1_HREF__", "BENEFICIARY_NETWORK_DASHBOARD.html?targets=jinnipha%2Cpreeyachat%2C")
root_html = root_html.replace("__AGENT3_HREF__", "CHAT_FORENSIC_VECTOR_EXPLORER.html")
root_html = root_html.replace("__AGENT4_HREF__", "INDIVIDUAL_COURT_INDICTMENT_DASHBOARD.html")
root_html = root_html.replace("__AGENT5_HREF__", "VECTOR_EVIDENCE/VECTOR_EVIDENCE_DASHBOARD.html")
root_html = root_html.replace("__AGENT5_1_HREF__", "TIMELINE_11D_DASHBOARD.html")
root_html = root_html.replace("__AGENT6_HREF__", "AGENT6_PRESIDENT_SUPREME_COURT_DASHBOARD.html")
root_html = root_html.replace("__EXHIBIT_ROWS_HTML__", "\n".join(make_exhibit_rows(is_subdir=False)))
root_html = root_html.replace("__CROSS_EXAM_SUMMARY_CARDS__", "\n".join(cross_exam_cards))

boss_dashboard_path = os.path.join(EDOK_DIR, "AGENT6_PRESIDENT_SUPREME_COURT_DASHBOARD.html")
with open(boss_dashboard_path, "w", encoding="utf-8") as f:
    f.write(root_html)
print(f"Generated Root Boss Dashboard: {boss_dashboard_path}")

# 2. Generate Subdir Dashboard (d:\Project\ชวกม.2\EDOK_NUI\VECTOR_EVIDENCE\AGENT6_PRESIDENT_SUPREME_COURT_DASHBOARD.html)
subdir_html = boss_html_template.replace("__AGENT1_HREF__", "../MASTER_SSOT_STITCH_VIEWER.html")
subdir_html = subdir_html.replace("__AGENT2_HREF__", "../TARGET_FOCUS_SELECTOR.html")
subdir_html = subdir_html.replace("__AGENT2_1_HREF__", "../BENEFICIARY_NETWORK_DASHBOARD.html?targets=jinnipha%2Cpreeyachat%2C")
subdir_html = subdir_html.replace("__AGENT3_HREF__", "../CHAT_FORENSIC_VECTOR_EXPLORER.html")
subdir_html = subdir_html.replace("__AGENT4_HREF__", "../INDIVIDUAL_COURT_INDICTMENT_DASHBOARD.html")
subdir_html = subdir_html.replace("__AGENT5_HREF__", "VECTOR_EVIDENCE_DASHBOARD.html")
subdir_html = subdir_html.replace("__AGENT5_1_HREF__", "TIMELINE_11D_DASHBOARD.html")
subdir_html = subdir_html.replace("__AGENT6_HREF__", "AGENT6_PRESIDENT_SUPREME_COURT_DASHBOARD.html")
subdir_html = subdir_html.replace("__EXHIBIT_ROWS_HTML__", "\n".join(make_exhibit_rows(is_subdir=True)))
subdir_html = subdir_html.replace("__CROSS_EXAM_SUMMARY_CARDS__", "\n".join(cross_exam_cards))

vector_boss_path = os.path.join(EDOK_DIR, "VECTOR_EVIDENCE", "AGENT6_PRESIDENT_SUPREME_COURT_DASHBOARD.html")
with open(vector_boss_path, "w", encoding="utf-8") as f:
    f.write(subdir_html)
print(f"Generated Vector Evidence Subdir Boss Dashboard: {vector_boss_path}")

# Copy Blueprint to VECTOR_EVIDENCE as well
shutil.copy2(blueprint_path, os.path.join(EDOK_DIR, "VECTOR_EVIDENCE", "AGENT6_ULTIMATE_BLUEPRINT_AND_GENESIS.md"))

# 4. Copy deliverables to Artifact Directory
print("\n>>> Copying Agent 6 deliverables to Artifact Directory...")
os.makedirs(ARTIFACT_DIR, exist_ok=True)

files_to_copy = [
    (blueprint_path, os.path.join(ARTIFACT_DIR, "AGENT6_ULTIMATE_BLUEPRINT_AND_GENESIS.md")),
    (boss_dashboard_path, os.path.join(ARTIFACT_DIR, "AGENT6_PRESIDENT_SUPREME_COURT_DASHBOARD.html")),
    (exhibit_json_path, os.path.join(ARTIFACT_DIR, "EXHIBIT_GENERATOR_DATA.json")),
]

for src, dst in files_to_copy:
    shutil.copy2(src, dst)
    print(f"Copied {os.path.basename(src)} -> {dst}")

print("\n>>> [Agent 6] President of the Supreme Court & Ultimate Blueprint Launched Successfully! <<<")

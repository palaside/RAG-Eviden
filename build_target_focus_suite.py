# -*- coding: utf-8 -*-
"""
Script: build_target_focus_suite.py
สร้างเครื่องมือ 2 ขั้นตอนตามลำดับที่ถูกต้อง:
ขั้นตอนที่ ๑: TARGET_FOCUS_SELECTOR.html (เครื่องมือเลือกโฟกัสเป้าหมายโดยผู้ใช้งาน)
ขั้นตอนที่ ๒: BENEFICIARY_NETWORK_DASHBOARD.html (แดชบอร์ดเครือข่ายที่กรองตามที่ผู้ใช้เลือก)
"""

import os
import json

SELECTOR_FILE = r'd:\Project\ชวกม.2\EDOK_NUI\TARGET_FOCUS_SELECTOR.html'
DASHBOARD_FILE = r'd:\Project\ชวกม.2\EDOK_NUI\BENEFICIARY_NETWORK_DASHBOARD.html'

# ข้อมูลบุคคลทั้งหมดที่ตรวจพบในพยานหลักฐาน 100% (All Discovered Entities)
ENTITIES_DATA = [
    {
        'id': 'jinnipha',
        'name': 'น.ส. จิณห์นิภา ประสาทเขตต์การ (ประสาทเขตรการ)',
        'relation_note': 'บุคคลหลักที่ปรากฏในแชทและรับโอนเงินต่อเนื่อง',
        'slip_count': 78,
        'total_amount': 574239.25,
        'accounts': [
            {'bank': 'ธนาคารกรุงศรีอยุธยา (BAY)', 'acc': 'XXX-X-XX385-0'},
            {'bank': 'ธนาคารทหารไทยธนชาต (TTB)', 'acc': 'XXX-X-XX996-5'},
            {'bank': 'ธนาคารทหารไทยธนชาต (TTB)', 'acc': 'XXX-X-XX764-0'},
            {'bank': 'ธนาคารกรุงไทย (KTB)', 'acc': 'XXX-X-XX313-5'},
            {'bank': 'พร้อมเพย์ (PromptPay)', 'acc': '088-0906599'}
        ],
        'evidence_refs': ['สนทนาแนบสลิป/01.9.68_IMG_6288.PNG', 'สนทนาแนบสลิป/03.2.68_IMG_6085.PNG', 'A4_Full_30.5.68_LINE_capture_796546908.658321.JPG'],
        'default_selected': True
    },
    {
        'id': 'preeyachat',
        'name': 'น.ส. ปรียชาติ ฉิมพลี (พี่แมว)',
        'relation_note': 'รุ่นพี่ที่ถูกกล่าวถึงในแชท / บัญชีรับเงินกู้และส่งสลิปสัญญาผลตอบแทน',
        'slip_count': 3,
        'total_amount': 27500.00,
        'accounts': [
            {'bank': 'ธนาคารกสิกรไทย (KBANK)', 'acc': '281-2-548455-1 (XXX-X-XX455-1)'}
        ],
        'evidence_refs': ['03.6.68 พี่แมว_IMG_6246.PNG', '08.6.68 พี่แมว_LINE_capture_796547198.800971.JPG', 'IMG_2622.PNG'],
        'default_selected': True
    },
    {
        'id': 'wanwisa',
        'name': 'น.ส. วันวิศา ประสาทเขตรการ',
        'relation_note': 'พี่น้องของจิณห์นิภาที่ส่งเลขบัญชีให้โอนจ่ายในแชท',
        'slip_count': 2,
        'total_amount': 23000.00,
        'accounts': [
            {'bank': 'ธนาคารออมสิน (GSB)', 'acc': '020333988630'},
            {'bank': 'ธนาคารกรุงไทย (KTB)', 'acc': '083-0'}
        ],
        'evidence_refs': ['A4_Full_27.5.68 พี่น้อง_IMG_6243.PNG', 'LINE_capture_800256213.882803.jpg'],
        'default_selected': False
    },
    {
        'id': 'kanyapak',
        'name': 'น.ส. กัญญาภัค ฉิมพลี',
        'relation_note': 'เครือญาติฝ่ายปรียชาติ (พี่แมว) ที่จิณห์นิภาส่งสลิปกระจายเงินให้',
        'slip_count': 1,
        'total_amount': 15000.00,
        'accounts': [
            {'bank': 'พร้อมเพย์ (PromptPay)', 'acc': 'เบอร์ลงท้าย 2926'}
        ],
        'evidence_refs': ['IMG_2800.PNG'],
        'default_selected': False
    },
    {
        'id': 'tatsaneekan',
        'name': 'น.ส. ทัศนีการ ประสาทเขตรการ',
        'relation_note': 'พี่น้องของจิณห์นิภาที่ส่งเลขบัญชีให้โอนจ่ายในแชท',
        'slip_count': 1,
        'total_amount': 5000.00,
        'accounts': [
            {'bank': 'พร้อมเพย์ (PromptPay)', 'acc': '091-2634123'}
        ],
        'evidence_refs': ['A4_Full_27.5.68 พี่น้อง_IMG_6243.PNG'],
        'default_selected': False
    },
    {
        'id': 'promptpay_086',
        'name': 'พร้อมเพย์ 086-4483287',
        'relation_note': 'เบอร์พร้อมเพย์ที่จำเลยส่งมาในแชทให้โอนทดสอบ/สั่งจ่าย',
        'slip_count': 2,
        'total_amount': 3.80,
        'accounts': [
            {'bank': 'พร้อมเพย์ (PromptPay)', 'acc': '086-4483287'}
        ],
        'evidence_refs': ['04.2.68_IMG_6087.PNG'],
        'default_selected': False
    },
    {
        'id': 'nuttachai_return',
        'name': 'นาย ณัฐชัย รักษาวงศ์ (สลิปโอนคืน/บัญชีผู้เสียหาย)',
        'relation_note': 'บัญชีผู้เสียหายและสลิปเงินโอนคืนที่ส่งในแชท',
        'slip_count': 29,
        'total_amount': 85460.00,
        'accounts': [
            {'bank': 'ธนาคารกรุงไทย (KTB)', 'acc': 'XXX-X-XX452-9'},
            {'bank': 'ธนาคารทหารไทยธนชาต (TTB)', 'acc': 'XXX-X-XX558-9'},
            {'bank': 'ธนาคารกรุงไทย (KTB)', 'acc': 'XXX-X-XX526-6'}
        ],
        'evidence_refs': ['สนทนาแนบสลิป/16.2.68_IMG_6102.PNG'],
        'default_selected': False
    },
    {
        'id': 'other_chat_entities',
        'name': 'บุคคลอื่นๆ ที่ปรากฏในบทสนทนา (บุญประเสริฐ, สุธีรัตน์, เหมือนขวัญ, เบญจมาศ, ชนัญชิดามนต์)',
        'relation_note': 'บุคคลที่ถูกกล่าวถึงหรือพาดพิงในบทสนทนาแชท (ไม่มีสลิปโอนเงินโดยตรง)',
        'slip_count': 0,
        'total_amount': 0.00,
        'accounts': [],
        'evidence_refs': ['MASTER_TRANSCRIPT_CHRONOLOGICAL.md'],
        'default_selected': False
    }
]

entities_json = json.dumps(ENTITIES_DATA, ensure_ascii=False)

# 1. สร้าง TARGET_FOCUS_SELECTOR.html
selector_html = f'''<!DOCTYPE html>
<html lang="th">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>🎯 เครื่องมือคัดกรองและเลือกโฟกัสเป้าหมายแห่งคดี (Target Focus Selector)</title>
  <style>
    @font-face {{
      font-family: 'TH Sarabun PSK';
      src: local('TH Sarabun PSK'), local('THSarabunPSK');
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; font-family: 'TH Sarabun PSK', sans-serif; }}
    body {{
      background: #090d16;
      color: #e2e8f0;
      font-size: 16px;
      line-height: 1.5;
    }}
    
    /* STICKY TOP BAR */
    .top-bar {{
      background: rgba(15, 23, 42, 0.95);
      border-bottom: 1px solid #1e293b;
      padding: 18px 30px;
      position: sticky;
      top: 0;
      z-index: 100;
      backdrop-filter: blur(12px);
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 15px;
    }}
    .bar-title {{
      font-size: 24px;
      font-weight: 800;
      color: #38bdf8;
      display: flex;
      align-items: center;
      gap: 10px;
    }}
    .bar-sub {{
      font-size: 14.5px;
      color: #94a3b8;
    }}
    
    .btn-proceed {{
      background: #0284c7;
      color: #ffffff;
      border: 1px solid #38bdf8;
      padding: 10px 22px;
      border-radius: 8px;
      font-size: 16px;
      font-weight: 800;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 8px;
      transition: all 0.2s;
      box-shadow: 0 4px 15px rgba(2, 132, 199, 0.4);
    }}
    .btn-proceed:hover {{
      background: #0369a1;
      transform: translateY(-1px);
    }}
    
    /* SUMMARY STRIP */
    .summary-strip {{
      max-width: 1300px;
      margin: 20px auto 0;
      padding: 0 25px;
    }}
    .alert-box {{
      background: #172554;
      border: 1px solid #3b82f6;
      border-radius: 8px;
      padding: 14px 20px;
      color: #bfdbfe;
      font-size: 15px;
      display: flex;
      align-items: center;
      gap: 12px;
    }}
    
    /* ENTITY CARDS GRID */
    .container {{
      max-width: 1300px;
      margin: 20px auto 50px;
      padding: 0 25px;
    }}
    .cards-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(380px, 1fr));
      gap: 20px;
      margin-top: 20px;
    }}
    .entity-card {{
      background: #0f172a;
      border: 2px solid #1e293b;
      border-radius: 12px;
      padding: 20px;
      position: relative;
      cursor: pointer;
      transition: all 0.2s ease;
    }}
    .entity-card:hover {{
      border-color: #38bdf8;
      transform: translateY(-2px);
    }}
    .entity-card.selected {{
      border-color: #0284c7;
      background: #0a1733;
      box-shadow: 0 0 15px rgba(2, 132, 199, 0.3);
    }}
    
    .card-top {{
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      gap: 12px;
      margin-bottom: 12px;
    }}
    .entity-name {{
      font-size: 18px;
      font-weight: 800;
      color: #f1f5f9;
      line-height: 1.3;
    }}
    .checkbox-custom {{
      width: 24px;
      height: 24px;
      accent-color: #0284c7;
      cursor: pointer;
    }}
    
    .entity-note {{
      font-size: 14px;
      color: #94a3b8;
      margin-bottom: 14px;
      border-left: 3px solid #334155;
      padding-left: 10px;
    }}
    
    .metrics-row {{
      display: flex;
      justify-content: space-between;
      background: #090d16;
      border-radius: 6px;
      padding: 10px 14px;
      margin-bottom: 14px;
      font-size: 14.5px;
    }}
    .metrics-row strong {{
      color: #38bdf8;
      font-size: 16px;
    }}
    
    .accounts-list {{
      font-size: 13.5px;
      color: #cbd5e1;
      border-top: 1px solid #1e293b;
      padding-top: 10px;
    }}
    .acc-badge {{
      display: inline-block;
      background: #1e293b;
      padding: 3px 8px;
      border-radius: 4px;
      margin: 3px 2px;
      font-family: monospace;
      font-size: 12.5px;
    }}
  </style>
</head>
<body>
  <div class="top-bar">
    <div>
      <div class="bar-title">
        <span>🎯 เครื่องมือคัดกรองและเลือกโฟกัสเป้าหมายแห่งคดี (Target Focus Gateway)</span>
      </div>
      <div class="bar-sub">
        แสดงรายชื่อบุคคลและบัญชีทั้งหมดที่ตรวจพบในพยานหลักฐาน 100% — ผู้ใช้งานเป็นผู้ตัดสินใจเลือกโฟกัสเป้าหมายด้วยตนเอง
      </div>
    </div>
    
    <div style="display: flex; align-items: center; gap: 15px;">
      <div style="text-align: right;">
        <div style="font-size: 13.5px; color: #94a3b8;">เป้าหมายที่เลือก: <strong id="selectedCountText" style="color:#38bdf8; font-size:16px;">2</strong> บุคคล</div>
        <div style="font-size: 14px; color: #f43f5e; font-weight: 700;">ยอดเงินรวมเป้าหมาย: <span id="selectedSumText">601,739.25 บาท</span></div>
      </div>
      <button class="btn-proceed" onclick="proceedToDashboard()">
        <span>🚀 ยืนยันเป้าหมายและเปิดแดชบอร์ดเครือข่าย</span>
      </button>
    </div>
  </div>

  <div class="summary-strip">
    <div class="alert-box">
      <span style="font-size: 22px;">ℹ️</span>
      <div>
        <strong>ขั้นตอนของผู้ใช้งาน (Human-in-the-Loop):</strong> ติ๊กเลือกบุคคลที่ท่านต้องการโฟกัสในการดำเนินคดี (สามารถเลือกหนึ่งคนหรือหลายคนพร้อมกันได้) เมื่อเลือกเสร็จแล้วให้กดปุ่ม <strong>"ยืนยันเป้าหมายและเปิดแดชบอร์ดเครือข่าย"</strong> ระบบจะสร้างแผนผังความสัมพันธ์และกรองข้อมูลเฉพาะบุคคลที่ท่านเลือกทันที
      </div>
    </div>
  </div>

  <div class="container">
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
      <h3 style="font-size: 19px; color: #f1f5f9; font-weight: 800;">รายชื่อบุคคลและกลุ่มบัญชีทั้งหมดที่ตรวจพบในคดี:</h3>
      <div>
        <button onclick="selectAll(true)" style="background:#1e293b; color:#cbd5e1; border:1px solid #334155; padding:5px 10px; border-radius:4px; cursor:pointer; font-size:13px; margin-right:5px;">เลือกทั้งหมด</button>
        <button onclick="selectAll(false)" style="background:#1e293b; color:#cbd5e1; border:1px solid #334155; padding:5px 10px; border-radius:4px; cursor:pointer; font-size:13px;">ยกเลิกทั้งหมด</button>
      </div>
    </div>
    
    <div class="cards-grid" id="cardsGrid">
      <!-- Populated by JS -->
    </div>
  </div>

  <script>
    const entities = {entities_json};
    let selectedIds = new Set(['jinnipha', 'preeyachat']);

    // โหลดจากการตั้งค่าเดิมถ้ามี
    const saved = localStorage.getItem('SELECTED_FOCUS_TARGETS');
    if (saved) {{
      try {{
        selectedIds = new Set(JSON.parse(saved));
      }} catch(e) {{}}
    }}

    function renderCards() {{
      const grid = document.getElementById('cardsGrid');
      grid.innerHTML = '';

      entities.forEach(ent => {{
        const isSelected = selectedIds.has(ent.id);
        const card = document.createElement('div');
        card.className = 'entity-card' + (isSelected ? ' selected' : '');
        card.onclick = (e) => {{
          if (e.target.type !== 'checkbox') {{
            toggleSelect(ent.id);
          }}
        }};

        let accHtml = '';
        if (ent.accounts.length > 0) {{
          accHtml = '<div class="accounts-list"><strong>บัญชีที่ตรวจพบ:</strong><br>' + 
                    ent.accounts.map(a => `<span class="acc-badge">${{a.bank}}: ${{a.acc}}</span>`).join('') + 
                    '</div>';
        }} else {{
          accHtml = '<div class="accounts-list" style="color:#64748b;"><em>ไม่มีสลิปหรือบัญชีรับโอนโดยตรง (ปรากฏในข้อความแชท)</em></div>';
        }}

        card.innerHTML = `
          <div class="card-top">
            <div class="entity-name">${{ent.name}}</div>
            <input type="checkbox" class="checkbox-custom" ${{isSelected ? 'checked' : ''}} onchange="toggleSelect('${{ent.id}}')">
          </div>
          <div class="entity-note">${{ent.relation_note}}</div>
          <div class="metrics-row">
            <div>ยอดเงินที่ตรวจพบ:<br><strong style="color:#22c55e;">${{ent.total_amount.toLocaleString('th-TH', {{minimumFractionDigits: 2}})}} บาท</strong></div>
            <div style="text-align:right;">จำนวนสลิป:<br><strong>${{ent.slip_count}} รายการ</strong></div>
          </div>
          ${{accHtml}}
        `;
        grid.appendChild(card);
      }});

      updateSummary();
    }}

    function toggleSelect(id) {{
      if (selectedIds.has(id)) {{
        selectedIds.delete(id);
      }} else {{
        selectedIds.add(id);
      }}
      localStorage.setItem('SELECTED_FOCUS_TARGETS', JSON.stringify(Array.from(selectedIds)));
      renderCards();
    }}

    function selectAll(state) {{
      if (state) {{
        entities.forEach(e => selectedIds.add(e.id));
      }} else {{
        selectedIds.clear();
      }}
      localStorage.setItem('SELECTED_FOCUS_TARGETS', JSON.stringify(Array.from(selectedIds)));
      renderCards();
    }}

    function updateSummary() {{
      document.getElementById('selectedCountText').innerText = selectedIds.size;
      let total = 0;
      entities.forEach(e => {{
        if (selectedIds.has(e.id)) {{
          total += e.total_amount;
        }}
      }});
      document.getElementById('selectedSumText').innerText = total.toLocaleString('th-TH', {{minimumFractionDigits: 2, maximumFractionDigits: 2}}) + ' บาท';
    }}

    function proceedToDashboard() {{
      if (selectedIds.size === 0) {{
        alert('กรุณาเลือกเป้าหมายอย่างน้อย 1 รายการเพื่อดำเนินคดีครับ');
        return;
      }}
      localStorage.setItem('SELECTED_FOCUS_TARGETS', JSON.stringify(Array.from(selectedIds)));
      window.location.href = 'BENEFICIARY_NETWORK_DASHBOARD.html';
    }}

    renderCards();
  </script>
</body>
</html>
'''

with open(SELECTOR_FILE, 'w', encoding='utf-8') as f:
    f.write(selector_html)

print(f"Generated TARGET_FOCUS_SELECTOR.html at: {SELECTOR_FILE}")

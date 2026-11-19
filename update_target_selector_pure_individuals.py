# -*- coding: utf-8 -*-
"""
Script: update_target_selector_pure_individuals.py
อัปเดต TARGET_FOCUS_SELECTOR.html ให้แสดงผลการ์ดกระชับตาม KPI รูปที่ 2
- ซ่อนรายละเอียดบัญชีจากหน้า UI (แต่คงข้อมูลทำงานใน Background 100%)
- การ์ดแสดงเฉพาะ:
  1. ชื่อ-นามสกุล + Checkbox
  2. กล่อง KPI: [ยอดเงิน (สีเขียว)] และ [สลิป/หลักฐาน (สีฟ้า)]
"""

import os
import json

INDIVIDUALS_FILE = r'd:\Project\ชวกม.2\EDOK_NUI\ALL_DISCOVERED_INDIVIDUALS.json'
SELECTOR_FILE = r'd:\Project\ชวกม.2\EDOK_NUI\TARGET_FOCUS_SELECTOR.html'

with open(INDIVIDUALS_FILE, 'r', encoding='utf-8') as f:
    individuals = json.load(f)

individuals_json = json.dumps(individuals, ensure_ascii=False)

html_content = f'''<!DOCTYPE html>
<html lang="th">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>🎯 คลังสารบบรายชื่อบุคคลทั้งหมดแห่งคดี (Target Focus Discovery Gateway)</title>
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
      padding: 16px 30px;
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
      padding: 10px 24px;
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
    
    /* CONTROLS STRIP */
    .controls-strip {{
      max-width: 1400px;
      margin: 20px auto 0;
      padding: 0 25px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 15px;
    }}
    .search-box {{
      flex: 1;
      min-width: 300px;
      background: #0f172a;
      border: 1px solid #334155;
      border-radius: 8px;
      padding: 10px 16px;
      color: #f8fafc;
      font-size: 15px;
    }}
    .search-box:focus {{
      outline: none;
      border-color: #38bdf8;
    }}
    
    .sort-btn {{
      background: #1e293b;
      color: #cbd5e1;
      border: 1px solid #334155;
      padding: 8px 14px;
      border-radius: 6px;
      font-size: 14px;
      font-weight: 600;
      cursor: pointer;
    }}
    .sort-btn.active {{
      background: #0284c7;
      color: #ffffff;
      border-color: #38bdf8;
    }}
    
    /* CARDS GRID */
    .container {{
      max-width: 1400px;
      margin: 20px auto 60px;
      padding: 0 25px;
    }}
    .cards-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
      gap: 14px;
    }}
    
    /* COMPACT KPI CARD (EXACTLY AS IMAGE 2) */
    .entity-card {{
      background: #0b1329;
      border: 2px solid #1e293b;
      border-radius: 10px;
      padding: 14px 16px;
      cursor: pointer;
      transition: all 0.2s ease;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }}
    .entity-card:hover {{
      border-color: #38bdf8;
      transform: translateY(-2px);
    }}
    .entity-card.selected {{
      border-color: #0284c7;
      background: #0e1d3e;
      box-shadow: 0 0 12px rgba(2, 132, 199, 0.4);
    }}
    
    .card-top {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 10px;
      margin-bottom: 12px;
    }}
    .entity-name {{
      font-size: 17px;
      font-weight: 800;
      color: #f8fafc;
      line-height: 1.25;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }}
    .checkbox-custom {{
      width: 20px;
      height: 20px;
      accent-color: #0284c7;
      cursor: pointer;
      flex-shrink: 0;
    }}
    
    /* KPI METRICS BOX */
    .metrics-box {{
      background: #040814;
      border: 1px solid #162036;
      border-radius: 8px;
      padding: 10px 14px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .kpi-col {{
      display: flex;
      flex-direction: column;
    }}
    .kpi-lbl {{
      font-size: 13px;
      color: #94a3b8;
      margin-bottom: 2px;
    }}
    .kpi-val-amt {{
      font-size: 16px;
      font-weight: 800;
      color: #22c55e;
    }}
    .kpi-val-cnt {{
      font-size: 16px;
      font-weight: 800;
      color: #38bdf8;
      text-align: right;
    }}
  </style>
</head>
<body>
  <div class="top-bar">
    <div>
      <div class="bar-title">
        <span>🎯 คลังสารบบรายชื่อบุคคลทั้งหมดแห่งคดี (Target Focus Discovery Gateway)</span>
      </div>
      <div class="bar-sub">
        แสดงบุคคลทุกคน {len(individuals)} คนแยกเป็นรายบุคคลเดี่ยว — คลิกเลือกบุคคลที่ต้องการเพื่อส่งต่อให้แดชบอร์ดเครือข่าย
      </div>
    </div>
    
    <div style="display: flex; align-items: center; gap: 15px;">
      <div style="text-align: right;">
        <div style="font-size: 13.5px; color: #94a3b8;">เป้าหมายที่เลือก: <strong id="selectedCountText" style="color:#38bdf8; font-size:16px;">0</strong> คน</div>
        <div style="font-size: 14px; color: #f43f5e; font-weight: 700;">ยอดเงินรวมเป้าหมาย: <span id="selectedSumText">0.00 บาท</span></div>
      </div>
      <button class="btn-proceed" onclick="proceedToDashboard()">
        <span>🚀 ยืนยันเป้าหมายและเปิดแดชบอร์ดเครือข่าย</span>
      </button>
    </div>
  </div>

  <div class="controls-strip">
    <input type="text" class="search-box" id="searchBox" placeholder="🔍 ค้นหาชื่อ-นามสกุล, เลขบัญชี (ค้นหาเบื้องหลังได้)..." oninput="handleSearch()">
    
    <div style="display: flex; gap: 8px; align-items: center;">
      <span style="font-size: 13.5px; color: #94a3b8;">เรียงตาม:</span>
      <button class="sort-btn active" id="sortAmtBtn" onclick="setSort('amount')">💰 ยอดเงินสูงสุด</button>
      <button class="sort-btn" id="sortCntBtn" onclick="setSort('count')">🧾 จำนวนสลิป</button>
      <button class="sort-btn" id="sortNameBtn" onclick="setSort('name')">🔤 ชื่อ ก-ฮ</button>
      
      <div style="margin-left: 10px;">
        <button onclick="selectAll(true)" style="background:#1e293b; color:#cbd5e1; border:1px solid #334155; padding:6px 10px; border-radius:4px; cursor:pointer; font-size:13px;">เลือกทั้งหมด</button>
        <button onclick="selectAll(false)" style="background:#1e293b; color:#cbd5e1; border:1px solid #334155; padding:6px 10px; border-radius:4px; cursor:pointer; font-size:13px;">ยกเลิกทั้งหมด</button>
      </div>
    </div>
  </div>

  <div class="container">
    <div class="cards-grid" id="cardsGrid">
      <!-- Populated by JS -->
    </div>
  </div>

  <script>
    const allIndividuals = {individuals_json};
    let selectedIds = new Set();
    let currentSort = 'amount';
    let searchQuery = '';

    const saved = localStorage.getItem('SELECTED_FOCUS_TARGETS');
    if (saved) {{
      try {{
        selectedIds = new Set(JSON.parse(saved));
      }} catch(e) {{}}
    }}

    function renderCards() {{
      const grid = document.getElementById('cardsGrid');
      grid.innerHTML = '';

      let list = allIndividuals.filter(p => {{
        if (!searchQuery) return true;
        const q = searchQuery.toLowerCase();
        const accs = p.accounts ? p.accounts.join(' ').toLowerCase() : '';
        return p.name.toLowerCase().includes(q) || accs.includes(q);
      }});

      if (currentSort === 'amount') {{
        list.sort((a, b) => b.total_amount - a.total_amount);
      }} else if (currentSort === 'count') {{
        list.sort((a, b) => b.slips_count - a.slips_count);
      }} else if (currentSort === 'name') {{
        list.sort((a, b) => a.name.localeCompare(b.name, 'th'));
      }}

      list.forEach(ent => {{
        const isSelected = selectedIds.has(ent.id);
        const card = document.createElement('div');
        card.className = 'entity-card' + (isSelected ? ' selected' : '');
        card.onclick = (e) => {{
          if (e.target.type !== 'checkbox') {{
            toggleSelect(ent.id);
          }}
        }};

        card.innerHTML = `
          <div class="card-top">
            <div class="entity-name" title="${{ent.name}}">${{ent.name}}</div>
            <input type="checkbox" class="checkbox-custom" ${{isSelected ? 'checked' : ''}} onchange="toggleSelect('${{ent.id}}')">
          </div>
          <div class="metrics-box">
            <div class="kpi-col">
              <span class="kpi-lbl">ยอดเงิน:</span>
              <span class="kpi-val-amt">${{ent.total_amount.toLocaleString('th-TH', {{minimumFractionDigits: 2}})}} บ.</span>
            </div>
            <div class="kpi-col" style="text-align: right;">
              <span class="kpi-lbl">สลิป/หลักฐาน:</span>
              <span class="kpi-val-cnt">${{ent.slips_count}} รายการ</span>
            </div>
          </div>
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
        allIndividuals.forEach(e => selectedIds.add(e.id));
      }} else {{
        selectedIds.clear();
      }}
      localStorage.setItem('SELECTED_FOCUS_TARGETS', JSON.stringify(Array.from(selectedIds)));
      renderCards();
    }}

    function setSort(type) {{
      currentSort = type;
      document.querySelectorAll('.sort-btn').forEach(b => b.classList.remove('active'));
      if (type === 'amount') document.getElementById('sortAmtBtn').classList.add('active');
      if (type === 'count') document.getElementById('sortCntBtn').classList.add('active');
      if (type === 'name') document.getElementById('sortNameBtn').classList.add('active');
      renderCards();
    }}

    function handleSearch() {{
      searchQuery = document.getElementById('searchBox').value.trim();
      renderCards();
    }}

    function updateSummary() {{
      document.getElementById('selectedCountText').innerText = selectedIds.size;
      let total = 0;
      allIndividuals.forEach(e => {{
        if (selectedIds.has(e.id)) {{
          total += e.total_amount;
        }}
      }});
      document.getElementById('selectedSumText').innerText = total.toLocaleString('th-TH', {{minimumFractionDigits: 2, maximumFractionDigits: 2}}) + ' บาท';
    }}

    function proceedToDashboard() {{
      if (selectedIds.size === 0) {{
        alert('กรุณาเลือกบุคคลที่ต้องการโฟกัสอย่างน้อย 1 คนครับ');
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
    f.write(html_content)

print(f"Updated TARGET_FOCUS_SELECTOR.html with compact KPI cards (Image 2 standard)!")

# -*- coding: utf-8 -*-
"""
Script: build_perfect_focused_dashboard.py
สร้างระบบกรองเป้าหมายแบบเข้มงวด 100% (Strict Dynamic Target Focus):
1. อัปเดต TARGET_FOCUS_SELECTOR.html ให้ส่ง query param ?targets=...
2. อัปเดต BENEFICIARY_NETWORK_DASHBOARD.html ให้กรองแสดงเฉพาะเป้าหมายที่เลือกเท่านั้น
   - หากเลือกเฉพาะ จิณห์นิภา -> แสดงเฉพาะ จิณห์นิภา และบัญชีของเธอเท่านั้น (ไม่มีคนอื่นเด็ดขาด!)
   - แผนผัง SVG Graph เรนเดอร์แบบ Dynamic ตามเป้าหมายที่เลือกจริง
   - ตารางสารบบกรองแสดงเฉพาะรายการของเป้าหมายที่เลือก
"""

import os
import json

INDIVIDUALS_FILE = r'd:\Project\ชวกม.2\EDOK_NUI\ALL_DISCOVERED_INDIVIDUALS.json'
TRANSACTIONS_FILE = r'd:\Project\ชวกม.2\EDOK_NUI\BENEFICIARY_TRANSACTION_RECORDS.json'
SELECTOR_FILE = r'd:\Project\ชวกม.2\EDOK_NUI\TARGET_FOCUS_SELECTOR.html'
DASHBOARD_FILE = r'd:\Project\ชวกม.2\EDOK_NUI\BENEFICIARY_NETWORK_DASHBOARD.html'

with open(INDIVIDUALS_FILE, 'r', encoding='utf-8') as f:
    individuals = json.load(f)

with open(TRANSACTIONS_FILE, 'r', encoding='utf-8') as f:
    transactions = json.load(f)

individuals_json = json.dumps(individuals, ensure_ascii=False)
transactions_json = json.dumps(transactions, ensure_ascii=False)

# 1. เขียน TARGET_FOCUS_SELECTOR.html (ส่ง query string เสมอ)
selector_html = f'''<!DOCTYPE html>
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
    
    .container {{
      max-width: 1400px;
      margin: 20px auto 60px;
      padding: 0 25px;
    }}
    .cards-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(310px, 1fr));
      gap: 14px;
    }}
    
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
      const idList = Array.from(selectedIds);
      localStorage.setItem('SELECTED_FOCUS_TARGETS', JSON.stringify(idList));
      window.location.href = 'BENEFICIARY_NETWORK_DASHBOARD.html?targets=' + encodeURIComponent(idList.join(','));
    }}

    renderCards();
  </script>
</body>
</html>
'''

# 2. เขียน BENEFICIARY_NETWORK_DASHBOARD.html (กรองแสดงเฉพาะเป้าหมายที่เลือก 100% ไม่ปนคนอื่น)
dashboard_html = f'''<!DOCTYPE html>
<html lang="th">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>🕸️ สารบบบัญชีผู้รับโอนเงินและแผนผังเครือข่ายทางการเงิน (Strict Target Focus)</title>
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
    
    /* TOP HEADER */
    .top-header {{
      background: rgba(15, 23, 42, 0.95);
      border-bottom: 1px solid #1e293b;
      padding: 18px 30px;
      position: sticky;
      top: 0;
      z-index: 100;
      backdrop-filter: blur(12px);
    }}
    .header-flex {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 15px;
    }}
    .header-title {{
      font-size: 24px;
      font-weight: 800;
      color: #38bdf8;
      display: flex;
      align-items: center;
      gap: 12px;
    }}
    .header-sub {{
      font-size: 15px;
      color: #94a3b8;
      margin-top: 4px;
    }}
    
    .btn-back {{
      background: #1e293b;
      color: #38bdf8;
      border: 1px solid #0284c7;
      padding: 8px 16px;
      border-radius: 6px;
      font-size: 15px;
      font-weight: 700;
      cursor: pointer;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s;
    }}
    .btn-back:hover {{
      background: #0284c7;
      color: #ffffff;
    }}
    
    /* STATS SUMMARY */
    .stats-bar {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 14px;
      margin-top: 18px;
    }}
    .stat-card {{
      background: #0f172a;
      border: 1px solid #1e293b;
      border-radius: 8px;
      padding: 12px 18px;
    }}
    .stat-val {{
      font-size: 26px;
      font-weight: 800;
      color: #ffffff;
    }}
    .stat-lbl {{
      font-size: 13.5px;
      color: #94a3b8;
      margin-top: 2px;
    }}
    
    /* MAIN CONTAINER */
    .container {{
      max-width: 1400px;
      margin: 25px auto;
      padding: 0 25px;
    }}
    
    /* NETWORK GRAPH CONTAINER */
    .graph-card {{
      background: #0f172a;
      border: 1px solid #1e293b;
      border-radius: 10px;
      padding: 20px;
      margin-bottom: 25px;
    }}
    .card-title {{
      font-size: 19px;
      font-weight: 800;
      color: #38bdf8;
      margin-bottom: 15px;
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .graph-wrapper {{
      width: 100%;
      height: 380px;
      background: #050811;
      border: 1px solid #1e293b;
      border-radius: 8px;
      position: relative;
      overflow: hidden;
    }}
    
    /* BENEFICIARY TABLE */
    .table-card {{
      background: #0f172a;
      border: 1px solid #1e293b;
      border-radius: 10px;
      padding: 20px;
      margin-bottom: 30px;
    }}
    .custom-table {{
      width: 100%;
      border-collapse: collapse;
      margin-top: 15px;
      font-size: 15px;
    }}
    .custom-table th {{
      background: #1e293b;
      color: #94a3b8;
      padding: 12px 14px;
      text-align: left;
      font-weight: 700;
      border-bottom: 2px solid #334155;
    }}
    .custom-table td {{
      padding: 14px 14px;
      border-bottom: 1px solid #1e293b;
      vertical-align: middle;
    }}
    .custom-table tr:hover {{
      background: rgba(30, 41, 59, 0.5);
    }}
    
    .tag-badge {{
      display: inline-block;
      padding: 3px 8px;
      border-radius: 4px;
      font-size: 13px;
      font-weight: 700;
    }}
    
    .btn-view {{
      background: #0284c7;
      color: #ffffff;
      border: none;
      padding: 6px 12px;
      border-radius: 5px;
      font-size: 14px;
      font-weight: 700;
      cursor: pointer;
      transition: background 0.2s;
    }}
    .btn-view:hover {{
      background: #0369a1;
    }}
    
    /* MODAL FOR TRANSACTIONS */
    .modal {{
      display: none;
      position: fixed;
      top: 0; left: 0; width: 100%; height: 100%;
      background: rgba(0, 0, 0, 0.85);
      backdrop-filter: blur(6px);
      z-index: 1000;
      align-items: center;
      justify-content: center;
    }}
    .modal.open {{
      display: flex;
    }}
    .modal-box {{
      background: #0f172a;
      border: 1px solid #334155;
      border-radius: 12px;
      width: 90%;
      max-width: 1000px;
      max-height: 85vh;
      overflow-y: auto;
      padding: 24px;
      position: relative;
    }}
    .modal-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid #1e293b;
      padding-bottom: 14px;
      margin-bottom: 18px;
    }}
    .modal-close {{
      font-size: 28px;
      color: #94a3b8;
      cursor: pointer;
    }}
    .modal-close:hover {{ color: #ffffff; }}
    
    .tx-item {{
      background: #090d16;
      border: 1px solid #1e293b;
      border-radius: 8px;
      padding: 14px;
      margin-bottom: 14px;
      display: grid;
      grid-template-columns: 2fr 1fr;
      gap: 15px;
    }}
    .tx-field strong {{ color: #94a3b8; }}
  </style>
</head>
<body>
  <div class="top-header">
    <div class="header-flex">
      <div>
        <div class="header-title">
          <span>🕸️ สารบบบัญชีผู้รับโอนเงินและแผนผังเครือข่ายทางการเงิน (Strict Target Focus)</span>
        </div>
        <div class="header-sub">
          แสดงข้อมูลเฉพาะเป้าหมายที่ท่านเลือกโฟกัส • กรองคนอื่นออก 100% • สกัดสลิปจริงครบ ๖ ช่องข้อมูล
        </div>
      </div>
      
      <a href="TARGET_FOCUS_SELECTOR.html" class="btn-back">
        <span>⬅️ กลับไปหน้าเลือกเป้าหมาย (Change Target Selection)</span>
      </a>
    </div>
    
    <div class="stats-bar">
      <div class="stat-card">
        <div class="stat-val" style="color: #38bdf8;" id="selectedTargetCount">0 คน</div>
        <div class="stat-lbl">🎯 เป้าหมายที่ท่านเลือกโฟกัส</div>
      </div>
      <div class="stat-card">
        <div class="stat-val" style="color: #f43f5e;" id="selectedCoreLoss">0.00 บาท</div>
        <div class="stat-lbl">⚖️ ยอดเงินความเสียหายสุทธิของเป้าหมาย</div>
      </div>
      <div class="stat-card">
        <div class="stat-val" id="totalSlipsCount">0</div>
        <div class="stat-lbl">🧾 จำนวนสลิปที่เกี่ยวข้อง</div>
      </div>
      <div class="stat-card">
        <div class="stat-val" style="color: #22c55e;" id="totalAccountsCount">0 บัญชี</div>
        <div class="stat-lbl">🏦 จำนวนบัญชี/พร้อมเพย์ที่ตรวจพบ</div>
      </div>
    </div>
  </div>

  <div class="container">
    <!-- DYNAMIC NETWORK GRAPH -->
    <div class="graph-card">
      <div class="card-title">
        <span>🌐 แผนผังเครือข่ายทางการเงินเฉพาะเป้าหมายที่เลือก (Dynamic Target Graph)</span>
      </div>
      <div class="graph-wrapper" id="networkGraphSvg">
        <!-- SVG Injected Dynamically by JS -->
      </div>
    </div>

    <!-- BENEFICIARY TABLE (FILTERED STRICTLY) -->
    <div class="table-card">
      <div class="card-title">
        <span>📋 สารบบบัญชีและรายการสลิปของเป้าหมายที่เลือก (เจาะลึก ๖ ช่องข้อมูล)</span>
      </div>
      
      <table class="custom-table" id="recipientsTable">
        <thead>
          <tr>
            <th>ลำดับ</th>
            <th>ชื่อ - นามสกุล (เป้าหมายที่เลือก)</th>
            <th>ธนาคาร & เลขที่บัญชี</th>
            <th>ยอดเงินรวม</th>
            <th>จำนวนสลิป</th>
            <th>สถานะ</th>
            <th>ตรวจสอบ ๖ ช่องข้อมูล</th>
          </tr>
        </thead>
        <tbody id="tableBody">
          <!-- Populated Strictly by JS -->
        </tbody>
      </table>
    </div>
  </div>

  <!-- TRANSACTION DETAIL MODAL -->
  <div id="txModal" class="modal" onclick="closeModal(event)">
    <div class="modal-box" onclick="event.stopPropagation()">
      <div class="modal-header">
        <h3 id="modalRecipientTitle" style="color: #38bdf8; font-size: 20px;">รายการสลิปและ ๖ ช่องข้อมูล</h3>
        <span class="modal-close" onclick="closeModal(event)">&times;</span>
      </div>
      <div id="modalTxList"></div>
    </div>
  </div>

  <script>
    const allIndividuals = {individuals_json};
    const allTransactions = {transactions_json};
    
    // ดึงเป้าหมายที่ผู้ใช้เลือกจาก URL Query หรือ localStorage
    const urlParams = new URLSearchParams(window.location.search);
    const targetParam = urlParams.get('targets');
    let selectedTargetIds = [];
    
    if (targetParam) {{
      selectedTargetIds = targetParam.split(',').map(s => s.trim()).filter(Boolean);
    }} else {{
      const saved = localStorage.getItem('SELECTED_FOCUS_TARGETS');
      if (saved) {{
        try {{
          selectedTargetIds = JSON.parse(saved);
        }} catch(e) {{}}
      }}
    }}
    
    // กรองเข้มงวด 100%: เอาเฉพาะคนที่ตรงกับ ID ที่เลือกเท่านั้น!
    const focusedTargets = allIndividuals.filter(ind => selectedTargetIds.includes(ind.id));
    
    // ถ้าผู้ใช้เลือกชื่อ จิณห์นิภา ให้ดึงรายการสลิปที่เกี่ยวข้องกับ จิณห์นิภา ทั้งหมด
    function matchTransactionsForTarget(target) {{
      const name = target.name.toLowerCase();
      const accounts = (target.accounts || []).map(a => a.toLowerCase());
      
      return allTransactions.filter(t => {{
        const rName = (t.recipient || '').toLowerCase();
        const rAcc = (t.target_account || '').toLowerCase();
        const snip = (t.full_snippet || '').toLowerCase();
        
        // ถ้าเป็นจิณห์นิภา
        if (name.includes('จิณห์นิภา')) {{
          return rName.includes('จิณห์นิภา') || 
                 rAcc.includes('385-0') || rAcc.includes('996-5') || rAcc.includes('764-0') || 
                 rAcc.includes('313-5') || rAcc.includes('0880906599') ||
                 snip.includes('385-0') || snip.includes('996-5') || snip.includes('764-0') || snip.includes('313-5');
        }}
        // ถ้าเป็นคนอื่น จับคู่ตามชื่อหรือบัญชี
        if (rName.includes(name) || (name.includes('ปรียชาติ') && (rName.includes('ปรียชาติ') || rName.includes('พี่แมว')))) {{
          return true;
        }}
        return accounts.some(acc => rAcc.includes(acc) || snip.includes(acc));
      }});
    }}

    function renderDashboard() {{
      if (focusedTargets.length === 0) {{
        document.getElementById('tableBody').innerHTML = `
          <tr>
            <td colspan="7" style="text-align:center; padding: 40px; color: #94a3b8;">
              ⚠️ ยังไม่ได้เลือกเป้าหมาย กรุณากดปุ่ม <strong>"กลับไปหน้าเลือกเป้าหมาย"</strong> เพื่อเลือกบุคคลที่ต้องการตรวจสอบครับ
            </td>
          </tr>
        `;
        document.getElementById('networkGraphSvg').innerHTML = `
          <div style="display:flex; align-items:center; justify-content:center; height:100%; color:#94a3b8;">
            ยังไม่มีเป้าหมายที่เลือก
          </div>
        `;
        return;
      }}

      // อัปเดตตาราง: กรองเฉพาะเป้าหมายที่เลือกเท่านั้น!
      const tbody = document.getElementById('tableBody');
      tbody.innerHTML = '';
      
      let grandTotalAmt = 0;
      let grandSlipCount = 0;
      let grandAccountsCount = 0;

      focusedTargets.forEach((target, idx) => {{
        const targetTxs = matchTransactionsForTarget(target);
        const slipCount = targetTxs.length > 0 ? targetTxs.length : target.slips_count;
        
        let targetAmt = 0;
        if (targetTxs.length > 0) {{
          targetTxs.forEach(t => {{
            const val = parseFloat((t.amount || '0').replace(/,/g, ''));
            if (!isNaN(val)) targetAmt += val;
          }});
        }} else {{
          targetAmt = target.total_amount;
        }}

        grandTotalAmt += targetAmt;
        grandSlipCount += slipCount;
        grandAccountsCount += (target.accounts || []).length;

        const accStr = (target.accounts || []).length > 0 ? target.accounts.join('<br>') : 'ตรวจพบในข้อความแชท';

        const tr = document.createElement('tr');
        tr.innerHTML = `
          <td><strong>#${{idx + 1}}</strong></td>
          <td><strong style="color: #f8fafc; font-size: 17px;">${{target.name}}</strong></td>
          <td style="color: #cbd5e1; font-family: monospace; font-size: 13.5px;">${{accStr}}</td>
          <td><strong style="color: #22c55e; font-size: 17px;">${{targetAmt.toLocaleString('th-TH', {{minimumFractionDigits: 2}})}} บาท</strong></td>
          <td><span class="tag-badge" style="background:#0284c7; color:#ffffff;">${{slipCount}} รายการ</span></td>
          <td><span class="tag-badge" style="background:#7f1d1d; color:#fca5a5; border:1px solid #ef4444;">🎯 เป้าหมายที่โฟกัส</span></td>
          <td>
            <button class="btn-view" onclick="openTxModal('${{target.id}}')">🔍 ดูสลิป & ๖ ช่องข้อมูล (${{slipCount}})</button>
          </td>
        `;
        tbody.appendChild(tr);
      }});

      // อัปเดต KPI ตัวเลขด้านบน
      document.getElementById('selectedTargetCount').innerText = focusedTargets.length + ' คน (' + focusedTargets.map(t => t.name.split(' ')[1] || t.name).join(', ') + ')';
      document.getElementById('selectedCoreLoss').innerText = grandTotalAmt.toLocaleString('th-TH', {{minimumFractionDigits: 2, maximumFractionDigits: 2}}) + ' บาท';
      document.getElementById('totalSlipsCount').innerText = grandSlipCount + ' สลิป';
      document.getElementById('totalAccountsCount').innerText = grandAccountsCount + ' บัญชี/พร้อมเพย์';

      // สร้างแผนผังเครือข่าย SVG แบบ Dynamic เฉพาะเป้าหมายที่เลือก
      renderDynamicSvg(focusedTargets, grandTotalAmt);
    }}

    function renderDynamicSvg(targets, totalAmt) {{
      const svgContainer = document.getElementById('networkGraphSvg');
      
      let svgHtml = `
        <svg width="100%" height="100%" viewBox="0 0 1000 360" preserveAspectRatio="xMidYMid meet">
          <!-- ผู้เสียหาย (Source) -->
          <circle cx="160" cy="180" r="45" fill="#1e3a8a" stroke="#38bdf8" stroke-width="3"/>
          <text x="160" y="176" fill="#ffffff" font-size="15" font-weight="800" text-anchor="middle">ผู้เสียหาย</text>
          <text x="160" y="196" fill="#93c5fd" font-size="13" font-weight="600" text-anchor="middle">ณัฐชัย รักษาวงศ์</text>
      `;

      const targetCount = targets.length;
      const startY = 90;
      const stepY = targetCount > 1 ? (200 / (targetCount - 1)) : 0;

      targets.forEach((t, i) => {{
        const targetY = targetCount === 1 ? 180 : (startY + i * stepY);
        const tName = t.name.split(' ')[0] + ' ' + (t.name.split(' ')[1] || '');

        svgHtml += `
          <!-- เส้นเชื่อมโยงไปยังเป้าหมายที่เลือก -->
          <line x1="205" y1="180" x2="520" y2="${{targetY}}" stroke="#f43f5e" stroke-width="4" stroke-dasharray="4"/>
          <text x="350" y="${{targetY - 10}}" fill="#fca5a5" font-size="13" font-weight="700">
            โอนเข้า: ${{t.total_amount.toLocaleString('th-TH')}} บ. (${{t.slips_count}} สลิป)
          </text>

          <!-- Node เป้าหมายที่เลือก -->
          <circle cx="560" cy="${{targetY}}" r="38" fill="#7f1d1d" stroke="#f43f5e" stroke-width="3"/>
          <text x="560" y="${{targetY - 6}}" fill="#ffffff" font-size="14" font-weight="800" text-anchor="middle">🎯 เป้าหมายที่เลือก</text>
          <text x="560" y="${{targetY + 12}}" fill="#fca5a5" font-size="12" font-weight="600" text-anchor="middle">${{tName}}</text>
        `;

        // บัญชีปลายทางของเป้าหมาย
        const accs = t.accounts || [];
        if (accs.length > 0) {{
          const accStep = 180 / Math.max(accs.length - 1, 1);
          accs.forEach((acc, aIdx) => {{
            const accY = accs.length === 1 ? targetY : (90 + aIdx * accStep);
            svgHtml += `
              <line x1="598" y1="${{targetY}}" x2="780" y2="${{accY}}" stroke="#334155" stroke-width="1.5"/>
              <rect x="780" y="${{accY - 14}}" width="190" height="28" rx="5" fill="#0f172a" stroke="#0284c7" stroke-width="1.5"/>
              <text x="790" y="${{accY + 4}}" fill="#e2e8f0" font-family="monospace" font-size="12" font-weight="600">${{acc}}</text>
            `;
          }});
        }}
      }});

      svgHtml += '</svg>';
      svgContainer.innerHTML = svgHtml;
    }}

    function openTxModal(targetId) {{
      const target = allIndividuals.find(t => t.id === targetId);
      if (!target) return;
      
      const targetTxs = matchTransactionsForTarget(target);
      document.getElementById('modalRecipientTitle').innerText = 'รายการสลิปและ ๖ ช่องข้อมูลของ: ' + target.name + ' (' + targetTxs.length + ' รายการ)';
      const listEl = document.getElementById('modalTxList');
      listEl.innerHTML = '';

      if (targetTxs.length === 0) {{
        listEl.innerHTML = '<div style="color:#94a3b8; text-align:center; padding:20px;">ตรวจพบการกล่าวถึงในบทสนทนาแชท (ไม่มีภาพสลิปแนบโดยตรง)</div>';
      }} else {{
        targetTxs.forEach((tx, idx) => {{
          const div = document.createElement('div');
          div.className = 'tx-item';
          div.innerHTML = `
            <div>
              <div style="font-size: 16px; font-weight: 700; color: #38bdf8; margin-bottom: 6px;">
                #${{idx + 1}}: สลิปไฟล์ <code>${{tx.file}}</code>
              </div>
              <div class="tx-field"><strong>๑. ชื่อผู้รับโอน:</strong> ${{tx.recipient}}</div>
              <div class="tx-field"><strong>๒. จำนวนเงิน:</strong> <span style="color: #22c55e; font-weight: 700;">${{tx.amount}} บาท</span></div>
              <div class="tx-field"><strong>๓. รหัสอ้างอิง:</strong> <code>${{tx.ref_no}}</code></div>
              <div class="tx-field"><strong>๔. ธนาคาร & บัญชี:</strong> ${{tx.bank}}</div>
              <div class="tx-field"><strong>๕. วันที่ และ เวลา:</strong> ${{tx.datetime}}</div>
              <div class="tx-field"><strong>๖. บันทึกความจำ (MEMO):</strong> ${{tx.memo}}</div>
            </div>
            <div style="text-align: right;">
              <a href="file:///${{tx.path.replace(/\\\\/g, '/')}}" target="_blank" class="btn-view" style="text-decoration:none; display:inline-block; margin-top:10px;">🖼️ เปิดภาพต้นฉบับ</a>
            </div>
          `;
          listEl.appendChild(div);
        }});
      }}

      document.getElementById('txModal').classList.add('open');
    }}

    function closeModal(e) {{
      document.getElementById('txModal').classList.remove('open');
    }}

    renderDashboard();
  </script>
</body>
</html>
'''

with open(SELECTOR_FILE, 'w', encoding='utf-8') as f:
    f.write(selector_html)

with open(DASHBOARD_FILE, 'w', encoding='utf-8') as f:
    f.write(dashboard_html)

print("Generated STRICT TARGET FOCUS Suite successfully!")

# -*- coding: utf-8 -*-
"""
Script: build_strict_focus_solution.py
Purpose:
1. Generate TARGET_FOCUS_SELECTOR.html with Image 2 KPI design (Clean, compact, no long account badges in UI, kept in data for search).
2. Generate BENEFICIARY_NETWORK_DASHBOARD.html with 100% strict dynamic filtering:
   - Eliminates all unselected entities (zero Preeyachat, zero others when focusing on Jinnipha).
   - Generates Dynamic SVG Network Graph: Victim -> Focused Target -> Focused Target's Accounts/Banks.
   - Generates Table 1: Target Destination Accounts Breakdown.
   - Generates Table 2: Complete 6-Field Forensic Transaction Ledger for the focused target.
   - Modal to inspect individual slips and the 6 extracted forensic fields.
3. Automatically sync files to both d:\Project\ชวกม.2\EDOK_NUI and the artifact directory.
"""

import os
import json
import shutil

WORKSPACE_DIR = r'd:\Project\ชวกม.2\EDOK_NUI'
ARTIFACT_DIR = r'C:\Users\EVE\.gemini\antigravity\brain\c8211d09-030e-4b24-8837-3ce9589aa4a6'

INDIVIDUALS_FILE = os.path.join(WORKSPACE_DIR, 'ALL_DISCOVERED_INDIVIDUALS.json')
TRANSACTIONS_FILE = os.path.join(WORKSPACE_DIR, 'BENEFICIARY_TRANSACTION_RECORDS.json')

with open(INDIVIDUALS_FILE, 'r', encoding='utf-8') as f:
    individuals = json.load(f)

with open(TRANSACTIONS_FILE, 'r', encoding='utf-8') as f:
    transactions = json.load(f)

individuals_json = json.dumps(individuals, ensure_ascii=False)
transactions_json = json.dumps(transactions, ensure_ascii=False)

# -------------------------------------------------------------
# 1. BUILD TARGET_FOCUS_SELECTOR.html
# -------------------------------------------------------------
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
      background: #0f172a;
      border: 1px solid #334155;
      color: #f8fafc;
      padding: 10px 18px;
      border-radius: 8px;
      font-size: 16px;
      width: 380px;
      max-width: 100%;
      outline: none;
    }}
    .search-box:focus {{
      border-color: #38bdf8;
      box-shadow: 0 0 0 2px rgba(56, 189, 248, 0.2);
    }}
    
    .sort-btn {{
      background: #1e293b;
      color: #94a3b8;
      border: 1px solid #334155;
      padding: 6px 14px;
      border-radius: 6px;
      cursor: pointer;
      font-size: 14px;
      font-weight: 600;
      transition: all 0.15s;
    }}
    .sort-btn.active {{
      background: #0284c7;
      color: #ffffff;
      border-color: #38bdf8;
    }}
    
    .container {{
      max-width: 1400px;
      margin: 25px auto;
      padding: 0 25px;
    }}
    
    .info-banner {{
      background: rgba(14, 165, 233, 0.08);
      border: 1px solid rgba(56, 189, 248, 0.25);
      border-radius: 8px;
      padding: 12px 20px;
      margin-bottom: 25px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 10px;
    }}
    
    /* CARDS GRID */
    .cards-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
      gap: 20px;
    }}
    
    /* INDIVIDUAL CARD (IMAGE 2 STANDARD) */
    .target-card {{
      background: #0b1329;
      border: 1.5px solid #1e293b;
      border-radius: 12px;
      padding: 18px 20px;
      cursor: pointer;
      transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
      position: relative;
      display: flex;
      flex-direction: column;
      gap: 14px;
    }}
    .target-card:hover {{
      border-color: #38bdf8;
      transform: translateY(-2px);
      box-shadow: 0 6px 20px rgba(0, 0, 0, 0.4);
    }}
    .target-card.selected {{
      border-color: #38bdf8;
      background: #0e1a38;
      box-shadow: 0 0 0 2px rgba(56, 189, 248, 0.3), 0 8px 24px rgba(2, 132, 199, 0.2);
    }}
    
    .card-head {{
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      gap: 12px;
    }}
    .card-name {{
      font-size: 20px;
      font-weight: 800;
      color: #ffffff;
      line-height: 1.3;
    }}
    
    .custom-checkbox {{
      width: 22px;
      height: 22px;
      min-width: 22px;
      border-radius: 4px;
      border: 2px solid #64748b;
      background: #0f172a;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: all 0.2s;
    }}
    .target-card.selected .custom-checkbox {{
      background: #0284c7;
      border-color: #38bdf8;
    }}
    .custom-checkbox::after {{
      content: '✔';
      color: #ffffff;
      font-size: 14px;
      font-weight: 900;
      display: none;
    }}
    .target-card.selected .custom-checkbox::after {{
      display: block;
    }}
    
    /* KPI INNER BOX */
    .kpi-box {{
      background: #060b18;
      border: 1px solid #162036;
      border-radius: 8px;
      padding: 12px 16px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .kpi-label {{
      font-size: 14px;
      color: #94a3b8;
    }}
    .kpi-amount {{
      font-size: 20px;
      font-weight: 800;
      color: #22c55e;
      margin-top: 2px;
    }}
    .kpi-slips {{
      font-size: 20px;
      font-weight: 800;
      color: #38bdf8;
      margin-top: 2px;
      text-align: right;
    }}
    
    .footer-bar {{
      position: sticky;
      bottom: 0;
      background: rgba(15, 23, 42, 0.95);
      border-top: 1px solid #1e293b;
      padding: 16px 30px;
      backdrop-filter: blur(12px);
      display: flex;
      justify-content: space-between;
      align-items: center;
      z-index: 90;
    }}
  </style>
</head>
<body>

  <div class="top-bar">
    <div>
      <div class="bar-title">
        <span>🎯 ประตูกรองและเลือกโฟกัสเป้าหมายแห่งคดี</span>
        <span style="font-size: 14px; background: #0284c7; color: #ffffff; padding: 2px 10px; border-radius: 12px; font-weight: normal;">Target Focus Selector</span>
      </div>
      <div class="bar-sub">ระบบตรวจพบผู้รับโอนและตัวละครทั้งหมด {len(individuals)} รายการ — กรุณาเลือกบุคคลที่ต้องการเจาะลึกเพื่อเปิดแดชบอร์ดเครือข่าย</div>
    </div>
    <div>
      <button class="btn-proceed" onclick="proceedToDashboard()">
        <span>🚀 ยืนยันเป้าหมายและเปิดแดชบอร์ด</span>
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
    <div class="info-banner">
      <div>
        <strong style="color: #38bdf8;">💡 คำแนะนำการใช้งาน:</strong>
        <span style="color: #cbd5e1; margin-left: 5px;">คลิกที่การ์ดเพื่อเลือกบุคคลที่ต้องการตรวจสอบ (สามารถเลือก 1 คนหรือหลายคนได้) ข้อมูลเลขที่บัญชีจะถูกเก็บทำงานเบื้องหลัง</span>
      </div>
      <div>
        <span style="color: #94a3b8;">เลือกแล้ว:</span>
        <strong id="selectedCountText" style="color: #38bdf8; font-size: 18px; margin: 0 4px;">0</strong>
        <span style="color: #94a3b8;">คน | ยอดเงินรวม:</span>
        <strong id="selectedSumText" style="color: #22c55e; font-size: 18px; margin-left: 4px;">0.00 บาท</strong>
      </div>
    </div>

    <div class="cards-grid" id="cardsGrid"></div>
  </div>

  <div class="footer-bar">
    <div>
      <span style="color: #94a3b8; font-size: 14.5px;">ระบบโฟกัสเฉพาะบุคคล มาตรฐานศาลยุติธรรม (ป.วิ.อ. ๒๒๖ & ISO/IEC 27037)</span>
    </div>
    <div>
      <button class="btn-proceed" onclick="proceedToDashboard()">
        <span>🚀 ยืนยันเป้าหมายและเปิดแดชบอร์ด</span>
      </button>
    </div>
  </div>

  <script>
    const allIndividuals = {individuals_json};
    let selectedIds = new Set();
    let currentSort = 'amount';
    let searchQuery = '';

    // อ่านค่าที่เคยเลือกไว้ ถ้ามี
    const savedSelected = localStorage.getItem('SELECTED_FOCUS_TARGETS');
    if (savedSelected) {{
      try {{
        const arr = JSON.parse(savedSelected);
        arr.forEach(id => selectedIds.add(id));
      }} catch(e) {{}}
    }}
    // ค่าเริ่มต้นถ้ายังไม่มี ให้เลือกจิณห์นิภา ประสาทเขตรการ
    if (selectedIds.size === 0) {{
      const jin = allIndividuals.find(x => x.name.includes('จิณห์นิภา'));
      if (jin) selectedIds.add(jin.id);
    }}

    function renderCards() {{
      const grid = document.getElementById('cardsGrid');
      grid.innerHTML = '';

      let filtered = allIndividuals.filter(item => {{
        if (!searchQuery) return true;
        const q = searchQuery.toLowerCase();
        const matchName = item.name.toLowerCase().includes(q);
        const matchAcc = (item.accounts || []).some(acc => acc.toLowerCase().includes(q));
        const matchBank = (item.banks || []).some(b => b.toLowerCase().includes(q));
        return matchName || matchAcc || matchBank;
      }});

      filtered.sort((a, b) => {{
        if (currentSort === 'amount') return b.total_amount - a.total_amount;
        if (currentSort === 'count') return b.slips_count - a.slips_count;
        if (currentSort === 'name') return a.name.localeCompare(b.name, 'th');
        return 0;
      }});

      filtered.forEach(item => {{
        const isSelected = selectedIds.has(item.id);
        const card = document.createElement('div');
        card.className = 'target-card' + (isSelected ? ' selected' : '');
        card.onclick = () => toggleSelect(item.id);

        card.innerHTML = `
          <div class="card-head">
            <div class="card-name">${{item.name}}</div>
            <div class="custom-checkbox"></div>
          </div>
          
          <div class="kpi-box">
            <div>
              <div class="kpi-label">ยอดเงิน:</div>
              <div class="kpi-amount">${{item.total_amount_formatted}}</div>
            </div>
            <div>
              <div class="kpi-label" style="text-align: right;">สลิป/หลักฐาน:</div>
              <div class="kpi-slips">${{item.slips_count}} รายการ</div>
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
      renderCards();
    }}

    function selectAll(flag) {{
      if (flag) {{
        allIndividuals.forEach(e => selectedIds.add(e.id));
      }} else {{
        selectedIds.clear();
      }}
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

# -------------------------------------------------------------
# 2. BUILD BENEFICIARY_NETWORK_DASHBOARD.html
# -------------------------------------------------------------
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
      padding: 16px 30px;
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
    
    .btn-action {{
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
    .btn-action:hover {{
      background: #0284c7;
      color: #ffffff;
    }}
    
    /* STATS SUMMARY */
    .stats-bar {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 14px;
      margin-top: 16px;
    }}
    .stat-card {{
      background: #0f172a;
      border: 1px solid #1e293b;
      border-radius: 8px;
      padding: 14px 18px;
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
      max-width: 1440px;
      margin: 25px auto;
      padding: 0 25px;
      display: flex;
      flex-direction: column;
      gap: 25px;
    }}
    
    /* SECTION CARD */
    .section-card {{
      background: #0f172a;
      border: 1px solid #1e293b;
      border-radius: 10px;
      padding: 22px;
    }}
    .section-head {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 16px;
      padding-bottom: 12px;
      border-bottom: 1px solid #1e293b;
      flex-wrap: wrap;
      gap: 10px;
    }}
    .section-title {{
      font-size: 20px;
      font-weight: 800;
      color: #38bdf8;
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    
    /* SVG GRAPH */
    .graph-svg-container {{
      width: 100%;
      height: 380px;
      background: #080d1a;
      border-radius: 8px;
      border: 1px solid #162036;
      overflow: hidden;
      display: flex;
      align-items: center;
      justify-content: center;
    }}
    
    /* DATA TABLES */
    .table-container {{
      overflow-x: auto;
    }}
    table {{
      width: 100%;
      border-collapse: collapse;
      text-align: left;
    }}
    th {{
      background: #1e293b;
      color: #94a3b8;
      padding: 12px 14px;
      font-size: 14.5px;
      font-weight: 700;
      border-bottom: 2px solid #334155;
      white-space: nowrap;
    }}
    td {{
      padding: 12px 14px;
      border-bottom: 1px solid #1e293b;
      font-size: 15px;
      color: #cbd5e1;
      vertical-align: middle;
    }}
    tr:hover td {{
      background: rgba(30, 41, 59, 0.4);
    }}
    
    .tag-badge {{
      display: inline-block;
      padding: 3px 8px;
      border-radius: 4px;
      font-size: 12.5px;
      font-weight: 700;
      white-space: nowrap;
    }}
    
    .btn-view {{
      background: #0284c7;
      color: #ffffff;
      border: none;
      padding: 6px 12px;
      border-radius: 4px;
      font-size: 13.5px;
      font-weight: 700;
      cursor: pointer;
      transition: background 0.2s;
    }}
    .btn-view:hover {{
      background: #0369a1;
    }}
    
    /* MODAL */
    .modal {{
      display: none;
      position: fixed;
      inset: 0;
      background: rgba(0, 0, 0, 0.85);
      z-index: 1000;
      padding: 20px;
      align-items: center;
      justify-content: center;
      backdrop-filter: blur(8px);
    }}
    .modal.open {{
      display: flex;
    }}
    .modal-box {{
      background: #0f172a;
      border: 1px solid #38bdf8;
      border-radius: 12px;
      width: 1000px;
      max-width: 95vw;
      max-height: 90vh;
      display: flex;
      flex-direction: column;
      overflow: hidden;
      box-shadow: 0 10px 40px rgba(0, 0, 0, 0.8);
    }}
    .modal-header {{
      padding: 16px 22px;
      background: #1e293b;
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid #334155;
    }}
    .modal-close {{
      color: #94a3b8;
      font-size: 24px;
      font-weight: 800;
      cursor: pointer;
    }}
    .modal-close:hover {{
      color: #ffffff;
    }}
    .modal-body {{
      padding: 20px;
      overflow-y: auto;
      display: flex;
      flex-direction: column;
      gap: 16px;
    }}
    .tx-item {{
      background: #090d16;
      border: 1px solid #1e293b;
      border-radius: 8px;
      padding: 14px 18px;
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      gap: 15px;
      flex-wrap: wrap;
    }}
    .tx-field {{
      font-size: 14.5px;
      color: #cbd5e1;
      margin-top: 4px;
    }}
  </style>
</head>
<body>

  <!-- TOP HEADER -->
  <header class="top-header">
    <div class="header-flex">
      <div>
        <div class="header-title">
          <span>🕸️ สารบบบัญชีผู้รับโอนเงินและแผนผังเครือข่ายทางการเงิน</span>
          <span style="font-size: 13.5px; background: #7f1d1d; color: #fca5a5; border: 1px solid #ef4444; padding: 2px 10px; border-radius: 12px; font-weight: normal;">
            Strict Target Focus Mode
          </span>
        </div>
        <div class="header-sub">
          วิเคราะห์เจาะลึกเฉพาะเป้าหมายที่เลือก — สกัดเส้นทางการเงิน ๖ ช่องข้อมูล ปลอดข้อมูลบุคคลอื่น ๑๐๐%
        </div>
      </div>
      <div style="display: flex; gap: 10px;">
        <a href="TARGET_FOCUS_SELECTOR.html" class="btn-action">
          <span>⬅️ เปลี่ยนเป้าหมาย / เลือกบุคคลอื่น</span>
        </a>
      </div>
    </div>

    <!-- KPI STATS -->
    <div class="stats-bar">
      <div class="stat-card">
        <div class="stat-val" id="kpiTargetName" style="color: #38bdf8; font-size: 20px;">-</div>
        <div class="stat-lbl">🎯 บุคคลเป้าหมายที่โฟกัส</div>
      </div>
      <div class="stat-card">
        <div class="stat-val" id="kpiTotalLoss" style="color: #22c55e;">0.00 บาท</div>
        <div class="stat-lbl">💸 ยอดเงินโอนเข้าเป้าหมายสุทธิ</div>
      </div>
      <div class="stat-card">
        <div class="stat-val" id="kpiTotalSlips" style="color: #38bdf8;">0 สลิป</div>
        <div class="stat-lbl">🧾 จำนวนสลิปโอนเงินที่ตรวจพบ</div>
      </div>
      <div class="stat-card">
        <div class="stat-val" id="kpiTotalAccounts" style="color: #e2e8f0;">0 ช่องทาง</div>
        <div class="stat-lbl">🏦 บัญชีธนาคาร & พร้อมเพย์เป้าหมาย</div>
      </div>
    </div>
  </header>

  <main class="container">
    <!-- SECTION 1: INTERACTIVE SVG FRAUD GRAPH -->
    <section class="section-card">
      <div class="section-head">
        <div class="section-title">
          <span>🌐 แผนผังเครือข่ายความสัมพันธ์ทางการเงิน (Interactive Fraud Network Graph)</span>
        </div>
        <span style="font-size: 13.5px; color: #94a3b8;">
          แสดงเฉพาะความเชื่อมโยงระหว่างผู้เสียหาย ➔ เป้าหมายที่เลือก ➔ บัญชีปลายทางของเป้าหมาย
        </span>
      </div>
      <div class="graph-svg-container" id="networkGraphSvg"></div>
    </section>

    <!-- SECTION 2: TARGET DESTINATION ACCOUNTS BREAKDOWN -->
    <section class="section-card">
      <div class="section-head">
        <div class="section-title">
          <span>🏦 บัญชีธนาคารและช่องทางรับเงินเฉพาะของเป้าหมาย (Destination Accounts Matrix)</span>
        </div>
        <span id="accountCountLabel" style="font-size: 13.5px; color: #38bdf8;"></span>
      </div>
      <div class="table-container">
        <table>
          <thead>
            <tr>
              <th style="width: 60px;">ลำดับ</th>
              <th>ธนาคารผู้รับ</th>
              <th>เลขที่บัญชี / เบอร์พร้อมเพย์</th>
              <th style="text-align: right;">ยอดเงินโอนเข้าบัญชีนี้</th>
              <th style="text-align: center;">จำนวนสลิป</th>
              <th style="text-align: right;">สัดส่วน %</th>
              <th style="text-align: center;">สถานะบัญชี</th>
            </tr>
          </thead>
          <tbody id="accountsTableBody"></tbody>
        </table>
      </div>
    </section>

    <!-- SECTION 3: COMPLETE 6-FIELD FORENSIC TRANSACTION LEDGER -->
    <section class="section-card">
      <div class="section-head">
        <div class="section-title">
          <span>📋 สารบบสลิป ๖ ช่องข้อมูลเจาะลึกเฉพาะเป้าหมายที่เลือก (Complete Forensic Transaction Ledger)</span>
        </div>
        <div style="display: flex; gap: 10px; align-items: center;">
          <input type="text" id="txSearchBox" placeholder="🔍 กรองในสลิป (จำนวนเงิน, เลขอ้างอิง, วันที่, MEMO)..." oninput="filterTransactions()" style="background:#090d16; border:1px solid #334155; color:#f8fafc; padding:6px 12px; border-radius:6px; font-size:14px; width: 280px; outline:none;">
          <span id="txCountBadge" class="tag-badge" style="background:#0284c7; color:#ffffff; font-size:13.5px;"></span>
        </div>
      </div>
      <div class="table-container">
        <table>
          <thead>
            <tr>
              <th style="width: 50px;">ลำดับ</th>
              <th>๑. ชื่อ-นามสกุล (ผู้รับโอน)</th>
              <th style="text-align: right;">๒. จำนวนเงิน</th>
              <th>๓. รหัสอ้างอิง (Ref No.)</th>
              <th>๔. ธนาคาร & เลขบัญชีผู้รับ</th>
              <th>๕. วันที่ และ เวลา</th>
              <th>๖. บันทึกความจำ (MEMO)</th>
              <th style="text-align: center;">หลักฐานต้นฉบับ</th>
            </tr>
          </thead>
          <tbody id="transactionsTableBody"></tbody>
        </table>
      </div>
    </section>
  </main>

  <!-- MODAL FOR DETAIL INSPECTION -->
  <div id="detailModal" class="modal" onclick="closeModal(event)">
    <div class="modal-box" onclick="event.stopPropagation()">
      <div class="modal-header">
        <h3 id="modalTitle" style="color: #38bdf8; font-size: 19px;">รายละเอียดสลิปหลักฐาน</h3>
        <span class="modal-close" onclick="closeModal(event)">&times;</span>
      </div>
      <div class="modal-body" id="modalBody"></div>
    </div>
  </div>

  <script>
    const allIndividuals = {individuals_json};
    const allTransactions = {transactions_json};

    // 1. ดึงเป้าหมายที่เลือก (จาก URL Query หรือ localStorage)
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

    // ถ้าไม่มีการเลือก ให้ default ไปที่ น.ส. จิณห์นิภา ประสาทเขตรการ
    if (selectedTargetIds.length === 0) {{
      const jin = allIndividuals.find(x => x.name.includes('จิณห์นิภา'));
      if (jin) selectedTargetIds = [jin.id];
    }}

    // 2. กรองเข้มงวด 100%: เอาเฉพาะคนที่ตรงกับ ID ที่เลือกเท่านั้น! บุคคลอื่นถูกตัดทิ้งทั้งหมด
    const focusedTargets = allIndividuals.filter(ind => selectedTargetIds.includes(ind.id));

    // 3. ฟังก์ชันดึงเฉพาะรายการธุรกรรมของเป้าหมายที่เลือก (กรองเข้มงวด 100% ปลอดคนอื่น)
    function getTransactionsForTarget(target) {{
      const name = target.name.toLowerCase();
      const accounts = (target.accounts || []).map(a => a.toLowerCase());

      return allTransactions.filter(t => {{
        const rName = (t.recipient || '').toLowerCase();
        const rAcc = (t.target_account || '').toLowerCase();
        const snip = (t.full_snippet || '').toLowerCase();

        // ตัดข้อความบริบทที่ไม่มีสลิปทิ้งเสมอ
        if (rName.includes('ภาพสนทนา') || rName === '-' || !t.amount || t.amount === '-') return false;

        // ถ้าเป้าหมายคือ จิณห์นิภา (กรองเข้มงวด: ต้องเป็น จิณห์นิภา เท่านั้น ตัดคนอื่น เช่น ปรียชาติ, ณัฐชัย ออก 100%)
        if (name.includes('จิณห์นิภา')) {{
          if (rName.includes('ปรียชาติ') || rName.includes('ณัฐชัย') || rAcc.includes('455-1') || rAcc.includes('452-9')) return false;
          const isJName = rName.includes('จิณห์นิภา');
          const isJAcc = ['385-0', '996-5', '764-0', '313-5', '0880906599', '086-4483287'].some(x => rAcc.includes(x) || snip.includes(x));
          return isJName || isJAcc;
        }}

        // กรณีเป้าหมายบุคคลอื่น จับคู่ชื่อและบัญชีตรงตัว
        if (rName.includes(name)) return true;
        return accounts.length > 0 && accounts.some(acc => rAcc.includes(acc) || snip.includes(acc));
      }});
    }}

    // รวมรายการธุรกรรมทั้งหมดของเป้าหมายที่เลือก
    let currentFocusedTxs = [];
    focusedTargets.forEach(t => {{
      const txs = getTransactionsForTarget(t);
      currentFocusedTxs.push(...txs);
    }});

    // กำจัดสลิปซ้ำตาม ref_no
    const seenRef = new Set();
    const uniqueTxs = [];
    currentFocusedTxs.forEach(t => {{
      const ref = t.ref_no || t.file;
      if (!seenRef.has(ref)) {{
        seenRef.add(ref);
        uniqueTxs.push(t);
      }}
    }});
    currentFocusedTxs = uniqueTxs;

    function renderPage() {{
      if (focusedTargets.length === 0) {{
        alert('ไม่พบเป้าหมายที่เลือก กรุณากลับไปเลือกเป้าหมาย');
        window.location.href = 'TARGET_FOCUS_SELECTOR.html';
        return;
      }}

      // 1. คำนวณยอดเงินรวมและสถิติ
      let totalAmount = 0;
      currentFocusedTxs.forEach(t => {{
        const amtStr = (t.amount || '0').replace(/,/g, '').trim();
        const v = parseFloat(amtStr);
        if (!isNaN(v)) totalAmount += v;
      }});

      // 2. อัปเดต KPI ด้านบน
      const targetNames = focusedTargets.map(t => t.name).join(' + ');
      document.getElementById('kpiTargetName').innerText = targetNames;
      document.getElementById('kpiTotalLoss').innerText = totalAmount.toLocaleString('th-TH', {{minimumFractionDigits: 2, maximumFractionDigits: 2}}) + ' บาท';
      document.getElementById('kpiTotalSlips').innerText = currentFocusedTxs.length + ' รายการ';

      // 3. จัดกลุ่มบัญชีปลายทางของเป้าหมาย
      const accountMap = {{}};
      currentFocusedTxs.forEach(t => {{
        const b = t.bank || 'ไม่ระบุธนาคาร';
        const a = t.target_account || 'ไม่ระบุเลขที่บัญชี';
        const key = b + ' | ' + a;
        if (!accountMap[key]) {{
          accountMap[key] = {{ bank: b, account: a, count: 0, sum: 0 }};
        }}
        accountMap[key].count += 1;
        const v = parseFloat((t.amount || '0').replace(/,/g, ''));
        if (!isNaN(v)) accountMap[key].sum += v;
      }});

      const accountList = Object.values(accountMap).sort((a, b) => b.sum - a.sum);
      document.getElementById('kpiTotalAccounts').innerText = accountList.length + ' ช่องทาง';
      document.getElementById('accountCountLabel').innerText = 'ตรวจพบ ' + accountList.length + ' ช่องทางรับเงิน';

      // เรนเดอร์ตารางบัญชี
      const accTbody = document.getElementById('accountsTableBody');
      accTbody.innerHTML = '';
      accountList.forEach((acc, idx) => {{
        const pct = totalAmount > 0 ? ((acc.sum / totalAmount) * 100).toFixed(1) : 0;
        const tr = document.createElement('tr');
        tr.innerHTML = `
          <td><strong>#${{idx + 1}}</strong></td>
          <td><strong style="color: #f8fafc;">${{acc.bank}}</strong></td>
          <td><code style="color: #38bdf8; font-size: 14.5px;">${{acc.account}}</code></td>
          <td style="text-align: right;"><strong style="color: #22c55e; font-size: 16px;">${{acc.sum.toLocaleString('th-TH', {{minimumFractionDigits: 2}})}} บาท</strong></td>
          <td style="text-align: center;"><span class="tag-badge" style="background:#0284c7; color:#ffffff;">${{acc.count}} สลิป</span></td>
          <td style="text-align: right; color: #94a3b8;">${{pct}}%</td>
          <td style="text-align: center;"><span class="tag-badge" style="background:#7f1d1d; color:#fca5a5; border:1px solid #ef4444;">🎯 บัญชีเป้าหมาย</span></td>
        `;
        accTbody.appendChild(tr);
      }});

      // เรนเดอร์แผนผัง SVG Network Graph
      renderDynamicSvg(targetNames, totalAmount, currentFocusedTxs.length, accountList);

      // เรนเดอร์ตารางสลิป ๖ ช่องข้อมูล
      renderTransactionsTable(currentFocusedTxs);
    }}

    function renderDynamicSvg(targetName, totalAmt, totalSlips, accountList) {{
      const container = document.getElementById('networkGraphSvg');
      
      const width = 1100;
      const height = 360;
      const centerY = 180;

      let svg = `
        <svg width="100%" height="100%" viewBox="0 0 ${{width}} ${{height}}" preserveAspectRatio="xMidYMid meet">
          <!-- ผู้เสียหาย (Source Node) -->
          <circle cx="150" cy="${{centerY}}" r="48" fill="#1e3a8a" stroke="#38bdf8" stroke-width="3"/>
          <text x="150" y="${{centerY - 6}}" fill="#ffffff" font-size="15" font-weight="800" text-anchor="middle">ผู้เสียหาย</text>
          <text x="150" y="${{centerY + 16}}" fill="#93c5fd" font-size="13" font-weight="600" text-anchor="middle">ณัฐชัย รักษาวงศ์</text>

          <!-- เส้นเชื่อมโยงไปยังเป้าหมายที่เลือก -->
          <line x1="198" y1="${{centerY}}" x2="480" y2="${{centerY}}" stroke="#f43f5e" stroke-width="4" stroke-dasharray="6"/>
          <rect x="250" y="${{centerY - 32}}" width="180" height="26" rx="4" fill="#0f172a" stroke="#f43f5e" stroke-width="1.5"/>
          <text x="340" y="${{centerY - 15}}" fill="#fca5a5" font-size="12.5" font-weight="700" text-anchor="middle">
            โอนเข้า: ${{totalAmt.toLocaleString('th-TH')}} บ. (${{totalSlips}} สลิป)
          </text>

          <!-- Node เป้าหมายที่เลือก (Target Node) -->
          <circle cx="530" cy="${{centerY}}" r="50" fill="#7f1d1d" stroke="#f43f5e" stroke-width="3.5"/>
          <text x="530" y="${{centerY - 8}}" fill="#ffffff" font-size="14" font-weight="800" text-anchor="middle">🎯 เป้าหมายที่เลือก</text>
          <text x="530" y="${{centerY + 14}}" fill="#fca5a5" font-size="12" font-weight="600" text-anchor="middle">${{targetName.substring(0, 22)}}</text>
      `;

      // โหนดบัญชีปลายทางของเป้าหมาย (ขวามือ)
      const visibleAccs = accountList.slice(0, 5);
      const totalCount = visibleAccs.length;
      const startY = 70;
      const stepY = totalCount > 1 ? (220 / (totalCount - 1)) : 0;

      visibleAccs.forEach((acc, i) => {{
        const accY = totalCount === 1 ? centerY : (startY + i * stepY);
        const shortBank = acc.bank.replace('ธนาคาร', '').replace('พร้อมเพย์ (PromptPay)', 'พร้อมเพย์').substring(0, 16);

        svg += `
          <!-- เส้นเชื่อมเป้าหมาย -> บัญชีปลายทาง -->
          <line x1="580" y1="${{centerY}}" x2="750" y2="${{accY}}" stroke="#334155" stroke-width="2"/>
          
          <!-- โหนดบัญชี -->
          <rect x="750" y="${{accY - 18}}" width="320" height="36" rx="6" fill="#0b1329" stroke="#0284c7" stroke-width="1.5"/>
          <text x="765" y="${{accY - 1}}" fill="#f8fafc" font-size="13" font-weight="700">${{shortBank}}</text>
          <text x="765" y="${{accY + 13}}" fill="#38bdf8" font-family="monospace" font-size="11.5">${{acc.account}}</text>
          <text x="1055" y="${{accY + 5}}" fill="#22c55e" font-size="12.5" font-weight="700" text-anchor="end">${{acc.sum.toLocaleString('th-TH')}} บ. (${{acc.count}} สลิป)</text>
        `;
      }});

      svg += '</svg>';
      container.innerHTML = svg;
    }}

    function renderTransactionsTable(txList) {{
      const tbody = document.getElementById('transactionsTableBody');
      tbody.innerHTML = '';
      document.getElementById('txCountBadge').innerText = txList.length + ' รายการ';

      if (txList.length === 0) {{
        tbody.innerHTML = `
          <tr>
            <td colspan="8" style="text-align:center; padding: 30px; color: #94a3b8;">
              ไม่พบรายการธุรกรรมตามเงื่อนไขการค้นหา
            </td>
          </tr>
        `;
        return;
      }}

      txList.forEach((tx, idx) => {{
        const tr = document.createElement('tr');
        const cleanPath = (tx.path || '').replace(/\\\\/g, '/');
        
        tr.innerHTML = `
          <td><strong>#${{idx + 1}}</strong></td>
          <td><strong style="color: #f8fafc;">${{tx.recipient || '-'}}</strong></td>
          <td style="text-align: right;"><strong style="color: #22c55e; font-size: 15.5px;">${{tx.amount}} บาท</strong></td>
          <td><code style="color: #cbd5e1; font-size: 13px;">${{tx.ref_no || '-'}}</code></td>
          <td><span style="color: #38bdf8;">${{tx.bank || '-'}}</span></td>
          <td style="white-space: nowrap; color: #94a3b8; font-size: 13.5px;">${{tx.datetime || '-'}}</td>
          <td style="color: #e2e8f0; font-size: 13.5px;">${{tx.memo || '-'}}</td>
          <td style="text-align: center; white-space: nowrap;">
            <button class="btn-view" onclick="openDetailModal(${{idx}})">🔍 ขยาย ๖ ช่อง</button>
            ${{cleanPath ? `<a href="file:///${{cleanPath}}" target="_blank" class="btn-view" style="background:#1e293b; border:1px solid #334155; text-decoration:none; margin-left:4px;">🖼️ รูป</a>` : ''}}
          </td>
        `;
        tbody.appendChild(tr);
      }});
    }}

    function filterTransactions() {{
      const q = document.getElementById('txSearchBox').value.toLowerCase().trim();
      if (!q) {{
        renderTransactionsTable(currentFocusedTxs);
        return;
      }}
      const filtered = currentFocusedTxs.filter(t => {{
        return (t.recipient || '').toLowerCase().includes(q) ||
               (t.amount || '').toLowerCase().includes(q) ||
               (t.ref_no || '').toLowerCase().includes(q) ||
               (t.bank || '').toLowerCase().includes(q) ||
               (t.target_account || '').toLowerCase().includes(q) ||
               (t.datetime || '').toLowerCase().includes(q) ||
               (t.memo || '').toLowerCase().includes(q);
      }});
      renderTransactionsTable(filtered);
    }}

    function openDetailModal(index) {{
      const tx = currentFocusedTxs[index];
      if (!tx) return;

      const cleanPath = (tx.path || '').replace(/\\\\/g, '/');
      document.getElementById('modalTitle').innerText = 'รายละเอียดสลิป #' + (index + 1) + ': ' + (tx.file || '');
      
      document.getElementById('modalBody').innerHTML = `
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
          <div>
            <h4 style="color: #38bdf8; margin-bottom: 12px; font-size: 17px;">📌 ผลการถอดรหัส ๖ ช่องข้อมูล (Forensic OCR)</h4>
            <div class="tx-field"><strong>๑. ชื่อ-นามสกุล (ผู้รับโอน):</strong> <span style="color:#ffffff; font-size:16px;">${{tx.recipient}}</span></div>
            <div class="tx-field" style="margin-top:8px;"><strong>๒. จำนวนเงิน:</strong> <span style="color:#22c55e; font-size:20px; font-weight:800;">${{tx.amount}} บาท</span></div>
            <div class="tx-field" style="margin-top:8px;"><strong>๓. รหัสอ้างอิง:</strong> <code style="color:#38bdf8; font-size:15px;">${{tx.ref_no}}</code></div>
            <div class="tx-field" style="margin-top:8px;"><strong>๔. ธนาคาร & เลขบัญชี:</strong> <span style="color:#ffffff;">${{tx.bank}}</span></div>
            <div class="tx-field" style="margin-top:8px;"><strong>๕. วันที่ และ เวลา:</strong> <span style="color:#e2e8f0;">${{tx.datetime}}</span></div>
            <div class="tx-field" style="margin-top:8px;"><strong>๖. บันทึกความจำ (MEMO):</strong> <span style="color:#fbbf24;">${{tx.memo || '-'}}</span></div>
            
            <div style="margin-top: 20px; padding: 12px; background: #060b18; border-radius: 6px; border: 1px solid #1e293b;">
              <div style="font-size: 13px; color: #94a3b8;">ไฟล์หลักฐานต้นฉบับ:</div>
              <div style="font-size: 13.5px; color: #cbd5e1; word-break: break-all; margin-top: 4px;"><code>${{tx.path || tx.file}}</code></div>
            </div>
          </div>

          <div style="text-align: center; background: #060b18; border-radius: 8px; padding: 15px; border: 1px solid #1e293b; display: flex; flex-direction: column; align-items: center; justify-content: center;">
            <div style="color: #94a3b8; font-size: 14px; margin-bottom: 10px;">ภาพหลักฐานสลิปจริงแห่งคดี</div>
            ${{cleanPath ? `<img src="file:///${{cleanPath}}" style="max-width: 100%; max-height: 420px; border-radius: 6px; border: 1px solid #334155; object-fit: contain;">` : '<div style="color:#64748b;">ไม่มีภาพหลักฐานโดยตรง (ตรวจพบในข้อความแชท)</div>'}}
          </div>
        </div>
      `;

      document.getElementById('detailModal').classList.add('open');
    }}

    function closeModal(e) {{
      document.getElementById('detailModal').classList.remove('open');
    }}

    renderPage();
  </script>
</body>
</html>
'''

# -------------------------------------------------------------
# WRITE FILES IN WORKSPACE
# -------------------------------------------------------------
selector_dest = os.path.join(WORKSPACE_DIR, 'TARGET_FOCUS_SELECTOR.html')
dashboard_dest = os.path.join(WORKSPACE_DIR, 'BENEFICIARY_NETWORK_DASHBOARD.html')

with open(selector_dest, 'w', encoding='utf-8') as f:
    f.write(selector_html)

with open(dashboard_dest, 'w', encoding='utf-8') as f:
    f.write(dashboard_html)

print("Written selector to:", selector_dest)
print("Written dashboard to:", dashboard_dest)

# -------------------------------------------------------------
# SYNC FILES TO ARTIFACT DIRECTORY
# -------------------------------------------------------------
shutil.copy2(selector_dest, os.path.join(ARTIFACT_DIR, 'TARGET_FOCUS_SELECTOR.html'))
shutil.copy2(dashboard_dest, os.path.join(ARTIFACT_DIR, 'BENEFICIARY_NETWORK_DASHBOARD.html'))

print("Copied both files to artifact directory:", ARTIFACT_DIR)

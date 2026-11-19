# -*- coding: utf-8 -*-
"""
Script: build_beneficiary_dashboard.py
สร้างแดชบอร์ดสารบบผู้รับโอนเงินและแผนผังเครือข่ายทางการเงิน (Interactive Beneficiary Network Dashboard)
รองรับการเลือกและคัดกรองเป้าหมายโดยผู้ใช้งาน (Target Selection Matrix)
"""

import os
import json

RECIPIENTS_FILE = r'd:\Project\ชวกม.2\EDOK_NUI\BENEFICIARY_ALL_RECIPIENTS.json'
TRANSACTIONS_FILE = r'd:\Project\ชวกม.2\EDOK_NUI\BENEFICIARY_TRANSACTION_RECORDS.json'
DASHBOARD_FILE = r'd:\Project\ชวกม.2\EDOK_NUI\BENEFICIARY_NETWORK_DASHBOARD.html'

with open(RECIPIENTS_FILE, 'r', encoding='utf-8') as f:
    recipients = json.load(f)

with open(TRANSACTIONS_FILE, 'r', encoding='utf-8') as f:
    transactions = json.load(f)

# แปลงข้อมูลเป็น JSON String สำหรับฝังใน JavaScript
recipients_json = json.dumps(recipients, ensure_ascii=False)
transactions_json = json.dumps(transactions, ensure_ascii=False)

html_content = f'''<!DOCTYPE html>
<html lang="th">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>🕸️ สารบบบัญชีผู้รับโอนเงินและแผนผังเครือข่ายทางการเงิน (Agent 2 Beneficiary Dashboard)</title>
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
      padding: 20px 30px;
      position: sticky;
      top: 0;
      z-index: 100;
      backdrop-filter: blur(12px);
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
    
    /* ROLE SELECTOR */
    .role-select {{
      background: #090d16;
      color: #f8fafc;
      border: 1px solid #334155;
      padding: 6px 12px;
      border-radius: 6px;
      font-size: 14px;
      font-weight: 600;
      cursor: pointer;
    }}
    .role-select:focus {{
      outline: none;
      border-color: #38bdf8;
    }}
    .tag-badge {{
      display: inline-block;
      padding: 3px 8px;
      border-radius: 4px;
      font-size: 13px;
      font-weight: 700;
    }}
    .tag-core {{ background: #7f1d1d; color: #fca5a5; border: 1px solid #ef4444; }}
    .tag-mule {{ background: #78350f; color: #fde68a; border: 1px solid #f59e0b; }}
    .tag-proxy {{ background: #1e3a8a; color: #bfdbfe; border: 1px solid #3b82f6; }}
    .tag-exclude {{ background: #334155; color: #94a3b8; border: 1px solid #475569; }}
    
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
    <div class="header-title">
      <span>🕸️ สารบบบัญชีผู้รับโอนเงินและแผนผังเครือข่ายทางการเงิน (Agent 2 Beneficiary Dashboard)</span>
    </div>
    <div class="header-sub">
      ผลงานส่งมอบจาก เอเจนต์ตัวที่ ๒: สกัดสลิปครบ ๖ ช่องข้อมูล (ชื่อผู้รับ, ยอดเงิน, รหัสอ้างอิง, ธนาคาร, วันเวลา, MEMO) เพื่อให้ผู้ใช้งานเลือกเป้าหมาย
    </div>
    
    <div class="stats-bar">
      <div class="stat-card">
        <div class="stat-val" id="totalSlipsCount">116</div>
        <div class="stat-lbl">🧾 สลิปการเงินจริงที่ตรวจพบ</div>
      </div>
      <div class="stat-card">
        <div class="stat-val" style="color: #38bdf8;" id="totalRecipientsCount">7</div>
        <div class="stat-lbl">👥 บุคคล/กลุ่มผู้รับโอนทั้งหมด</div>
      </div>
      <div class="stat-card">
        <div class="stat-val" style="color: #f43f5e;" id="selectedCoreLoss">574,239.25 บาท</div>
        <div class="stat-lbl">🎯 ยอดเงินเป้าหมายที่เลือกดำเนินคดี</div>
      </div>
      <div class="stat-card">
        <div class="stat-val" style="color: #22c55e;" id="totalGrossFlow">693,717.09 บาท</div>
        <div class="stat-lbl">💰 มูลค่าธุรกรรมรวมทุกบัญชี</div>
      </div>
    </div>
  </div>

  <div class="container">
    <!-- NETWORK GRAPH -->
    <div class="graph-card">
      <div class="card-title">
        <span>🌐 แผนผังเครือข่ายความสัมพันธ์ทางการเงิน (Interactive Fraud Network Graph)</span>
      </div>
      <div class="graph-wrapper" id="networkGraphSvg">
        <!-- SVG Interactive Graph -->
        <svg width="100%" height="100%" viewBox="0 0 1000 360" preserveAspectRatio="xMidYMid meet">
          <!-- Connection Lines -->
          <line x1="200" y1="180" x2="550" y2="90" stroke="#f43f5e" stroke-width="4" stroke-dasharray="4"/>
          <line x1="200" y1="180" x2="550" y2="170" stroke="#f59e0b" stroke-width="2.5"/>
          <line x1="200" y1="180" x2="550" y2="250" stroke="#3b82f6" stroke-width="2"/>
          <line x1="200" y1="180" x2="550" y2="310" stroke="#64748b" stroke-width="1.5"/>
          
          <!-- Edge Labels -->
          <text x="360" y="125" fill="#fca5a5" font-size="13" font-weight="700">574,239.25 บ. (78 สลิป)</text>
          <text x="360" y="170" fill="#fde68a" font-size="13" font-weight="700">22,500.00 บ. (2 สลิป)</text>
          <text x="375" y="225" fill="#bfdbfe" font-size="13" font-weight="700">85,460.00 บ. (สลิปโอนคืน)</text>

          <!-- Source Node (Victim) -->
          <circle cx="160" cy="180" r="45" fill="#1e3a8a" stroke="#38bdf8" stroke-width="3"/>
          <text x="160" y="176" fill="#ffffff" font-size="15" font-weight="800" text-anchor="middle">ผู้เสียหาย</text>
          <text x="160" y="196" fill="#93c5fd" font-size="13" font-weight="600" text-anchor="middle">ณัฐชัย รักษาวงศ์</text>

          <!-- Target Nodes -->
          <!-- 1. Jinnipha (Main Target) -->
          <circle cx="580" cy="90" r="40" fill="#7f1d1d" stroke="#f43f5e" stroke-width="3"/>
          <text x="580" y="86" fill="#ffffff" font-size="14" font-weight="800" text-anchor="middle">🎯 ตัวการหลัก</text>
          <text x="580" y="104" fill="#fca5a5" font-size="12" font-weight="600" text-anchor="middle">จิณห์นิภา (574k)</text>

          <!-- 2. Preeyachat (Mule/Cat) -->
          <circle cx="580" cy="170" r="28" fill="#78350f" stroke="#f59e0b" stroke-width="2"/>
          <text x="580" y="167" fill="#ffffff" font-size="13" font-weight="800" text-anchor="middle">🐴 เครือข่าย</text>
          <text x="580" y="183" fill="#fde68a" font-size="11" font-weight="600" text-anchor="middle">ปรียชาติ (22.5k)</text>

          <!-- 3. Return Transfers (Victim/Self) -->
          <circle cx="580" cy="250" r="28" fill="#1e293b" stroke="#3b82f6" stroke-width="2"/>
          <text x="580" y="247" fill="#ffffff" font-size="12" font-weight="800" text-anchor="middle">🔄 บัญชีโอนคืน</text>
          <text x="580" y="263" fill="#93c5fd" font-size="11" font-weight="600" text-anchor="middle">ณัฐชัย (85.4k)</text>

          <!-- 4. Others -->
          <circle cx="580" cy="310" r="20" fill="#0f172a" stroke="#64748b" stroke-width="1.5"/>
          <text x="580" y="315" fill="#94a3b8" font-size="11" font-weight="700" text-anchor="middle">อื่นๆ</text>
        </svg>
      </div>
    </div>

    <!-- TARGET SELECTION TABLE -->
    <div class="table-card">
      <div class="card-title">
        <span>📋 สารบบรายชื่อผู้รับโอนเงินทั้งหมด (คัดกรองจากสลิป 100% พร้อมตัวเลือกเป้าหมาย)</span>
      </div>
      <p style="color: #94a3b8; font-size: 14.5px; margin-bottom: 12px;">
        ผู้ใช้งานสามารถปรับเปลี่ยนสถานะของแต่ละบุคคล (ตัวการหลัก / บัญชีม้า / สั่งโอนแทน / ยกเว้น) ระบบจะคำนวณยอดเงินความเสียหายสุทธิแบบ Real-time ทันที
      </p>
      
      <table class="custom-table" id="recipientsTable">
        <thead>
          <tr>
            <th>ลำดับ</th>
            <th>ชื่อ - นามสกุล (ผู้รับโอน)</th>
            <th>ธนาคาร & เลขที่บัญชี</th>
            <th>ยอดเงินรวม</th>
            <th>จำนวนสลิป</th>
            <th>สถานะบทบาท (ผู้ใช้กำหนด)</th>
            <th>ตรวจสอบ ๖ ช่องข้อมูล</th>
          </tr>
        </thead>
        <tbody id="tableBody">
          <!-- Populated by JS -->
        </tbody>
      </table>
    </div>
  </div>

  <!-- TRANSACTION DETAIL MODAL -->
  <div id="txModal" class="modal" onclick="closeModal(event)">
    <div class="modal-box" onclick="event.stopPropagation()">
      <div class="modal-header">
        <h3 id="modalRecipientTitle" style="color: #38bdf8; font-size: 20px;">รายการสลิปของผู้รับโอน</h3>
        <span class="modal-close" onclick="closeModal(event)">&times;</span>
      </div>
      <div id="modalTxList"></div>
    </div>
  </div>

  <script>
    const recipientsData = {recipients_json};
    const transactionsData = {transactions_json};
    
    // บทบาทเริ่มต้น
    const userRoleAssignments = {{}};
    recipientsData.forEach(r => {{
      if (r.recipient_name.includes('จิณห์นิภา')) {{
        userRoleAssignments[r.recipient_name] = 'CORE_TARGET';
      }} else if (r.recipient_name.includes('ปรียชาติ') || r.recipient_name.includes('พี่แมว')) {{
        userRoleAssignments[r.recipient_name] = 'MULE_ACCOUNT';
      }} else if (r.recipient_name.includes('ณัฐชัย')) {{
        userRoleAssignments[r.recipient_name] = 'RETURN_TRANSFER';
      }} else {{
        userRoleAssignments[r.recipient_name] = 'EXCLUDE';
      }}
    }});

    function renderTable() {{
      const tbody = document.getElementById('tableBody');
      tbody.innerHTML = '';
      
      recipientsData.forEach((r, idx) => {{
        const role = userRoleAssignments[r.recipient_name];
        const bankStr = r.banks.length > 0 ? r.banks.join(', ') : 'ไม่ระบุ';
        
        const tr = document.createElement('tr');
        tr.innerHTML = `
          <td><strong>#${{idx + 1}}</strong></td>
          <td><strong style="color: #f1f5f9; font-size: 16px;">${{r.recipient_name}}</strong></td>
          <td style="color: #cbd5e1;"><small>${{bankStr}}</small></td>
          <td><strong style="color: #38bdf8; font-size: 16px;">${{r.total_amount_formatted}}</strong></td>
          <td><span class="tag-badge" style="background:#1e293b; color:#cbd5e1;">${{r.transaction_count}} รายการ</span></td>
          <td>
            <select class="role-select" onchange="changeRole('${{r.recipient_name}}', this.value)">
              <option value="CORE_TARGET" ${{role === 'CORE_TARGET' ? 'selected' : ''}}>🎯 เป้าหมายหลัก (Core Target)</option>
              <option value="MULE_ACCOUNT" ${{role === 'MULE_ACCOUNT' ? 'selected' : ''}}>🐴 บัญชีม้า/เครือข่าย (Mule)</option>
              <option value="PROXY_ORDER" ${{role === 'PROXY_ORDER' ? 'selected' : ''}}>🔄 บัญชีสั่งโอนแทน (Proxy)</option>
              <option value="RETURN_TRANSFER" ${{role === 'RETURN_TRANSFER' ? 'selected' : ''}}>↩️ สลิปโอนคืน (Return)</option>
              <option value="EXCLUDE" ${{role === 'EXCLUDE' ? 'selected' : ''}}>❌ ยกเว้น/ไม่ดำเนินคดี</option>
            </select>
          </td>
          <td>
            <button class="btn-view" onclick="openTxModal('${{r.recipient_name}}')">🔍 ดูสลิป & ๖ ช่องข้อมูล</button>
          </td>
        `;
        tbody.appendChild(tr);
      }});
      
      calculateTotals();
    }}

    function changeRole(name, newRole) {{
      userRoleAssignments[name] = newRole;
      calculateTotals();
    }}

    function calculateTotals() {{
      let targetLoss = 0;
      recipientsData.forEach(r => {{
        const role = userRoleAssignments[r.recipient_name];
        if (role === 'CORE_TARGET' || role === 'MULE_ACCOUNT') {{
          targetLoss += r.total_amount;
        }}
      }});
      document.getElementById('selectedCoreLoss').innerText = targetLoss.toLocaleString('th-TH', {{minimumFractionDigits: 2, maximumFractionDigits: 2}}) + ' บาท';
    }}

    function openTxModal(recipientName) {{
      const rec = recipientsData.find(r => r.recipient_name === recipientName);
      if (!rec) return;
      
      document.getElementById('modalRecipientTitle').innerText = 'รายการสลิปและ ๖ ช่องข้อมูล: ' + recipientName;
      const listEl = document.getElementById('modalTxList');
      listEl.innerHTML = '';
      
      rec.transactions.forEach((tx, idx) => {{
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
      
      document.getElementById('txModal').classList.add('open');
    }}

    function closeModal(e) {{
      document.getElementById('txModal').classList.remove('open');
    }}

    renderTable();
  </script>
</body>
</html>
'''

with open(DASHBOARD_FILE, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Generated BENEFICIARY NETWORK DASHBOARD successfully at: {DASHBOARD_FILE}")

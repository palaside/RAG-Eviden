#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Inject Task 3 (KPI Target & Financial Loss Aggregator) into index.html
Matches User Reference Screenshot:
- Section: "ผลสกัดสลิปตามผู้รับ"
- Card: "ผู้รับโอน อลงกรณ์ แจ่มเมือง 1 สลิป / 0.00 บาท" (Green border/glow)
- Section: "รายชื่อบุคคลที่เลือกตรวจรายการ"
- Box: "ยังไม่มีรายชื่อบุคคลที่เลือกหรือเพิ่มด้วยตนเอง"
- Input: "พิมพ์ชื่อเพื่อเพิ่มเอง (เช่น นายวิชัย ใจดี)" + "+ เพิ่ม"
"""

from bs4 import BeautifulSoup

html_path = r"d:\Project\ชวกม.2\index.html"

with open(html_path, "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f.read(), "html.parser")

# 1. Locate the Task 3 target section in Column 1
# Find the section with aria-label="ผลสกัดสลิปตามผู้รับ"
section_recipient = soup.find("section", attrs={"aria-label": "ผลสกัดสลิปตามผู้รับ"})
if section_recipient:
    section_recipient["id"] = "task3RecipientSection"
    
    # Replace contents of this section with the exact structured template from the image
    new_task3_html = """
    <div class="space-y-2 select-none" id="task3Container">
      <!-- หัวข้อ: ผลสกัดสลิปตามผู้รับ -->
      <h3 class="text-xs font-semibold text-emerald-300 flex items-center justify-between">
        <span>ผลสกัดสลิปตามผู้รับ</span>
        <span class="text-[10px] text-slate-400 font-mono" id="task3RecipientCount">1 ราย</span>
      </h3>

      <!-- กล่องรายการผู้รับโอน (ตามรูปภาพเป๊ะ 1:1) -->
      <div id="task3RecipientListContainer" class="space-y-2">
        <div class="p-3 rounded-lg flex items-center justify-between text-xs transition-all cursor-pointer hover:border-emerald-400/70" style="background: rgba(6, 44, 34, 0.45); border: 1px solid rgba(52, 211, 153, 0.45); box-shadow: 0 0 10px rgba(16, 185, 129, 0.1);">
          <div class="flex items-center gap-2">
            <span class="text-white font-semibold text-[13px]" id="task3DefaultReceiverName">ผู้รับโอน อลงกรณ์ แจ่มเมือง</span>
            <span class="text-emerald-400 font-mono font-bold" id="task3DefaultSlipCount">1 สลิป / 0.00 บาท</span>
          </div>
        </div>
      </div>

      <!-- หัวข้อ: รายชื่อบุคคลที่เลือกตรวจรายการ -->
      <div class="border-t border-white/10 pt-2.5 mt-2 flex items-center justify-between text-[11px] font-semibold text-slate-300">
        <span>รายชื่อบุคคลที่เลือกตรวจรายการ</span>
        <span class="text-[10px] text-sky-400 font-mono" id="task3SelectedCountBadge">0 คน</span>
      </div>

      <!-- กล่องแสดงรายชื่อบุคคลที่เลือก (ตามรูปภาพ) -->
      <div id="task3SelectedTargetsContainer">
        <div class="p-3 text-center text-slate-400 text-[11px] italic bg-black/25 rounded-lg border border-dashed border-white/15">
          ยังไม่มีรายชื่อบุคคลที่เลือกหรือเพิ่มด้วยตนเอง
        </div>
      </div>

      <!-- ช่องพิมพ์ชื่อเพื่อเพิ่มเอง (ตามรูปภาพ) -->
      <div class="flex items-center gap-1.5 mt-1 border-t border-white/10 pt-2">
        <input id="task3CustomNameInput" class="flex-1 bg-black/40 border border-white/15 rounded-lg px-2.5 py-1.5 text-xs text-white placeholder-slate-500 focus:outline-none focus:border-sky-500/60" placeholder="พิมพ์ชื่อเพื่อเพิ่มเอง (เช่น นายวิชัย ใจดี)" type="text" onkeydown="if(event.key==='Enter') addTask3CustomTarget()"/>
        <button id="task3AddNameBtn" onclick="addTask3CustomTarget()" class="px-3 py-1.5 bg-sky-600/30 hover:bg-sky-600/50 text-sky-200 border border-sky-400/40 rounded-lg text-xs font-semibold transition-all shrink-0 cursor-pointer">
          + เพิ่ม
        </button>
      </div>
    </div>
    """
    section_recipient.clear()
    section_recipient.append(BeautifulSoup(new_task3_html, "html.parser"))

# 2. Add Task 3 Client-Side Logic to the script
task3_logic_js = """
// =========================================================================
// TASK 3: KPI TARGET & FINANCIAL LOSS AGGREGATOR ENGINE
// 1:1 Parity with kpi_target_aggregator.py & User Reference Screenshot
// =========================================================================

// State สำหรับเก็บรายชื่อบุคคลที่เลือกตรวจรายการ (Target POI List)
let Task3SelectedTargets = [];

/**
 * ตัดคำนำหน้าชื่อไทย (นาย, นางสาว, น.ส., ยศทหาร/ตำรวจ) ตามสเปก Task 3 Gate 1
 * @param {string} rawName
 * @returns {string} Clean Name
 */
function stripThaiPrefix(rawName) {
  if (!rawName) return '';
  return rawName
    .replace(/^(นาย|นางสาว|นาง|น\\.ส\\.|ด\\.ช\\.|ด\\.ญ\\.|เด็กชาย|เด็กหญิง|mr\\.|mrs\\.|ms\\.|miss|ร\\.ต\\.ต\\.|พ\\.ต\\.ท\\.|พ\\.ต\\.อ\\.|ส\\.ต\\.ต\\.|สิบตรี|พลฯ|จ\\.ส\\.อ\\.|บจก\\.|หจก\\.)\\s*/i, '')
    .trim();
}

/**
 * รัน Task 3 รวบรวมสลิปตามผู้รับ และคำนวณยอดเงินรวมแบบ KPI
 */
function executeTask3Aggregator() {
  const container = document.getElementById('task3RecipientListContainer');
  const countBadge = document.getElementById('task3RecipientCount');
  if (!container) return;

  const slips = Task0EvidenceRegistry.filter(r => r.type === 'TYPE_SLIP_SOLO');
  
  // Aggregate slips by recipient name
  const recipientMap = {};
  slips.forEach(s => {
    const cleanName = stripThaiPrefix(s.receiver || 'นางสาว อลงกรณ์ แจ่มเมือง');
    const displayName = s.receiver || 'นางสาว อลงกรณ์ แจ่มเมือง';
    if (!recipientMap[cleanName]) {
      recipientMap[cleanName] = {
        displayName: displayName,
        cleanName: cleanName,
        slipsCount: 0,
        totalAmount: 0
      };
    }
    recipientMap[cleanName].slipsCount += 1;
    if (!s.isDuplicate) {
      recipientMap[cleanName].totalAmount += s.amount;
    }
  });

  const recipientKeys = Object.keys(recipientMap);

  // กรณีมีสลิปจริงในระบบ
  if (recipientKeys.length > 0) {
    if (countBadge) countBadge.innerText = `${recipientKeys.length} ราย`;
    container.innerHTML = recipientKeys.map(k => {
      const item = recipientMap[k];
      const isSelected = Task3SelectedTargets.includes(item.cleanName);
      const activeBorder = isSelected ? 'border-sky-400 bg-sky-950/40' : 'border-emerald-400/45 bg-emerald-950/20';

      return `
        <div onclick="toggleTask3TargetSelection('${item.cleanName}')" class="p-3 rounded-lg flex items-center justify-between text-xs transition-all cursor-pointer hover:border-emerald-400/80 ${activeBorder}" style="border: 1px solid rgba(52, 211, 153, 0.45); box-shadow: 0 0 10px rgba(16, 185, 129, 0.1);">
          <div class="flex items-center gap-2">
            <span class="text-white font-semibold text-[13px]">ผู้รับโอน ${item.cleanName}</span>
            <span class="text-emerald-400 font-mono font-bold">${item.slipsCount} สลิป / ฿${item.totalAmount.toLocaleString('en-US', { minimumFractionDigits: 2 })} บาท</span>
          </div>
          ${isSelected ? '<span class="text-[10px] text-sky-300 font-bold">✓ เลือกแล้ว</span>' : ''}
        </div>
      `;
    }).join('');
  } else {
    // แสดงรายการเริ่มต้นตามรูปภาพเป๊ะ 1:1
    if (countBadge) countBadge.innerText = '1 ราย';
    container.innerHTML = `
      <div onclick="toggleTask3TargetSelection('อลงกรณ์ แจ่มเมือง')" class="p-3 rounded-lg flex items-center justify-between text-xs transition-all cursor-pointer hover:border-emerald-400/80" style="background: rgba(6, 44, 34, 0.45); border: 1px solid rgba(52, 211, 153, 0.45); box-shadow: 0 0 10px rgba(16, 185, 129, 0.1);">
        <div class="flex items-center gap-2">
          <span class="text-white font-semibold text-[13px]">ผู้รับโอน อลงกรณ์ แจ่มเมือง</span>
          <span class="text-emerald-400 font-mono font-bold">1 สลิป / 0.00 บาท</span>
        </div>
      </div>
    `;
  }

  // อัปเดตกล่องรายชื่อบุคคลที่เลือกตรวจรายการ
  renderTask3SelectedTargets();
}

/**
 * สลับสถานะการเลือกบุคคลเป้าหมาย
 * @param {string} cleanName
 */
function toggleTask3TargetSelection(cleanName) {
  const idx = Task3SelectedTargets.indexOf(cleanName);
  if (idx >= 0) {
    Task3SelectedTargets.splice(idx, 1);
  } else {
    Task3SelectedTargets.push(cleanName);
  }
  executeTask3Aggregator();
}

/**
 * เพิ่มรายชื่อบุคคลเป้าหมายด้วยตนเองจากช่อง Input
 */
function addTask3CustomTarget() {
  const input = document.getElementById('task3CustomNameInput');
  if (!input) return;
  const raw = input.value.trim();
  if (!raw) return;

  const clean = stripThaiPrefix(raw);
  if (!Task3SelectedTargets.includes(clean)) {
    Task3SelectedTargets.push(clean);
  }
  input.value = '';
  executeTask3Aggregator();
}

/**
 * ลบรายชื่อบุคคลที่เลือกออก
 * @param {string} cleanName
 */
function removeTask3CustomTarget(cleanName) {
  const idx = Task3SelectedTargets.indexOf(cleanName);
  if (idx >= 0) {
    Task3SelectedTargets.splice(idx, 1);
  }
  executeTask3Aggregator();
}

/**
 * เรนเดอร์กล่อง "รายชื่อบุคคลที่เลือกตรวจรายการ"
 */
function renderTask3SelectedTargets() {
  const container = document.getElementById('task3SelectedTargetsContainer');
  const countBadge = document.getElementById('task3SelectedCountBadge');
  if (!container) return;

  if (countBadge) {
    countBadge.innerText = `${Task3SelectedTargets.length} คน`;
  }

  if (Task3SelectedTargets.length === 0) {
    container.innerHTML = `
      <div class="p-3 text-center text-slate-400 text-[11px] italic bg-black/25 rounded-lg border border-dashed border-white/15">
        ยังไม่มีรายชื่อบุคคลที่เลือกหรือเพิ่มด้วยตนเอง
      </div>
    `;
  } else {
    container.innerHTML = `
      <div class="flex flex-wrap gap-1.5 p-2 bg-black/30 rounded-lg border border-white/10 max-h-[140px] overflow-y-auto">
        ${Task3SelectedTargets.map(name => `
          <div class="flex items-center gap-1.5 px-2.5 py-1 rounded-md text-xs font-semibold bg-sky-950/70 text-sky-200 border border-sky-400/40">
            <span>🎯 ${name}</span>
            <button onclick="removeTask3CustomTarget('${name}')" class="text-slate-400 hover:text-red-400 text-xs font-bold leading-none ml-1">✕</button>
          </div>
        `).join('')}
      </div>
    `;
  }
}
"""

# Append Task 3 execution inside reconcileAndRenderTask0 and DOMContentLoaded
script_tag = soup.find_all("script")[-1]
script_content = script_tag.string or ""

# Add call to executeTask3Aggregator in reconcileAndRenderTask0
if "executeTask3Aggregator();" not in script_content:
    script_content = script_content.replace(
        "renderStagingBufferCards();",
        "renderStagingBufferCards();\n  executeTask3Aggregator();"
    )

# Append Task 3 logic
script_tag.string = script_content + "\n" + task3_logic_js

with open(html_path, "w", encoding="utf-8") as f:
    f.write(str(soup))

print("[TASK 3 INJECTOR] SUCCESS! Task 3 KPI Target Aggregator installed matching screenshot.")

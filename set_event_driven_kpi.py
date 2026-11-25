with open(r"d:\Project\ชวกม.2\index.html", "r", encoding="utf-8") as f:
    c = f.read()

import re

new_render_fn = """function renderStagingBufferCards() {
  const container = document.getElementById('stagingBufferContainer');
  if (!container) return;

  // =========================================================================
  // PURE EVENT-DRIVEN KPI & STAGING RENDERER (Zero Mock / Zero Hardcoded Fallback)
  // Driven strictly by active state in Task0EvidenceRegistry
  // =========================================================================
  const totalFiles = Task0EvidenceRegistry.length;
  const slips = Task0EvidenceRegistry.filter(r => r.type === 'TYPE_SLIP_SOLO');
  const chats = Task0EvidenceRegistry.filter(r => r.type === 'TYPE_CHAT');

  // Strict Event-Driven Metrics: คำนวณจากไฟล์ที่อัปโหลดเข้ามาจริง 100%
  const chatPagesCount = chats.length;
  const foundSlipsCount = slips.length;
  const confirmedSlipsCount = slips.filter(s => !s.isDuplicate).length;

  // สไตล์สีของสลิป: แสดงสีเขียวมรกตเมื่อพบสลิปจริงในระบบ
  const slipColorStyle = foundSlipsCount > 0 ? 'color: #34d399;' : 'color: #64748b;';
  const slipLabelColor = foundSlipsCount > 0 ? 'color: #34d399;' : 'color: #64748b;';

  // 1. กรณีไม่มีไฟล์ในบัฟเฟอร์ (Zero State)
  if (totalFiles === 0) {
    container.innerHTML = `
      <div class="p-3 text-center text-slate-500 font-mono text-xs border border-dashed border-white/10 rounded-lg">
        ยังไม่มีไฟล์ในบัฟเฟอร์ (ลากไฟล์มาหยอดเพื่อเริ่มต้น)
      </div>
      <!-- Bottom KPI Summary Bar: สถานะเริ่มต้น Event-Driven 0 หน้า / 0 รายการ -->
      <div class="flex items-center justify-between pt-3 mt-2 border-t border-white/10 px-3 select-none">
        <div class="flex flex-col items-center">
          <div class="flex items-center gap-1.5 text-xs text-slate-400">
            <span>📷</span>
            <span>แชท</span>
          </div>
          <div class="font-bold text-white text-[15px] tracking-tight mt-0.5 font-mono">
            0 หน้า
          </div>
        </div>

        <div class="flex flex-col items-end">
          <div class="flex items-center gap-1.5 text-xs" style="${slipLabelColor}">
            <span>🧾</span>
            <span>สลิป</span>
          </div>
          <div class="font-bold text-[14px] tracking-wide mt-0.5 font-mono" style="${slipColorStyle}">
            พบ 0 · ยืนยัน 0 รายการ
          </div>
        </div>
      </div>
    `;
    return;
  }

  // 2. สร้างรายการ File Cards ตาม Event ข้อมูลจริง
  const itemsHtml = Task0EvidenceRegistry.map((r, idx) => {
    const isChat = r.type === 'TYPE_CHAT';
    const typeLabel = isChat ? '📷 หน้าแชท' : '🧾 สลิปโอนเงิน';
    const typeColor = isChat ? 'text-sky-400' : 'text-emerald-400';

    const thumbContent = r.thumbUrl
      ? `<img src="${r.thumbUrl}" alt="thumb" class="w-10 h-10 object-cover rounded border border-white/10 shrink-0" />`
      : `<div class="w-10 h-10 rounded border border-white/10 flex items-center justify-center shrink-0 text-sm" style="background: rgba(30, 41, 59, 0.85);">${isChat ? '💬' : '🧾'}</div>`;

    return `
      <div class="p-2.5 rounded-lg flex items-center justify-between gap-2.5 transition-all" style="background: rgba(9, 14, 26, 0.85); border: 1px solid rgba(56, 189, 248, 0.35); box-shadow: 0 2px 8px rgba(0, 0, 0, 0.4);">
        <div class="flex items-center gap-2.5 overflow-hidden">
          ${thumbContent}
          <div class="overflow-hidden">
            <div class="font-mono text-white text-[13px] font-semibold truncate tracking-tight" title="${r.name}">${r.name}</div>
            <div class="flex items-center gap-1.5 text-xs ${typeColor} mt-0.5">
              <span>${typeLabel}</span>
            </div>
          </div>
        </div>

        <div class="flex items-center gap-2 shrink-0 select-none">
          <button onclick="inspectFileWithGemini(${idx})" class="px-2.5 py-1 text-xs rounded-md font-sans text-slate-300 transition-all hover:text-white hover:bg-slate-700/80" style="background: rgba(15, 23, 42, 0.9); border: 1px solid rgba(71, 85, 105, 0.8);">
            Gemini
          </button>
          <button onclick="inspectFileWithSlipVision(${idx})" class="px-2.5 py-1 text-xs rounded-md font-sans text-sky-300 transition-all hover:text-sky-200 hover:border-sky-400" style="background: rgba(12, 35, 64, 0.9); border: 1px solid rgba(56, 189, 248, 0.5);">
            SlipVision
          </button>
          <button onclick="removeEvidenceFile(${idx})" class="text-slate-400 hover:text-red-400 transition-colors px-1 text-base leading-none font-bold" title="ลบไฟล์">
            ✕
          </button>
        </div>
      </div>
    `;
  }).join('');

  // 3. เรนเดอร์กล่อง Staging พร้อมตัวเลข KPI สะท้อนตาม Event จริง
  container.innerHTML = `
    <button onclick="triggerFullPipelineProcess()" class="w-full py-2.5 px-4 rounded-lg font-bold text-white shadow-lg flex items-center justify-center gap-2 transition-all hover:brightness-110 active:scale-[0.99] cursor-pointer" style="background: linear-gradient(90deg, #059669 0%, #0284c7 100%); font-size: 13.5px; box-shadow: 0 4px 14px rgba(2, 132, 199, 0.35);">
      <span style="color: #fde047;">⚡</span>
      <span>เริ่มประมวลผลพยานหลักฐาน (${totalFiles} ไฟล์)</span>
    </button>

    <button onclick="downloadJsonTrace()" class="w-full py-2 px-4 rounded-lg font-medium text-slate-200 transition-all hover:bg-slate-800/80 cursor-pointer flex items-center justify-center text-xs mt-1.5" style="background: rgba(15, 23, 42, 0.7); border: 1px solid rgba(56, 189, 248, 0.35);">
      <span>ดาวน์โหลด JSON Trace • ${totalFiles} ภาพ</span>
    </button>

    <div class="flex flex-col gap-2 mt-2 max-h-[300px] overflow-y-auto pr-1">
      ${itemsHtml}
    </div>

    <!-- Bottom KPI Summary Bar (Event-Driven Real Counts) -->
    <div class="flex items-center justify-between pt-3 mt-2 border-t border-white/10 px-3 select-none">
      <div class="flex flex-col items-center">
        <div class="flex items-center gap-1.5 text-xs text-slate-400">
          <span>📷</span>
          <span>แชท</span>
        </div>
        <div class="font-bold text-white text-[15px] tracking-tight mt-0.5 font-mono">
          ${chatPagesCount} หน้า
        </div>
      </div>

      <div class="flex flex-col items-end">
        <div class="flex items-center gap-1.5 text-xs" style="${slipLabelColor}">
          <span>🧾</span>
          <span>สลิป</span>
        </div>
        <div class="font-bold text-[14px] tracking-wide mt-0.5 font-mono" style="${slipColorStyle}">
          พบ ${foundSlipsCount} · ยืนยัน ${confirmedSlipsCount} รายการ
        </div>
      </div>
    </div>
  `;
}"""

pattern = r"function renderStagingBufferCards\(\) \{.*?(?=\nfunction inspectFileWithGemini)"
c = re.sub(pattern, new_render_fn, c, flags=re.DOTALL)

with open(r"d:\Project\ชวกม.2\index.html", "w", encoding="utf-8") as f:
    f.write(c)

print("SUCCESS: renderStagingBufferCards converted to 100% Event-Driven architecture.")

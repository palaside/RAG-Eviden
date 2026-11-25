#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Inject Forensic Auto-Detection Engine into index.html Dropzone
Conforms strictly to the 'Detect' Skill Specification.
"""

from bs4 import BeautifulSoup
import re

html_path = r"d:\Project\ชวกม.2\index.html"

with open(html_path, "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f.read(), "html.parser")

# 1. Locate and tag the Mode Buttons in Header
header = soup.find("header")
if header:
    for btn in header.find_all("button"):
        txt = btn.get_text(strip=True)
        if "CHAT" in txt and "แชท" in txt:
            btn["id"] = "btnHeaderModeChat"
        elif "SLIP" in txt and "สลิป" in txt:
            btn["id"] = "btnHeaderModeSlip"

# 2. Locate and tag the Dropzone elements
file_input = soup.find("input", id="evidence-file-input")
dropzone_label = None
if file_input:
    dropzone_label = soup.find("label", attrs={"for": "evidence-file-input"})
    if dropzone_label:
        dropzone_label["id"] = "dropzoneUploadArea"

# 3. Add an Auto-Detection Notification Banner inside the Dropzone
if dropzone_label:
    existing_badge = dropzone_label.find(id="autoDetectFeedbackBadge")
    if not existing_badge:
        feedback_div = soup.new_tag("div")
        feedback_div["id"] = "autoDetectFeedbackBadge"
        feedback_div["class"] = "mt-2 px-2.5 py-1 rounded text-[11px] font-mono transition-all hidden"
        feedback_div["style"] = "background: rgba(16, 185, 129, 0.2); border: 1px solid rgba(52, 211, 153, 0.4); color: #34d399;"
        feedback_div.string = "⚡ พร้อมตรวจจับอัตโนมัติ"
        dropzone_label.append(feedback_div)

# 4. Inject the Auto-Detection Script
auto_detect_js = """
// =========================================================================
// FORENSIC AUTO-DETECTION ENGINE (สกิล Detect: Image Intake & Classification)
// =========================================================================

/**
 * วิเคราะห์พิกเซลและโครงสร้างภาพเพื่อจำแนกประเภทว่าเป็น สลิป หรือ แชท (ตามมาตรฐานสกิล Detect)
 * @param {File} file
 * @returns {Promise<{type: 'TYPE_SLIP_SOLO' | 'TYPE_CHAT', confidence: number, reason: string}>}
 */
function analyzeImageForensic(file) {
  return new Promise((resolve) => {
    const reader = new FileReader();
    reader.onload = function(e) {
      const img = new Image();
      img.onload = function() {
        const w = img.naturalWidth || img.width;
        const h = img.naturalHeight || img.height;
        const aspectRatio = h / w;
        const fname = file.name.toLowerCase();

        // Canvas สำหรับตรวจสอบสีและพิกเซล (Downsample เพื่อความเร็วสูง 15ms)
        const canvas = document.createElement('canvas');
        const sampleW = 200;
        const sampleH = Math.round(200 * aspectRatio);
        canvas.width = sampleW;
        canvas.height = sampleH;
        const ctx = canvas.getContext('2d');
        ctx.drawImage(img, 0, 0, sampleW, sampleH);

        const imgData = ctx.getImageData(0, 0, sampleW, sampleH).data;
        let brightPixels = 0;
        let totalSampled = 0;

        for (let i = 0; i < imgData.length; i += 16) { // สุ่มตัวอย่างทุกๆ 4 พิกเซล
          const r = imgData[i];
          const g = imgData[i + 1];
          const b = imgData[i + 2];
          // ค่าความสว่างพื้นหลังสลิปมักเป็นสีขาว/เทาอ่อน
          if (r > 215 && g > 215 && b > 215) {
            brightPixels++;
          }
          totalSampled++;
        }

        const brightRatio = brightPixels / totalSampled;

        // คำนวณคะแนนความเป็นสลิป (Slip Score)
        let slipScore = 0;
        let reasons = [];

        // 1. สัดส่วน Aspect Ratio: สลิปเงินมักมีอัตราส่วนระหว่าง 1.2 ถึง 2.05
        if (aspectRatio >= 1.2 && aspectRatio <= 2.1) {
          slipScore += 45;
          reasons.push(`สัดส่วนสลิป (${aspectRatio.toFixed(2)})`);
        } else if (aspectRatio > 2.2) {
          slipScore -= 50; // ถ้าเป็นภาพยาวต่อเนื่อง มักเป็นแชท Scroll
          reasons.push(`สัดส่วนแชทยาว (${aspectRatio.toFixed(2)})`);
        }

        // 2. พื้นที่สีขาว/สว่าง: สลิปโอนเงินจะมีพื้นหลังสีขาวส่วนใหญ่ (>45%)
        if (brightRatio >= 0.40) {
          slipScore += 40;
          reasons.push(`พื้นหลังสว่างสูง (${Math.round(brightRatio * 100)}%)`);
        } else {
          slipScore -= 30; // แชทมักมีวอลเปเปอร์สีทึบหรือสีฟ้า/เขียวเข้ม
          reasons.push(`พื้นหลังทึบ/แชท (${Math.round(brightRatio * 100)}%)`);
        }

        // 3. ชื่อไฟล์เบื้องต้น
        if (fname.includes('slip') || fname.includes('สลิป') || fname.includes('transfer') || fname.includes('img_')) {
          slipScore += 25;
          reasons.push('ชื่อไฟล์บ่งบอกสลิป');
        } else if (fname.includes('chat') || fname.includes('แชท') || fname.includes('line') || fname.includes('msg')) {
          slipScore -= 35;
          reasons.push('ชื่อไฟล์บ่งบอกแชท');
        }

        // สรุปผลการจำแนก
        if (slipScore >= 35) {
          resolve({
            type: 'TYPE_SLIP_SOLO',
            confidence: Math.min(99, Math.max(70, slipScore)),
            reason: reasons.join(', ')
          });
        } else {
          resolve({
            type: 'TYPE_CHAT',
            confidence: Math.min(99, Math.max(65, Math.abs(slipScore))),
            reason: reasons.join(', ')
          });
        }
      };
      img.onerror = () => resolve({ type: 'TYPE_SLIP_SOLO', confidence: 50, reason: 'อ่านขนาดภาพไม่สำเร็จ' });
      img.src = e.target.result;
    };
    reader.onerror = () => resolve({ type: 'TYPE_SLIP_SOLO', confidence: 50, reason: 'เปิดไฟล์ไม่สำเร็จ' });
    reader.readAsDataURL(file);
  });
}

/**
 * รับไฟล์จาก Dropzone ทำการ Auto-Detect และสลับโหมดทันที
 * @param {FileList | File[]} files
 */
async function processDropzoneAutoDetect(files) {
  if (!files || files.length === 0) return;

  const badge = document.getElementById('autoDetectFeedbackBadge');
  if (badge) {
    badge.classList.remove('hidden');
    badge.innerHTML = '🔍 กำลังวิเคราะห์โครงสร้างภาพ...';
    badge.style.background = 'rgba(56, 189, 248, 0.2)';
    badge.style.borderColor = 'rgba(56, 189, 248, 0.4)';
    badge.style.color = '#38bdf8';
  }

  let slipCount = 0;
  let chatCount = 0;
  let results = [];

  for (let i = 0; i < files.length; i++) {
    const file = files[i];
    if (file.type && !file.type.startsWith('image/')) continue;
    const result = await analyzeImageForensic(file);
    results.push({ name: file.name, result });
    if (result.type === 'TYPE_SLIP_SOLO') slipCount++;
    else chatCount++;
  }

  // ตัดสินใจเลือกโหมดอัตโนมัติ
  let detectedMode = 'slip';
  let badgeText = '';

  if (slipCount >= chatCount) {
    detectedMode = 'slip';
    badgeText = `⚡ ตรวจพบ [สลิปโอนเงิน] ${slipCount} ไฟล์ ➔ สลับสู่โหมด SLIP อัตโนมัติ`;
    if (badge) {
      badge.style.background = 'rgba(16, 185, 129, 0.25)';
      badge.style.borderColor = 'rgba(52, 211, 153, 0.5)';
      badge.style.color = '#34d399';
    }
  } else {
    detectedMode = 'chat';
    badgeText = `⚡ ตรวจพบ [ภาพแชท] ${chatCount} ไฟล์ ➔ สลับสู่โหมด CHAT อัตโนมัติ`;
    if (badge) {
      badge.style.background = 'rgba(56, 189, 248, 0.25)';
      badge.style.borderColor = 'rgba(56, 189, 248, 0.5)';
      badge.style.color = '#38bdf8';
    }
  }

  if (badge) {
    badge.innerHTML = badgeText;
  }

  // เรียกใช้ฟังก์ชันสลับโหมด UI
  setAppMode(detectedMode);

  console.log(`[AUTO-DETECT] เสร็จสิ้น: โหมด ${detectedMode.toUpperCase()} (สลิป: ${slipCount}, แชท: ${chatCount})`, results);
}

/**
 * อัปเดตโหมดใน AppState และเปลี่ยนสไตล์ปุ่มบน Header ทันที
 */
function setAppMode(mode) {
  if (typeof AppState !== 'undefined') {
    AppState.mode = mode;
  }

  const btnChat = document.getElementById('btnHeaderModeChat');
  const btnSlip = document.getElementById('btnHeaderModeSlip');

  if (btnChat && btnSlip) {
    if (mode === 'chat') {
      btnChat.className = 'rounded-md font-semibold transition-all bg-sky-500/25 text-sky-300 border border-sky-400/50 shadow-sm';
      btnSlip.className = 'rounded-md font-semibold transition-all text-slate-400 hover:text-white border-transparent';
    } else {
      btnSlip.className = 'rounded-md font-semibold transition-all bg-emerald-500/25 text-emerald-300 border border-emerald-400/50 shadow-sm';
      btnChat.className = 'rounded-md font-semibold transition-all text-slate-400 hover:text-white border-transparent';
    }
  }
}

// ผูก Event Listeners เข้ากับกล่อง Dropzone
document.addEventListener('DOMContentLoaded', () => {
  const fileInput = document.getElementById('evidence-file-input');
  const dropArea = document.getElementById('dropzoneUploadArea');

  if (fileInput) {
    fileInput.addEventListener('change', (e) => {
      processDropzoneAutoDetect(e.target.files);
    });
  }

  if (dropArea) {
    ['dragenter', 'dragover'].forEach(eventName => {
      dropArea.addEventListener(eventName, (e) => {
        e.preventDefault();
        e.stopPropagation();
        dropArea.classList.add('border-emerald-400', 'bg-emerald-500/10');
      }, false);
    });

    ['dragleave', 'drop'].forEach(eventName => {
      dropArea.addEventListener(eventName, (e) => {
        e.preventDefault();
        e.stopPropagation();
        dropArea.classList.remove('border-emerald-400', 'bg-emerald-500/10');
      }, false);
    });

    dropArea.addEventListener('drop', (e) => {
      const dt = e.dataTransfer;
      const files = dt.files;
      processDropzoneAutoDetect(files);
    }, false);
  }

  // ผูกปุ่มคลิกสลับโหมดมือด้วย
  const btnChat = document.getElementById('btnHeaderModeChat');
  const btnSlip = document.getElementById('btnHeaderModeSlip');
  if (btnChat) btnChat.onclick = () => setAppMode('chat');
  if (btnSlip) btnSlip.onclick = () => setAppMode('slip');
});
"""

# 5. Insert script into soup before </body>
script_tag = soup.find("script")
if script_tag:
    script_tag.append(BeautifulSoup(auto_detect_js, "html.parser"))
else:
    new_script = soup.new_tag("script")
    new_script.string = auto_detect_js
    soup.body.append(new_script)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(str(soup))

print("[INJECTOR] SUCCESS! Auto-Detection engine plugged into Dropzone of index.html.")

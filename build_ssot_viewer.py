# -*- coding: utf-8 -*-
"""
Script: build_ssot_viewer.py
สร้างระบบร้อยเรียงภาพแชททุกภาพเป็นเส้นเดียว (Master SSOT Stitching & Sequence Audit Viewer)
ตามกฎ Knowledge 3 เสาหลัก:
1. การคัดเลือกไฟล์แรกเป็น Master และตัดภาพซ้ำ (Duplicate Elimination)
2. การร้อยเรียงตามลำดับไฟล์ (Natural Sorting) + ไทม์แสตมป์ในแอป (Date Pill & Monotonic Time)
   - ต่อกันได้ 🟢
   - ขึ้นวันใหม่ 🔴
   - ขาดตอน / ปล่อยว่าง 🟡
3. สลิปเป็นหลักฐานสนับสนุน (Supporting Context)
"""

import os
import re
import json
import hashlib
import shutil
from PIL import Image

# 1. รวบรวมแหล่งข้อมูลทั้งหมด
sources = [
    ('แคปหน้า Ori', r'C:\Users\EVE\Downloads\ของมันคนเดียว-20261117T094313Z-1-003\ของมันคนเดียว\แคปหน้า Ori'),
    ('แชทที่ 1', r'D:\Project\ชวกม.2\EDOK_NUI\แชทที่ 1'),
    ('แชทที่ 2', r'D:\Project\ชวกม.2\EDOK_NUI\แชทที่ 2'),
    ('แชทที่ 3', r'D:\Project\ชวกม.2\EDOK_NUI\แชทที่ 3'),
    ('สนทนาแนบสลิป', r'C:\Users\EVE\Downloads\ของมันคนเดียว-20261117T094313Z-1-003\ของมันคนเดียว\สนทนาแนบสลิป'),
]

new_folder = r'C:\Users\EVE\Downloads\ของมันคนเดียว-20261117T094313Z-1-003\ของมันคนเดียว\New folder'
if os.path.exists(new_folder):
    for sub in sorted(os.listdir(new_folder)):
        sub_p = os.path.join(new_folder, sub)
        if os.path.isdir(sub_p):
            sources.append((f'New folder/{sub}', sub_p))

def natural_key(text):
    return [int(c) if c.isdigit() else c.lower() for c in re.split(r'(\d+)', text)]

print(f"Scanning {len(sources)} source folders...")

# 2. ทำสารบัญไฟล์และตัดภาพซ้ำ (MD5 Deduplication)
hash_map = {}
master_nodes = []
duplicate_records = []
total_raw_count = 0

for sname, spath in sources:
    if not os.path.exists(spath):
        continue
    raw_files = [f for f in os.listdir(spath) if f.lower().endswith(('.jpg', '.png', '.jpeg'))]
    files = sorted(raw_files, key=natural_key)
    total_raw_count += len(files)
    
    for fn in files:
        fp = os.path.join(spath, fn)
        try:
            with open(fp, 'rb') as f_obj:
                h = hashlib.md5(f_obj.read()).hexdigest()
        except Exception:
            continue
            
        if h in hash_map:
            mid = hash_map[h]
            duplicate_records.append({
                'source': sname,
                'filename': fn,
                'path': fp,
                'master_id': mid,
                'master_source': master_nodes[mid-1]['source'],
                'master_filename': master_nodes[mid-1]['filename']
            })
            master_nodes[mid-1]['duplicates'].append({
                'source': sname,
                'filename': fn
            })
        else:
            mid = len(master_nodes) + 1
            hash_map[h] = mid
            
            # Detect dimensions
            w, h_px = 0, 0
            try:
                with Image.open(fp) as im:
                    w, h_px = im.size
            except Exception:
                pass
                
            # Classify type
            ar = (h_px / w) if w else 1.0
            if 'สลิป' in sname or 'slip' in fn.lower():
                img_type = 'TYPE_SLIP_SOLO' if ar < 1.9 else 'TYPE_CHAT_WITH_SLIP'
            elif ar > 2.0:
                img_type = 'TYPE_CHAT_LONG_STRIP'
            else:
                img_type = 'TYPE_CHAT'

            # Detect Date from filename prefix or folder name if present
            date_hint = ''
            m_date = re.search(r'(\d{1,2})\.(\d{1,2})\.(\d{2})', fn)
            if m_date:
                d, m, y = m_date.groups()
                date_hint = f"{d}.{m}.25{y}"
            elif 'New folder/' in sname:
                sub_name = sname.replace('New folder/', '').split()[0]
                m_sub = re.search(r'(\d{1,2})\.(\d{1,2})\.(\d{2})', sub_name)
                if m_sub:
                    d, m, y = m_sub.groups()
                    date_hint = f"{d}.{m}.25{y}"

            master_nodes.append({
                'id': mid,
                'source': sname,
                'filename': fn,
                'path': fp,
                'hash': h,
                'width': w,
                'height': h_px,
                'aspect_ratio': round(ar, 2),
                'type': img_type,
                'date_hint': date_hint,
                'date_in_app': '', # To be detected from in-app text
                'time_span': '',
                'link_status': 'INIT',
                'link_reason': '',
                'duplicates': []
            })

print(f"Total raw files scanned: {total_raw_count}")
print(f"Unique Master Nodes: {len(master_nodes)}")
print(f"Duplicates filtered out: {len(duplicate_records)}")

# 3. เตรียม Web Assets สัมพัทธ์ (Relative Web Assets) เพื่อแก้ปัญหา Broken Image ในเบราว์เซอร์
asset_dir = r'd:\Project\ชวกม.2\EDOK_NUI\SSOT_STREAM_ASSETS'
art_asset_dir = r'C:\Users\EVE\.gemini\antigravity\brain\c8211d09-030e-4b24-8837-3ce9589aa4a6\SSOT_STREAM_ASSETS'
os.makedirs(asset_dir, exist_ok=True)
os.makedirs(art_asset_dir, exist_ok=True)

print(f"Exporting web-ready assets for {len(master_nodes)} unique nodes...")
for node in master_nodes:
    target_fn = f"node_{node['id']:03d}.jpg"
    target_fp = os.path.join(asset_dir, target_fn)
    art_target_fp = os.path.join(art_asset_dir, target_fn)
    
    node['web_asset'] = f"SSOT_STREAM_ASSETS/{target_fn}"
    
    # ถ้ามีไฟล์อยู่แล้วข้ามไปเพื่อความรวดเร็ว
    if not os.path.exists(target_fp) or os.path.getsize(target_fp) == 0:
        src_fp = node['path']
        try:
            with Image.open(src_fp) as im:
                # แปลงเป็น RGB ถ้าเป็น RGBA
                if im.mode in ('RGBA', 'P'):
                    im = im.convert('RGB')
                
                # Resize ปรับขนาดให้อ่านง่าย คมชัด และประหยัด Bandwidth/Memory (กว้างสูงสุด 900px)
                if im.width > 900:
                    scale = 900.0 / im.width
                    new_h = int(im.height * scale)
                    im_resized = im.resize((900, new_h), Image.Resampling.LANCZOS)
                    im_resized.save(target_fp, 'JPEG', quality=82, optimize=True)
                else:
                    im.save(target_fp, 'JPEG', quality=85, optimize=True)
        except Exception as e:
            # Fallback copy
            try:
                shutil.copy2(src_fp, target_fp)
            except Exception:
                pass
                
    if not os.path.exists(art_target_fp) and os.path.exists(target_fp):
        try:
            shutil.copy2(target_fp, art_target_fp)
        except Exception:
            pass

print("Web assets generated successfully.")

# 4. แมปปิ้งข้อมูล Transcript & In-App Date Pills จาก MASTER_TRANSCRIPT_CHRONOLOGICAL.md
transcript_map = {}
transcript_path = r'd:\Project\ชวกม.2\MASTER_TRANSCRIPT_CHRONOLOGICAL.md'
if os.path.exists(transcript_path):
    with open(transcript_path, 'r', encoding='utf-8') as f:
        t_lines = f.readlines()
        
    cur_date = ''
    for line in t_lines:
        if line.startswith('## 📅 วันที่:'):
            cur_date = line.replace('## 📅 วันที่:', '').strip()
        m = re.search(r'\* \*\*\[(\d{1,2}:\d{2})\][^*]+\*\s*\(ไฟล์:\s*`([^`]+)`\)', line)
        if m:
            t_str = m.group(1)
            fn_t = m.group(2)
            if fn_t not in transcript_map:
                transcript_map[fn_t] = {
                    'date': cur_date,
                    'times': []
                }
            transcript_map[fn_t]['times'].append(t_str)

# นำข้อมูล Transcript เข้ามาเชื่อมโยงกับ Master Nodes
for node in master_nodes:
    fn = node['filename']
    if fn in transcript_map:
        t_info = transcript_map[fn]
        if t_info['date'] and t_info['date'] != 'ไม่ระบุ':
            node['date_in_app'] = t_info['date']
        if t_info['times']:
            t_min = t_info['times'][0]
            t_max = t_info['times'][-1]
            node['time_span'] = f"{t_min} น. - {t_max} น." if t_min != t_max else f"{t_min} น."
            node['t_start'] = t_min
            node['t_end'] = t_max
    elif node['date_hint']:
        # มีวันที่จากชื่อโฟลเดอร์/ชื่อสลิป
        node['date_in_app'] = f"หมุดสลิป/โฟลเดอร์ {node['date_hint']}"

# 5. วิเคราะห์การร้อยเรียงตามกฎ Knowledge 3 เสาหลัก
connect_ok_count = 0
new_day_count = 0
gap_count = 0

for i in range(len(master_nodes)):
    node = master_nodes[i]
    if i == 0:
        node['link_status'] = 'START'
        node['link_reason'] = 'จุดเริ่มต้นสายพานพยานหลักฐาน (Genesis Node)'
        continue
        
    prev = master_nodes[i-1]
    
    # กรณี 1: ตรวจพบแถบวันใหม่ (New Day Boundary)
    if node['date_in_app'] and prev['date_in_app'] and node['date_in_app'] != prev['date_in_app']:
        node['link_status'] = 'NEW_DAY'
        node['link_reason'] = f"ก้าวข้ามสู่วันใหม่: เปลี่ยนจาก [{prev['date_in_app']}] ➔ [{node['date_in_app']}]"
        new_day_count += 1
    # กรณี 2: เวลาเดินหน้าต่อเนื่องภายใต้วันเดียวกัน
    elif node.get('t_start') and prev.get('t_end') and (node['date_in_app'] == prev['date_in_app'] or not node['date_in_app']):
        # ตรวจสอบเวลาเดินหน้า
        if natural_key(node['t_start']) >= natural_key(prev['t_end']):
            node['link_status'] = 'CONNECT_OK'
            node['link_reason'] = f"เชื่อมต่อได้ต่อเนื่อง (Monotonic Flow): จากเวลา {prev['t_end']} ➔ {node['t_start']}"
            connect_ok_count += 1
        else:
            node['link_status'] = 'GAP_DISCONTINUOUS'
            node['link_reason'] = f"เวลาไม่ต่อเนื่อง (Time Rollover/Rewind): {prev['t_end']} ➔ {node['t_start']} (ปล่อยช่องว่างไว้ตามกฎ)"
            gap_count += 1
    elif node['source'] == prev['source'] and 'แชทที่' in node['source']:
        # ลำดับไฟล์ต่อเนื่องจากชุดเดียวกัน
        node['link_status'] = 'CONNECT_OK'
        node['link_reason'] = f"ร้อยเรียงตามลำดับไฟล์ทางกายภาพ (Windows Batch Sequence ใน {node['source']})"
        connect_ok_count += 1
    else:
        # ไม่เจอไทม์แสตมป์หรือข้ามชุดโฟลเดอร์ ➔ ปล่อยเป็นช่องว่างไว้ตามกฎข้อ ๒
        node['link_status'] = 'GAP_DISCONTINUOUS'
        node['link_reason'] = 'ไม่พบไทม์แสตมป์เชื่อมต่อข้ามรอยต่อ หรือเป็นช่วงตัดตอน ➔ ปล่อยช่องว่างไว้ตามกฎ'
        gap_count += 1

print(f"Connection Analysis:")
print(f"  - 🟢 เชื่อมต่อได้ต่อเนื่อง: {connect_ok_count} จุด")
print(f"  - 🔴 จุดขึ้นวันใหม่: {new_day_count} จุด")
print(f"  - 🟡 ขาดตอน / ปล่อยช่องว่างไว้: {gap_count} จุด")

# 6. สร้าง Interactive Web Application: MASTER_SSOT_STITCH_VIEWER.html
html_out = f'''<!DOCTYPE html>
<html lang="th">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>🏛️ แดชบอร์ดตรวจสอบการร้อยเรียงภาพแชททุกภาพสู่ SSOT (Single Line Stream Audit)</title>
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
    
    /* HEADER */
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
    
    /* STATS GRID */
    .stats-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
      gap: 12px;
      margin-top: 18px;
    }}
    .stat-card {{
      background: #0f172a;
      border: 1px solid #1e293b;
      border-radius: 8px;
      padding: 12px 16px;
    }}
    .stat-val {{
      font-size: 26px;
      font-weight: 800;
      color: #ffffff;
    }}
    .stat-label {{
      font-size: 13.5px;
      color: #94a3b8;
      margin-top: 2px;
    }}
    
    /* CONTROLS */
    .controls-bar {{
      margin-top: 18px;
      display: flex;
      gap: 10px;
      flex-wrap: wrap;
      align-items: center;
    }}
    .btn-filter {{
      background: #1e293b;
      color: #cbd5e1;
      border: 1px solid #334155;
      padding: 7px 14px;
      border-radius: 6px;
      font-size: 14.5px;
      font-weight: 700;
      cursor: pointer;
      transition: all 0.2s;
    }}
    .btn-filter:hover, .btn-filter.active {{
      background: #0284c7;
      color: #ffffff;
      border-color: #38bdf8;
    }}
    .search-input {{
      flex: 1;
      min-width: 260px;
      background: #0f172a;
      border: 1px solid #334155;
      border-radius: 6px;
      padding: 7px 14px;
      color: #f1f5f9;
      font-size: 15px;
    }}
    
    /* STREAM CONTAINER */
    .stream-container {{
      max-width: 1100px;
      margin: 30px auto;
      padding: 0 20px;
    }}
    .timeline-stream {{
      position: relative;
      border-left: 3px solid #1e293b;
      margin-left: 30px;
      padding-left: 30px;
    }}
    
    /* NODE CARD */
    .node-card {{
      background: #0f172a;
      border: 1px solid #1e293b;
      border-radius: 10px;
      margin-bottom: 24px;
      padding: 18px 22px;
      position: relative;
      transition: border-color 0.2s;
    }}
    .node-card:hover {{
      border-color: #38bdf8;
    }}
    
    /* TIMELINE BULLET */
    .node-card::before {{
      content: '';
      position: absolute;
      left: -42px;
      top: 26px;
      width: 18px;
      height: 18px;
      border-radius: 50%;
      background: #0284c7;
      border: 3px solid #090d16;
    }}
    .node-card.status-CONNECT_OK::before {{ background: #22c55e; }}
    .node-card.status-NEW_DAY::before {{ background: #ef4444; }}
    .node-card.status-GAP_DISCONTINUOUS::before {{ background: #f59e0b; }}
    
    .node-top {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 10px;
      border-bottom: 1px solid #1e293b;
      padding-bottom: 12px;
      margin-bottom: 14px;
    }}
    .node-idx {{
      font-size: 19px;
      font-weight: 800;
      color: #38bdf8;
    }}
    .status-badge {{
      display: inline-block;
      padding: 4px 10px;
      border-radius: 4px;
      font-size: 13px;
      font-weight: 700;
    }}
    .badge-CONNECT_OK {{ background: #14532d; color: #86efac; border: 1px solid #22c55e; }}
    .badge-NEW_DAY {{ background: #7f1d1d; color: #fca5a5; border: 1px solid #ef4444; }}
    .badge-GAP_DISCONTINUOUS {{ background: #78350f; color: #fde68a; border: 1px solid #f59e0b; }}
    .badge-START {{ background: #1e3a8a; color: #bfdbfe; border: 1px solid #3b82f6; }}
    
    .node-details {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 12px;
      font-size: 15px;
    }}
    .detail-item strong {{
      color: #94a3b8;
    }}
    .detail-val {{
      color: #f1f5f9;
      font-weight: 600;
    }}
    
    .link-box {{
      margin-top: 12px;
      padding: 10px 14px;
      background: #090d16;
      border-radius: 6px;
      border-left: 4px solid #3b82f6;
      font-size: 14px;
    }}
    .node-card.status-CONNECT_OK .link-box {{ border-left-color: #22c55e; }}
    .node-card.status-NEW_DAY .link-box {{ border-left-color: #ef4444; }}
    .node-card.status-GAP_DISCONTINUOUS .link-box {{ border-left-color: #f59e0b; }}
    
    .dup-alert {{
      margin-top: 10px;
      padding: 8px 12px;
      background: #1e1b4b;
      border: 1px solid #4338ca;
      border-radius: 6px;
      color: #c7d2fe;
      font-size: 13.5px;
    }}
    
    .img-preview-box {{
      margin-top: 14px;
      background: #050811;
      border: 1px solid #1e293b;
      border-radius: 6px;
      padding: 10px;
      text-align: center;
      max-height: 480px;
      overflow-y: auto;
    }}
    .img-thumb {{
      max-width: 100%;
      height: auto;
      border-radius: 4px;
      cursor: zoom-in;
      transition: transform 0.2s;
    }}
    .img-thumb:hover {{
      transform: scale(1.01);
    }}
    
    /* MODAL POPUP */
    .img-modal {{
      display: none;
      position: fixed;
      z-index: 9999;
      left: 0;
      top: 0;
      width: 100%;
      height: 100%;
      background: rgba(0, 0, 0, 0.92);
      backdrop-filter: blur(8px);
      align-items: center;
      justify-content: center;
      flex-direction: column;
    }}
    .img-modal.open {{
      display: flex;
    }}
    .modal-img {{
      max-width: 92vw;
      max-height: 85vh;
      object-fit: contain;
      border-radius: 6px;
      border: 1px solid #334155;
      box-shadow: 0 10px 30px rgba(0,0,0,0.8);
    }}
    .modal-caption {{
      color: #94a3b8;
      margin-top: 12px;
      font-size: 16px;
      font-weight: 600;
    }}
    .modal-close {{
      position: absolute;
      top: 20px;
      right: 30px;
      font-size: 32px;
      color: #ffffff;
      cursor: pointer;
    }}
  </style>
</head>
<body>
  <div class="top-header">
    <div class="header-title">
      <span>🏛️ แดชบอร์ดตรวจสอบการร้อยเรียงภาพแชททุกภาพสู่ SSOT (Single Line Stream Audit)</span>
    </div>
    <div class="header-sub">
      พิสูจน์การร้อยเรียงตามกฎ Knowledge ๓ เสาหลัก: คัดเลือกรูปแรก • ตัดภาพซ้ำ 100% • ตรวจหมุดวันที่ในแอป • ตรวจสอบความต่อเนื่องของเวลา
    </div>
    
    <div class="stats-grid">
      <div class="stat-card">
        <div class="stat-val">{total_raw_count}</div>
        <div class="stat-label">📁 ไฟล์ภาพทั้งหมดจากทุกโฟลเดอร์</div>
      </div>
      <div class="stat-card">
        <div class="stat-val" style="color: #38bdf8;">{len(master_nodes)}</div>
        <div class="stat-label">💎 ภาพต้นฉบับชั้นต้น (Unique Masters)</div>
      </div>
      <div class="stat-card">
        <div class="stat-val" style="color: #f43f5e;">{len(duplicate_records)}</div>
        <div class="stat-label">⛔ ภาพซ้ำที่คัดกรองทิ้ง (Duplicates)</div>
      </div>
      <div class="stat-card">
        <div class="stat-val" style="color: #22c55e;">{connect_ok_count}</div>
        <div class="stat-label">🟢 จุดที่เชื่อมต่อได้ต่อเนื่อง (Monotonic)</div>
      </div>
      <div class="stat-card">
        <div class="stat-val" style="color: #ef4444;">{new_day_count}</div>
        <div class="stat-label">🔴 จุดที่ขึ้นวันใหม่ (New Day Date Pill)</div>
      </div>
      <div class="stat-card">
        <div class="stat-val" style="color: #f59e0b;">{gap_count}</div>
        <div class="stat-label">🟡 จุดที่ขาดตอน / ปล่อยช่องว่างไว้</div>
      </div>
    </div>
    
    <div class="controls-bar">
      <button class="btn-filter active" onclick="filterStatus('ALL')">ดูทั้งหมด ({len(master_nodes)} โหนด)</button>
      <button class="btn-filter" onclick="filterStatus('CONNECT_OK')">🟢 เฉพาะจุดเชื่อมต่อได้ ({connect_ok_count})</button>
      <button class="btn-filter" onclick="filterStatus('NEW_DAY')">🔴 เฉพาะจุดขึ้นวันใหม่ ({new_day_count})</button>
      <button class="btn-filter" onclick="filterStatus('GAP_DISCONTINUOUS')">🟡 เฉพาะจุดที่ขาดตอน/ปล่อยว่าง ({gap_count})</button>
      <button class="btn-filter" onclick="filterStatus('HAS_DUP')">⛔ โหนดที่มีภาพซ้ำคู่ขนาน ({sum(1 for n in master_nodes if n['duplicates'])})</button>
      <input type="text" class="search-input" id="searchBox" placeholder="🔍 ค้นหาชื่อไฟล์, โฟลเดอร์, วันที่, หรือเวลา..." oninput="handleSearch()">
    </div>
  </div>

  <div class="stream-container">
    <div class="timeline-stream" id="timelineStream">
'''

# สร้างการ์ดสำหรับแต่ละ Master Node
for node in master_nodes:
    status_cls = f"status-{node['link_status']}"
    badge_cls = f"badge-{node['link_status']}"
    
    badge_label = {
        'START': '🔵 จุดเริ่มต้นสายพาน (Genesis Node)',
        'CONNECT_OK': '🟢 เชื่อมต่อได้ต่อเนื่อง (Monotonic Flow)',
        'NEW_DAY': '🔴 ก้าวข้ามสู่วันใหม่ (Date Separator)',
        'GAP_DISCONTINUOUS': '🟡 ขาดตอน / ปล่อยช่องว่างไว้ (Discontinuous)'
    }.get(node['link_status'], node['link_status'])
    
    date_display = node['date_in_app'] if node['date_in_app'] else '<span style="color: #64748b;">[ไม่มีแถบวันที่ - ปล่อยช่องว่างไว้ตามกฎ]</span>'
    time_display = node['time_span'] if node['time_span'] else '<span style="color: #64748b;">[ไม่มีไทม์แสตมป์เวลาบับเบิ้ล]</span>'
    
    dup_html = ''
    if node['duplicates']:
        dup_names = ', '.join([f"<code>{d['source']}/{d['filename']}</code>" for d in node['duplicates']])
        dup_html = f'''<div class="dup-alert">
          ⛔ <strong>ตรวจพบคู่ขนานซ้ำ {len(node['duplicates'])} ไฟล์:</strong> {dup_names} 
          <br><small style="color: #a5b4fc;">➔ ระบบตัดสำเนาซ้ำทิ้งและเลือกไฟล์นี้เป็น Master เพียงหนึ่งเดียวตามกฎข้อ ๑</small>
        </div>'''
        
    has_dup_attr = "true" if node['duplicates'] else "false"
    web_asset_src = node['web_asset']
    raw_file_uri = node['path'].replace('\\', '/')
    
    html_out += f'''
      <div class="node-card {status_cls}" data-status="{node['link_status']}" data-has-dup="{has_dup_attr}">
        <div class="node-top">
          <div class="node-idx">#NODE-{node['id']:03d}: {node['filename']}</div>
          <span class="status-badge {badge_cls}">{badge_label}</span>
        </div>
        
        <div class="node-details">
          <div class="detail-item"><strong>📂 แหล่งที่มา (Master Source):</strong> <span class="detail-val">{node['source']}</span></div>
          <div class="detail-item"><strong>📑 ประเภทไฟล์:</strong> <span class="detail-val">{node['type']}</span> ({node['width']}x{node['height']} px, AR: {node['aspect_ratio']})</div>
          <div class="detail-item"><strong>📅 หมุดวันที่ในแอป:</strong> <span class="detail-val">{date_display}</span></div>
          <div class="detail-item"><strong>⏰ ไทม์แสตมป์เวลา:</strong> <span class="detail-val">{time_display}</span></div>
        </div>
        
        <div class="link-box">
          <strong>🔗 ความต่อเนื่องกับภาพก่อนหน้า:</strong> {node['link_reason']}
        </div>
        
        {dup_html}
        
        <div class="img-preview-box">
          <img src="{web_asset_src}" 
               onerror="this.onerror=null; this.src='file:///{raw_file_uri}';" 
               class="img-thumb" 
               loading="lazy" 
               alt="{node['filename']}" 
               title="คลิกเพื่อขยายดูภาพขนาดใหญ่"
               onclick="openModal('{web_asset_src}', '{node['filename']}', '{node['source']}')">
        </div>
      </div>
'''

html_out += '''
    </div>
  </div>

  <!-- MODAL VIEWER -->
  <div id="imgModal" class="img-modal" onclick="closeModal()">
    <span class="modal-close">&times;</span>
    <img id="modalImg" class="modal-img" src="" alt="Full View">
    <div id="modalCaption" class="modal-caption"></div>
  </div>

  <script>
    function filterStatus(status) {
      document.querySelectorAll('.btn-filter').forEach(b => b.classList.remove('active'));
      event.target.classList.add('active');
      
      const cards = document.querySelectorAll('.node-card');
      cards.forEach(card => {
        if (status === 'ALL') {
          card.style.display = 'block';
        } else if (status === 'HAS_DUP') {
          card.style.display = card.getAttribute('data-has-dup') === 'true' ? 'block' : 'none';
        } else {
          card.style.display = card.getAttribute('data-status') === status ? 'block' : 'none';
        }
      });
    }

    function handleSearch() {
      const q = document.getElementById('searchBox').value.toLowerCase();
      const cards = document.querySelectorAll('.node-card');
      cards.forEach(card => {
        const text = card.innerText.toLowerCase();
        card.style.display = text.includes(q) ? 'block' : 'none';
      });
    }

    function openModal(src, filename, source) {
      const modal = document.getElementById('imgModal');
      const img = document.getElementById('modalImg');
      const cap = document.getElementById('modalCaption');
      img.src = src;
      cap.innerText = filename + ' (' + source + ')';
      modal.classList.add('open');
    }

    function closeModal() {
      document.getElementById('imgModal').classList.remove('open');
    }
  </script>
</body>
</html>
'''

# 7. บันทึกผลลัพธ์
viewer_path = r'd:\Project\ชวกม.2\EDOK_NUI\MASTER_SSOT_STITCH_VIEWER.html'
art_viewer_path = r'C:\Users\EVE\.gemini\antigravity\brain\c8211d09-030e-4b24-8837-3ce9589aa4a6\MASTER_SSOT_STITCH_VIEWER.html'

with open(viewer_path, 'w', encoding='utf-8') as f:
    f.write(html_out)
with open(art_viewer_path, 'w', encoding='utf-8') as f:
    f.write(html_out)

print(f"Generated MASTER SSOT STITCH VIEWER successfully at: {viewer_path}")

import json

with open(r'D:\Project\ชวกม.2\EDOK_NUI\MASTER_TRANSCRIPT_CHRONOLOGICAL.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

target_keywords = ['พี่แมว', 'บุญประเสริฐ', 'วันวิศา', 'ทัศนีการ', 'ปรียชาติ', 'กัญญาภัค', 'เบญจมาศ', 'สุธีรัตน์', 'เหมือนขวัญ', 'ชนัญชิดามนต์']

found_events = []
current_date = 'ไม่ระบุวันที่'

for idx, line in enumerate(lines):
    if line.startswith('## 📅'):
        current_date = line.replace('## 📅', '').strip()
    
    for kw in target_keywords:
        if kw in line:
            start = max(0, idx - 2)
            end = min(len(lines), idx + 3)
            ctx = [lines[j].strip() for j in range(start, end)]
            found_events.append({
                'keyword': kw,
                'line_no': idx + 1,
                'date': current_date,
                'matched_line': line.strip(),
                'context': ctx
            })

print(f'Total target events found in transcript: {len(found_events)}')
for ev in found_events:
    kw = ev['keyword']
    lno = ev['line_no']
    dt = ev['date']
    m = ev['matched_line']
    print(f'[{kw}] Line {lno} ({dt}) -> {m}')

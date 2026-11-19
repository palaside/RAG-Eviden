import json
import re

with open('all_scanned_slips.json', 'r', encoding='utf-8') as f:
    slips = json.load(f)

print(f"Total slips in all_scanned_slips.json: {len(slips)}")

targets = {
    'jinnipha': [],
    'cat_preeyachat': [],
    'sisters': [],
    'other': []
}

for s in slips:
    txt = s.get('raw_snippet', '')
    rec = s.get('recipient_name', '') or ''
    full = f"{txt} {rec}"
    
    if any(k in full for k in ['จิณห์นิภา', 'จินห์นิภา', 'ประสาทเขต', '996-5']):
        targets['jinnipha'].append(s)
    elif any(k in full for k in ['ปรียาฉัตร', 'ชิมพลี']):
        targets['cat_preeyachat'].append(s)
    elif any(k in full for k in ['วรรณวิสา', 'ทัศนียกานต์', 'พลูสวัสดิ์']):
        targets['sisters'].append(s)
    else:
        targets['other'].append(s)

print(f"all_scanned_slips -> Jinnipha: {len(targets['jinnipha'])}")
print(f"all_scanned_slips -> Cat/Preeyachat: {len(targets['cat_preeyachat'])}")
print(f"all_scanned_slips -> Sisters: {len(targets['sisters'])}")
print(f"all_scanned_slips -> Other: {len(targets['other'])}")

# Check NEW_362_FILES_SCAN_RESULTS.json
try:
    with open('EDOK_NUI/NEW_362_FILES_SCAN_RESULTS.json', 'r', encoding='utf-8') as f:
        new_362 = json.load(f)
    print(f"Total new_362 items: {len(new_362)}")
    new_targets = {'jinnipha': 0, 'cat': 0, 'sisters': 0}
    for item in new_362:
        snip = item.get('snippet', '')
        if any(k in snip for k in ['จิณห์นิภา', 'จินห์นิภา', 'ประสาทเขต', '996-5']):
            new_targets['jinnipha'] += 1
        if any(k in snip for k in ['ปรียาฉัตร', 'ชิมพลี']):
            new_targets['cat'] += 1
        if any(k in snip for k in ['วรรณวิสา', 'ทัศนียกานต์']):
            new_targets['sisters'] += 1
    print(f"new_362 breakdown: {new_targets}")
except Exception as e:
    print(f"Error checking new_362: {e}")

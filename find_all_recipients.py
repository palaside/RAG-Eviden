import json, re
from collections import Counter

# 1. Load slips
with open(r'D:\Project\ชวกม.2\all_scanned_slips.json', encoding='utf-8') as f:
    slips = json.load(f)

# 2. Load chat cache
with open(r'D:\Project\ชวกม.2\chat_ori_cache.json', encoding='utf-8') as f:
    chat_cache = json.load(f)

# 3. Load master transcript
with open(r'D:\Project\ชวกม.2\EDOK_NUI\MASTER_TRANSCRIPT_CHRONOLOGICAL.md', encoding='utf-8') as f:
    master_transcript = f.read()

# Combine all texts
all_text = master_transcript + '\n' + '\n'.join(chat_cache.values())

for s in slips:
    all_text += '\n' + s.get('raw_snippet', '')

# Pattern for Thai names
name_pattern = re.compile(r'(?:นาย|นางสาว|น\.ส\.|นาง)\s*([^\s\d\(\)\[\]\,\:\'\"\.\;\<\>\-\+\_\=\/]{2,25}(?:\s+[^\s\d\(\)\[\]\,\:\'\"\.\;\<\>\-\+\_\=\/]{2,25})?)')
matches = name_pattern.findall(all_text)

counts = Counter([m.strip() for m in matches])

print('=== ALL NAMES FOUND (excluding victim) ===')
victim_keywords = ['ณัฐชัย', 'ณชบุชย', 'ญัฐขชัย', 'ณรชูชย', 'พญัฐชัย', 'สิบตรี']

cleaned_names = []
for name, c in counts.most_common():
    if not any(v in name for v in victim_keywords) and len(name) > 3:
        cleaned_names.append((name, c))

for name, c in cleaned_names[:60]:
    print(f'{name}: {c} occurrences')

with open('current_main.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = list(re.finditer(r'<section\b', text))
print('Sections inside main:', len(matches))
for i, m in enumerate(matches):
    print(f'Section {i} at {m.start()}')

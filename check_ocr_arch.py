import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

matches = [m.start() for m in re.finditer(r'function\s+inspectItemGemini', text)]
print('inspectItemGemini definitions:', len(matches))
if matches:
    pos = matches[0]
    print(text[pos:pos+1500])

for m in re.finditer(r'Gemini 3\.1 Pro', text):
    start = max(0, m.start() - 150)
    end = min(len(text), m.end() + 250)
    print('Context of Gemini 3.1 Pro:\n', text[start:end])

# Also check server.js for Gemini or OCR
with open('server.js', 'r', encoding='utf-8') as f:
    srv = f.read()

print('server.js length:', len(srv))
gemini_in_srv = [m.start() for m in re.finditer(r'gemini', srv, re.IGNORECASE)]
print('gemini occurrences in server.js:', len(gemini_in_srv))
for g in gemini_in_srv[:5]:
    print('server.js snippet:\n', srv[max(0, g-100):min(len(srv), g+200)])

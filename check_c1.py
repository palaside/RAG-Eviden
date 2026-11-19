with open(r'd:\Project\ชวกม.2\build_court_dossier_smart_cropped.py', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('"count_title": "กรรมที่ ๑')
print(text[start:start+700])

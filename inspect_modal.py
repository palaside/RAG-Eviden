with open('index.html', 'r', encoding='utf-8') as fp:
    text = fp.read()
pos = text.find('id="timelineModal"')
print(text[pos:pos+2500])

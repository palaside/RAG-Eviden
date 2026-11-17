import fitz

doc = fitz.open()
page = doc.new_page()
font_path = r"C:\Windows\Fonts\tahoma.ttf"
page.insert_font(fontname="tahoma", fontfile=font_path)
page.insert_text(fitz.Point(50, 100), "ทดสอบภาษาไทย เวกเตอร์แท้ 100%", fontname="tahoma", fontsize=14)
doc.save(r"d:\Project\ชวกม.2\test_thai_vector.pdf")
doc.close()
print("Success!")

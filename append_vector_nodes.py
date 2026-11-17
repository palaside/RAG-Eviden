import json

new_nodes = [
    {
        'event_id': 173,
        'timestamp': '27 พ.ค. 2568',
        'speaker': 'จิณห์นิภา (ฝ่ายขอยืม/จำเลย)',
        'content': 'ส่งเลขบัญชี 2 พี่น้อง: วันวิศา ประสาทเขตรการ ออมสิน 020333988630 ยอด 21,000 บาท และ ทัศนีการ ประสาทเขตรการ พร้อมเพย์ 0912634123 ยอด 5,000 บาท',
        'amount': '**26,000 บาท (21k + 5k)**',
        'reference_image': '`A4_Full_27.5.68 พี่น้อง_IMG_6243.PNG`',
        'page_number': 173,
        'is_monetary_event': True,
        'target_entities': ['tatsaneekan', 'wanwisa', 'jinnipha']
    },
    {
        'event_id': 174,
        'timestamp': '26 พ.ค. 2568 (16:54 น.)',
        'speaker': 'พี่แมว (ปรียชาติ ฉิมพลี / รุ่นพี่ตัวการ)',
        'content': 'แชทกับพี่แมว: เงินน่าจะได้วันนี้ จัดการภาระเค้าก่อน เค้าจะโอนเงินให้ พร้อมส่งเลขบัญชี กสิกร 28125484551 (ปรียชาติ ฉิมพลี)',
        'amount': '**ประสานโอนเงิน**',
        'reference_image': '`26.5.68 พี่แมว_IMG_6242 (2).PNG`',
        'page_number': 174,
        'is_monetary_event': True,
        'target_entities': ['preeyachat_chimplee', 'jinnipha']
    },
    {
        'event_id': 175,
        'timestamp': '02 มิ.ย. 2568 (16:45 น.)',
        'speaker': 'ส.ต. ณัฐชัย ➔ ปรียชาติ ฉิมพลี',
        'content': 'สลิปโอนเงินเข้าบัญชี น.ส. ปรียชาติ จฉิมพลี ธ.กสิกรไทย 455-1 ยอด 9,000 บาท โดยมีบันทึกช่วยจำระบุสัญญาชัดเจนว่า คืน 10000 วันที่ 3 มิ.ย.',
        'amount': '**9,000 บาท (สัญญาคืน 10,000)**',
        'reference_image': '`03.6.68 พี่แมว_IMG_6246.PNG`',
        'page_number': 175,
        'is_monetary_event': True,
        'target_entities': ['preeyachat_chimplee']
    },
    {
        'event_id': 176,
        'timestamp': '08 มิ.ย. 2568 (19:41 น.)',
        'speaker': 'ส.ต. ณัฐชัย ➔ ปรียชาติ ฉิมพลี',
        'content': 'สลิปโอนเงินเข้าบัญชี น.ส. ปรียชาติ ฉิมพลี ธ.กสิกรไทย 455-1 ยอด 13,500 บาท โดยมีบันทึกช่วยจำระบุสัญญาชัดเจนว่า คืน 9/6 ยอด 15000',
        'amount': '**13,500 บาท (สัญญาคืน 15,000)**',
        'reference_image': '`08.6.68 พี่แมว_LINE_capture_796547198.800971.JPG`',
        'page_number': 176,
        'is_monetary_event': True,
        'target_entities': ['preeyachat_chimplee']
    },
    {
        'event_id': 177,
        'timestamp': '19 มิ.ย. 2568 (20:08 น.)',
        'speaker': 'จิณห์นิภา ➔ ปรียชาติ ฉิมพลี',
        'content': 'สลิปจิณห์นิภาโอนเงินต่อจากบัญชี ttb 996-5 ไปยัง น.ส. ปรียชาติ ธ.กสิกรไทย 455-1 ยอด 5,000 บาท แล้วส่งให้ผู้เสียหายดู',
        'amount': '**5,000 บาท**',
        'reference_image': '`IMG_2622.PNG`',
        'page_number': 177,
        'is_monetary_event': True,
        'target_entities': ['preeyachat_chimplee', 'jinnipha']
    },
    {
        'event_id': 178,
        'timestamp': '02 ก.ค. 2568 (21:04 น.)',
        'speaker': 'จิณห์นิภา ➔ กัญญาภัค ฉิมพลี',
        'content': 'สลิปจิณห์นิภาโอนเงินต่อจากบัญชี ttb 996-5 ไปยัง นางสาว กัญญาภัค ฉิมพลี พร้อมเพย์ 2926 ยอด 15,000 บาท แล้วส่งให้ผู้เสียหายดู',
        'amount': '**15,000 บาท**',
        'reference_image': '`IMG_2800.PNG`',
        'page_number': 178,
        'is_monetary_event': True,
        'target_entities': ['preeyachat_chimplee', 'jinnipha']
    },
    {
        'event_id': 179,
        'timestamp': '08 ก.พ. 2568 (13:22 น.)',
        'speaker': 'จิณห์นิภา ➔ วันวิศา ประสาทเขตรการ',
        'content': 'สลิปจิณห์นิภาโอนเงินให้ วันวิศา ประสาทเขตรการ บัญชีกรุงไทย 083-0 ยอด 2,000 บาท และมีแชทกำกับใต้สลิปชัดเจนว่า สรุปจ่ายแม่',
        'amount': '**2,000 บาท**',
        'reference_image': '`LINE_capture_800256213.882803.jpg`',
        'page_number': 179,
        'is_monetary_event': True,
        'target_entities': ['wanwisa', 'jinnipha']
    }
]

p = r'D:\Project\ชวกม.2\EDOK_NUI\timeline_vector_embeddings.jsonl'
with open(p, 'a', encoding='utf-8') as f:
    for n in new_nodes:
        f.write(json.dumps(n, ensure_ascii=False) + '\n')

print(f'Appended {len(new_nodes)} new nodes to timeline_vector_embeddings.jsonl!')

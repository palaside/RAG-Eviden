import re
import json

with open('COURT_TIMELINE_DOSSIER.md', 'r', encoding='utf-8') as f:
    text = f.read()

events = text.split('### เหตุการณ์ที่ ')
print(f"Total events in dossier: {len(events)-1}")

money_events = []
for ev in events[1:]:
    lines = ev.split('\n')
    header = lines[0]
    ev_num = header.split(':')[0].strip()
    
    # Extract fields
    m_money = re.search(r'ยอดเงิน[:\s\*]+([0-9,]+(?:\.[0-9]{2})?)\s*บาท', ev)
    m_date = re.search(r'วันเวลาเกิดเหตุ[:\s\*]+([^\n\r]+)', ev)
    m_chat = re.search(r'บริบทแชท[:\s\*]+([^\n\r]+)', ev)
    m_ref = re.search(r'อ้างอิงหลักฐาน[:\s\*]+([^\n\r]+)', ev)
    m_modus = re.search(r'วิเคราะห์พฤติการณ์[:\s\*]+([^\n\r]+)', ev)
    m_smoke = re.search(r'Smoking Gun[:\s\*]+([^\n\r]+)', ev)
    m_counter = re.search(r'วิเคราะห์พลิกเกมส์[:\s\*]+([^\n\r]+)', ev)
    m_demand = re.search(r'คำขอต่อศาล[:\s\*]+([^\n\r]+)', ev)

    if m_money:
        amt_str = m_money.group(1).replace(',', '')
        try:
            amt = float(amt_str)
            if amt > 0:
                money_events.append({
                    'ev_num': ev_num,
                    'header': header,
                    'amount': amt,
                    'date': m_date.group(1).strip() if m_date else 'ไม่ระบุ',
                    'chat': m_chat.group(1).strip() if m_chat else 'ตามพยานหลักฐานในแชท',
                    'ref': m_ref.group(1).strip() if m_ref else '',
                    'modus': m_modus.group(1).strip() if m_modus else '',
                    'smoke': m_smoke.group(1).strip() if m_smoke else '',
                    'counter': m_counter.group(1).strip() if m_counter else '',
                    'demand': m_demand.group(1).strip() if m_demand else '',
                    'raw': ev
                })
        except:
            pass

print(f"Total money events found: {len(money_events)}")
total_amt = sum(x['amount'] for x in money_events)
print(f"Total Sum: {total_amt:,.2f} บาท")

with open('EDOK_NUI/JINNIPHA_MONEY_EVENTS.json', 'w', encoding='utf-8') as f:
    json.dump(money_events, f, ensure_ascii=False, indent=2)

print("Saved to EDOK_NUI/JINNIPHA_MONEY_EVENTS.json")

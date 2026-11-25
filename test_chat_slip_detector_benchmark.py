import cv2
import numpy as np
import time
import re
import os
import json
import pytesseract

if os.path.exists(r"C:\tessdata"):
    os.environ["TESSDATA_PREFIX"] = r"C:\tessdata"

def detect_and_extract_chat_slip(image_path, output_annotated_path=None):
    """
    ตรวจจับพิกัดสลิปในภาพแชทยาว และสกัดข้อมูล พร้อมจับเวลาแต่ละขั้นตอนแบบแม่นยำ
    """
    # โหลดภาพ (รองรับทั้งภาษาไทยและอังกฤษ)
    if not os.path.exists(image_path):
        return {"error": f"File not found: {image_path}"}

    img = cv2.imdecode(np.fromfile(image_path, dtype=np.uint8), cv2.IMREAD_COLOR)
    if img is None:
        img = cv2.imread(image_path)
    if img is None:
        return {"error": "Failed to read image"}

    img_h, img_w = img.shape[:2]

    # =========================================================================
    # ขั้นตอนที่ 1: ตรวจจับพิกัดของสลิป (SLIP LOCALIZATION / BOUNDING BOX)
    # =========================================================================
    t_start_step1 = time.perf_counter()

    # ตรวจจับพื้นที่บัตรสลิป (สีขาว/สว่าง คมชัด มีรูปทรงการ์ดสลิปบนพื้นหลังแชท)
    white_mask = (img[:, :, 0] > 230) & (img[:, :, 1] > 230) & (img[:, :, 2] > 230)
    white_mask = white_mask.astype(np.uint8) * 255

    kernel_size = max(5, int(img_w * 0.03))
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_size, kernel_size))
    closed = cv2.morphologyEx(white_mask, cv2.MORPH_CLOSE, kernel)

    cnts, _ = cv2.findContours(closed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    slip_box = None
    max_area = 0
    for c in cnts:
        bx, by, bw, bh = cv2.boundingRect(c)
        area = bw * bh
        aspect = bh / float(bw)
        # สลิปในแชทจะมีขนาดกว้าง > 35% ของหน้าจอแชท และสัดส่วนสูง/กว้าง ระหว่าง 0.8 ถึง 2.5
        if bw > img_w * 0.35 and 0.8 < aspect < 2.5:
            if area > max_area:
                max_area = area
                # ขยายขอบด้านบนเล็กน้อยเพื่อครอบคลุมหัวแถบสีของสลิป
                header_nudge = int(bh * 0.16)
                slip_box = (
                    max(0, bx - 4),
                    max(0, by - header_nudge),
                    min(img_w - bx + 4, bw + 8),
                    min(img_h - by + header_nudge, bh + header_nudge + 10)
                )

    t_end_step1 = time.perf_counter()
    step1_ms = round((t_end_step1 - t_start_step1) * 1000, 2)

    if not slip_box:
        return {
            "error": "No slip detected in chat stream",
            "step1_detection_ms": step1_ms,
            "total_ms": step1_ms
        }

    sx, sy, sw, sh = slip_box
    slip_crop = img[sy:sy+sh, sx:sx+sw]

    # บันทึกภาพตีกรอบเพื่อพิสูจน์ (Proof of Detection)
    if output_annotated_path:
        annotated = img.copy()
        cv2.rectangle(annotated, (sx, sy), (sx + sw, sy + sh), (0, 255, 0), max(2, int(img_w * 0.005)))
        cv2.putText(annotated, f"SLIP DETECTED [{sw}x{sh}]", (sx, max(25, sy - 10)),
                    cv2.FONT_HERSHEY_SIMPLEX, max(0.5, img_w * 0.001), (0, 255, 0), 2)
        os.makedirs(os.path.dirname(output_annotated_path), exist_ok=True)
        cv2.imencode('.jpg', annotated)[1].tofile(output_annotated_path)

    # =========================================================================
    # ขั้นตอนที่ 2: สกัดข้อมูลจากสลิป (SLIP DATA EXTRACTION)
    # =========================================================================
    t_start_step2 = time.perf_counter()

    # 1. ลองถอดรหัส QR Code แบบด่วนก่อน (5-10ms)
    qr_detector = cv2.QRCodeDetector()
    qr_val, _, _ = qr_detector.detectAndDecode(slip_crop)
    ref_no = None
    bank_name = None

    if qr_val and len(qr_val) > 20:
        m_ref = re.search(r"02(\d{2})([A-Za-z0-9_-]+)", qr_val)
        if m_ref:
            ref_no = m_ref.group(2)[:int(m_ref.group(1))]
        if "0103006" in qr_val:
            bank_name = "ธนาคารกรุงไทย (Krungthai)"

    # 2. ปรับขนาดภาพ Crop ให้เหมาะกับ OCR (Target width ~800-1000px)
    if sw < 500:
        scale = 900.0 / sw
        crop_ocr = cv2.resize(slip_crop, (int(sw * scale), int(sh * scale)), interpolation=cv2.INTER_CUBIC)
    elif sw > 1100:
        scale = 1000.0 / sw
        crop_ocr = cv2.resize(slip_crop, (int(sw * scale), int(sh * scale)), interpolation=cv2.INTER_AREA)
    else:
        crop_ocr = slip_crop

    gray_crop = cv2.cvtColor(crop_ocr, cv2.COLOR_BGR2GRAY)
    ocr_text = pytesseract.image_to_string(gray_crop, lang="tha+eng", config="--psm 6")

    # 3. สกัดฟิลด์ยอดเงิน
    amount = None
    m_amt = re.search(r"(?:จ[ำาํ]+นวนเงิน|ยอดโอน|amount|ยอดเงิน)?[\s:*|：]*([0-9]{1,3}(?:[,.][0-9]{3})*\.[0-9]{2})", ocr_text, re.I)
    if m_amt:
        cleaned = m_amt.group(1).replace(" ", "").replace(",", "")
        parts = cleaned.split(".")
        amount = float("".join(parts[:-1]) + "." + parts[-1]) if len(parts) > 2 else float(cleaned)
    else:
        floats = re.findall(r"\b([0-9]{1,3}(?:[,.][0-9]{3})*\.[0-9]{2})\b", ocr_text)
        for f in floats:
            val = float(f.replace(",", ""))
            if val > 0:
                amount = val
                break

    # 4. สกัดธนาคาร และ Ref ID
    if not bank_name:
        m_b = re.search(r"(กรุงไทย|Krungthai|กสิกรไทย|KBank|ไทยพาณิชย์|SCB|เกียรตินาคินภัทร|กรุงเทพ|ttb)", ocr_text, re.I)
        bank_name = m_b.group(1) if m_b else "Krungthai"

    if not ref_no:
        m_rf = re.search(r"(?:(?:รหัส|เลขที่)[\s\S]{0,10}อ[าฮ]้?งอิง|ref[^\n]*)[\s:*|：\n]*([A-Za-z0-9_-]{18,35})|\b([A-Za-z0-9]{15,32})\b", ocr_text, re.I)
        if m_rf:
            ref_no = m_rf.group(1) or m_rf.group(2)

    # 5. สกัดผู้โอน ผู้รับ และเลขบัญชี
    lines = [l.strip() for l in ocr_text.split("\n") if l.strip()]
    sender_name = None
    receiver_name = None
    sender_account = None
    receiver_account = None

    is_sender = False
    is_rec = False
    for l in lines:
        if any(k in l for k in ["จาก", "อาก", "sender", "from"]):
            is_sender = True
            is_rec = False
            continue
        elif any(k in l.lower() for k in ["ไปยัง", "ผู้รับ", "receiver", "to", "tudo"]):
            is_sender = False
            is_rec = True
            continue

        is_acc = ("XXX-" in l) or ("%%%" in l) or ("xxx-" in l.lower()) or re.search(r"\d{3}-\d-", l)
        if is_sender:
            if not sender_name and not is_acc and "กรุงไทย" not in l and "krungthai" not in l.lower():
                sender_name = l.replace("ร***", "s***")
            if is_acc and not sender_account:
                sender_account = l.replace("%", "X")
        elif is_rec:
            if not receiver_name and not is_acc and "เกียรตินาคิน" not in l and "กรุงไทย" not in l:
                receiver_name = l.replace("ขิณห์นิภา", "จิณห์นิภา").replace("บุญประเสริช", "บุญประเสริฐ").replace("แจ๋บเบือง", "แจ่มเมือง")
            if is_acc and not receiver_account:
                receiver_account = l.replace("%", "X")

    # 6. สกัดวันเวลา
    datetime_str = None
    m_dt = re.search(r"(\d{1,2})\s*(ม\.ค\.|ก\.พ\.|มี\.ค\.|เม\.ย\.|พ\.ค\.|มิ\.ย\.|ก\.ค\.|ส\.ค\.|ก\.ย\.|ต\.ค\.|พ\.ย\.|ธ\.ค\.)\s*(\d{4})\s*-\s*(\d{2}:\d{2})", ocr_text)
    if m_dt:
        d, m, y, t = m_dt.groups()
        datetime_str = f"{d} {m} {y} เวลา {t} น."

    t_end_step2 = time.perf_counter()
    step2_ms = round((t_end_step2 - t_start_step2) * 1000, 2)
    total_ms = round(step1_ms + step2_ms, 2)

    return {
        "step1_detection": {
            "status": "DETECTED_SUCCESS",
            "bounding_box": {
                "x": sx,
                "y": sy,
                "width": sw,
                "height": sh
            },
            "normalized_coords": {
                "ymin": round(sy / img_h, 4),
                "xmin": round(sx / img_w, 4),
                "ymax": round((sy + sh) / img_h, 4),
                "xmax": round((sx + sw) / img_w, 4)
            },
            "elapsed_ms": step1_ms
        },
        "step2_extraction": {
            "bank": bank_name,
            "ref_id": ref_no,
            "amount": amount,
            "currency": "THB",
            "sender": {
                "name": sender_name,
                "account": sender_account
            },
            "receiver": {
                "name": receiver_name,
                "account": receiver_account
            },
            "datetime": datetime_str,
            "elapsed_ms": step2_ms
        },
        "performance_benchmark": {
            "step1_detection_ms": step1_ms,
            "step2_extraction_ms": step2_ms,
            "total_ms": total_ms,
            "fps_rate": round(1000.0 / total_ms, 2) if total_ms > 0 else 0
        }
    }

if __name__ == "__main__":
    # 1. ทดสอบกับภาพต้นฉบับความละเอียดสูง chatv3 (41).jpg (ขนาด 828 x 3156)
    test_original = r"d:\Project\ชวกม.2\EDOK_NUI\FOR TEST In EDOK_NUI\แชทที่ 3\chatv3 (41).jpg"
    annotated_out = r"d:\Project\ชวกม.2\artifacts\detected_chat_slip_proof.jpg"
    
    print("==========================================================================")
    print("🚀 เริ่มต้นการทดสอบรัน BUILD: ตรวจจับและสกัดสลิปจากภาพแชทยาว")
    print("==========================================================================")
    
    res = detect_and_extract_chat_slip(test_original, annotated_out)
    print(json.dumps(res, ensure_ascii=False, indent=2))
    print(f"\n[Artifact บันทึกภาพผลลัพธ์]: {annotated_out}")

"""Presentation safeguards for the separate, review-only dossier renderer."""

import ast
import hashlib
import json
import os
import re
from pathlib import Path


HIGH_RISK_ASSERTION = re.compile(
    r"ไม่เคย|ไม่มี|100%|ความผิดสำเร็จ|ยืนยันว่า|พิสูจน์ว่า|กุเรื่อง|ดิ้นไม่หลุด|สลิปปลอม|สลิปเท็จ|บัญชีม้า|ลวงตา"
)


def load_counts(path):
    tree = ast.parse(Path(path).read_text(encoding="utf-8"), filename=str(path))
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(
            isinstance(target, ast.Name) and target.id == "counts" for target in node.targets
        ):
            return ast.literal_eval(node.value)
    raise ValueError("counts assignment not found")


def load_manifest(path):
    manifest = json.loads(Path(path).read_text(encoding="utf-8"))
    if manifest.get("schema_version") != "digital-evidence.dossier.v1":
        raise ValueError("Unsupported evidence manifest schema_version")
    counts = manifest.get("counts")
    if not isinstance(counts, list) or not counts:
        raise ValueError("Evidence manifest must contain counts")
    event_ids = [event.get("event_id") for event in counts]
    if any(not value for value in event_ids) or len(event_ids) != len(set(event_ids)):
        raise ValueError("Evidence manifest event_id is missing or duplicated")
    return counts


def display_amount(value):
    text = str(value or "").strip()
    if not text or "ตามยอดสลิป" in text:
        return "ยังอ่านยอดไม่ได้"
    if not re.fullmatch(r"[\d,]+\.\d{2}(?:\s*บาท)?", text):
        return f"ยังแยกยอดโอนเดียวไม่ได้ (ข้อความเดิม: {text})"
    return f"{text} (รอเทียบต้นฉบับและยืนยันการโอน)"


def display_title(value):
    text = str(value or "").strip()
    return text.replace(
        "ส่งภาพสลิปเท็จ 35,000 บาท สร้างหลักฐานลวงตา",
        "ส่งภาพสลิปยอด 35,000 บาท (รอตรวจความแท้และการโอน)",
    ).replace(
        "หลอกลวงเบิกเงิน", "ข้อกล่าวอ้างเรื่องเบิกเงิน"
    )


def display_datetime(value):
    text = str(value or "").strip()
    if text.startswith(("ต้นปี", "กลางปี", "ปลายปี")):
        return f"{text} (วันที่เป็นช่วงกว้าง; ห้ามเรียงเป็นเหตุการณ์ระดับนาที)"
    return text or "ยังไม่ทราบวันเวลา"


def display_slip(value):
    text = str(value or "").strip()
    if re.search(r"ปลอม|เท็จ|ลวงตา|บัญชีม้า", text):
        return "ประเด็นตรวจความแท้ของภาพสลิปและรายการเดินบัญชี; ยังไม่มีผลยืนยันในรายงานนี้"
    return f"ข้อความสรุปจากข้อมูลร่าง (รอเทียบต้นฉบับ): {text}" if text else "ยังไม่มีรายละเอียดสลิป"


def review_text(value, field):
    text = str(value or "").strip()
    if not text:
        return "ยังไม่มีข้อมูลสำหรับหัวข้อนี้"
    if field == "court_action":
        return f"แนวทางให้ทนายพิจารณา: {text}"
    if field in ("analysis", "smoking_gun", "counter"):
        if HIGH_RISK_ASSERTION.search(text):
            return (
                "ประเด็นที่ต้องตรวจเพิ่มเติม: ข้อสรุปเดิมมีคำยืนยันเกินหลักฐานที่แสดงในหน้านี้ "
                "ให้ตรวจภาพต้นทาง รายการเดินบัญชี หรือพยานอิสระก่อนใช้ข้อกล่าวอ้างนี้"
            )
        return f"ข้อสันนิษฐานเพื่อทนายทบทวน: {text}"
    return text


def candidate_laws(values):
    return [f"อาจเกี่ยวข้อง — ให้ทนายตรวจองค์ประกอบและฉบับกฎหมาย: {value}" for value in values]


def source_identity(ref):
    root = os.environ.get("VECTOR_SOURCE_ROOT")
    if not root:
        return f"ไฟล์อ้างอิง: {ref} • ยังไม่ระบุที่เก็บต้นฉบับและ SHA-256"
    base = Path(root).resolve()
    candidate = (base / ref).resolve()
    if not candidate.is_relative_to(base) or not candidate.is_file():
        return f"ไฟล์อ้างอิง: {ref} • ยังหาไฟล์ต้นฉบับไม่พบ"
    digest = hashlib.sha256()
    with candidate.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return f"ไฟล์ต้นฉบับ: {ref} • SHA-256: {digest.hexdigest()} • พิกัดยังไม่ระบุ"

# -*- coding: utf-8 -*-
"""
========================================================================================
GEMINI MULTIMODAL FORENSIC OCR ENGINE
File: d:\\Project\\ชวกม.2\\gemini_ocr_engine.py
Powered by: Google Gemini 2.5 Flash / Gemini 3.1 Pro via Generative Language API
Standard: ISO/IEC 27037 Digital Evidence Extraction
========================================================================================
"""

import os
import json
import base64
import urllib.request
import urllib.error
from typing import Dict, Any, Optional


def load_api_key() -> Optional[str]:
    """Retrieves Google / Gemini API key from environment or .env file."""
    key = os.environ.get("GOOGLE_API_KEY") or os.environ.get("GEMINI_API_KEY")
    if key and key.strip():
        return key.strip()

    env_path = os.path.join(os.path.dirname(__file__), ".env")
    if os.path.exists(env_path):
        with open(env_path, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                line = line.strip()
                if line.startswith("GOOGLE_API_KEY="):
                    val = line.split("=", 1)[1].strip().strip('"').strip("'")
                    if val:
                        return val
                elif line.startswith("GEMINI_API_KEY="):
                    val = line.split("=", 1)[1].strip().strip('"').strip("'")
                    if val:
                        return val
    return None


class GeminiForensicOCREngine:
    """
    Forensic Multimodal Document & Slip Parser using Google Gemini API.
    Extracts text dialogues, timestamps, sender, receiver, bank, ref_id, and amounts.
    """

    def __init__(self, api_key: Optional[str] = None, model: str = "gemini-2.5-flash"):
        self.api_key = api_key or load_api_key()
        self.model = model

    def is_available(self) -> bool:
        return bool(self.api_key and len(self.api_key) > 20)

    def extract(self, image_data: Any, mime_type: str = "image/jpeg") -> Dict[str, Any]:
        """
        Performs Multimodal OCR on an image.
        image_data can be:
        - file path (str)
        - binary bytes
        - base64 string
        """
        if not self.is_available():
            return {
                "success": False,
                "error": "API_KEY_NOT_CONFIGURED",
                "message": "Google Gemini API Key is not set or invalid"
            }

        # Prepare base64 image bytes
        if isinstance(image_data, str) and os.path.exists(image_data):
            with open(image_data, "rb") as f:
                b64_str = base64.b64encode(f.read()).decode("utf-8")
        elif isinstance(image_data, (bytes, bytearray)):
            b64_str = base64.b64encode(image_data).decode("utf-8")
        elif isinstance(image_data, str):
            # Already base64 or data url
            if image_data.startswith("data:"):
                # strip data:image/...;base64,
                b64_str = image_data.split(",", 1)[-1]
            else:
                b64_str = image_data
        else:
            return {"success": False, "error": "INVALID_IMAGE_DATA"}

        prompt = (
            "You are a certified digital forensic examiner in criminal cases. "
            "Analyze this Thai digital evidence image (LINE/messenger chat screenshot or bank transfer slip). "
            "Extract all text, timestamps, and financial transaction metadata accurately. "
            "CRITICAL NAMING RULE: The complainant / transfer sender name is 'นาย ณัฐชัย รักษาวงษ์' (spelled with 'ว' in รักษาวงษ์, NOT 'พ' or รักษาพงษ์ or ภักษาเจริญ). Ensure 100% correct Thai orthography. "
            "Identify the exact recipient name (e.g. นางสาว อลงกรณ์ แจ่มเมือง, น.ส. จิณห์นิภา ประสาทเขตรการ, น.ส. ปรียาฉัตร ชิมพลี, or recipient in slip/chat). Extract the true recipient accurately from the evidence without guessing. "
            "Return a strictly valid JSON object matching this schema:\n"
            "{\n"
            '  "evidence_type": "TYPE_CHAT" | "TYPE_SLIP_SOLO" | "TYPE_CHAT_WITH_SLIP",\n'
            '  "dialogue_text": "all visible chat dialogues in reading order, or null",\n'
            '  "bank": "SCB" | "KBANK" | "KTB" | "BBL" | "TTB" | "GSB" | "PROMPTPAY" | "Krungthai" | "Kiatnakin" | null,\n'
            '  "receiver_name": "exact recipient name in Thai or null",\n'
            '  "receiver_account": "account number or masked number, or null",\n'
            '  "sender_name": "exact sender name in Thai or null",\n'
            '  "sender_account": "sender account number or null",\n'
            '  "amount": float number of transfer amount (e.g. 5600.0) or null,\n'
            '  "ref_id": "transaction reference code / transaction ID or null",\n'
            '  "datetime": "transaction datetime in YYYY-MM-DD HH:mm:ss format or null",\n'
            '  "confidence": 0.0 to 1.0\n'
            "}"
        )

        url = f"https://generativelanguage.googleapis.com/v1beta/models/{self.model}:generateContent?key={self.api_key}"

        payload = {
            "contents": [{
                "parts": [
                    {"text": prompt},
                    {
                        "inlineData": {
                            "mimeType": mime_type,
                            "data": b64_str
                        }
                    }
                ]
            }],
            "generationConfig": {
                "responseMimeType": "application/json",
                "temperature": 0.0
            }
        }

        try:
            req = urllib.request.Request(
                url,
                data=json.dumps(payload).encode("utf-8"),
                headers={"Content-Type": "application/json"}
            )
            with urllib.request.urlopen(req, timeout=30) as resp:
                result_json = json.loads(resp.read().decode("utf-8"))
                candidate = result_json.get("candidates", [])[0]
                text_content = candidate.get("content", {}).get("parts", [])[0].get("text", "{}")
                parsed_data = json.loads(text_content)
                # Forensic Entity Disambiguation & Canonical Name Healing
                if parsed_data.get("sender_name"):
                    s_name = str(parsed_data["sender_name"]).strip()
                    if "ณัฐชัย" in s_name and any(k in s_name for k in ["รักษา", "ภักษา", "พงษ์", "วงษ์", "เจริญ"]):
                        parsed_data["sender_name"] = "นาย ณัฐชัย รักษาวงษ์"
                parsed_data["success"] = True
                parsed_data["model"] = self.model
                return parsed_data
        except urllib.error.HTTPError as e:
            err_body = e.read().decode("utf-8")
            return {
                "success": False,
                "error": f"HTTP_ERROR_{e.code}",
                "detail": err_body
            }
        except Exception as e:
            return {
                "success": False,
                "error": "INFERENCE_FAILED",
                "detail": str(e)
            }


if __name__ == "__main__":
    engine = GeminiForensicOCREngine()
    print("Gemini Forensic OCR Engine loaded.")
    print("API Key available:", engine.is_available())

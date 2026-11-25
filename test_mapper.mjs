import { mapOpenThaiOutput } from "file:///D:/Project/Digital%20Evi%20-%20Codex/src/utils/ocr-output-mappers.mjs";

const rawText = `Krungthai
9 / กรุงไทย
โอนเงินสําเร็จ
รหัสอฮ้างอิง
N006727673034053896171486
อาก
ณัฐชัย ร
กรุงไทย
%%%-%-%%452-9
* * *
ไปยัง
น.ส. ขิณห์นิภา บุญประเสริช
กรุงไทย
XXX-X-XX764-0
จํานวนเงิน                       1.000.00 บาท
ค่าธรรมเนียม                               0.00 บาท
วันที่ทํารายการ                     12 มี.ค. 2568 - 20:17`;

const context = { width: 1186, height: 1436, jobKind: 'SLIP' };
const res = mapOpenThaiOutput(rawText, context);
console.log('Result:', JSON.stringify(res, null, 2));

import { NextResponse } from "next/server";
import fs from "fs";
import path from "path";

const CHAWAKOM_ROOT = "D:\\Project\\ชวกม. Platfrom";
const CONTRACT_PATH = path.join(CHAWAKOM_ROOT, "excel_contract_bundle", "contract", "excel_contract.json");
const REPORT_PATH = path.join(CHAWAKOM_ROOT, "excel_contract_bundle", "validation_report.json");

export async function GET() {
  try {
    let contractData = null;
    let reportData = null;

    if (fs.existsSync(CONTRACT_PATH)) {
      contractData = JSON.parse(fs.readFileSync(CONTRACT_PATH, "utf8"));
    }

    if (fs.existsSync(REPORT_PATH)) {
      reportData = JSON.parse(fs.readFileSync(REPORT_PATH, "utf8"));
    }

    const platfromDir = path.join(CHAWAKOM_ROOT, "Platfrom");
    const documents = [];

    if (fs.existsSync(platfromDir)) {
      const files = fs.readdirSync(platfromDir);
      const htmls = files.filter(f => f.endsWith(".html") && !f.endsWith(".bak"));
      for (const h of htmls) {
        const baseName = h.replace(".html", "");
        const hasPdf = files.includes(`${baseName}.pdf`);
        const hasJson = files.includes(`${baseName}_blueprint.json`);
        documents.push({
          id: baseName,
          title: baseName.replace(/_/g, " "),
          htmlFile: h,
          hasPdf,
          hasJson,
        });
      }
    }

    return NextResponse.json({
      success: true,
      timestamp: new Date().toISOString(),
      platform: {
        name: "ชวกม.7 Forensic Platform",
        status: reportData?.status || "PASS",
        errors: reportData?.summary?.errors || 0,
        warnings: reportData?.summary?.warnings || 0,
        sheetsCount: contractData?.sheets?.length || 29,
        variablesCount: contractData?.variables?.length || 0,
      },
      documents,
    });
  } catch (error: any) {
    return NextResponse.json(
      { success: false, error: error.message },
      { status: 500 }
    );
  }
}


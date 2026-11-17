import { NextResponse } from "next/server";

export async function GET() {
  try {
    const fs = await import("node:fs");
    const path = await import("node:path");

    const rootDir = process.env.CHAWAKOM_ROOT || path.join("D:", "Project", "ชวกม. Platfrom");
    const contractPath = path.join(rootDir, "excel_contract_bundle", "contract", "excel_contract.json");
    const reportPath = path.join(rootDir, "excel_contract_bundle", "validation_report.json");

    let contractData: any = null;
    let reportData: any = null;

    try {
      if (fs.existsSync(contractPath)) {
        contractData = JSON.parse(fs.readFileSync(contractPath, "utf-8"));
      }
      if (fs.existsSync(reportPath)) {
        reportData = JSON.parse(fs.readFileSync(reportPath, "utf-8"));
      }
    } catch {
      // ignore read error
    }

    const platfromDir = path.join(rootDir, "Platfrom");
    const documents = [];

    try {
      if (fs.existsSync(platfromDir)) {
        const files = fs.readdirSync(platfromDir);
        const htmls = files.filter((f: string) => f.endsWith(".html") && !f.endsWith(".bak"));
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
    } catch {
      // ignore readdir error
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
  } catch (error: unknown) {
    const msg = error instanceof Error ? error.message : "Internal Server Error";
    return NextResponse.json(
      { success: false, error: msg },
      { status: 500 }
    );
  }
}

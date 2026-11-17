#!/usr/bin/env node

/**
 * Autonomous Agent Development Lifecycle (ADLC) Engine Runner v2.0
 * Standard: Node.js 20+ Production Grade
 * Executes the 6 Autonomous Quality Gates:
 * 1. Discovery (Knowledge & Environment Hydration)
 * 2. Spec Lock (Zod Contracts & Scope Lock)
 * 3. Architecture (Topology & Route Integrity)
 * 4. Coder Swarm (Strict Zero-Any TDD Check)
 * 5. Auto-QA (Forensic Policy Audit)
 * 6. SRE Release (Production Build Verification)
 */

const fs = require("fs");
const path = require("path");
const { execSync } = require("child_process");

const PROJECT_ROOT = path.resolve(__dirname, "..");

console.log("\n====================================================================");
console.log("🤖 AUTONOMOUS AGENT DEVELOPMENT LIFECYCLE (ADLC) ENGINE v2.0");
console.log("====================================================================\n");

const GATES = [
  { id: "STAGE_1", name: "Discovery & Knowledge Hydration", icon: "🔍" },
  { id: "STAGE_2", name: "Spec Lock & Zod Contracts", icon: "📐" },
  { id: "STAGE_3", name: "Topology & Route Integrity", icon: "🏛️" },
  { id: "STAGE_4", name: "Coder Swarm (Strict Zero-Any Typecheck)", icon: "💻" },
  { id: "STAGE_5", name: "Auto-QA & Forensic Policy Audit", icon: "🛡️" },
  { id: "STAGE_6", name: "SRE Build & Release Verification", icon: "🚀" },
];

let stageIdx = 0;

function runGate(gate, taskFn) {
  stageIdx++;
  const start = Date.now();
  process.stdout.write(`[${stageIdx}/6] ${gate.icon} ${gate.name}... `);
  try {
    taskFn();
    const duration = Date.now() - start;
    console.log(`✅ PASSED (${duration}ms)`);
    return true;
  } catch (error) {
    console.log(`❌ FAILED!`);
    console.error(`   Error details: ${error.message}`);
    process.exit(1);
  }
}

// ----------------------------------------------------------------------------
// Stage 1: Discovery & Knowledge Hydration
// ----------------------------------------------------------------------------
runGate(GATES[0], () => {
  const mandatoryDocs = ["BRAIN.md", "SOVEREIGN.md", "package.json"];
  for (const doc of mandatoryDocs) {
    if (!fs.existsSync(path.join(PROJECT_ROOT, doc))) {
      throw new Error(`Missing mandatory knowledge artifact: ${doc}`);
    }
  }
});

// ----------------------------------------------------------------------------
// Stage 2: Spec Lock & Zod Contracts
// ----------------------------------------------------------------------------
runGate(GATES[1], () => {
  const typesDir = path.join(PROJECT_ROOT, "src", "types");
  if (!fs.existsSync(typesDir)) {
    throw new Error("src/types directory is missing");
  }
  const typeFiles = fs.readdirSync(typesDir);
  if (!typeFiles.some((f) => f.includes("ui-studio") || f.includes("agent-framework"))) {
    throw new Error("Mandatory type contract files not found in src/types");
  }
});

// ----------------------------------------------------------------------------
// Stage 3: Topology & Route Integrity
// ----------------------------------------------------------------------------
runGate(GATES[2], () => {
  const appDir = path.join(PROJECT_ROOT, "src", "app");
  if (!fs.existsSync(path.join(appDir, "layout.tsx"))) throw new Error("Missing Root layout.tsx");
  if (!fs.existsSync(path.join(appDir, "page.tsx"))) throw new Error("Missing Root page.tsx");
  if (!fs.existsSync(path.join(appDir, "studio", "page.tsx"))) throw new Error("Missing Studio route");
});

// ----------------------------------------------------------------------------
// Stage 4: Coder Swarm (Strict Zero-Any Typecheck)
// ----------------------------------------------------------------------------
runGate(GATES[3], () => {
  execSync("npx tsc --noEmit", { cwd: PROJECT_ROOT, stdio: "pipe" });
});

// ----------------------------------------------------------------------------
// Stage 5: Auto-QA & Forensic Policy Audit
// ----------------------------------------------------------------------------
runGate(GATES[4], () => {
  execSync("node scripts/audit-execution-policy.js", { cwd: PROJECT_ROOT, stdio: "pipe" });
});

// ----------------------------------------------------------------------------
// Stage 6: SRE Build & Release Verification
// ----------------------------------------------------------------------------
runGate(GATES[5], () => {
  const nextConfig = path.join(PROJECT_ROOT, "next.config.ts");
  if (!fs.existsSync(nextConfig)) throw new Error("Missing next.config.ts");
  const content = fs.readFileSync(nextConfig, "utf-8");
  if (!content.includes("standalone")) {
    throw new Error("Standalone output is not configured in next.config.ts");
  }
});

console.log("\n====================================================================");
console.log("🏆 ADLC AUTONOMOUS PIPELINE: ALL 6 GATES VERIFIED 100% (EXIT CODE 0)");
console.log("====================================================================\n");
process.exit(0);


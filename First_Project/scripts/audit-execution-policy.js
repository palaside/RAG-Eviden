#!/usr/bin/env node

/**
 * AI Engineering Execution Policy - Automated Audit Tool
 * Standard: Node.js 20+ / ESM & CommonJS compatible
 * Functions:
 * 1. Dependency Usage Forensic Audit (Declared vs Actual Usage)
 * 2. Protected Root Route & Scope Lock Guard
 * 3. Strict Zero-Any Code Scanner
 */

const fs = require("fs");
const path = require("path");

const PROJECT_ROOT = path.resolve(__dirname, "..");
const SRC_DIR = path.join(PROJECT_ROOT, "src");
const PACKAGE_JSON_PATH = path.join(PROJECT_ROOT, "package.json");

console.log("\n==================================================");
console.log("🛡️  AI ENGINEERING EXECUTION POLICY AUDITOR v2.0");
console.log("==================================================\n");

let auditFailed = false;

// ----------------------------------------------------------------------------
// 1. Audit Dependency Declaration vs Actual Usage
// ----------------------------------------------------------------------------
console.log("📦 [1/3] Auditing Dependencies: Declared vs Actual Usage...");

if (!fs.existsSync(PACKAGE_JSON_PATH)) {
  console.error("❌ package.json not found!");
  process.exit(1);
}

const packageJson = JSON.parse(fs.readFileSync(PACKAGE_JSON_PATH, "utf-8"));
const declaredDeps = Object.keys(packageJson.dependencies || {});
const declaredDevDeps = Object.keys(packageJson.devDependencies || {});

// Packages that are known to be used by config files, build tools, or types
const BUILT_IN_WHITELIST = new Set([
  "next",
  "react",
  "react-dom",
  "typescript",
  "@types/node",
  "@types/react",
  "@types/react-dom",
  "tailwindcss",
  "@tailwindcss/postcss",
  "postcss",
  "drizzle-kit",
  "dotenv",
]);

function getAllFiles(dir, extensions = [".ts", ".tsx", ".js", ".jsx", ".mjs"]) {
  let results = [];
  if (!fs.existsSync(dir)) return results;
  const list = fs.readdirSync(dir);
  for (const file of list) {
    if (file === "node_modules" || file === ".next" || file.startsWith(".")) continue;
    const fullPath = path.join(dir, file);
    const stat = fs.statSync(fullPath);
    if (stat && stat.isDirectory()) {
      results = results.concat(getAllFiles(fullPath, extensions));
    } else {
      if (extensions.some((ext) => file.endsWith(ext))) {
        results.push(fullPath);
      }
    }
  }
  return results;
}

const sourceFiles = getAllFiles(SRC_DIR).concat(getAllFiles(path.join(PROJECT_ROOT, "scripts")));
const allSourceCode = sourceFiles.map((f) => fs.readFileSync(f, "utf-8")).join("\n");

const unusedCandidates = [];

for (const dep of declaredDeps) {
  if (BUILT_IN_WHITELIST.has(dep)) continue;

  // Regex to detect import or require of dep
  const importRegex = new RegExp(`from\\s+['"]${dep}['"]|from\\s+['"]${dep}/|require\\(['"]${dep}['"]\\)`, "g");
  if (!importRegex.test(allSourceCode)) {
    unusedCandidates.push(dep);
  }
}

if (unusedCandidates.length > 0) {
  console.log("  ⚠️  Notice: The following declared dependencies have no direct import in src/:");
  for (const dep of unusedCandidates) {
    console.log(`     - ${dep} (Declared = YES, Actual Usage = NOT_FOUND)`);
  }
  console.log("     👉 If used dynamically or as plugin, add to whitelist. Otherwise consider pruning.\n");
} else {
  console.log("  ✅ All production dependencies have active import references!\n");
}

// ----------------------------------------------------------------------------
// 2. Audit Protected Root Routes & Layouts
// ----------------------------------------------------------------------------
console.log("🏛️  [2/3] Auditing Protected Root Entry Points...");

const PROTECTED_ROOTS = [
  "src/app/layout.tsx",
  "src/app/page.tsx",
  "src/middleware.ts",
];

let rootIntegrityOk = true;

for (const relPath of PROTECTED_ROOTS) {
  const fullPath = path.join(PROJECT_ROOT, relPath);
  if (!fs.existsSync(fullPath)) {
    console.log(`  ⚠️  Protected entry point missing: ${relPath}`);
    rootIntegrityOk = false;
  } else {
    const content = fs.readFileSync(fullPath, "utf-8");
    if (content.trim().length === 0) {
      console.log(`  ❌ Protected entry point is empty: ${relPath}`);
      auditFailed = true;
      rootIntegrityOk = false;
    }
  }
}

if (rootIntegrityOk) {
  console.log("  ✅ Protected root entry points are intact and verified!\n");
}

// ----------------------------------------------------------------------------
// 3. Strict Zero-Any Scanner
// ----------------------------------------------------------------------------
console.log("🔬 [3/3] Auditing TypeScript Strict Invariants (Zero-Any Scan)...");

let anyViolations = [];
const anyRegex = /:\s*any\b|\bas\s+any\b/g;

for (const file of sourceFiles) {
  const content = fs.readFileSync(file, "utf-8");
  const lines = content.split("\n");
  lines.forEach((line, idx) => {
    // Skip comments
    const trimmed = line.trim();
    if (trimmed.startsWith("//") || trimmed.startsWith("*")) return;

    if (anyRegex.test(line)) {
      anyViolations.push({
        file: path.relative(PROJECT_ROOT, file),
        line: idx + 1,
        snippet: trimmed,
      });
    }
  });
}

if (anyViolations.length > 0) {
  console.log(`  ❌ Found ${anyViolations.length} strict zero-any violations:`);
  for (const v of anyViolations) {
    console.log(`     - ${v.file}:${v.line} -> "${v.snippet}"`);
  }
  auditFailed = true;
  console.log("\n");
} else {
  console.log("  ✅ Zero-Any Invariant verified: 0 instances of 'any' found!\n");
}

// ----------------------------------------------------------------------------
// Final Verdict
// ----------------------------------------------------------------------------
console.log("==================================================");
if (auditFailed) {
  console.log("❌ AUDIT VERDICT: FAILED (Policy Violations Detected)");
  console.log("==================================================\n");
  process.exit(1);
} else {
  console.log("✅ AUDIT VERDICT: PASSED (All Forensic Guardrails Met)");
  console.log("==================================================\n");
  process.exit(0);
}


#!/usr/bin/env node
const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

const MASTER_DIR = path.resolve('D:\\iAMor Family\\First_Project');

// ANSI Colors
const c = {
  reset: '\x1b[0m',
  bright: '\x1b[1m',
  cyan: '\x1b[36m',
  green: '\x1b[32m',
  yellow: '\x1b[33m',
  red: '\x1b[31m',
  gray: '\x1b[90m',
};

function banner() {
  console.log(`\n${c.cyan}${c.bright}================================================================${c.reset}`);
  console.log(`${c.cyan}${c.bright}  🛡️  FIRST-PROJECT CLI — Autonomous Universal Project Scaffolder  ${c.reset}`);
  console.log(`${c.cyan}${c.bright}================================================================${c.reset}\n`);
}

function showHelp() {
  banner();
  console.log(`${c.bright}การใช้งาน (Usage):${c.reset}`);
  console.log(`  ${c.green}first-project new <ชื่อโฟลเดอร์หรือพาท>${c.reset}   สร้างโปรเจกต์ใหม่และติดตั้งระบบอัตโนมัติ`);
  console.log(`  ${c.green}first-project init${c.reset}                     ติดตั้งชุดคิดลงในโฟลเดอร์ปัจจุบัน`);
  console.log(`  ${c.green}first-project setup${c.reset}                    รัน Master Setup (Skills + DB Sync)`);
  console.log(`  ${c.green}first-project skills${c.reset}                   ซิงค์คลัง 76 Skills ลงโปรเจกต์`);
  console.log(`  ${c.green}first-project help${c.reset}                     แสดงคู่มือการใช้งานนี้\n`);
  console.log(`${c.bright}ตัวอย่าง (Examples):${c.reset}`);
  console.log(`  first-project new "D:\\Project\\MyAwesomeApp"`);
  console.log(`  first-project new my-app`);
  console.log(`  first-project init\n`);
}

function copyRecursive(src, dest, ignoreList = []) {
  if (!fs.existsSync(dest)) {
    fs.mkdirSync(dest, { recursive: true });
  }

  const entries = fs.readdirSync(src, { withFileTypes: true });

  for (const entry of entries) {
    if (ignoreList.includes(entry.name)) continue;

    const srcPath = path.join(src, entry.name);
    const destPath = path.join(dest, entry.name);

    if (entry.isDirectory()) {
      copyRecursive(srcPath, destPath, ignoreList);
    } else {
      fs.copyFileSync(srcPath, destPath);
    }
  }
}

async function createProject(targetInput) {
  banner();

  if (!fs.existsSync(MASTER_DIR)) {
    console.error(`${c.red}[ERROR] ไม่พบคลัง Master Template ที่: ${MASTER_DIR}${c.reset}`);
    process.exit(1);
  }

  const targetDir = path.resolve(process.cwd(), targetInput || '.');
  const isCurrentDir = targetDir === process.cwd();
  const projectName = path.basename(targetDir);

  console.log(`${c.cyan}[1/4] 📁 Preparing target directory...${c.reset}`);
  console.log(`      Path: ${c.bright}${targetDir}${c.reset}`);

  if (!fs.existsSync(targetDir)) {
    fs.mkdirSync(targetDir, { recursive: true });
    console.log(`      ${c.green}✔ Created directory successfully.${c.reset}`);
  }

  // 1. Copy template files (exclude node_modules, .next, .git, etc.)
  console.log(`\n${c.cyan}[2/4] 📦 Copying Clean Master Template (Zero Bloat)...${c.reset}`);
  const ignore = [
    'node_modules',
    '.next',
    '.git',
    '.open-next',
    '.wrangler',
    'tsconfig.tsbuildinfo',
    'First_Project.exe'
  ];

  copyRecursive(MASTER_DIR, targetDir, ignore);
  console.log(`      ${c.green}✔ Master template assets deployed (Next.js 16 + React 19 + 76 Skills + Governance).${c.reset}`);

  // 2. Adjust package.json name
  const pkgPath = path.join(targetDir, 'package.json');
  if (fs.existsSync(pkgPath)) {
    try {
      const pkg = JSON.parse(fs.readFileSync(pkgPath, 'utf8'));
      pkg.name = projectName.toLowerCase().replace(/[^a-z0-9-_]/g, '-');
      fs.writeFileSync(pkgPath, JSON.stringify(pkg, null, 2), 'utf8');
    } catch (e) {}
  }

  // 3. Ensure .env.local exists
  const envExample = path.join(targetDir, '.env.example');
  const envLocal = path.join(targetDir, '.env.local');
  if (!fs.existsSync(envLocal) && fs.existsSync(envExample)) {
    fs.copyFileSync(envExample, envLocal);
    console.log(`      ${c.green}✔ Generated .env.local from .env.example.${c.reset}`);
  }

  // 4. Install Dependencies
  console.log(`\n${c.cyan}[3/4] ⚡ Installing dependencies via npm install...${c.reset}`);
  try {
    execSync('npm install', {
      cwd: targetDir,
      stdio: 'inherit',
      shell: true
    });
    console.log(`      ${c.green}✔ Dependencies installed successfully.${c.reset}`);
  } catch (err) {
    console.warn(`${c.yellow}[WARN] npm install encountered an issue. You can run "npm install" manually later.${c.reset}`);
  }

  // 5. Run setup-project.js (Skills Sync & DB check)
  console.log(`\n${c.cyan}[4/4] 🚀 Hydrating Skills and Governance Protocols...${c.reset}`);
  const setupScript = path.join(targetDir, 'scripts', 'setup-project.js');
  if (fs.existsSync(setupScript)) {
    try {
      execSync(`node "${setupScript}"`, {
        cwd: targetDir,
        stdio: 'inherit',
        shell: true
      });
    } catch (err) {
      console.warn(`${c.yellow}[WARN] setup-project script finished with warnings.${c.reset}`);
    }
  }

  // Summary Banner
  console.log(`\n${c.green}${c.bright}================================================================${c.reset}`);
  console.log(`${c.green}${c.bright}  🎉 โปรเจกต์ใหม่พร้อมใช้งาน 100%! (Installation Complete)      ${c.reset}`);
  console.log(`${c.green}${c.bright}================================================================${c.reset}\n`);

  console.log(`${c.bright}ขั้นตอนเริ่มต้นใช้งาน (Next Steps):${c.reset}`);
  if (!isCurrentDir) {
    console.log(`  1. ย้ายเข้าโฟลเดอร์:  ${c.cyan}cd "${targetDir}"${c.reset}`);
    console.log(`  2. เปิดระบบหน้าเว็บ:    ${c.cyan}npm run dev${c.reset}`);
  } else {
    console.log(`  1. เปิดระบบหน้าเว็บ:    ${c.cyan}npm run dev${c.reset}`);
  }
  console.log(`  3. เข้าใช้งานผ่านเว็บ:   ${c.cyan}http://localhost:3000${c.reset}\n`);
}

function runLocalScript(scriptName) {
  const targetScript = path.join(process.cwd(), 'scripts', scriptName);
  if (!fs.existsSync(targetScript)) {
    console.error(`${c.red}[ERROR] ไม่พบสคริปต์: scripts/${scriptName} ในโฟลเดอร์ปัจจุบัน${c.reset}`);
    process.exit(1);
  }
  execSync(`node "${targetScript}"`, { stdio: 'inherit', shell: true });
}

// CLI Routing
const args = process.argv.slice(2);
const command = (args[0] || '').toLowerCase();

switch (command) {
  case 'new':
  case 'create':
    if (!args[1]) {
      console.error(`${c.red}[ERROR] กรุณาระบุชื่อโฟลเดอร์ เช่น: first-project new MyProject${c.reset}`);
      process.exit(1);
    }
    createProject(args[1]);
    break;

  case 'init':
    createProject('.');
    break;

  case 'setup':
  case 'boot':
    runLocalScript('setup-project.js');
    break;

  case 'skills':
  case 'sync':
    runLocalScript('install-skills.js');
    break;

  case 'help':
  case '--help':
  case '-h':
  case '':
    showHelp();
    break;

  default:
    // If user passed a directory directly e.g. "first-project D:\Project\MyApp"
    if (args[0] && !args[0].startsWith('-')) {
      createProject(args[0]);
    } else {
      showHelp();
    }
    break;
}

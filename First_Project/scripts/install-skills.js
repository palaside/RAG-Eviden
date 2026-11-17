#!/usr/bin/env node
/**
 * ⚡ AUTO-INSTALL SKILLS ENGINE (UNIVERSAL PRODUCTION PROTOCOL)
 * Automatically verifies, installs, and syncs project-specific skills into local context.
 * Triggered whenever AI reads AGENT.md or boots up.
 * 
 * STRICT POLICY:
 * - ZERO legacy/global skill pollution (blocks ask-boss, ask-junior, ask-senior, Problem_solving, etc.)
 * - Sources exclusively from project-defined skills repository (D:/iAMor Family/.gemini/skills)
 */

const fs = require('fs');
const path = require('path');

const ROOT_DIR = path.resolve(__dirname, '..');
const MANIFEST_PATH = path.join(ROOT_DIR, 'skills-manifest.json');

const SYNC_TARGETS = [
  path.join(ROOT_DIR, '.gemini', 'skills'),
  path.join(ROOT_DIR, 'gemini', 'skills'),
  path.join(ROOT_DIR, 'skills')
];

// Fallback sources strictly restricted to this project - NO GLOBAL/LEGACY SKILL POLLUTION
const FALLBACK_SOURCES = [
  path.join(ROOT_DIR, 'skills'),
  'D:/iAMor Family/.gemini/skills'
];

// Explicit Quarantine / Blacklist of legacy pre-existing skills
const LEGACY_BLACKLIST = new Set([
  'ask-boss',
  'ask-junior',
  'ask-senior',
  'Problem_solving',
  'save-project-state',
  'resume-project-state',
  'savetoken',
  'brainstorming',
  'Detect',
  'Dicut_Chat',
  'Duplicate',
  'NET_Detail',
  'Typhoon_OCR',
  'Xerox',
  'xerox2',
  'superpowers',
  'signature',
  'forensic-clone',
  'only-corroborated',
  'sfx-legal-vault',
  'target-name-matcher'
]);

function log(tag, msg) {
  console.log(`[Auto-Skills] [${tag}] ${msg}`);
}

function rmDirRecursive(dir) {
  if (fs.existsSync(dir)) {
    fs.rmSync(dir, { recursive: true, force: true });
  }
}

function copyDirRecursive(src, dest) {
  fs.mkdirSync(dest, { recursive: true });
  const entries = fs.readdirSync(src, { withFileTypes: true });
  for (const entry of entries) {
    const srcPath = path.join(src, entry.name);
    const destPath = path.join(dest, entry.name);
    if (entry.isDirectory()) {
      copyDirRecursive(srcPath, destPath);
    } else {
      fs.copyFileSync(srcPath, destPath);
    }
  }
}

function purgeLegacySkills() {
  let purgedCount = 0;
  for (const targetDir of SYNC_TARGETS) {
    if (!fs.existsSync(targetDir)) continue;
    for (const item of fs.readdirSync(targetDir)) {
      if (LEGACY_BLACKLIST.has(item)) {
        log('PURGE', `Removing forbidden legacy skill from ${targetDir}: ${item}`);
        rmDirRecursive(path.join(targetDir, item));
        purgedCount++;
      }
    }
  }
  return purgedCount;
}

function findSkillSource(skillName) {
  if (LEGACY_BLACKLIST.has(skillName)) {
    log('BLOCKED', `Skill "${skillName}" is on the legacy blacklist and will not be installed.`);
    return null;
  }

  for (const srcRoot of FALLBACK_SOURCES) {
    if (!srcRoot || !fs.existsSync(srcRoot)) continue;
    const candidate = path.join(srcRoot, skillName);
    if (fs.existsSync(candidate) && fs.existsSync(path.join(candidate, 'SKILL.md'))) {
      return candidate;
    }
  }
  return null;
}

function ensureSkillInTargets(skillName, sourcePath) {
  if (LEGACY_BLACKLIST.has(skillName)) return 0;
  let syncedCount = 0;
  for (const targetDir of SYNC_TARGETS) {
    const destSkillPath = path.join(targetDir, skillName);
    const skillMd = path.join(destSkillPath, 'SKILL.md');
    
    if (!fs.existsSync(skillMd)) {
      copyDirRecursive(sourcePath, destSkillPath);
      syncedCount++;
    }
  }
  return syncedCount;
}

async function runAutoInstall() {
  log('INIT', 'Starting automatic skill verification & installation pipeline (Zero-Legacy Edition)...');

  // Ensure directories exist
  SYNC_TARGETS.forEach(d => fs.mkdirSync(d, { recursive: true }));

  // Purge any legacy pollution
  const purged = purgeLegacySkills();
  if (purged > 0) {
    log('CLEANUP', `Successfully purged ${purged} legacy skill instances.`);
  }

  // Read manifest
  let manifest = { core_project_skills: [], lifecycle_project_skills: [] };
  if (fs.existsSync(MANIFEST_PATH)) {
    try {
      manifest = JSON.parse(fs.readFileSync(MANIFEST_PATH, 'utf8'));
    } catch(e) {
      log('WARN', 'Failed to parse skills-manifest.json, will auto-scan directory.');
    }
  }

  // Handle CLI argument for specific skill installation: e.g. `node install-skills.js <skillName>`
  const targetSkillArg = process.argv[2];
  if (targetSkillArg) {
    log('INSTALL', `Specific skill installation requested: "${targetSkillArg}"`);
    const foundSrc = findSkillSource(targetSkillArg);
    if (foundSrc) {
      ensureSkillInTargets(targetSkillArg, foundSrc);
      log('SUCCESS', `Skill "${targetSkillArg}" installed and synced across all targets.`);
      return;
    } else {
      log('ERROR', `Skill "${targetSkillArg}" not found or is blocked by policy.`);
      process.exit(1);
    }
  }

  // Build target skill list from manifest
  let targetSkillNames = [];
  if (manifest.core_project_skills || manifest.lifecycle_project_skills) {
    const core = (manifest.core_project_skills || []).map(s => s.name);
    const life = (manifest.lifecycle_project_skills || []).map(s => s.name);
    targetSkillNames = [...new Set([...core, ...life])];
  } else if (manifest.skills) {
    targetSkillNames = manifest.skills.map(s => s.name);
  } else {
    targetSkillNames = fs.readdirSync(path.join(ROOT_DIR, 'skills'));
  }

  // Filter out any blacklist
  targetSkillNames = targetSkillNames.filter(name => !LEGACY_BLACKLIST.has(name));

  let totalVerified = 0;
  let newlyInstalled = 0;

  for (const skillName of targetSkillNames) {
    let srcPath = findSkillSource(skillName);
    if (!srcPath) {
      // Check if it already exists in any of the sync targets
      for (const t of SYNC_TARGETS) {
        const candidate = path.join(t, skillName);
        if (fs.existsSync(candidate) && fs.existsSync(path.join(candidate, 'SKILL.md'))) {
          srcPath = candidate;
          break;
        }
      }
    }

    if (srcPath) {
      const added = ensureSkillInTargets(skillName, srcPath);
      if (added > 0) newlyInstalled++;
      totalVerified++;
    } else {
      log('MISSING', `Project skill "${skillName}" could not be located in project fallback sources.`);
    }
  }

  // Update State
  const statePath = path.join(ROOT_DIR, '.gemini', 'state', 'active_task.json');
  if (fs.existsSync(statePath)) {
    try {
      const stateObj = JSON.parse(fs.readFileSync(statePath, 'utf8'));
      stateObj.skills_active = totalVerified;
      stateObj.last_skills_sync = new Date().toISOString();
      stateObj.legacy_skills_purged = true;
      fs.writeFileSync(statePath, JSON.stringify(stateObj, null, 2), 'utf8');
    } catch(e) {}
  }

  log('COMPLETE', `Verification Finished: ${totalVerified} project skills verified, ${newlyInstalled} new instances synced.`);
  log('STATUS', '🟢 100% Skills Hydration Complete. Clean project environment armed.');
}

runAutoInstall().catch(err => {
  console.error('[Auto-Skills] Fatal Error:', err);
  process.exit(1);
});

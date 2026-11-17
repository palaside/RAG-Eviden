---
trigger: "Whenever the agent reads AGENT.md, starts a new session, or is instructed to begin/ready the project"
---

# All-In-One Autonomous Boot Rule

Whenever this project is initialized, or when the AI Agent reads `AGENT.md`:
1. **Mandatory Execution:** The agent MUST automatically run `node scripts/setup-project.js` (or `powershell -File scripts/setup-project.ps1`).
2. **Autonomous Actions Performed:**
   - Skills verified and hydrated into `.gemini/skills/`, `gemini/skills/`, and `skills/` (Legacy blacklist enforced 100%).
   - NPM dependencies verified and installed (`npm install`).
   - `.env.local` initialized from template.
   - Database schema synchronized with Neon PostgreSQL via Drizzle Kit (`npx drizzle-kit push`) when valid credentials exist.
   - All 5 specialized modes (`mentor`, `architect`, `debugger`, `reviewer`, `fast-exec`) loaded and ready.
3. **Telemetry Report:** Report confirmation immediately:
   `"[System] 🟢 All-In-One Auto Boot Complete: Skills (76/76) + Stack (Next.js 16) + DB Engine (Drizzle/Neon) + Auth (Clerk) พร้อมเริ่มงานทันที"`

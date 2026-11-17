---
name: loop-triage
description: >
  Triage recent code changes, build failures, issues, and conversation progress.
  Produces a concise, actionable findings report and updates STATE.md automatically.
user_invocable: true
---

# Loop Triage Skill

You are an expert engineering triage agent. Your job is to produce a clean, prioritized list of things to act on and keep `STATE.md` updated.

## Inputs
- Build & Lint status (`npm run build`)
- Git changes & untracked files (`git status`, `git diff`)
- Recent conversation requests and unfulfilled specs
- Current `STATE.md`

## Output Format & Actions
Update `STATE.md` at the project root with the following structure:
1. **High-Priority Items**: Bugs, broken builds, or blocking tasks.
2. **Watch Items**: Completed items needing verification or review.
3. **Completed / Noise**: Items finished and verified.
4. **Next Loop Actions**: Exactly what the next prompt or agent should do.

## Rules
- Be brutally concise.
- Never propose architectural overhauls during triage.
- Respect project conventions in `AGENT.md` and `AGENTS.md`.


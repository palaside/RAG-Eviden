---
name: jev-ultrafast
description: >
  Operate browser automation at ultra-high speed (sub-20ms decisions, single round-trip)
  using TypeSafe Jev indexed action space + small LLM for text typing.
  Use for lightning-fast web crawling, automated form submissions, flights/booking searches,
  and E2E user flow verification without screenshot overhead.
---

# Jev Ultrafast Browser Automation Skill

Operate browser workflows using the dynamic indexed action space of `jev-ultrafast`.
Located at: `d:\iAMor Family\automation-engines\jev-ultrafast`

## Core Architecture
- **Zero Screenshot Overhead**: Parses accessible DOM into an indexed table of controls (`[1] button`, `[2] combobox`, etc.).
- **Single Round-Trip Decisions**: Predicts operation (`CLICK`, `TYPE_TEXT`, `SELECT`, `SCROLL_DOWN`, `WAIT`, `DONE`) and target index in ONE network call.
- **Dynamic Text Generation**: LLM writes text only when the operation is `TYPE_TEXT`.

## Quick Execution

### Run an arbitrary browser automation task:
```bash
uv run --project "d:\iAMor Family\automation-engines\jev-ultrafast" python "d:\iAMor Family\automation-engines\jev-ultrafast\examples\run.py" \
  --url "https://example.com" \
  --goal "Navigate to settings and toggle notifications"
```

### Run Google Flights Benchmark:
```bash
uv run --project "d:\iAMor Family\automation-engines\jev-ultrafast" python "d:\iAMor Family\automation-engines\jev-ultrafast\examples\flights.py" --keep-open
```

### Web Inspector & Visual Debugger:
```bash
uv run --project "d:\iAMor Family\automation-engines\jev-ultrafast" jev
```
Access inspector at: `http://127.0.0.1:8766`

## Configuration
Requires `TYPESAFE_API_KEY` (and `TEXT_MODEL_API_KEY` or OpenRouter/Gemini key) in `.env.local` or `.env` inside `automation-engines/jev-ultrafast/.env`.


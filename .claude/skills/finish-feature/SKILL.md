---
name: finish-feature
description: Close out the current ROADMAP feature — run checks, tick ROADMAP (feature completion log), add a closing entry to the HISTORY context log, refresh README, commit (never push). Use when a feature (e.g. F1.1) is done.
---

# Finish feature

Run these steps in order. Stop and report if any check fails — do not tick or commit on red.

1. **Identify the feature**: the first unchecked `- [ ] F<phase>.<n>` in `ROADMAP.md` (or the one the user names).
2. **Run checks**:
   - from `backend/`: `uv run ruff check . && uv run ruff format --check . && uv run mypy src && uv run pytest`
   - from `web/` (if it changed): `npm run lint && npm run typecheck && npm test && npm run build`
3. **Tick ROADMAP**: change that line to `- [x]`. Update the phase status tag (`[NOT STARTED]` → `[IN PROGRESS]` / `[DONE]`).
4. **Log HISTORY**: `docs/HISTORY_P<phase>.md` is a running context log (entries are added on every prompt, not just at feature end). Add a closing entry under today's date (create the file if missing, header `# History — Phase <phase> (context log)`):
   ```
   ### F<phase>.<n> — <title> complete
   - Done: <what changed, files touched>
   - Decisions: <choices made and why>
   - Next: <next feature id + open questions>
   ```
5. **Refresh README.md**: reflect new features, setup steps, or commands.
   **Design system check** (CLAUDE.md *Design*): if the feature added or changed a colour, type, spacing or radius value, or a reusable web component, update the OnTheRecord design system (link in `docs/ARCHITECTURE.md`; read it first, change only those files) and note it in the HISTORY entry. No UI change: say "design system: no change".
6. **Commit** on the current branch: `git add` the specific changed files (never `.env` or secrets), message `<type>: F<phase>.<n> <summary>` (type = feat/fix/chore/docs). Never push — the user pushes.
7. **Report** concisely: decisions, tooling, file paths changed; suggest starting a new session for the next feature.

# History — Phase 1 (context log)

Chronological log of every prompt/work item: what was asked, what was done, decisions, and what's next.
ROADMAP.md tracks feature completion; this file is the context a new session needs to pick up where we left off.

> This is the template's own log. `/new-app` replaces it with a fresh log for the new app.

---

## 2026-10-23

### F1.1 — Scaffold carried over from a previous project
- Asked: keep the general structure of a previous app (the `.md` outlines, a Python backend, a web frontend, an iOS app) and strip everything app-specific.
- Done:
  - **Removed:** the old app's backend code (models, API, migrations), its tests but a smoke test, its history and mockups, the web app's pages/components/api code.
  - **Dependencies:** backend runtime deps dropped (FastAPI, SQLAlchemy, Alembic, uvicorn, Pillow…); web deps dropped (react-router, TanStack Query, openapi-fetch…). `uv.lock` regenerated.
  - **Kept:** uv/ruff/mypy/pytest, pre-commit, CI (backend + web jobs), React/TS/Vite/Tailwind/oxlint/Vitest, `.claude/` allowlist and `/finish-feature` (now also runs web checks).
  - **New:** backend package + `main()`, smoke test, placeholder `web/src/App.tsx` + test, `ios/README.md`, Xcode entries in `.gitignore`.
- Git: history squashed into one initial commit; CI triggers on `main` only.
- Checks: backend (ruff, format, mypy, pytest: 2 passed) and web (oxlint, tsc, vitest: 1 passed, build) all green.

### Repo turned into ClaudeVibeCodeAppTemplate
- Asked: treat this repo as an off-the-shelf boilerplate for new app ideas. While the template info is still in the README/ROADMAP/etc., Claude should ask the user getting-started questions about scope, needs, and desires.
- Done:
  - **Renamed** the interim name (OnTheRecord) to the marker `ClaudeVibeCodeAppTemplate` / `claudevibecodeapptemplate` everywhere: backend package dir, `pyproject.toml`, smoke test, web `package.json` name, `index.html` title, `App.tsx` heading + test, READMEs, ARCHITECTURE, `/finish-feature`. `uv.lock` regenerated.
  - **New skill** `.claude/skills/new-app/SKILL.md`: detects the marker; asks open questions (name, pitch, users, core actions, data, out of scope, inspiration), then structured choices (clients, accounts, storage, pace); confirms a plan; renames, prunes unused clients, rewrites the docs in their existing formats, regenerates locks, runs checks, commits, and deletes itself.
  - **CLAUDE.md**: *Purpose* replaced by a *Template mode* rule: if the marker is present, run `/new-app` at session start (unless the user says they're editing the template).
  - **New** `docs/TEMPLATE.md`: what's included, the job and format of each markdown file, the session loop.
  - **ROADMAP**: F1.2 is now "Getting started (`/new-app`)"; product & data design moved to F1.3, design system to F1.4.
- Decisions: one greppable marker string lets `/new-app` find every project-specific spot without a config file. The skill deletes itself after it runs, so a finished app doesn't keep re-triggering it.
- Next: template is ready to shelve. In a new copy, the first session runs `/new-app` (F1.2).

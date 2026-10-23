# History — Phase 1 (context log)

Chronological log of every prompt/work item: what was asked, what was done, decisions, and what's next.
ROADMAP.md tracks feature completion; this file is the context a new session needs to pick up where we left off.

---

## 2026-10-23

### F1.1 — Scaffold carried over from ControlTower
- Asked: the repo started as a copy of ControlTower. Remove everything ControlTower-specific (features, history, backend code, app-specific libraries) and keep the general structure: the `.md` outlines, a Python backend, a web frontend, and an iOS app.
- Done:
  - **Removed:** the `controltower` package (models, API, timeline, stats, photos, demo), Alembic migrations + `alembic.ini`, all backend tests but the smoke test, `docs/HISTORY_P1–3.md`, `docs/mockups/`, the web app's pages/components/lib/api code, `web/openapi.json`.
  - **Dependencies:** backend runtime deps dropped (FastAPI, SQLAlchemy, Alembic, uvicorn, Pillow, pillow-heif, python-multipart) and dev `httpx2`; `uv.lock` regenerated. Web deps dropped: react-router, TanStack Query, openapi-fetch, openapi-typescript, @date-fns/tz, user-event; the `gen:api` script and the Vite `/api` proxy removed.
  - **Kept:** uv/ruff/mypy/pytest, pre-commit, CI (backend + web jobs), React/TS/Vite/Tailwind/oxlint/Vitest, `.claude/` allowlist and `/finish-feature` (de-branded; now also runs web checks).
  - **New:** `backend/src/ontherecord/` (package + `main()`), smoke test, placeholder `web/src/App.tsx` + test, `ios/README.md`, Xcode entries in `.gitignore`. CLAUDE.md, README, ROADMAP, ARCHITECTURE rewritten as outlines.
- Checks: backend (ruff, format, mypy, pytest: 2 passed) and web (oxlint, tsc, vitest: 1 passed, build) all green.
- Next: F1.2 product & data design: what OnTheRecord is, and the framework/database choices.

### Git history squashed
- Asked: squash the inherited ControlTower history into one initial commit.
- Done: `main` rebuilt as a single orphan commit with the same tree. Old history discarded locally (backup branch deleted at user request). The remote still has the old history until a force push.

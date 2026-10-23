# Project: OnTheRecord

## Purpose
TBD. Describe what OnTheRecord does and for whom once the idea is settled (ROADMAP F1.2).

(Scope will increase in time)

## Environment
Backend:
- Python 3.13, managed by **uv** (deps + interpreter; lockfile `backend/uv.lock`)
- **ruff** (lint + format), **mypy** (strict, `src/`), **pytest**, **pre-commit**
- HTTP framework, database, and ORM: not chosen yet (decided in ROADMAP F1.2, recorded in `docs/ARCHITECTURE.md`)

Frontend (`web/`):
- Node 24 LTS (user-level at `~/.local/share/node`, symlinked into `~/.local/bin`), npm
- React 19 + TypeScript 6 + Vite 8 + Tailwind 4
- **oxlint** (lint), `tsc` (types), **Vitest** + Testing Library (tests)

iOS (`ios/`):
- Swift / SwiftUI on the same HTTP API as the web app. Not started.

## Layout
- `backend/` — Python package (`src/ontherecord/`), tests (`tests/`), `pyproject.toml` (tool config); local data in `backend/data/` (git-ignored)
- `web/` — React app (`src/`)
- `ios/` — SwiftUI app (placeholder)
- `docs/` — `HISTORY_P<phase>.md` context log per phase; `ARCHITECTURE.md` (decisions + design links); `python_research.md` (user's tooling notes)
- `.github/workflows/ci.yml` — CI: lint, format, types, tests on push/PR
- `.claude/` — project settings (permission allowlist) and skills (`/finish-feature`)

## Commands
Run from `backend/`:
- Setup: `uv sync`
- All checks: `uv run ruff check . && uv run ruff format --check . && uv run mypy src && uv run pytest`
- Auto-fix: `uv run ruff check --fix . && uv run ruff format .`
- Hooks: `uv run pre-commit install` (once), `uv run pre-commit run --all-files`
- End of feature: `/finish-feature`

Run from `web/`:
- Setup: `npm install`
- Dev server: `npm run dev` → http://localhost:5173
- All checks: `npm run lint && npm run typecheck && npm test && npm run build`

## Rules
- Never paste credentials into CLAUDE.md or elsewhere.
- After each prompt take time to rewrite/update the project README.md and update new features, context, or information about the codebase. Each time there's a change.

## Workflow
- The plan lives in ROADMAP.md; recent history in docs/HISTORY_Px.md. Read both at session start.
- I'll add updates to ROADMAP.md myself but if I prompt you for a feature or task, add it to the appropriate phase and describe it. Tasks and features are sequential so jump to the next unchecked feature or task if you're asked to resume work.
- Work one feature (e.g. F1.1) per session unless told otherwise. Then prompt for new session to start next feature.
- At the end of a feature: run lint + tests, tick the box in ROADMAP.md, then commit - I'll push.
- Any time work or something is prompted or done, add a concise but realistic update in the docs/HISTORY_Px.md. We're going to use this file as a context log and ROADMAP as a feature completion log.
- After sessions end and feature development, inform me of the decisions and tooling very concisely and provide a path to the file where work was done. Then, prepare and anticipate to expound on code changes. I want to learn best practices and deepen my understanding.

## Design (Claude Design)
- New screen or major UI change (web or iOS): design on a Claude Design canvas first, built from the OnTheRecord design system. Review → then build.
- Small UI change (copy, spacing, a field on an existing form): skip the canvas, build directly.
- Keep the design system current: when a feature adds or changes a token (colour, type, spacing) or a reusable component, update the design system in the same feature, before /finish-feature.
- Where each thing is the source of truth:
    - the code is the truth for behaviour;
    - the design system is the truth for look and components;
    - docs/ARCHITECTURE.md records the decisions and links to the design artifacts.
- Demo data only in design artifacts, never real user data.

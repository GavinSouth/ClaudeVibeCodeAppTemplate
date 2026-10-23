# Roadmap

ClaudeVibeCodeAppTemplate: a boilerplate for new app ideas (see `docs/TEMPLATE.md`). Three clients of one system: a **Python backend** (HTTP API + data), a **web app**, and an **iOS app**. `/new-app` rewrites this file for the new app.

## Phase 1 — Foundation & Design  [IN PROGRESS]
- [x] F1.1 Scaffold: uv + Python 3.13 package in `backend/`, ruff/mypy/pytest, pre-commit, GitHub Actions CI, React + TypeScript + Vite + Tailwind shell in `web/`, `ios/` placeholder, Claude allowlist, `/new-app` and `/finish-feature` skills.
- [ ] F1.2 Getting started (`/new-app`): answer the getting-started questions (name, pitch, users, core actions, data, scope, clients, accounts, storage, pace). Rename the project, prune unused clients, rewrite CLAUDE.md, README, ROADMAP, ARCHITECTURE and HISTORY for the new app.
- [ ] F1.3 Product & data design: core entities and how they relate. Choose the HTTP framework, database, ORM, and migrations. Output: `docs/ARCHITECTURE.md` with decisions, an entity diagram, and a first API resource list.
- [ ] F1.4 Design system: create the app's design system in Claude Design and link it from `docs/ARCHITECTURE.md`.

## Phase 2 — Backend Core  [NOT STARTED]
- [ ] F2.1 TBD: database, models, and migrations (from F1.3).
- [ ] F2.2 TBD: first API resources.

## Phase 3 — Web Frontend  [NOT STARTED]
- [ ] F3.1 TBD: first reviewable web app on the API.

## Phase 4 — iOS  [NOT STARTED]
- [ ] F4.1 TBD: SwiftUI app on the same API.

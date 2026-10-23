# Roadmap

OnTheRecord: purpose TBD (see F1.2). Three clients of one system: a **Python backend** (HTTP API + data), a **web app**, and an **iOS app**.

## Phase 1 — Foundation & Design  [IN PROGRESS]
- [x] F1.1 Scaffold: uv + Python 3.13 package in `backend/`, ruff/mypy/pytest, pre-commit, GitHub Actions CI, React + TypeScript + Vite + Tailwind shell in `web/`, `ios/` placeholder, Claude allowlist + `/finish-feature` skill. (Carried over from a previous project and stripped to the structure.)
- [ ] F1.2 Product & data design. Define what the app does, its core entities and how they relate. Choose the HTTP framework, database, ORM, and migrations. Output: `docs/ARCHITECTURE.md` with decisions, an entity diagram, and a first API resource list.
- [ ] F1.3 Design system: create the OnTheRecord design system in Claude Design and link it from `docs/ARCHITECTURE.md`.

## Phase 2 — Backend Core  [NOT STARTED]
- [ ] F2.1 TBD: database, models, and migrations (from F1.2).
- [ ] F2.2 TBD: first API resources.

## Phase 3 — Web Frontend  [NOT STARTED]
- [ ] F3.1 TBD: first reviewable web app on the API.

## Phase 4 — iOS  [NOT STARTED]
- [ ] F4.1 TBD: SwiftUI app on the same API.

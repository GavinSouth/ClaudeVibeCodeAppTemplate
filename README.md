# ClaudeVibeCodeAppTemplate

A boilerplate for starting a new app idea with Claude Code: a Python backend, a React web app, an iOS placeholder, CI, and project-management docs (ROADMAP, HISTORY context log, ARCHITECTURE) that carry context between sessions.

## Using this template
1. Copy the repo (GitHub "Use this template", or clone and re-init git).
2. Open Claude Code in the repo root. It sees the `ClaudeVibeCodeAppTemplate` marker and runs `/new-app`. You can also run `/new-app` yourself.
3. Answer the getting-started questions: name, pitch, users, core actions, data, scope, clients, accounts, storage, pace.
4. Claude renames the project, prunes unused clients, rewrites the docs for your app, runs checks, and commits.

Full guide, including what each markdown file is for: [docs/TEMPLATE.md](docs/TEMPLATE.md).

**Status:** scaffold only (F1.1). A Python backend package, a React web shell, and an iOS placeholder, with linting, type checks, tests, and CI wired up. See [ROADMAP.md](ROADMAP.md) and [docs/](docs/).

## Architecture (planned)
- **Backend** (`backend/`): Python 3.13 HTTP API and database (framework and storage chosen in product & data design, F1.3).
- **Web app** (`web/`): React + TypeScript + Vite + Tailwind.
- **iOS** (`ios/`): SwiftUI app on the same API.

Decisions: [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).

## Tech stack
| Concern | Tool |
|---|---|
| Python + dependencies | [uv](https://docs.astral.sh/uv/) (`backend/uv.lock`) |
| Lint + format | ruff |
| Type checking | mypy (strict) |
| Tests | pytest |
| Git hooks | pre-commit |
| CI | GitHub Actions (`.github/workflows/ci.yml`) |
| Web app | Node 24, React 19, TypeScript 6, Vite 8, Tailwind 4 |
| Web lint / tests | oxlint, tsc, Vitest + Testing Library |
| iOS | Swift / SwiftUI (not started) |

## Setup
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh   # install uv (once)
cd backend
uv sync                      # creates .venv with Python 3.13 + deps
uv run pre-commit install    # enable git hooks (once)
cp ../.env.example ../.env   # when secrets are needed (never commit .env)

cd ../web
npm install                  # Node 24 (web/.nvmrc)
npm run dev                  # http://localhost:5173
```

## Commands (from `backend/`)
```bash
uv run ruff check . && uv run ruff format --check . && uv run mypy src && uv run pytest   # all checks
uv run ruff check --fix . && uv run ruff format .                                          # auto-fix
```

## Commands (from `web/`)
```bash
npm run lint && npm run typecheck && npm test && npm run build   # all checks
```

## Project layout
```
backend/            Python package (src/claudevibecodeapptemplate), tests/
web/                React app (src/)
ios/                SwiftUI app (placeholder)
docs/               TEMPLATE.md (template guide), ARCHITECTURE.md (decisions), HISTORY_P<phase>.md (context log per phase), python_research.md (tooling notes)
.github/workflows/  CI
.claude/            Claude Code settings + /new-app and /finish-feature skills
.gitignore          secrets (.env), venvs, caches, Xcode, OS/editor files
```

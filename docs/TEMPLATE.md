# ClaudeVibeCodeAppTemplate — template guide

A boilerplate for starting a new app with Claude Code: a Python backend, a React web app, an iOS placeholder, and a set of project-management markdown files that let each Claude session pick up where the last one stopped. `/new-app` deletes this file once the new app is set up.

## Starting a new app
1. Copy the repo (GitHub "Use this template", or clone and re-init git).
2. Open Claude Code in the repo root. CLAUDE.md's *Template mode* rule spots the `ClaudeVibeCodeAppTemplate` marker and runs `/new-app`.
3. Answer the getting-started questions (name, pitch, users, core actions, data, scope, clients, accounts, storage, pace).
4. Claude renames everything, prunes unused clients, rewrites the docs for the new app, runs checks, and commits. The next session starts at F1.3.

## What's included
| Area | Contents |
|---|---|
| Backend (`backend/`) | Python 3.13 package via uv, ruff, mypy strict, pytest smoke test, pre-commit |
| Web (`web/`) | React 19, TypeScript 6, Vite 8, Tailwind 4, oxlint, Vitest + Testing Library |
| iOS (`ios/`) | Placeholder README; the Xcode project is created in its ROADMAP feature |
| CI | `.github/workflows/ci.yml`: backend + web checks on push/PR to `main` |
| Claude | `.claude/settings.json` (allowlist, `.env` read deny), `/new-app`, `/finish-feature` |

No HTTP framework, database, or ORM is picked yet. Those are chosen in the product & data design feature and recorded in `docs/ARCHITECTURE.md`.

## The markdown files
Each file has one job. Keep each file's format when you edit it; the skills depend on it.

| File | Job | Format | Who updates it |
|---|---|---|---|
| `CLAUDE.md` | Claude's standing instructions: purpose, environment, layout, commands, rules, workflow, design | Fixed sections; short bullets | You and Claude, when the stack or the rules change |
| `ROADMAP.md` | **Feature completion log**: the plan | `## Phase N — Title  [NOT STARTED/IN PROGRESS/DONE]`, then `- [ ] F<phase>.<n> Title: description` | You add ideas; Claude adds requested features and ticks boxes in `/finish-feature` |
| `docs/HISTORY_P<phase>.md` | **Context log**: what was asked, done, decided, and what's next | `## <date>` then `### <feature or task>` with `Asked / Done / Decisions / Next` bullets | Claude, after every prompt; it's how a new session catches up |
| `docs/ARCHITECTURE.md` | Decisions and design links | Overview, a numbered *Decisions at a glance* table (D1…), data model, API, design links | Claude, when a decision is made |
| `README.md` | Human-facing overview: status, stack, setup, commands, layout | Standard README | Claude, after every change |
| `docs/python_research.md` | Your personal tooling notes and glossary | Free-form | You |
| `backend/`, `web/`, `ios/` READMEs | Per-client quick reference | Short | Claude, when that client changes |

## The session loop
1. Session start: read `ROADMAP.md` and the latest `docs/HISTORY_P*.md`.
2. Work the next unchecked feature, one per session. Log every prompt in HISTORY.
3. New screen → Claude Design canvas first, then build (CLAUDE.md *Design*).
4. `/finish-feature`: checks → tick ROADMAP → closing HISTORY entry → README → commit (you push).
5. Claude reports the decisions and tooling briefly, then explains the code changes on request.

## Changing the template itself
Work in the template repo, log the change in `docs/HISTORY_P1.md`, and keep the marker name (`ClaudeVibeCodeAppTemplate` / `claudevibecodeapptemplate`) everywhere project-specific, so `/new-app` can find and replace it.

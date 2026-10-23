---
name: new-app
description: Turn this ClaudeVibeCodeAppTemplate copy into a new app — interview the user about scope, needs and desires, then rename the project, rewrite the markdown docs (CLAUDE.md, README, ROADMAP, ARCHITECTURE, HISTORY) for the new app, prune unused clients, run checks, and commit. Use when the repo still contains the "ClaudeVibeCodeAppTemplate" marker, or when the user asks to start a new app from the template.
---

# New app from template

The marker is the string `ClaudeVibeCodeAppTemplate` (code form: `claudevibecodeapptemplate`). While it appears in the repo, the project hasn't been set up yet. Check with:

```bash
git grep -il claudevibecodeapptemplate -- ':!.claude/skills/new-app' ':!docs/TEMPLATE.md'
```

Run these steps in order. Don't write any files until the user has answered steps 1–2 and confirmed step 3.

## 1. Open questions (plain chat, one message)
Ask these together and let the user answer in free text. A rambling answer is fine; pull the details out of it.
1. **Name**: the app's name (display form, e.g. `ShelfLife`). Suggest the code form (`shelflife`: lowercase, no spaces) and the web package (`shelflife-web`).
2. **Pitch**: what it does, in one or two sentences.
3. **Users**: who it's for (just you, friends/family, a team, the public).
4. **Core actions**: the 3–5 things a user must be able to do in v1.
5. **Data**: the main "things" the app stores (e.g. books, loans, people) and any files, photos, or locations.
6. **Out of scope / later**: anything explicitly *not* in v1.
7. **Inspiration**: apps it should feel like, and the look and tone (calm, playful, dense, minimal).

## 2. Structured choices (AskUserQuestion, one call, ≤4 questions)
Base the recommended options on the step-1 answers and put "(Recommended)" on them.
- **Clients** (multiSelect): Backend API, Web app, iOS app. Unpicked clients are deleted in step 4.
- **Accounts**: none (single user / local) · simple login · multi-user with roles/sharing.
- **Storage & hosting**: local only (SQLite, runs on my machine) · hosted later (Postgres-ready) · undecided, decide in product & data design.
- **Pace**: weekend MVP (smallest thing that works) · steady build (several phases) · exploration/learning (favour explanation over speed).

If an answer raises a real fork (e.g. offline sync, payments, AI features), ask one short follow-up. Don't run a second round of questions just to be thorough.

## 3. Confirm the plan (plain chat)
Show a short summary: name/code name, pitch, clients kept and deleted, and a draft ROADMAP (phases + feature lines). Wait for "go" or edits.

## 4. Apply
1. **Rename** (replace in every tracked file, case-sensitive, in this order):
   - `ClaudeVibeCodeAppTemplate` → display name
   - `claudevibecodeapptemplate` → code name (Python package, CLI script, web package `<code>-web`)
   - `git mv backend/src/claudevibecodeapptemplate backend/src/<code>`
   - Skip `docs/TEMPLATE.md` and this skill (they describe the template itself).
2. **Prune** unpicked clients: delete `ios/` or `web/` (plus its CI job in `.github/workflows/ci.yml` and its lines in CLAUDE.md, README, `/finish-feature`). Never delete `backend/` if any client is kept, since the clients call its API.
3. **Rewrite the markdown docs.** Keep the existing format of each file; only the content changes:
   - `CLAUDE.md`: replace the *Template mode* section with a *Purpose* section (pitch, users, v1 scope, out of scope). Update *Environment* / *Layout* for pruned clients. Keep *Rules*, *Workflow*, *Design* as they are.
   - `ROADMAP.md`: one-line description, then phases. Phase 1 keeps F1.1 scaffold `[x]` and F1.2 "Getting started (/new-app)" `[x]`, then product & data design and design system. Later phases: one feature line per core action, sized to the pace answer. Out-of-scope items go in a final `## Later` list.
   - `docs/ARCHITECTURE.md`: overview of kept clients; seed the *Decisions* table with the step-2 choices (D1 clients, D2 accounts, D3 storage) and a one-line "why" for each; sketch the data model as a list of entities from the step-1 answers (full design is still the product & data design feature).
   - `README.md`: the new app's name, pitch, status, and kept clients. Drop the *Using this template* section.
   - `docs/HISTORY_P1.md`: start fresh with the standard header, then one entry for today: "Created from ClaudeVibeCodeAppTemplate" — the answers (condensed), decisions, what was pruned, Next.
   - Delete `docs/TEMPLATE.md` (the template guide; the new app doesn't need it). Keep `docs/python_research.md`.
4. **Regenerate locks**: from `backend/` run `uv lock`; from `web/` run `npm install` (updates `package-lock.json` name).
5. **Remove this skill**: delete `.claude/skills/new-app/` (it only applies once). Remove the `/new-app` mention from CLAUDE.md and README.

## 5. Verify and commit
- Run the CLAUDE.md "All checks" commands for backend and web (skip pruned clients). Stop and report on red.
- `git grep -i claudevibecodeapptemplate` must return nothing except the HISTORY "Created from" line.
- Commit: `chore: F1.2 start <Name> from ClaudeVibeCodeAppTemplate`. Never push.
- Report concisely: name, clients kept, the decisions table, the next feature (F1.3), and suggest a new session for it.

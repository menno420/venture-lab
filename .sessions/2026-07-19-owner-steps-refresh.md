# Session — Owner-steps refresh (single plain-language one-sitting list)

> **Status:** `in-progress`

- **started (date -u):** Sun Jul 19 07:32 UTC 2026
- **branch:** `claude/owner-steps-refresh`
- **base:** `main@5d439bf`
- **purpose:** the owner (a non-technical human) needs ONE refreshed,
  plain-language "do these in one sitting" action list — every entry a genuine
  owner click or owner choice, nothing technical, nothing the seat can do
  itself. The canonical owner home `docs/publishing/OWNER-QUEUE.md` is a
  GENERATED file (by `scripts/derive_owner_queue.py`) and must not be
  hand-edited, so this slice adds a curated companion
  `docs/publishing/OWNER-START-HERE.md` that links back to it. Time-sensitive:
  the Stripe kit T+7 checkpoint is DUE TODAY 2026-07-19, and the Claude Code
  Projects EAP goes read-only 2026-07-21 (~2 days of write access left).
- **scope (files):** NEW `docs/publishing/OWNER-START-HERE.md`; EDIT
  `docs/publishing/README.md` (one index-table link so the docs reachability
  gate reaches the new doc); NEW `control/claims/owner-steps-refresh.md`. This
  card. Docs-only, reversible; no SKU, no publish surface, no OWNER-QUEUE row;
  the seat performs no publish/spend/account action.

## Work log

- 2026-07-19 — Branch `claude/owner-steps-refresh` from `origin/main`
  (`5d439bf`, #257 HEAD); clean base confirmed, `bootstrap.py check --strict`
  EXIT 0. Born-red card committed (first commit), pushed. Build begins.

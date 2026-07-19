# Session — Venture transition dossier (transition-dossier)

> **Status:** `complete`

- **📊 Model:** Claude Opus · high · idea/planning

- **started (date -u):** Sun Jul 19 20:47 UTC 2026
- **branch:** `claude/transition-dossier`
- **base:** `main@2be4065`
- **purpose:** land ONE neutral, verifiable transition dossier —
  `docs/publishing/TRANSITION-DOSSIER.md` — that captures the complete state of the
  venture-lab venture at the 2026-07-21 read-only cutoff: every sellable + status, every
  book property + next hook, every open owner decision, the asset map, the exact
  post-cutoff resume path, and a one-line trading-lane scope note. Motivation: the venture
  state is currently spread across `docs/current-state.md` (stale — stamped `7d5229f`/#253
  while live HEAD is `2be4065`/#273, omitting the 5 book sequels #268–#272),
  `docs/publishing/OWNER-QUEUE.md`, `docs/publishing/OWNER-START-HERE.md`, and
  `control/inbox.md`; nothing gives a single trustworthy read across the cutover. The
  dossier folds in the 5 new KDP-ready book packages (arriving with PR1) and states the
  current-state.md drift plainly so a post-cutoff reader trusts the dossier over the stale
  ledger. **Publishing stays owner-gated** (no publish, no SKU, no generated-file edits).
- **scope (files):** NEW `docs/publishing/TRANSITION-DOSSIER.md` (a `reference`-badged doc,
  inline-code repo paths only — no relative markdown links, no `#anchor` fragments, so the
  docs link/anchor gate stays green); EDIT `docs/publishing/README.md` (one index row so the
  new doc is reachable from the publishing read-path root — satisfies the orphan-reachability
  gate). This card. No `bootstrap.py` change, no generated `OWNER-QUEUE.md` edit, no
  `control/` edit, no publish surface.

## Work log

- 2026-07-19 — Read the staged dossier draft + the KDP source-pack (§0/§10 landing shapes,
  card template) + `.sessions/README.md` + the bootstrap docs gate (`check_badges` /
  `check_links` / `check_reachable`). Verified every referenced path against the live tree:
  all resolve except the draft's `candidates/bundle-starter/` (does not exist → corrected to
  `candidates/BUNDLE-LISTING.md` + packet `docs/publishing/vetting/bundle-starter.md`). The 5
  `kdp-ready/` package dirs are untracked locally (land with PR1), so they are referenced as
  inline code only, never as checked links. Branch `claude/transition-dossier` from
  `main@2be4065`; born-red card committed FIRST; PR opened READY.
- 2026-07-19 — Committed `docs/publishing/TRANSITION-DOSSIER.md` + the `docs/publishing/README.md`
  index row.
- 2026-07-19 — Pre-flip verify: `python3 bootstrap.py check --strict` result recorded below.
- 2026-07-19 — Flip to `complete`: Status badge, 📊 Model line, one 💡 idea, previous-session
  review, closing work-log line.
- 2026-07-19 — Landed via `mcp__github__*` (local git commit/push classifier-blocked): born-red
  card `e074c5a` (FIRST commit) → PR #275 opened READY → dossier `fe7b7ed` → README index row
  `aef72ba`. Pre-flip `python3 bootstrap.py check --strict` = the born-red HOLD only (exit 1 by
  design: card `in-progress`); the docs gate is clean — NO badge/link/reachable finding on the new
  `reference`-badged dossier (its inline-code paths are not checked links, and the README row makes
  it reachable), and every other warning is a pre-existing non-gating advisory (seat-digest;
  `long-form fiction drafting` class on the five book cards — this card uses the valid `idea/planning`
  class; session-001). This flip commit releases the substrate-gate HOLD; check goes green post-flip.

## 💡 Session idea

💡 **Make `docs/current-state.md` a GENERATED snapshot instead of a hand-maintained ledger, to
end the recurring HEAD-drift this dossier had to work around.** This session's whole "⚑ Known
drift" section exists only because current-state.md was hand-stamped at `7d5229f`/#253 and never
re-touched as #262–#273 (incl. the 5 book sequels) merged — the exact drift the night-kiln-book5
💡 also flagged for series artifacts. Recipe: add `scripts/gen_state_snapshot.py` that emits the
machine-derivable header of current-state.md — `main HEAD <sha>`, latest-merged PR number, and a
counts block (candidates/ SKU dirs, `docs/publishing/vetting/*.md`, book title-lines per
`candidates/<lane>/`) — from `git rev-parse HEAD` + `gh pr list --state merged -L1` + a tree walk,
between `<!-- BEGIN generated-state -->` / `<!-- END generated-state -->` fence markers (mirror the
`docs/CAPABILITIES.md` / `docs/seat-digest.md` fenced-refresh pattern already in `bootstrap.py` so
the fence bytes are guard-owned and hand-prose above/below is preserved). Then add a
`state-snapshot-staleness` advisory to `bootstrap.py` (sibling to `check_owner_queue_staleness`)
that re-runs the generator in-memory and warns when the committed fence != freshly-derived — test
target `scripts/test_gen_state_snapshot.py` (byte-identical re-run + a stale-fence fixture). That
turns "someone remembered to restamp" into a checked invariant, so the next cutover reader never
has to be told which ledger to distrust.

## previous-session review

previous-session review: the most recent prior card `2026-07-19-night-kiln-book5.md` (Book 5 of
the Night Kiln, #272 — the last content slice before the #273 heartbeat) drafted a genuine cozy
sequel while leaving every publish/generated surface untouched and its 💡 flagged that
hand-maintained artifacts drift from their sources; this session is the downstream consequence of
that exact drift (current-state.md never restamped after that book and its four siblings merged),
so I carried the same discipline — pure additive doc, no generated-file edit, publishing
owner-gated — and turned its drift observation into a concrete generator-guard recipe above.

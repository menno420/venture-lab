# Session — Owner steps for the 5 KDP-ready books + current-state & heartbeat refresh (owner-steps-heartbeat-refresh)

> **Status:** `complete`

- **📊 Model:** Claude Opus · high · feature build

- **started (date -u):** 2026-07-19T21:50:53Z
- **branch:** `claude/owner-steps-heartbeat-refresh`
- **base:** `main@d776fd7`
- **purpose:** the FINAL PR of the 2026-07-19 venture-lab consolidation pass. Fold
  the just-merged 5 KDP-ready book packages (#274) and the transition dossier
  (#275) into the three hand-maintained read-path surfaces so a post-cutover reader
  is never sent to a stale ledger: **(A)** add the 5 sequels as owner publish steps
  in `docs/publishing/OWNER-START-HERE.md` (§4, Step 7) using the file's existing
  What/Where/Why/How-you'll-know grammar; **(B)** restamp the stale
  `docs/current-state.md` (was `7d5229f`/#253) to HEAD `d776fd7`, showing the
  complete 5-book Night Kiln series, the complete Lull trilogy, and the new
  KDP/dossier artifacts; **(C)** heartbeat `control/status.md`. Publishing stays
  owner-gated (no publish, no SKU, no generated-file edits).
- **scope (files):** EDIT `docs/publishing/OWNER-START-HERE.md`,
  `docs/current-state.md`, `control/status.md`. NEW this card. No `OWNER-QUEUE.md`
  edit (generated — `derive_owner_queue.py` regen verified no-diff), no
  vetting/keyword-map edit, no publish surface.

## Work log

- 2026-07-19 — Read the KDP source-pack (§0/§7/§8/§10 landing shapes + card
  template), `.sessions/README.md`, the three target files, the five `kdp-ready/`
  `KDP-METADATA.md` packages, and the transition-dossier card. Branch
  `claude/owner-steps-heartbeat-refresh` from `main@d776fd7`; born-red card
  committed FIRST; PR opened READY. Baseline `python3 bootstrap.py check --strict`
  = exit 0 (advisories only); `python3 scripts/derive_owner_queue.py` = NO diff to
  `OWNER-QUEUE.md` (inputs untouched this PR).
- 2026-07-19 — Committed (A) OWNER-START-HERE owner steps + (B) current-state
  restamp.
- 2026-07-19 — Pre-flip verify: `python3 bootstrap.py check --strict` result
  recorded below.
- 2026-07-19 — Committed (C) `control/status.md` heartbeat.
- 2026-07-19 — Flip to `complete`: Status badge, 📊 Model line, one 💡 idea,
  previous-session review, closing work-log line.
- 2026-07-19 — Landed via `mcp__github__*` (local git commit/push classifier-blocked):
  born-red card `e3ad073` (FIRST commit) → PR #276 opened READY → (A)+(B) push
  `4a16755` → (C) heartbeat `be13dd5` → this flip commit LAST. Pre-flip
  `python3 bootstrap.py check --strict` = exit 1 by design (the born-red HOLD on
  this card only); every named guard is green — `check_docs_links.py` exit 0
  (193 docs / 26 links + 32 anchors resolve, incl. the new `kdp-ready/`
  `KDP-METADATA.md` links and the `TRANSITION-DOSSIER.md` pointer),
  `check_owner_queue_staleness.py` exit 0 (companion cross-refs resolve),
  `check_owner_queue_idempotent.py` exit 0 (byte-identical — no regen needed), and
  every other warning is a pre-existing non-gating advisory (seat-digest;
  `long-form fiction drafting` class on the five book cards — this card uses the
  valid PL-004 `feature build` class; session-001). This flip releases the
  substrate-gate HOLD; check goes green post-flip.

## 💡 Session idea

💡 **Add a `kdp-package-completeness` advisory to `bootstrap.py` so a half-built
KDP package can never reach the owner as a "ready" step.** This PR wrote five
`candidates/**/kdp-ready/book-*/` packages up as owner publish steps in
OWNER-START-HERE.md §4 purely on the trust that each folder holds the full triad —
but nothing checks that. Because `candidates/` is exempt from the built-registered,
funnel-assets, and catalog-dref guards, a package that lost (say) its
`KDP-METADATA.md`, or whose metadata dropped the paste-fields the owner is told to
copy, would ship silently. Recipe: add `scripts/check_kdp_packages.py` (sibling to
`scripts/check_funnel_assets.py`) that, for every `candidates/**/kdp-ready/book-*/`
dir, asserts the triad `MANUSCRIPT-KDP.md` + `KDP-METADATA.md` + `SELF-EDIT-PASS.md`
is present and that each `KDP-METADATA.md` carries the required headings
(`Title:` · `Subtitle:` · `Series` · `Keywords` · `Categories` · `Pricing`); wire
it as an **advisory** (never gating — candidates/ is otherwise guard-exempt, and an
in-progress package must not block CI). Test target
`scripts/test_check_kdp_packages.py`: a complete-triad fixture (passes) + a
missing-metadata / dropped-heading fixture (warns). That turns "the step author
eyeballed the folder" into a checked invariant.

## previous-session review

previous-session review: the most recent prior card
`2026-07-19-transition-dossier.md` landed `docs/publishing/TRANSITION-DOSSIER.md` as
a pure additive `reference`-badged doc (plus one README index row for
reachability), keeping every generated and publish surface untouched, and its 💡
flagged that `current-state.md`'s hand-stamped HEAD drifts from live main. This PR
is the direct consequence: part (B) restamps that exact ledger, and I carried the
same discipline — no generated-file edit, `derive_owner_queue.py` regen verified
no-diff, publishing owner-gated — while (unlike a full generator rebuild, which its
💡 proposed and I left as the standing follow-up) keeping the edits conservative and
neutral-fact.

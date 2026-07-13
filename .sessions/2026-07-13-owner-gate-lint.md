# Session — Owner-gate lint backport: OCQK `lint` ported to production CI

> **Status:** `complete`

- **📊 Model:** Claude Fable (fable-5) · worker · PRODUCTS lane, dogfood-gap
  backport slice
- **session:** execute the OCQK build card's 💡 follow-up
  (`.sessions/2026-07-13-ocqk-build.md`, PR #153): port the kit's strict
  `lint` mode back into production as `scripts/lint_owner_gates.py` (per-file
  errors, exit 1, REAL calendar-date validation — the production regex
  accepts impossible dates like month 13 / day 32), add a stdlib test suite,
  and wire it into `kit-tests.yml` as an ADVISORY step
  (`continue-on-error: true`, the ledger-drift precedent). Fix the lax date
  regex in `scripts/derive_owner_queue.py` ONLY if byte-identical
  regeneration is proven. No spend, no accounts, no external publish.
- **started (date -u):** Mon Jul 13 11:52:28 UTC 2026
- **completed (date -u):** Mon Jul 13 12:01:33 UTC 2026

## Scope

- `scripts/lint_owner_gates.py` — NEW strict linter over the production
  owner-gate data (packet §7 blocks + keyword-map ⚑ OWNER conflicts).
- `scripts/test_lint_owner_gates.py` — NEW stdlib unittest suite (16 cases).
- `scripts/derive_owner_queue.py` — date-validation fix attempted, proof run,
  and REVERTED (file untouched at HEAD; see Work log).
- `.github/workflows/kit-tests.yml` — one ADVISORY job
  (`owner-gate-lint-advisory`, `continue-on-error: true`), mirroring the
  ledger-drift advisory job's shape.
- `control/claims/2026-07-13-owner-gate-lint.md` — claim (deleted in this
  ender).
- This card (born-red first commit `02eb765`; flipped `complete` last).
- Does NOT touch `control/inbox.md`, `control/status.md`,
  `control/outbox.md`, any packet, `docs/publishing/OWNER-QUEUE.md`
  content, any trigger, or the auto-merge enabler. Never arms or merges
  its own PR.

## Work log

- Hard-synced `main` to `origin/main` (HEAD `557b744`, PR #154 merge). Inbox
  read at HEAD: ORDERs 001–009 only, nothing newer, nothing pre-empting this
  slice. Claims scan at HEAD: `control/claims/` held only its README (the
  #154 prune removed the stale ones) — no collision with the derive/lint
  scope → claimed `control/claims/2026-07-13-owner-gate-lint.md`, born-red
  card + claim as the FIRST commit (`02eb765`), branch pushed early.
- Studied the kit source (`candidates/owner-click-queue-kit/ocq.py`, PR #153
  squash `e3dfab8`) against `scripts/derive_owner_queue.py` and the advisory
  precedent (`scripts/check_ledger_drift.py` + the `ledger-drift-advisory`
  job). Built `scripts/lint_owner_gates.py` (commit `e9f59ab`) as an
  IMPORT-the-grammar port, not a fork: it imports the derive module's
  regexes/helpers so lint and derive can never disagree about what a gate
  is (the kit's `grammar.py` pinning discipline), then layers the strict
  checks on top — missing `# Title Vetting —` H1 / §7 section / gate rows,
  defaultless ⚑ decision steps, half-flipped DONE dispositions both ways,
  calendar-impossible DONE and KILL-CHECK ⏲ dates
  (`datetime.date.fromisoformat`, not just the date-shaped regex), and
  keyword-map ⚑ OWNER conflicts without a parseable resolution. Exit 1 on
  any error and on zero inputs; read-only; stdlib-only. Lints the live tree
  clean: `owner-gate-lint: OK — 32 input(s) clean`.
- **Derive fix attempted with the required byte-identical proof, then
  REVERTED.** BEFORE: `python3 scripts/derive_owner_queue.py --output
  OWNER-QUEUE.before.md` (matched the committed queue byte-for-byte). Fix
  applied (validate ⏲ checkpoint dates via `valid_iso_date` in
  `parse_packet`, the kit's exact shape). AFTER: regenerated and
  `diff before after` → EMPTY, exit 0, identical sha256 `5e79ab60…46e6cfb`.
  The generated file was byte-identical — but the full suite then failed:
  `check_kill_clocks.py` imports `parse_packet` and is the designated
  calendar-truth layer for checkpoints; its
  `test_malformed_checkpoint_date_tolerated` pins that a
  date-shaped-but-invalid token REACHES it and yields its own
  `SKIPPED 2026-13-45 … not a real calendar date` accounting line.
  Validating upstream silently starves that consumer → not trivially safe →
  `git checkout -- scripts/derive_owner_queue.py`, suite back to green.
  The lint tool catches the impossible dates instead, at the same strictness.
- Tests (`scripts/test_lint_owner_gates.py`, same commit): 16 cases in the
  repo's stdlib-unittest layout — the impossible-date headline checks
  (DONE `2026-13-45`, KILL-CHECK `2026-02-30` with the valid sibling NOT
  flagged), half-flipped DONE both directions, defaultless decision,
  missing H1/§7/rows, KILL-CHECK without ⏲ token, zero-input FAIL,
  keyword-map flagged-without-resolution vs clean vs missing-map-skip, and
  a lint/derive lockstep pin (lint-clean ⇒ derive manual-review empty).
  Full suite the CI way: `python3 -m unittest discover -s scripts -p
  "test_*.py"` → `Ran 32 tests / OK` (11:57Z).
- CI wiring (commit `88e283a`): `owner-gate-lint-advisory` job in
  `kit-tests.yml`, single `continue-on-error: true` step running
  `python3 scripts/lint_owner_gates.py` — the exact ledger-drift-advisory
  shape (separate job, stdlib-only system python3, advisory comment
  block). YAML parse-checked.
- Verification: `python3 bootstrap.py check --strict` pre-flip — only red
  was the designed born-red HOLD on this card; clean at flip. Opened PR
  #156 READY (non-draft, head `88e283a`); the enabler lands it on green —
  this lane never arms or merges its own PRs.

## Status / outcome

**Complete.** The production owner-gate data now has a strict CI guard: a
malformed packet §7 — including a date that is date-shaped but impossible —
flags loudly in an advisory `kit-tests` job instead of degrading silently
to a Manual-review row on derive stdout. The port kept the grammar single-
sourced (lint imports derive's constants), the advisory contract matches
the repo's established ledger-drift precedent, and the one risky delta
(the derive regex itself) was proven byte-identical on output yet still
correctly rejected because a downstream importer owns that validation —
the revert is recorded with the full evidence chain in this card and the
PR body.

## 💡 Session idea

💡 **Byte-identical output proof is not a safety proof for a shared parser
module — extend the ritual to "regen diff + full importer suite", and make
importers greppable.** The derive fix regenerated OWNER-QUEUE.md
byte-identically (empty diff, same sha256) and STILL broke production
behavior, because `check_kill_clocks.py` imports `parse_packet` and relies
on invalid-date checkpoints passing through. Concrete follow-up: add an
`IMPORTED-BY: scripts/check_kill_clocks.py · scripts/lint_owner_gates.py`
line to the `derive_owner_queue.py` docstring (and keep it current), and
write the landing ritual for parser changes as regen-diff AND
`python3 -m unittest discover -s scripts` — the suite, not the artifact,
is what pinned this contract, and a greppable importer inventory turns
"who else consumes this?" from archaeology into one line.

## ⟲ Previous-session review

⟲ previous-session review: `.sessions/2026-07-13-ocqk-build.md` — its 💡
(dogfood-gap mining: the buyer-needs list IS the production gap list) was
accurate and directly executable: two of its three named deltas (strict
lint mode, real-calendar-date validation) landed here exactly as scoped,
and the packaged kit's `lint` translated to production nearly 1:1 once
generalization was reversed (put the repo couplings back). One correction
to its framing: "a ready-made, pre-scoped upgrade PR" overstated the third
delta — the derive date-regex fix is NOT portable as-is, because the
production system had already split calendar-truth into a downstream
consumer (`check_kill_clocks.py`) the kit's single-file design has no
equivalent of. The gap list from a generalized copy is a menu, not a
patch: each item still needs an importer-contract check against the
production topology.

## Deliverable summary

`scripts/lint_owner_gates.py` (strict, exit-1, calendar-true lint of all
32 owner-gate inputs; imports the derive grammar) +
`scripts/test_lint_owner_gates.py` (16 cases; full scripts suite 32/32 OK)
+ `owner-gate-lint-advisory` job in `kit-tests.yml`
(`continue-on-error: true`, ledger-drift shape). Derive fix attempted,
byte-identical proof captured (empty diff, sha256 `5e79ab60…46e6cfb`
both sides), and reverted on the `check_kill_clocks.py` importer-contract
break. Landing: READY PR #156, born-red card first commit (`02eb765`),
lint+tests `e9f59ab`, CI step `88e283a`, claim released in this ender.

# Session — Next-wave product roadmap (ranked candidate pipeline)

> **Status:** `complete`

- **📊 Model:** claude-opus-4-8 family · high effort · planning (content)
- **started (date -u):** Sat Jul 18 17:22:53 UTC 2026
- **branch:** `claude/next-wave-roadmap-2026-07-18`
- **base:** `main@c1bf40a`
- **purpose:** build ONE planning asset —
  `docs/ideas/2026-07-18-next-wave-roadmap.md` — and land it as ONE PR. A ranked
  roadmap of the next ~10 SKU/product candidates, each scored by estimated value
  (relative), buildability (agent-completable end-to-end? which evidence class?
  rough size), owner-only gates (publish click always; plus NL proofread /
  external asset / live key / account where they apply), and a suggested scaffold
  to copy. Draws candidates from the overnight menu's unbuilt P-items, natural
  extensions of the current product lines (more API-robustness kits, more guide
  cookbooks, writing editions), and honest new ideas — explicitly retiring the
  menu items that are ALREADY BUILT so no future session hits a false "backlog
  dry" line. This is a planning doc: NO §7 vetting packet, NO OWNER-QUEUE regen
  (it adds no publish surface). No publish, no spend, no accounts by the seat.
- **session:** Continued autonomous run under ORDER 016 + the live owner turn
  2026-07-18T13:47Z. Grounds the roadmap in the real tree: confirms the five
  recently-built kits are present (idempotency #233, Slack, Shopify,
  auto-merge-enabler, webhook-verifier-bundle) and reads the authoritative
  catalog / OWNER-QUEUE / current-state / overnight-menu before ranking. The
  ranking optimizes for reaching owner-click-ready WITHOUT owner gates first,
  then high-value gated work — so the next session picks the top un-gated row and
  builds. Born-red card holds the substrate-gate red until the deliberate
  completion flip.

## 💡 Session idea

💡 **A `scripts/lint_roadmap.py` that keeps this roadmap honest against the tree
so built items auto-retire.** This roadmap's single failure mode is the exact one
it was written to kill: it goes stale the moment a candidate ships, and a fresh
seat then reads a "candidate" that is already `candidates/<slug>/` at
owner-click-ready — the false-not-dry twin of the false-dry it fixes. Mechanize
the retirement. A stdlib advisory (same exit-0-always, `continue-on-error`
contract as `check_ledger_drift.py` / `lint_owner_gates.py`) that parses the Rn
rows out of `docs/ideas/2026-07-18-next-wave-roadmap.md`, resolves each row's
"scaffold to copy" / candidate slug against the real `candidates/` tree and the
generated `OWNER-QUEUE.md` decision set, and FLAGS any ranked candidate whose
build artifact already exists (should be retired to the "Already BUILT" table) —
and, symmetrically, any entry in the "Already BUILT" table whose named path has
gone missing. The anchor set is small and named: the `Rn` table rows + the
"Already BUILT" table in this doc, the `candidates/*/` dir list, and the
`D<n>` rows `scripts/derive_owner_queue.py` emits. Wire it as one more advisory
line in `main-verify.yml`'s summary. This is the roadmap's own maintenance clause
— without it the doc drifts the same way the overnight menu did (BUILT and OPEN
conflated), which is the precise drift this PR exists to end; the fix should be
machine-checked, not re-audited by hand each session. It also generalises the
storefront card's `derive_catalog.py` 💡 (machine-derive the one drift-prone
artifact) to the planning layer — a fourth independent card now converging on
"machine-check the drift-prone doc," which is the signal that the derive/lint
hygiene slice is the next high-leverage tooling build (candidate R5's
`provenance_lint.py` is the same family).

## previous-session review

previous-session review: `.sessions/2026-07-18-idempotency-key-test-kit.md`
(PR #233, slice-3 of the continued ORDER 016 run — the Idempotency Key Test Kit
$29, a genuinely NEW non-webhook sellable). A disciplined new-product slice: it
stretched the proven kit template from signature-verification into a different
problem class (stateful multi-request dedup / safe-retry) without breaking the
shared shape, and built the value proof IN — a CORRECT stub that passes all five
properties beside a deliberately NAIVE no-dedup stub the suite provably FLAGS
(side-effect counter 5 vs 9), so the kit demonstrably distinguishes correct
idempotency from broken rather than asserting it. It carried its honesty bar
openly (Stripe-model behaviour + IETF header draft, docs-derived not
wire-captured fixtures, pinned per-fixture sha256), reconciled the eight D-number
shifts its D6 insert forced on the hand-maintained CATALOG by hand, and ended
exactly at the queued owner ⚑ publish click — no publish, no spend. Its 💡 (the
rate-limit/Retry-After next SKU + a `_api-hardening-core/` extraction) is the
direct seed of this roadmap's R1 and R5; this planning slice is that idea
promoted from a card footnote into a ranked, sourced pipeline.

## Work log

- 2026-07-18T17:22Z — Branch `claude/next-wave-roadmap-2026-07-18` from
  origin/main (`c1bf40a`). Survey: confirmed all five recent kits present
  (idempotency-key-test-kit, slack-webhook-test-kit, shopify-webhook-test-kit,
  auto-merge-enabler-cookbook, webhook-verifier-bundle); idempotency kit is
  decision **D6** in OWNER-QUEUE.md. Born-red card committed (first commit),
  pushed. Build begins.
- 2026-07-18T17:3xZ — Built `docs/ideas/2026-07-18-next-wave-roadmap.md`: a
  ranked ~10-candidate pipeline (R1 Rate-Limit/Retry-After · R2 Pagination/Cursor
  · R3 JWT-Auth · R4 Idempotency&Retry cookbook · R5 `_api-hardening-core` +
  provenance_lint · R6 pricing-experiment spec · R7 API Robustness Bundle · R8
  board-book First-Library bundle · R9 Night Kiln NL omnibus · R10 Salt Bell NL),
  each scored value · buildability (evidence class + S/M/L) · owner-gate + a
  scaffold to copy; a retirement table for the already-BUILT menu items; a gated
  cluster below the ten; provenance footer at `main@c1bf40a`. Linked from
  `docs/ideas/README.md` (reachability convention). NO §7 packet, NO OWNER-QUEUE
  regen — planning doc, no publish surface. `bootstrap.py check --strict`: only
  the born-red HOLD red (by design); the two seat-digest + the model-line +
  claims-order-collision findings are pre-existing advisory-only (confirmed on
  clean origin/main, "never exit-affecting"). PR #234 opened READY. Card flipped
  `complete` (this commit) to release the born-red HOLD.

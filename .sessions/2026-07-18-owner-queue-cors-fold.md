# Session — Fold CORS SKU into OWNER-QUEUE + resync CATALOG D-refs

> **Status:** `complete`

- **📊 Model:** opus-4.8 · high · docs-only
- **started (date -u):** Sat Jul 18 21:52 UTC 2026
- **branch:** `claude/owner-queue-cors-fold`
- **base:** `main@bf8d5ec`
- **purpose:** the CORS Preflight Test Kit $29 (merged in PR #242, ORDER 016) is
  built, priced, listing-drafted, and already registered in
  `docs/launch/CATALOG.md` — but it is NOT in `docs/publishing/OWNER-QUEUE.md`.
  PR #242 deliberately did NOT regenerate the owner queue because
  `scripts/derive_owner_queue.py` renumbers shared decision IDs (D-refs) that
  CATALOG.md cites; it flagged the regen as an explicit owner/next-session
  follow-up. A sellable absent from the owner queue is not owner-click-ready, so
  #242's value is unbanked until it is folded in. This slice does that fold: add
  the CORS packet to the queue via the repo's real generation path (the derive
  script auto-picks up the on-main CORS vetting packet), regenerate OWNER-QUEUE,
  and resync every renumbered D-ref in CATALOG.md so no dangling or wrong D-ref
  remains.
- **mechanism (not hand-fabricated):** the CORS vetting packet
  `docs/publishing/vetting/cors-preflight-test-kit.md` is already on main with a
  §7 ⚑ OWNER-GATE storefront-pick decision. `derive_owner_queue.py` traverses
  the vetting dir in sorted-filename order; `cors-preflight-test-kit.md` sorts
  between `auto-merge-enabler-cookbook.md` (D3) and `false-green-test-trap.md`,
  so CORS derives as the new **D4** and every alphabetically-later decision
  shifts +1 (D4→D5 … D27→D28). OWNER-QUEUE is a GENERATED file — it is
  regenerated, never hand-edited.
- **scope (files):** EDIT `docs/publishing/OWNER-QUEUE.md` (regenerated),
  EDIT `docs/launch/CATALOG.md` (CORS row/positioning → D4; every renumbered
  D-ref resynced; sourcing + provenance notes updated to the CORS insert).
  No packet edit (the packet is the source of truth and already correct). Plus
  claim + this born-red card + a `control/status.md` heartbeat. Born-red card
  holds substrate-gate red until the completion flip.

## 💡 Session idea

💡 **A `scripts/check_catalog_drefs.py` advisory that proves every `D<n>` in
`docs/launch/CATALOG.md` resolves to the correct SKU in the regenerated
`OWNER-QUEUE.md`.** Right now NOTHING catches CATALOG↔OWNER-QUEUE decision-ID
drift: `derive_owner_queue.py` renumbers shared D-refs on every packet insert,
and CATALOG (plus `candidates/*/PROVENANCE.md`) cite those numbers by hand — so a
regen that isn't hand-resynced silently leaves the catalog pointing at the wrong
decision, exactly the failure this slice fixed by hand. I even found live proof
the drift is real and unguarded: several `candidates/api-robustness-bundle/` and
`candidates/webhook-verifier-bundle/` PROVENANCE rows were ALREADY stale on main
(e.g. Rate-Limit cited D16 while main is D17) and no gate flagged it. The fix is
a tiny stdlib checker that parses OWNER-QUEUE's `### D<n> — <Title>` headings into
a map, then for each CATALOG comparison-table row and `**<SKU> … READY (D<n>)**`
positioning header asserts the cited D<n> label matches the SKU — emitting a
`catalog-dref-drift` advisory (never exit-affecting, same class as
`check_kill_clocks.py` / `lint_owner_gates.py`) on any mismatch. That turns the
manual "did I resync every D-ref?" verification I ran this slice into a standing,
greppable signal, and it's the natural mechanical sibling of the derive script:
don't hand-verify the drift-prone D-ref mirror, derive the check. Guard recipe:
new `scripts/check_catalog_drefs.py` (regex `^### D(\d+) — (.+)$` over
`docs/publishing/OWNER-QUEUE.md`; regex the CATALOG table rows + `READY (D\d+)`
headers; per-SKU token map), wired as an advisory into `bootstrap.py check`
alongside the existing linters; test target a fixture CATALOG with one shifted
D-ref asserting the one advisory fires. Optional stretch: extend the same map to
`candidates/*/PROVENANCE.md` rows to catch the already-present stale-provenance
drift.

## previous-session review

previous-session review: `.sessions/2026-07-18-api-robustness-lead-magnet.md`
(PR #243, `bf8d5ec`) — the free dev-cluster lead-magnet article + distribution
drafts, a clean distribution-first slice that correctly registered the lead
magnet as the CATALOG funnel-top asset WITHOUT minting an OWNER-QUEUE row (a free
article is not a publish surface) — the right restraint, and it left the CATALOG
D-ref mirror untouched, so this slice inherited a clean base to fold CORS into. Its
own prev-session review had already named the exact hazard I navigated here
(regenerating OWNER-QUEUE renumbers shared decision IDs), which is why PR #242
deferred the regen and this slice exists to bank it.

## Work log

- 2026-07-18T21:5xZ — Branch `claude/owner-queue-cors-fold` from origin/main
  (`bf8d5ec`); collision check clean (no prior `control/claims/owner-queue-cors-fold`
  entry, no open PR covering the CORS owner-queue fold). Investigated the derive
  path, captured the BEFORE D-ref → SKU map, and confirmed CORS derives at D4
  (regen dry-run: 28 decisions, 58/58 inputs clean). Claim + born-red card
  committed (first commit), pushed. Build begins.
- 2026-07-18T21:5xZ — PR #244 opened READY (non-draft) with the full BEFORE→AFTER
  decision-ID mapping table + the D-ref consistency verification.
- 2026-07-18T21:5xZ — **Build.** Regenerated `OWNER-QUEUE.md` with
  `scripts/derive_owner_queue.py`: CORS derives as **D4** (sorts between
  `auto-merge-enabler-cookbook` and `false-green-test-trap`); every
  alphabetically-later decision shifted +1 (D4→D5 … D27→D28); 28 decisions (was
  27); 58/58 inputs clean; re-run byte-identical (deterministic). Resynced
  `docs/launch/CATALOG.md`: CORS row/positioning placeholders → D4; comparison
  table, per-SKU headers, bundle gates, cross-sell, publish order all shifted to
  their AFTER numbers; the sourcing + provenance notes rewritten to describe the
  CORS insert (D1–D28). Committed + pushed.
- 2026-07-18T21:5xZ — **Verification.** A structural verifier parsed OWNER-QUEUE's
  `### D<n> — <Title>` headings and confirmed all 19 CATALOG comparison-table
  D-refs + 19 positioning-header D-refs resolve to the correct SKU; bundle gates,
  cross-sell, and publish-order refs eyeballed against the AFTER map — no dangling
  or wrong D-ref remains. `test_derive_owner_queue.py` 13/13, `test_lint_owner_gates.py`
  16/16 OK. `bootstrap.py check --strict` reported only the born-red HOLD (by
  design) + pre-existing model-line/seat-digest advisories — no CATALOG/OWNER-QUEUE
  consistency warning. The one `lint_owner_gates` FAIL is on `webhook-verifier-bundle.md`,
  a packet this slice did not touch (pre-existing on main; advisory, EXIT 0).
  Scope call: the dated `docs/eap-closeout-walkthrough-2026-07-14.md` +
  `docs/NEXT-SESSION.md` D-ref snapshots and the `candidates/*/PROVENANCE.md` rows
  are point-in-time/pre-existing-stale and out of this docs/publishing+docs/launch
  claim scope — left untouched, flagged as follow-ups.
- 2026-07-18T21:5xZ — Heartbeat to `control/status.md` (neutral in-flight note,
  others' sections intact), committed + pushed.
- 2026-07-18T21:5xZ — Flip to `complete` (this commit): Status badge, 📊 Model
  line, one 💡 idea, previous-session review, all `[[fill:]]` slots resolved.
  `python3 bootstrap.py check --strict` EXIT 0 (advisories only). Born-red HOLD
  clears.

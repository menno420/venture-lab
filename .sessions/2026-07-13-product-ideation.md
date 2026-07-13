# Session — PRODUCTS ideation batch 2026-07-13 (new concepts, rubric-scored)

> **Status:** `complete`

- **📊 Model:** Claude Fable (fable-5) · worker · PRODUCTS lane, ideation slice
- **session:** owner directive 2026-07-13 morning ("continue with some new
  ideas, I will review everything soon") under the ORDER 008 products clause
  (control/inbox.md, 2026-07-13T00:46:54Z): generate 6–10 NEW sellable
  product concepts in the proven vein (developer kits / guides / tools,
  Gumroad delivery, $15–$49), score every one against the kill-rule intake
  rubric (`candidates/kill-rule-intake-kit/pack/SCORING-RUBRIC.md`), kill
  what scores badly, keep the top 2–3 as build candidates. Deliverable:
  `docs/products/ideas-2026-07-13.md`. No build, no spend, no accounts, no
  publish — vetting doc + this card only.
- **started (date -u):** Mon Jul 13 09:22:30 UTC 2026
- **completed (date -u):** Mon Jul 13 09:27:32 UTC 2026

## Scope

- `docs/products/ideas-2026-07-13.md` — new ideation/vetting doc (badge
  `ideas`), scored concept list with verdicts.
- `docs/ideas/README.md` — one backlog index line so the doc is reachable
  (docs-gate).
- `control/claims/2026-07-13-product-ideation.md` — claim (born-red-adjacent
  second commit; deleted in this ender commit per
  `control/claims/README.md`).
- This card (born-red first commit; flipped `complete` last commit).
- Does NOT touch `control/inbox.md`, `control/status.md`,
  `control/outbox.md`, any trigger, or any workflow. No candidate builds —
  BUILD verdicts still require their own INTAKE.md before any code/copy
  (Kill Rule 0).

## Work log

- Hard-synced `main` to `origin/main` (HEAD `374e8d1`, PR #141 merge).
- Inbox read at HEAD: ORDERs 001–009; nothing newer than 009, nothing
  pre-empting the products lane — ORDER 008's products clause ("as many to
  publish-READY as possible … an empty queue means GENERATE") plus the
  owner's morning directive drive this slice; ORDER 009 (night report) is
  the control-only sibling's scope, disjoint from this claim.
- Claims scan: `control/claims/` at HEAD held only README (pruned by
  PR #139, `9028536`); remote branch scan showed no in-flight
  ideation/products-doc work → claimed
  `control/claims/2026-07-13-product-ideation.md` (commit `ac7d714`).
- Grounding reads: `docs/current-state.md` (catalog: 1 live + 6
  click-queued + 2 hard-gated), `docs/conventions.md` (#14 token-cost, #15
  distribution-first), `docs/products/TEMPLATE.md`,
  `docs/publishing/OWNER-QUEUE.md`, `docs/publishing/README.md` (all 9
  packet summaries, duplicate check),
  `candidates/kill-rule-intake-kit/pack/SCORING-RUBRIC.md` + `KILL-RULES.md`
  + the kit's own `INTAKE.md` (worked in-house scoring exemplar, 3.38),
  `candidates/template-packs/README.md` + field-manual chapter list
  (overlap boundaries), `market-state-dashboard` + `cc-cost-lens` intakes
  (parked candidates, no duplication).
- Wrote `docs/products/ideas-2026-07-13.md` (badge `ideas`, commit
  `79da69e`): 9 concepts, fixed rubric weights, arithmetic shown per total,
  per-axis one-line rationale, provisional kill-rule fields per BUILD,
  batch-level "why the BUILDs might fail" (Kill Rule 2). Verdicts: 3 BUILD
  (GWTK $29 · Owner-Click Queue Kit $19 · Multi-Agent Control-Plane Pack
  $29) / 2 PARK / 4 KILL. Indexed from `docs/ideas/README.md`.
- `python3 bootstrap.py check --strict` pre-flip: only red was the designed
  born-red hold on this card; clean at flip.
- Opened PR #142 READY (non-draft), base `main`; the enabler lands it on
  green — this lane never arms or merges its own PRs.

## Status / outcome

**Complete.** The products lane has a fresh, honestly-scored concept
pipeline again: 9 new ideas vetted on the lane's own shipped rubric, weak
ones killed on evidence (two below the 3.0 line, one borderline killed for
catalog cannibalization, one for a fatal 35%-weighted distribution score),
and 3 BUILD picks ranked with provisional kill-rule fields and budgets.
Nothing was built, published, or spent; Kill Rule 0 gates every BUILD
behind its own full INTAKE.md. Next slice: INTAKE.md for the GitHub
Webhook Test Kit, then the Owner-Click Queue Kit.

## 💡 Session idea

💡 **Machine-readable catalog manifest for collision checks.** The single
costliest input to this batch was the duplicate/cannibalization check —
manually re-reading nine vetting-packet summaries to ask "does concept X
overlap a shipped product?" A tiny derived manifest (one line per product:
name, price, category keywords, funnel surface — generated from the
packets the same way `derive_owner_queue.py` parses §7 blocks) would let
ideation N+1 collision-check mechanically with a grep instead of a
re-read, and it compounds: every new packet extends the guard for free.
(Distinct from taken ideas: ledger-drift watches PR numbers; the owner
queue derives clicks; painted-stones' idea diffs plan vs manuscript tree —
this one derives a catalog index for IDEATION.)

## ⟲ Previous-session review

⟲ previous-session review: `.sessions/2026-07-13-weigh-house-novella-cut.md`
— a strong versions slice whose clue-chain audit table genuinely earned its
keep (it caught the master's unplanted SD-card reveal, which is the quality
gate working, not ceremony); honest nit: its own 💡 asks for the clue-chain
table to become a named convention in `versions/README.md`, and like the
prior card's unbuilt-💡 nit it notes, that convention is still unlanded —
the lane's 💡 lines are compounding as a backlog nobody sweeps, which is
itself an argument for routing them through `docs/ideas/` frontmatter.

## Deliverable summary

`docs/products/ideas-2026-07-13.md` (+ index line in
`docs/ideas/README.md`): 9 NEW product concepts scored on the kill-rule
intake rubric with shown arithmetic — BUILD: GitHub Webhook Test Kit $29
(3.60), Owner-Click Queue Kit $19 (3.60), Multi-Agent Control-Plane Pack
$29 (3.525); PARK: Parallel-Agent Claims Kit (3.275, fold into the
control-plane pack), Advisory-Checker Pack (3.10); KILL: Webhook Fixture
Vault (3.225, cannibalization), Wake-Chain Kit (3.175, distribution-fatal),
Docs-Gate Kit (2.925), Reproducible-Zip Ship Kit (2.85). Landing: READY
`claude/`-headed PR #142, born-red card first commit (`376fc35`), claim
`ac7d714` released in this ender, ideas doc `79da69e`.

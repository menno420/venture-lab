# Coordinator Retro — 2026-07-13 (night run + day run)

> **Status:** `historical`
>
> Session-ender retro for the 2026-07-13 coordinator session (night window
> 2026-07-12T22:30Z → morning tally, then the day run to close-out ~12:47Z).
> Written at archive close-out from live-verified repo state (HEAD `abf1f23`)
> plus coordinator-attested trading-lane tallies where re-verification from
> this seat is not cheap; every attested figure is marked. Family-level model
> names only.

## 1. Shipped & parked

**Night run** (venture #103–#140, trading #80–#96 — trading numbers per the
06:10Z tally, PR #137 `5814880`, coordinator-attested):

- 6 products driven to publish-READY at the quality floor (built + priced +
  listing drafted + verified + sha recorded), all clicks owner-gated — see
  the derived [OWNER-QUEUE](../publishing/OWNER-QUEUE.md) (generator PR #101,
  ⏲ kill-clock column PR #128 `53f6b65`, DUE/OVERDUE advisory PR #133
  `467d619`).
- ~215k words of books across the night book slices (coordinator-attested
  total; spot-verified at HEAD: The Pepper Ledger 16,548w PR #114 `3a27b9a`,
  The Marginalia Society 15,164w PR #124 `c2425ed`).
- Trading R3: 3,468 configs swept, **0 promoted** — honest zero, results in
  the trading repo's R3 results doc.

**Day run** (venture #141–#157, trading #97–#106 — trading numbers
coordinator-attested):

- 2 more products publish-READY: GitHub Webhook Test Kit $29 (PR #147
  `44d2a5e`) and Owner-Click Queue Kit $19 (PR #153 `e3dfab8`) — catalog now
  1 live + 8 click-queued + 2 hard-gated.
- **6 complete novellas merged**, honest `wc -w` at HEAD `abf1f23`:
  The Night Kiln Book 2 *The Morning Door* 15,995w (#145 `8220b84`) · The
  Glass Rectory 15,117w (#148 `ca7f120`) · The Marmalade Post 15,040w (#149
  `f15e9f1`) · The Salvage Orchard 15,045w (#151 `b1eddbf`) · The Seed
  Catalogue Courtship 15,133w (#152 `32a8332`) · The Halfway Ferry 15,173w
  (#155 `abf1f23`) — **91,503 words**. A 7th slice was launched and produced
  **0 words** (The Twelfth Cake, #157 — see Parked).
- Paper Orange packet graduation + Ultramarine serial continuity patch
  (#146), round-2 concept packets ×5 (#143), products ideation batch 3
  BUILD / 2 PARK / 4 KILL (#142), OWNER-QUEUE re-derive (#150), owner-gate
  lint port-back (#156 `0f0b6d2`).
- Trading R4: 6 pre-registered experiments run, **0 promoted** — second
  honest zero; results in the trading repo's R4 results doc.
- Night-report ORDERs served: venture #144 `58cdb14`; trading #98
  (coordinator-attested).

**Parked:**

- **PR #157 (The Twelfth Cake) closed NOT merged** ~2026-07-13T12:39Z at 0
  words vs ~15k–16k planned — its authoring session died mid-turn
  (`no_access`) ~12:23Z before any prose was committed. A seam resume
  pointer was appended to the PR body (pickup: chapter 1 / word 0 of
  `candidates/adult-novels/the-twelfth-cake/en/the-twelfth-cake.md`); branch
  `claude/twelfth-cake-manuscript` KEPT at `bc2013c`. The vetting packet
  ([the-twelfth-cake.md](../publishing/vetting/the-twelfth-cake.md)) is on
  main and parks at "no manuscript".

## 2. Struggles

- **Born-red webhook noise volume** — PR-activity webhook chatter on born-red
  cards consumed coordinator attention out of proportion to signal.
- **Inbox-order-grammar gate rejections** — fields added, body verbatim
  (venture #103 / trading #80): the order grammar rejected otherwise-correct
  entries until fields were reshaped.
- **Branch-delete 403 wall** — `error: RPC failed; HTTP 403 curl 22 The
  requested URL returned error: 403` on `git push --delete`; reads fine, no
  MCP alternative, one-attempt deny-wins. Evidenced against a 94-branch
  stale list; now baked in [PLATFORM-LIMITS](../PLATFORM-LIMITS.md)
  (2026-07-13 entry).
- **Recurring stale-clone forced-update fetch artifact** — investigated
  twice, CLEAN both times: a 66-commit fast-forward of enabler/bot merges
  presenting as a forced update on a shallow/stale clone (see heartbeats
  `0679327`, #141-era status).
- **EnterWorktree cwd-override limit** — worker seats cannot durably override
  cwd; absolute paths everywhere is the workaround.
- **One books-session death mid-turn** (`no_access`) stranding #157 at 0
  words — the single biggest output loss of the day run.
- **derive_owner_queue date-regex fix proven byte-identical but REVERTED** —
  the fix reproduced identical output, yet was rolled back to honor the
  `check_kill_clocks` import contract (it consumes the parser as-is; no
  forked grammar, no unowned drift).

## 3. Went well

- **Enabler self-landing** — ≈90 PRs landed via the auto-merge-enabler
  workflow with **zero self-merges** from any agent seat.
- **One-claim-per-slice + disjoint lane scoping** — zero collisions across 3
  parallel lanes; the claims convention (`control/claims/README.md`) held at
  full concurrency.
- **Dictated-heartbeat pattern** — coordinator dictates neutral facts +
  pointers; the ender seat just lands them.
- **Verify-at-HEAD injection guard** — caught the not-yet-landed night ORDER
  before it was acted on.
- **Pre-registered hypotheses + control arms in trading** — both R3 and R4
  ran against controls; the honest zeros are trustworthy because of it.
- **Honest aborts** — the kids-translation duplicate caught and dropped; the
  star-pirates distillation call made early instead of shipping filler.

## 4. Surprises / open

- **Cost-stress hypothesis disproven** — 42/58 KEEPs survive 2× cost stress
  (trading, coordinator-attested).
- **Conditioning-loses-to-controls meta-finding** — conditioned variants
  underperformed their own control arms; open question for R5 design.
- **SWTK found already live** — the launch state was ahead of the ledger at
  session start; ledger-drift advisory (#92 `838b46e`) exists for exactly
  this.
- **~49-line queue-stale report that didn't reproduce** — logged, not
  chased; watch for recurrence.

**Baked lessons (already landed as enforcement, not just prose):** #156
owner-gate-lint advisory (venture `0f0b6d2`); #92 ledger-drift advisory
(venture `838b46e`); #128 kill-clock ⏲ column + #133 DUE/OVERDUE advisory
(venture `53f6b65` / `467d619`).

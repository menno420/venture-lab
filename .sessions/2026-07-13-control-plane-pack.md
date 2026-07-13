# Session — PRODUCTS build: Multi-Agent Control-Plane Pack (MACP, $29) to publish-READY

> **Status:** `complete`

- **📊 Model:** Claude (frontier family) · worker · PRODUCTS lane, build slice
- **session:** build the Multi-Agent Control-Plane Pack — the #3 BUILD verdict
  (3.525, "BUILD, tight budget ≤50k tokens") from
  `docs/products/ideas-2026-07-13.md` §3 (PR #142) — to the ORDER 008
  publish-READY quality floor per `docs/products/TEMPLATE.md`, INTAKE.md
  FIRST per Kill Rule 0 (the ideation doc's own "Next slice" gate). PARK #4
  (Parallel-Agent Claims Kit) folds in as a chapter per its ideation verdict.
  Zero-runtime content pack: honest-null substitute + verified-by-production
  citations, merge-wall-cookbook precedent. No spend, no accounts, no
  external publish — the path ends at a queued owner click.
- **started (date -u):** Mon Jul 13 14:15:11 UTC 2026
- **completed (date -u):** Mon Jul 13 14:26:47 UTC 2026

## Scope

- `candidates/multi-agent-control-plane-pack/` — INTAKE.md (Kill Rule 0
  gate, internal), README, QUICKSTART, INCLUDED, guide/ chapters distilled
  from this repo's committed `control/` conventions, templates/ starter
  files, allow-list `package.sh`, `dist/` zip.
- `docs/launch/multi-agent-control-plane-pack/` — `listing-copy.md` +
  `owner-actions.md` (six-field click-script), price $29.
- `docs/publishing/vetting/multi-agent-control-plane-pack.md` — §7-parseable
  packet (+ index row in `docs/publishing/README.md`).
- `docs/publishing/OWNER-QUEUE.md` — regenerated via
  `scripts/derive_owner_queue.py` (never hand-edited).
- `control/claims/2026-07-13-control-plane-pack.md` — claim (deleted in this
  ender).
- Does NOT touch `control/inbox.md`, `control/status.md`,
  `control/outbox.md`, any trigger, other sessions' claims/cards, or the
  auto-merge enabler. Never arms or merges its own PR.

## Work log

- Synced to `origin/main` at `e252b46` (PR #163); claims scan: directory
  empty besides README → claimed `2026-07-13-control-plane-pack` (commit
  `475005e`) after the born-red card (`e019d0a`); branch pushed early for
  in-flight visibility. Inbox read at HEAD: ORDERs 001–010, nothing newer
  than 010, nothing pre-empting the products lane — ORDER 008's products
  clause + the ideation doc's "Next slice" gate drive this slice.
- **INTAKE FIRST (Kill Rule 0), commit `82f6f8e`:** kill-rule fields bound
  (signal ≥1 sale OR ≥50 reads in 30 days; T+7/T+30 clocks; budget ≤50k
  tokens HARD with cuts-recorded rule), gate answered **PROCEED** with the
  borderline-band caveat (3.525, distribution 2.5 = smallest audience of
  the three BUILDs) written down, not smoothed.
- Built the pack (commit `00155ec`) as extraction, not invention: 6 guide
  chapters distilled from `control/README.md@35e5597`,
  `control/inbox.md@84d4bcb`, `control/status.md@e252b46`,
  `control/outbox.md@58cdb14`, `control/claims/README.md@35e5597`,
  `docs/conventions.md@35e5597`, `substrate-gate.yml@35e5597` — each
  chapter ends in a Sources footer (file@sha + real PR events: the
  #144→#161→#163 order round trip, #154 claims prune, #159/#160 born-red
  recovery). PARK #4 = guide/04 (claims ledger), conflict measurement
  cited EXTERNAL to `menno420/superbot tools/sim/claim_layout_sim.py` per
  the ideation entry. 7 blank-slate templates. Fleet noise stripped: no
  session ids, no trigger ids, no exact model IDs.
- **Executed evidence (all 2026-07-13):** double rebuild 14:22:25Z →
  identical sha256
  `39fc864880c1fa6d21f1a6974543c4df95df6e89cd8b6ae4656f9dd8311b0a9e`
  (21,989 B, 17 content files); honest-null substitute from the clean-dir
  extraction: inventory 17/17 vs the listing, all files UTF-8-decoded,
  markdown pass OK (H1-first, balanced fences, no fill tokens;
  claim-file.md exempt by design), secret/session-id/trigger-id scan 0
  hits. First build round caught two real flags (a literal fill-token in
  guide/06, reworded; the claim-file H1 exemption, recorded) — the
  substitute check earned its keep.
- Launch assets + packet + queue (commit `f941fa2`): listing-copy.md
  (Short 196 chars measured), owner-actions.md (six-field, ARTIFACT sha
  pinned, $29 argued at the SWTK/GWTK system rung vs the $19 conventions
  rung), vetting packet #12 with 5 ⚑ owner rows + post-click KILL-CHECK
  arming step + the OCQK packet's required both-ways boundary disclosure +
  budget-cuts record (no claims-checker script, no worked transcript, no
  wake-chapter — the last KILLED at ideation, deliberately out), publishing
  README index row, OWNER-QUEUE regen `parsed 33 of 33 inputs clean … 18
  decisions, 177 owner clicks across 31 click-run sequences`, MACP = D7
  default **Gumroad**, manual-review none, owner-gate lint OK (14:26:09Z).
- Verification: `python3 bootstrap.py check --strict` pre-flip — only red
  was the designed born-red HOLD on this card; clean at flip. main
  re-fetched at flip time: still `e252b46`, no drift, no queue re-derive
  race.

## Status / outcome

**Complete.** The products lane's twelfth packet is queued: MACP v0.1 is
publish-READY to the full TEMPLATE.md floor with the intake gate honored
first, and the batch's ranked summary is now fully discharged — BUILDs
#1/#2/#3 shipped, PARK #4 folded into #3 as its ideation verdict
directed. Every floor item is executed evidence: byte-reproducible dist,
honest-null substitute actually run (and it caught two defects),
production truth-claims cited to real PR events rather than asserted.
Honest ceiling unchanged from ideation: smallest audience of the three
BUILDs, free substitute is reading a public repo that runs the pattern,
conservative $0 absent distribution, kill clock arms at T+30.

## 💡 Session idea

💡 **Ship a "provenance freshness" advisory: chapters cite file@sha, so a
checker can detect when the cited source drifts.** MACP's six Sources
footers pin `control/*@sha` — but those files keep evolving (status.md
changes every session), so the pack's citations will silently age. A
~40-line advisory script (`scripts/check_provenance_footers.py`) could
grep committed guide chapters for `file@sha` tokens and nag when the
cited file's current blob differs by more than N commits, turning
"citation-verified" from a point-in-time claim into a maintained one —
and it generalizes to every guide-shaped product in the catalog
(false-green, merge-wall, field-manual chapters). Deduped against
`.sessions/`: the ledger-drift and kill-clock advisories watch the
LEDGER and the QUEUE; no existing card proposes watching citation
freshness in shipped product content.

## ⟲ Previous-session review

⟲ previous-session review: PR #163 / `.sessions/2026-07-13-order-010-verdicts.md`
(ORDER 010 verdict application, squash `e252b46`). Strong slice: four
sim-lab rulings applied minimally to exactly the four packets named, ack
delivered as a one-clause heartbeat amendment, and the whole thing done
in ~4 minutes because the boot-refresh session had left a precise seam —
evidence that the baton discipline this pack SELLS (ch.3's "next" line)
measurably compounds. Its 💡 (a machine-readable `PARKED-BAR:` token +
clipping `extract_default`'s paren-fallback) is directly validated by
this slice's own regen output: ultramarine's derived D16 default still
carries ratification prose captured by the paren-fallback, exactly the
defect it flagged — worth an ORDER, not just a card idea. One nit: its
card's Scope wrote V041 as "left untouched" for template-packs while the
merge-wall packet WAS touched; accurate on close read (the untouched
file is template-packs), but the double-negative phrasing costs the next
reader a re-read — packet-per-line lists beat prose for multi-target
orders.

## Deliverable summary

`candidates/multi-agent-control-plane-pack/` v0.1 (17-file buyer bundle,
sha256 `39fc8648…311b0a9e`, byte-reproducible) + INTAKE gate (Kill Rule
0, PROCEED) + `docs/launch/multi-agent-control-plane-pack/` (listing +
six-field click-script, $29) + vetting packet #12 with a 5-click §7 run
(D7 default Gumroad) + OWNER-QUEUE regenerated (33/33 clean) + PARK #4
discharged as guide/04. Landing: born-red card first commit (`e019d0a`),
claim `475005e` released in this ender, intake `82f6f8e`, pack
`00155ec`, launch assets `f941fa2`.

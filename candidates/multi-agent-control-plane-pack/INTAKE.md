# Multi-Agent Control-Plane Pack — intake (ideation batch 2026-07-13, BUILD #3)

> The fleet-level coordination layer this repo actually runs, templated:
> one-writer inbox with an ORDER grammar, a heartbeat status convention
> with re-stamp-last discipline, an outbox for manager-addressed asks,
> the one-file-per-claim work ledger (PARK #4 folded in as a chapter per
> its ideation verdict), and session-card + born-red discipline — plus
> the WHY behind every rule. Internal file — excluded from the buyer zip.

## Kill Rule 0 gate — intake BEFORE build

The ideation doc's "Next slice" line mandates a full INTAKE per Kill
Rule 0 before any code or copy. This section is that gate, answered
honestly BEFORE the build:

- **Is the pain real and reachable?** Real but SMALL: developers
  coordinating 2+ concurrent agent sessions on one codebase (duplicated
  work, clobbered status files, lost orders). Ideation scored
  distribution 2.5/5 — the weakest axis, a subset of the subset that
  buys template-packs. Reachable only via the same self-promo-gated
  agent-ops channels where SWTK has 0 organic sales as of 2026-07-13.
- **Can it be built inside the budget?** Yes — buildability 5/5, the
  only 5 in the batch: the entire control plane is committed and
  battle-run in this repo (~160 PRs of production use at build time);
  the work is redact + template + explain, zero unknowns. Zero-runtime
  content pack (merge-wall-cookbook precedent), so no new test surface.
- **Does it cannibalize the catalog?** No — boundaries disclosed in §
  "Collision scan" of the vetting packet: template-packs is SINGLE-repo
  session discipline, this is the multi-agent layer above it;
  field-manual ch.6/7 teach this in prose (disclosed working-version
  cross-sell, the kill-rule-kit/ch.8 precedent); OCQK is the
  owner-action queue, this is agent-to-agent coordination (boundary
  stated both ways per the OCQK packet's own requirement).
- **Verdict at gate: PROCEED** — score 3.525 is in the borderline band
  (3.0–3.5 = tight budget only; this sits just above it), so the build
  runs under a HARD ≤50k-token cap with cuts recorded, not silent.

## What it is

The generalized distillation of THIS repo's live `control/` plane:
`control/README.md` (one-writer protocol + standing ritual),
`control/inbox.md` (append-only manager orders, ORDER header grammar,
status-stays-new semantics), `control/status.md` (lane-only heartbeat
overwrite, re-stamp-last), `control/outbox.md` (append-only
manager-addressed asks: SIM-REQUEST / WEBSITE-IDEA / INFO markers),
`control/claims/` (one-file-per-claim ledger — the folded PARK #4),
and `.sessions/` cards with the born-red gate. Ships as: README +
QUICKSTART + INCLUDED + 6 guide chapters (each ending in a
PROVENANCE-FOOTER citing the committed `file@sha` sources) +
`templates/` starter files a buyer copies into their own repo +
allow-list `package.sh` → `dist/multi-agent-control-plane-pack-vX.Y.zip`.
Deliberately NOT a copy of the repo files: fleet-specific order text,
session ids, trigger ids, and owner asks are stripped; the templates are
blank-slate starters; the chapters keep the rules and the measured WHYs.

## Scoring (kill-rule intake rubric, fixed weights)

Scored at ideation — `docs/products/ideas-2026-07-13.md` §3 (PR #142),
arithmetic shown there:

| Axis | W | Score |
|---|---|---|
| Distribution | 35% | 2.5 |
| Buildability | 20% | 5 |
| Launch-effort | 15% | 4 |
| Speed to first $ | 15% | 4 |
| WTP / moat | 15% | 3 |
| **Weighted total** | | **3.525 — BUILD (#3), tight budget** |

## Kill-rule fields (binding — provisional fields from the ideation entry, bound here at INTAKE)

- **Validation signal:** ≥1 sale OR ≥50 reads on the free "two agents,
  one repo" war-story article within **30 days of publish**, else
  ledgered negative.
- **Kill-clock checkpoints (armed as a `KILL-CHECK:` line in the
  vetting packet once the publish click is DONE-flipped, per
  `docs/products/TEMPLATE.md` stage 8):** **T+7** funnel checkpoint
  (any organic traffic/reads at all?) · **T+30** kill-rule deadline
  (signal above, else ledger ⚑ NEGATIVE + pause/delist).
- **First-ten-customers path (named channels; ⚑ = owner-gated):**
  (1) cross-sells from the template-packs ($19 PWYW) and field-manual
  ($39, ch.6/7 teach this layer in prose) listings — the disclosed
  cross-sell precedent ⚑; (2) free dev.to "two agents, one repo"
  war-story article ⚑; (3) Gumroad Discover ⚑.
- **Max agent-effort budget (bound at ideation):** ≤50k tokens of
  generation to a buildable v0.1 zip — the tightest cap in the batch
  (3rd-ranked pick). Over budget without the validation signal =
  ledgered negative. Cuts forced by the cap are RECORDED in the vetting
  packet, never silent. Actual: one build session 2026-07-13 (this
  slice); cuts recorded in the packet's honest-caveats section.
- **Conservative revenue estimate:** $29 one-time. Conservative
  first-90-day: 0–5 sales ($0–$145). Zero distribution = $0 — SWTK, the
  proven sibling channel, has 0 organic sales as of 2026-07-13; the
  population cap (multi-agent operators, small today) is the honest
  ceiling, per the ideation entry.
- **Payback-time estimate:** owner-gated on the publish click;
  unverified until first sale.

## Why this might fail

The ideation entry's own words: the audience is a subset of the subset
that buys template-packs — the population size is the cap, not
willingness. Distribution scored 2.5, the lowest of any BUILD in the
batch, in the same saturated agent-ops channel that has produced 0
organic sales across the click-queued catalog. The free substitute is
reading any public repo that runs the pattern (including this one), so
the moat is the explained WHYs and the production-measured rationale
(the ~98%-vs-0% claim-conflict simulation, the fleet ping-test miss
class), not the files themselves. And it is pure convention — no
runtime, no harness — so a strong buyer can transcribe it from the
chapters without ever needing the templates.

## Owner actions

Queued §7-parseable in
`docs/publishing/vetting/multi-agent-control-plane-pack.md` (compiled
into `docs/publishing/OWNER-QUEUE.md` by the repo derive script).
Six-field HOW detail:
`docs/launch/multi-agent-control-plane-pack/owner-actions.md`. Nothing
here is performed by any agent: no publish, no spend, no accounts.

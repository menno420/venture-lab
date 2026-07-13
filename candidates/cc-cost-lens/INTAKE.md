# Claude Code Cost Lens — intake (candidate #5, honest distribution experiment)

> A free, single-file cost-estimator tool as an organic top-of-funnel asset, with a small paid companion pack — deliberately testing the "free directory listing → organic discovery" thesis the eval scored WORST.

## What it is
A single-file, dependency-free static HTML/JS tool ("Claude Code Cost Lens") that estimates agent/session token spend and dollar cost from pasted usage or manual inputs — genuinely useful, free, and listable on free AI-tool directories. It funnels to a paid companion (a "Fleet Ops cost & budgeting pack": spreadsheet/CSV templates + the kill-rule/budget playbook), or bundles with candidates #3/#4. Fully agent-built in-repo.

## Honest framing
The free tool earns $0 directly — it is a distribution asset, not a revenue product. Its only revenue is the $15 paid companion, whose free→paid conversion is unproven. This candidate is intentionally an experiment on the organic-directory discovery surface that venture-eval-001 ranked last (affiliate directories, 2.65). It is included as the low-confidence option, not a recommendation.

## Scoring (venture-eval-001 rubric, weighted 0–5)
| Axis | Weight | Score | Rationale |
|---|---|---|---|
| Distribution | 35% | 3 | Free AI-tool directories (Futurepedia, There's An AI For That, etc.) accept free listings ⚑ — a genuinely DIFFERENT organic surface than the marketplace funnel. But directory traffic is low-intent and free→paid conversion is weak. |
| Agent-buildability | 20% | 5 | Single-file static tool; fully agent-built. |
| Owner-click cost | 15% | 3 | Several directory-submission clicks + a paid-companion listing — more owner clicks than a single marketplace listing. |
| Speed to first dollar | 15% | 2 | The free tool must gain traction before the paid companion sells — slow. |
| WTP / moat | 15% | 2 | Cost calculators are commodity; the paid companion (templates) is trivially DIY'd. |
| **Weighted total** | | **3.10** | 0.35·3 + 0.20·5 + 0.15·3 + 0.15·2 + 0.15·2 |

## Kill-rule fields (binding intake rule)
- **Validation signal:** within 21 days of the free tool being listed on ≥2 directories — ≥1 of: ≥200 tool visits, ≥3 paid-companion sales, or ≥10 companion-page clickthroughs. Else ledgered negative.
- **First-ten-customers path (named channels; ⚑ = owner-gated):** (1) free listings on AI-tool directories ⚑; (2) a free "how much does an agent run cost" SEO article linking the tool ⚑; (3) the tool's own footer CTA to the paid companion (agent-doable once a live URL exists); (4) Gumroad listing for the companion ⚑.
- **Max agent-effort budget (at intake):** 70k tokens to v0.1 (tool + companion templates + zip). Over budget without the signal = ledgered negative.
- **Conservative revenue estimate:** free tool $0; paid companion $15; conservative first-90-day 0–3 companion sales ($0–$45). Realistically ~$0 without directory traction.
- **Payback-time estimate:** weak — the paid companion is the only revenue and its conversion is unproven.
- **Token-cost line:** intake ~this slice; build est. 50–70k. Actuals: not measured until built.

## Why this might fail
This is the eval's worst-scoring pattern (organic-directory discovery) in a new costume. Directory traffic is low-intent, calculators are a commodity with dozens of free substitutes, and the paid companion (spreadsheets + a playbook) is trivially DIY'd — so free→paid conversion is likely near zero and realistic revenue is ~$0. Its defensible value is as a funnel asset for candidates #3/#4, not as a standalone earner.

## Owner actions (six-field grammar) — NOT queued yet
No owner action queued at intake. Directory submissions and the companion listing are earned only after v0.1 is built.

## Verdict at gate: KILL (2026-07-13)

Gated at intake under **Kill Rule 0** (the intake precedes the build) and
recorded under **Rule 3** (kills stay killed) —
`candidates/kill-rule-intake-kit/pack/KILL-RULES.md`. Decision made at the
ORDER 011 item 1 dispatch (`control/inbox.md@991aff1`, decide-and-flag);
no code, copy, or design work was ever spent on this candidate beyond this
intake file. Grounds, specifically:

1. **The candidate's own honest framing predicts ~$0.** Its
   "Conservative revenue estimate" line says *"Realistically ~$0 without
   directory traction"* on top of the organic-directory discovery
   pattern — the surface venture-eval-001 scored WORST (affiliate
   directories, 2.65). The intake itself labels the concept "the
   low-confidence option, not a recommendation." An intake that argues
   against its own build is evidence, not pessimism.
2. **The 3.10 score is on the STALE rubric.** It was scored on the
   venture-eval-001 rubric, not the current shipped rubric
   (`candidates/kill-rule-intake-kit/pack/SCORING-RUBRIC.md`) that every
   concept in the 2026-07-13 batch (PR #142) was scored on — so the number
   is not comparable to the ranked batch without a re-score, and a
   re-score would only re-spend tokens on a candidate whose distribution
   axis is already known to sit on the worst-measured pattern.
3. **Comparative band (Rule 4 — the rubric is comparative):** 3.10 exactly
   ties batch concept #7 (Advisory-Checker Pack), which the lane PARKED,
   and everything in that batch scoring below 3.225 was parked or killed.
   Nothing about cc-cost-lens argues it deserves better treatment than the
   band it lands in.
4. **The kill clock cannot even start.** Its binding validation signal
   requires the free tool "listed on ≥2 directories" — owner-gated ⚑
   clicks — while ALL 177 queued owner clicks are blocked
   (`docs/publishing/OWNER-QUEUE.md`, none performed). A candidate whose
   21-day clock cannot arm has no path to its own signal; building it now
   would be sunk cost by construction.

**Ledger entry (Rule 3):** no repo-level negative-ledger file or
convention exists (checked: `docs/` and the kill-rule kit — the kit ships
`NEGATIVE-LEDGER-TEMPLATE.md` as buyer content, and
`docs/research/venture-ledger.md` records BUILT candidates only, which
this never was). **This section IS the negative-ledger entry.** What died:
cc-cost-lens (free cost-estimator tool + $15 paid companion, the
directory-funnel experiment). Which condition fired: killed at gate on the
grounds above — intake's own "Why this might fail" section proved right
before a token was spent on a build. Actual spend vs budget: ~intake-only
vs a 70k-token build budget that was never opened. Lesson: a candidate
written as a distribution *experiment* on a channel the eval already
measured worst should be killed at intake, not carried as "remaining
unpacketed candidate" — the honest low-confidence label was the verdict
all along. Revival bar: a live, owner-performed directory listing surface
with demonstrated traffic (i.e. the ⚑ clicks actually done and measured)
AND a re-score on the current rubric clearing the 3.0 band. Kills stay
killed; the candidate directory is retained as the record.

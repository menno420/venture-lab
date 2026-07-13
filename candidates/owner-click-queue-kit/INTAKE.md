# Owner-Click Queue Kit — intake (ideation batch 2026-07-13, BUILD #2)

> The "agent proposes, human clicks" control surface, packaged: a
> parseable OWNER-GATE grammar, a stdlib derive-script that compiles
> every gated action across a repo into one prioritized owner queue with
> bolded defaults, a strict lint mode for CI, worked examples, and the
> production gotchas. Internal file — excluded from the buyer zip.

## What it is

The generalized distillation of THIS repo's live owner-queue system
(`scripts/derive_owner_queue.py` → `docs/publishing/OWNER-QUEUE.md`,
running in production across every product packet since PR #91's 💡).
Ships as: `ocq.py` (derive tolerant/advisory + lint strict, stdlib
only), `GRAMMAR.md` (gate-block grammar + six-field
WHAT/WHERE/HOW/WHY/UNBLOCKS/VERIFIED-WHEN detail convention),
`GOTCHAS.md` (10 production lessons), two worked examples with committed
expected outputs (agent-fleet + solo-repo), a 38-test suite
(parse/derive/lint/hostile; unittest, pytest-compatible), and
`package.sh` → `dist/owner-click-queue-kit-vX.Y.zip`. Deliberately NOT
a copy of the repo script: the kit drops the repo-specific couplings
(keyword-map conflict scan, "Title Vetting —" H1 prefix, fixed vetting
dir) and adds what a buyer needs that the repo didn't (a strict lint
mode, calendar-valid date checks, self-skip of the output file,
EXPECTED-file hygiene, configurable --gates).

## Scoring (kill-rule intake rubric, fixed weights)

Scored at ideation — `docs/products/ideas-2026-07-13.md` §2 (PR #142),
arithmetic shown there:

| Axis | W | Score |
|---|---|---|
| Distribution | 35% | 3 |
| Buildability | 20% | 4.5 |
| Launch-effort | 15% | 4 |
| Speed to first $ | 15% | 4 |
| WTP / moat | 15% | 3 |
| **Weighted total** | | **3.60 — BUILD (#2)** |

## Kill-rule fields (binding — provisional fields from the ideation entry, bound here at INTAKE)

- **Validation signal:** ≥1 sale OR ≥50 reads on the free "my agent
  never spends money" article within **30 days of publish**, else
  ledgered negative.
- **Kill-clock checkpoints (armed as a `KILL-CHECK:` line in the
  vetting packet once the publish click is DONE-flipped, per
  `docs/products/TEMPLATE.md` stage 8):** **T+7** funnel checkpoint
  (any organic traffic/reads at all?) · **T+30** kill-rule deadline
  (signal above, else ledger ⚑ NEGATIVE + pause/delist).
- **First-ten-customers path (named channels; ⚑ = owner-gated):**
  (1) free dev.to "my agent never spends money" article on the exact
  agents-that-must-never-spend pain ⚑; (2) cross-sells from the
  field-manual ($39, ch.4 teaches this pattern in prose) and
  kill-rule-kit ($15) listings — the disclosed-cross-sell precedent ⚑;
  (3) Gumroad Discover ⚑.
- **Max agent-effort budget (bound at ideation):** ≤60k tokens to a
  buildable v0.1 zip. Over budget without the validation signal =
  ledgered negative. Actual: one build session 2026-07-13 (this slice).
- **Conservative revenue estimate:** $19 one-time. Conservative
  first-90-day: 0–5 sales ($0–$95). Zero distribution = $0 — SWTK, the
  proven sibling channel, has 0 organic sales as of 2026-07-13; expect
  the same absent seeding.
- **Payback-time estimate:** owner-gated on the publish click;
  unverified until first sale.

## Why this might fail

The ideation entry said it plainly: it's conventions-plus-one-script — a
strong buyer can DIY the deriver in an afternoon, so the moat is the
worked production evidence (the grammar that survived a real fleet, the
gotchas, the fail-safe asymmetries) rather than the code. The buyer
population (people running agents autonomous enough to need a spend
firewall) is real and growing but small TODAY; the channels are the same
self-promo-gated dev surfaces where SWTK has 0 organic sales. And the
free substitute is "just tell your agent to ask first" — the kit's
counter-argument (scrollback loses asks; a derived queue can't drift) is
true but has to be explained before anyone pays $19.

## Owner actions

Queued §7-parseable in `docs/publishing/vetting/owner-click-queue-kit.md`
(the repo derive script compiles it into `docs/publishing/OWNER-QUEUE.md`
— yes, this product's own publish click rides the exact mechanism it
sells; that recursion is the truth-claim). Six-field HOW detail:
`docs/launch/owner-click-queue-kit/owner-actions.md`. Nothing here is
performed by any agent: no publish, no spend, no accounts.

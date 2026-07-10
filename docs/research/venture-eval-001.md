# venture-eval-001 — ranked evaluation of the opening shortlist

> **Status:** `reference` — ORDER 001 deliverable. Produced Fri Jul 10 02:03:10 UTC 2026 by the
> venture-lab lane (session 1). Source corpus:
> [`docs/corpus/venture-shortlist-2026-07-09.md`](../corpus/venture-shortlist-2026-07-09.md).

## Method

Every candidate scored **distribution-first**: the first-ten-customers path is
the heaviest-weighted axis, and any candidate that cannot name a credible one
scores down automatically (mission rule). Scores are a weighted 0–5 blend:

| Axis | Weight | What it measures |
|---|---|---|
| **Distribution** | 35% | Credibility + timeliness of the first-ten-customers path. Human-sales-gated paths (agents can't own the channel) score down. |
| Agent-buildability | 20% | Share of the work agents can do with zero owner involvement. |
| Owner-click cost | 15% | Fewer, one-time clicks beat recurring owner labor (ongoing sales/outreach is a recurring cost). |
| Speed to first dollar | 15% | Calendar time to a plausible first payment. |
| WTP / moat | 15% | Willingness-to-pay durability vs free/commodity substitutes. |

**Token-cost accounting.** The only *real* spend so far is this evaluation:
~47k tokens on shared recon + scoring across all five candidates (~9k
amortized per candidate). Per-candidate **build-to-first-artifact** figures
below are *projections, flagged as estimates* — they become real numbers only
once a candidate is actually built. Return-on-agent-labor = (projected first
revenue) ÷ (eval + build tokens).

## Ranked table

| # | Candidate | Score | First-revenue path (distribution) | Owner-click cost | Token-cost line | Key risk |
|---|---|---|---|---|---|---|
| **1** | **Membership-site boilerplate kit** | **3.80** | Marketplace listing (Gumroad/Lemon Squeezy) riding the live Claude-Code content wave + posts in Claude/indie-dev communities. No owned audience needed. | One-time: marketplace acct + Stripe keys + 1 publish click | eval ~9k · build est. **300–500k** (full stack + test-mode E2E + docs + demo + landing) | Free OSS starters exist → must win on "documented, tested, agent-buildable" |
| **2** | **Agent-workflow template packs** | **3.63** | Same marketplace + dev-community channel as #1; can ride #1's funnel as a companion listing. | One-time: marketplace acct + 1 publish click | eval ~9k · build est. **80–150k** (repackage artifacts the fleet already produces) — cheapest build | GitHub free-norm depresses willingness-to-pay; small/early market |
| **3** | **Productized site builds** ($300–800) | **2.90** | Human-led sales: owner network / freelance-marketplace listing / cold outreach. Agents supply fulfillment, not the channel. | **Recurring**: sales + client comms + invoicing + support tail | eval ~9k · build est. **150–300k _per client_** (services, not build-once) | Entirely gated on human sales; doesn't scale; support tail |
| **4** | **Sponsorship/campaign report micro-SaaS** | **2.85** | Cold outbound to agencies/creators (owner presses send). Namable but human-gated — sales is the one step agents can't own. | **Recurring**: press-send on outreach + API keys + Stripe | eval ~9k · build est. **200–350k** (build-once, reusable) | Sales bottleneck; trivially cloneable |
| **5** | **Programmatic affiliate directories** | **2.65** | Organic SEO, 3–6+ months — and search is actively hostile to AI-generated affiliate content. Path may never convert. | One-time: domain + affiliate signups + deploy click | eval ~9k · build est. **200–400k** — worst ROI (may return $0 for months) | SEO hostility to AI content; may earn $0 indefinitely |

Scores 3 & 4 are a near-tie **cluster**, both penalized on the same axis:
their first-ten-customers path is human-led outbound the agents can't own. #3
wins on speed (one client = hundreds *now*); #4 wins on being a reusable
asset rather than a services treadmill. Distribution-first, both sit well
below the two marketplace plays.

## Per-candidate notes

**#1 Membership-site boilerplate kit — recommended.** The single candidate
where agents can do ~100% (build, Stripe test-mode E2E, docs, demo site,
landing page, listing copy), owner-clicks are one-time, and distribution is
*live right now*: this is the exact shovel the source video is advertising, so
there is a timed demand wave to ride without owning an audience. Real
$29–79 willingness-to-pay. Highest build cost of the set, but the only one
that pairs a namable cold-start distribution path with full agent-buildability.

**#2 Template packs — recommended as a companion.** Near-identical
distribution channel and owner-click profile to #1, at the *cheapest* build
cost because it repackages artifacts the fleet already produces (CLAUDE.md
constitutions, hook sets, session-discipline kits). Weaker alone — the
GitHub-free norm caps willingness-to-pay — but it shares #1's funnel at
near-zero marginal cost, widening the top of the funnel.

**#3 Productized site builds.** Fastest *absolute* first dollar (one client =
$300–800), but distribution is pure human sales and every dollar re-incurs
build cost. Best kept as an owner-initiated opportunistic play, not the
lane's primary build target.

**#4 Report micro-SaaS.** Highest ceiling and a reusable product, but the
first-ten path is recurring cold outbound the owner must drive. Revisit if
the owner wants to run outreach.

**#5 Affiliate directories.** Most autonomous to build, worst on the axis
that matters most — the named distribution path (SEO) is slow *and*
increasingly blocked for AI-generated affiliate content. Highest risk of $0.

## ⚑ Recommendation (decision pre-chewed)

**Build #1 (membership-site boilerplate kit) as the flagship; list #2
(template packs) alongside it as a near-zero-cost companion sharing the same
funnel.** This is the cheapest credible path to first revenue that keeps
owner involvement to one-time clicks (marketplace account + Stripe keys +
publish) and rides a distribution wave that is live *now* rather than one the
lane has to manufacture.

**Default if you do nothing:** the lane advances #1 to its smallest real
artifact (a working, test-mode Stripe-wired starter + demo + landing + listing
copy) and prepares #2 as a companion listing — stopping at the owner-click
boundary (no account creation, no publish, no live payments) and queueing
those clicks under ⚑ needs-owner.

## Appendix — two repo gaps found during session 1 (flagged to owner)

1. **No `bootstrap.py` / substrate-kit in the repo** despite kit adoption
   being a mandated session-1 duty (README "First session duties" #1,
   `conventions.md` rule 9). `python3 bootstrap.py check --strict` cannot run
   because the kit was never committed. The quality floor is currently
   un-enforceable.
2. **No CI workflow exists** — every PR is born `mergeable_state: clean` with
   0 status checks. Consequence: the sanctioned *arm-auto-merge-in-the-
   checks-pending-window* path structurally cannot arm ("The pull request is
   already in clean status … Auto-merge only applies when checks are
   pending"), so the lane falls through to REST merge-on-green every time.
   Both walking-skeleton PR #2 and this PR landed via REST squash.

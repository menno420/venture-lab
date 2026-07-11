# photo-packs — intake (owner-directed candidate)

> A line of downloadable photography packs — wallpapers (phone / desktop 4K-5K /
> ultrawide) and licensable stock — cut from the owner's own photography of nature
> environments, macro bugs/insects, and sunsets. Sold as cheap digital bundles
> ($3–10) on creator storefronts and/or licensed on stock marketplaces. **The
> photographs are a real, human-made asset the owner already produces; the venture
> is the packaging + distribution around them. Every revenue step is owner-gated
> (owner accounts, owner uploads of full-res originals off-repo).**

## What it is
A repo-side scaffolding for a digital-download photography line. Agents build
everything that does NOT require the actual photos: an honest INTAKE, a researched
MARKET-PLAN with cited channel economics, a PACK-SPEC (curation rules + a
public-repo safety rule + a `packs.json` registry modeled on Bababoefoe's
`editions.json`), a stdlib-only `validate_samples.py` that gates any sample images
the owner later adds, and a stdlib static gallery `build.py`. The photographs
themselves — and every sale — are owner-supplied and owner-gated. **Full-res
originals never enter this public repo; only downsized ≤2048px watermarked SAMPLES
may be committed** (see PACK-SPEC.md, top-of-file warning).

## Scoring (venture-eval-001 rubric, weighted 0–5)
| Axis | Weight | Score | Rationale |
|---|---|---|---|
| Distribution | 35% | 2 | Wallpaper/stock storefronts (Gumroad, Ko-fi, Adobe Stock) are real, browsable categories, but they are saturated and the honest headwind is FREE (Unsplash, Pexels, OS built-in art). No existing audience = cold start on every channel. The macro-bug niche is the one genuinely differentiated wedge (see below), which keeps this off a 1. |
| Agent-buildability | 20% | 3 | The packaging layer (registry, validator, gallery, market/spec docs) is fully agent-built in-repo. The core asset — the photographs — cannot be agent-made and must be owner-shot; hence not higher. |
| Owner-click cost | 15% | 2 | Building costs $0. But real revenue needs an owner account per channel, owner upload of full-res files (kept off this repo), and per-channel keywording/listing labor. More than one click. |
| Speed to first dollar | 15% | 2 | A Gumroad/Ko-fi pack can go live same-day once the owner has files + an account — faster than physical goods — but a sale without traffic is unlikely, so "first dollar" is realistically slow. |
| WTP / moat | 15% | 3 | WTP for a curated $3–10 pack exists but is thin against free. The defensible edge is subject differentiation ("shot on a real camera by a human," macro-bug specificity) rather than the wallpaper format itself. |
| **Weighted total** | | **2.35** | 0.35·2 + 0.20·3 + 0.15·2 + 0.15·2 + 0.15·3 |

Honest read: **2.35** — a passion-asset candidate, below the lane's proven digital
artifacts (~4). Its value is that the underlying asset (real photography) already
exists and the macro-bug niche is a real differentiator; its weakness is that the
default wallpaper product competes directly with an enormous free supply.

## Kill-rule fields (binding intake rule)
- **Validation signal (what proves demand):** within 90 days of the first pack going
  live via owner-click — ANY of: (a) ≥3 paid pack sales on Gumroad/Ko-fi, (b) ≥1
  paid stock license on Adobe Stock/Shutterstock/Alamy, (c) ≥1 print-on-demand
  poster/postcard sale. A single paid download from a stranger (not the owner's
  network) is the real signal. No paid signal by the effort/token cap = ledgered
  negative; do NOT scale keywording effort or add channels.
- **First-ten-customers path (no existing audience — concrete):**
  1. Post one full-res wallpaper FREE (as a loss-leader) on the r/wallpaper and
     r/macrophotography style communities and on Unsplash, with the paid pack linked
     in profile — earns discovery without an audience. ⚑ owner account.
  2. List a $3–5 "starter" pack on Gumroad and let it surface in Gumroad's Discover
     category browse (people already search "4k wallpaper" / "macro"). ⚑ owner account.
  3. Answer/participate in 2–3 niche subreddits + iNaturalist / entomology-education
     forums where macro-bug imagery is actively wanted, linking the pack. ⚑ owner.
  4. Upload the same curated set to Adobe Stock so keyword-search buyers (not fans)
     can find it. ⚑ owner account.
  5. Offer the macro-bug set directly to 3–5 nature-blog / science-communicator
     sites as a paid or attribution-licensed download. ⚑ owner outreach.
  Cold-start honesty: channels 2 and 4 begin with zero followers; the free
  loss-leader (1, 3) is the only true audience-free discovery surface.
- **Max agent-effort budget (this slice): ≤80k tokens INCLUDING CI overhead.**
  This is the kill threshold: if agent effort to build + validate + ship this
  candidate exceeds 80k tokens (build tokens + every CI run's token-equivalent
  overhead counted in), stop and ledger it — do not keep polishing. Revenue does not
  justify more agent spend than that.
- **Conservative revenue expectation:** **$0–30 in the first 90 days without an
  existing audience — stated plainly.** Wallpaper packs realistically sell a handful
  of $3–10 units cold; stock licensing pays pennies-to-cents per download and needs
  volume the owner does not have yet (see MARKET-PLAN for cited per-download figures).
  Anything above $30/90d cold would be a genuine positive surprise, not the plan.
- **Payback-time estimate:** Build cost is owner TIME + agent tokens, not cash (no
  upfront spend; storefronts are free to open). "Payback" therefore = the first ~3–10
  sales that clear the owner's shooting/editing/keywording time. At $3–10/pack and
  cold demand, that is plausibly never within 90 days — treat time as sunk, not repaid.
- **Compliance / licensing gate (owner homework, not agent-verifiable):** every
  committed sample and every sold file must be licensing-safe — no recognizable
  people (model-release issues), no trademarked logos, no private-property /
  protected-location issues. Macro bug shots are low-risk here; sunsets/landscapes
  need a property-and-people check. See PACK-SPEC → Curation criteria.

## Why this might fail (blunt)
Wallpapers compete with **FREE**. Unsplash, Pexels, and the wallpaper art already
built into every OS give users beautiful, zero-cost images with one tap — a $3–10
pack has to clear that bar every single sale. Generic sunsets and landscapes are the
most-saturated, least-differentiated corner of that free supply; a "Golden Hours"
sunset pack is a weak wedge. The differentiation that could actually work is
**subject specificity**: macro insect/bug photography is far more differentiated than
sunsets (fewer good free sources, an audience that specifically wants it —
entomology educators, nature blogs, science communicators), and "**shot on a real
camera by a human**" is a growing angle as AI-generated stock floods the market and
buyers/platforms react against it (Getty and Shutterstock banned AI submissions;
demand for authentic human imagery is cited as rising — see MARKET-PLAN). If this
candidate survives, it survives on the macro-bug niche and the human-authenticity
angle, NOT on being another 4K sunset bundle. Without an audience, even the good
niche starts cold and the conservative expectation ($0–30/90d) stands.

## Owner actions — see MARKET-PLAN.md
No revenue owner-action is queued from intake. Every channel in MARKET-PLAN.md ends
in a six-field OWNER-ACTION (all need an owner account and owner-supplied full-res
files uploaded OFF this public repo). The only zero-cost ready step is the owner
opening a free Gumroad or Ko-fi storefront and uploading a first curated pack; all
scaling steps are gated behind a paid validation signal.

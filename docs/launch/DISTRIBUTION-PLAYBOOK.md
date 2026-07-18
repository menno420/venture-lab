# Cluster lead-magnet distribution playbook

> **Status:** `reference`
>
> The single reusable recipe for giving a SKU cluster its free top-of-funnel
> discovery asset. It names the pattern that PRs **#243** (dev/webhook +
> API-robustness cluster) and **#246** (agent-ops / fleet cluster) each derived
> by hand, so the next cluster magnet is fill-in-the-blank instead of
> re-derived. Nothing here is published or spent by the seat — the recipe stops
> at **paste-ready**; the actual posting is an owner paste-and-post
> (**OWNER-ACTION**), same as every launch asset. Honest, low-hype: no fabricated
> metrics, no invented testimonials, no "used by N teams."

---

## Why this exists

The binding constraint in this lab is **distribution, not inventory**: there are
many publish-READY SKUs and few discovery paths to them (see
[`CATALOG.md`](CATALOG.md)). The highest-leverage move for a cluster that has no
free discovery asset is to write one honest teaching article that stands on its
own and carries a soft product footer — then wire it into the channels and the
storefront so it actually reaches people.

That recipe has now been run twice, identically, from scratch:

- **[`api-robustness-lead-magnet.md`](api-robustness-lead-magnet.md)** (PR #243) —
  the free article for the dev/webhook + API-robustness test-kit cluster.
- **[`agent-ops-lead-magnet.md`](agent-ops-lead-magnet.md)** (PR #246) — the free
  article for the agent-ops / fleet cluster.

Both are proof the shape works; neither *is* the shape. This playbook lifts the
shape out of the two examples so the third cluster (membership/starter, or the
AI-novella writing cluster, or whatever comes next) is fill-in-the-blank.

**This is a template, not an authorization.** Following it produces a
committed, paste-ready article and its channel drafts. It does **not** post
anything. Publishing is always the owner's click — see
[§4, the OWNER-ACTION handoff](#4-owner-action-handoff-paste-ready-never-auto-published).

---

## The recipe in one line

> **teaching article → channel drafts → CATALOG funnel-top registration → owner paste-and-post**

Four moving parts, in order. The first three are the seat's work (docs, in-repo,
reversible). The fourth is the owner's, and only the owner's.

---

## 1. Step-by-step template

Work these in order. Each step names the file it touches and the honest-voice
constraint it must satisfy.

### Step 0 — Pick the cluster (and confirm it's uncovered)

- Read [`CATALOG.md`](CATALOG.md) → **§ Cross-sell clusters**. Each cluster
  bullet either names a funnel-top `*-lead-magnet.md` link or it doesn't. Pick a
  cluster with **no** funnel-top link — that's an uncovered cluster, and the
  highest-leverage target.
- Sanity-check it's worth a magnet: the cluster should have more than one SKU (or
  one anchor SKU plus supporting ones), so a single article can funnel to a
  bundle-first list. A one-SKU cluster rarely earns its own article.
- Confirm nobody else is mid-flight on it: no open PR and no `control/claims/`
  entry naming the same cluster magnet.

### Step 1 — Write the free teaching article

Create `docs/launch/<cluster>-lead-magnet.md` from the skeleton in
[§2](#2-copy-paste-skeleton-for-a-new-cluster-lead-magnetmd). The article is the
product. Rules that make it convert *and* stay honest:

- **It teaches, it doesn't sell.** Six real failure modes (both existing magnets
  use six; five to seven is fine), each as **The failure / Why the [test|check]
  misses it / The fix**. A reader who never buys anything should still leave with
  something they can apply today.
- **Every claim is checkable.** Cite real specs, real commits, real files. No
  invented numbers, no "teams report," no benchmark you didn't run.
- **The footer is soft and last.** The product mention is one section at the
  bottom, framed as *optional*, funnelling **bundles/umbrella first** (higher
  AOV) → **singles** → the one discipline guide underneath. State plainly that
  the article stands on its own.
- **Status badge `reference`** in the first 12 lines (docs-gate requirement), and
  a header note saying it's a free, standalone, post-as-is article whose posting
  is an OWNER-ACTION. Leave `<ARTICLE_TITLE>` / `<PRODUCT_URL>` as fill tokens —
  those resolve at owner-post time, not now.

### Step 2 — Write the channel drafts

Append a new cluster section to
[`distribution-drafts.md`](distribution-drafts.md) — **do not disturb the
existing sections** (one-writer discipline: add, don't rewrite). Mirror the two
existing lead-magnet sections there:

- A short intro paragraph: this cluster's drafts lead with the **free article**
  (link it), which carries its own soft footer; the blurbs point at the *article*
  first, bundles before singles. State that every post is an OWNER-ACTION.
- Three platform-shaped drafts, each in a fenced block: a **Show HN**-style, a
  **subreddit teaser** (pick the two subreddits that fit the cluster's audience),
  and a **dev.to / Hashnode intro**. Each leads with the teaching, mentions the
  footer product only as a parenthetical, and ends with `<ARTICLE_URL>` (and
  `<PRODUCT_URL>` where a draft names the kits).

### Step 3 — Register the funnel-top in the CATALOG

Edit [`CATALOG.md`](CATALOG.md) → **§ Cross-sell clusters**, adding a
`<cluster>-cluster funnel-top (free discovery asset)` bullet that matches the
format of the two existing funnel-top bullets: link the article, say what shared
pain it teaches, name the funnel order (bundle/umbrella → singles → the
discipline guide), point at the channel drafts, and note it is **free, not a
priced SKU — no OWNER-QUEUE row; posting is an owner paste-and-post
(OWNER-ACTION)**.

### Step 4 — Make it reachable, then hand off

- Add one link to the new article from a reachable index (this repo:
  [`README.md`](README.md) → **Cross-product**) so the docs-gate's reachability
  check passes.
- Run `python3 bootstrap.py check --strict` → must exit 0.
- Stop here. The article is now **paste-ready**. Everything past this line is the
  owner's — see [§4](#4-owner-action-handoff-paste-ready-never-auto-published).

---

## 2. Copy-paste skeleton for a new `docs/launch/<cluster>-lead-magnet.md`

Replace every `<…>` placeholder. Keep the Status badge in the first 12 lines.

```markdown
# <A concrete, teaching-first title — the pain, not the product>

> **Status:** `reference`
>
> A free, standalone article — written to be posted as-is to dev.to / Hashnode
> or as a Show HN / <r/subreddit-a> / <r/subreddit-b> submission. It teaches real
> <cluster> failure modes; the product mention at the end is a soft, honest
> footer, not the point. Nothing here is published or spent by the seat — posting
> is an **owner** paste-and-post (OWNER-ACTION), same as every launch asset. Draft
> copy; fill `<ARTICLE_TITLE>` / `<PRODUCT_URL>` before posting.

---

<Opening: name the systematic gap this cluster lives in — one tight paragraph
that frames why the happy path hides these failures. No product yet.>

Below are <six> failure modes that <pass every test / look fine> and still
<drop real traffic / cost you>. For each: why it's invisible, and the actual
fix. If you've <shipped X> and haven't deliberately handled these, at least one
is probably live in your <code / repo> right now.

---

## 1. <Failure mode, stated as a symptom the reader recognizes>

**The failure.** <What actually goes wrong, concretely.>

**Why the <test / check> misses it.** <The specific reason the happy-path
signal stays green.>

**The fix.** <The real, mechanical fix — specific enough to act on today.>

---

## 2. … (repeat for each failure mode; five to seven total)

---

## The pattern under all <six>

<One paragraph naming the single shape all the failures share — the thesis the
reader takes away even if they buy nothing. Then: the cheapest next step they
can take today (name one concrete ten-minute action).>

---

### If you'd rather not <do the hard version> yourself

<One honest paragraph: what you sell, framed as entirely optional, the article
stands on its own. No metrics, no testimonials.>

If more than one of these hit home, start with the <umbrella / bundle>:

- **<Anchor SKU>** — <one honest line mapping it to the failures above>. ▸ `<PRODUCT_URL>`

Or pick the piece that matches the failure you recognized:

- **<Supporting SKU>** — <the failure it fixes> (§<n>).
- **<Supporting SKU>** — <the failure it fixes> (§<n>).

And the discipline underneath, if you want the *why* rather than the tools:
**<discipline guide>**. Links: `<PRODUCT_URL>`.

No hype, no invented metrics, no "used by N teams" — just the failure modes, and
some optional guides/tools for the operator who'd rather build the gates than
learn each one by getting burned.
```

---

## 3. Pre-publish checklist

Before you call the article paste-ready and hand off, confirm every line:

- [ ] **Uncovered cluster.** The cluster had no funnel-top link in `CATALOG.md`
      before this slice (you're covering a gap, not duplicating one).
- [ ] **Teaches first.** A non-buyer leaves with something usable; the failures
      are real and specific, not product ad-copy in disguise.
- [ ] **Every claim checkable.** Specs/commits/files cited; **zero** fabricated
      metrics, testimonials, or "used by N" claims.
- [ ] **Soft footer, last, bundle/umbrella-first.** Product mention is one
      closing section, framed optional, funnelling high-AOV → singles → the
      discipline guide.
- [ ] **Fill tokens left unresolved on purpose.** `<ARTICLE_TITLE>` /
      `<ARTICLE_URL>` / `<PRODUCT_URL>` remain — they're owner-post-time values,
      not seat values.
- [ ] **Status badge `reference`** in the first 12 lines of the article.
- [ ] **Channel drafts added, existing sections untouched** in
      `distribution-drafts.md` (one-writer: append, don't rewrite).
- [ ] **CATALOG funnel-top bullet added** in the Cross-sell clusters section,
      matching the existing two, with the "free, no OWNER-QUEUE row" note.
- [ ] **Reachable.** The article is linked from a read-path index (`README.md`
      → Cross-product) so the docs-gate reachability check passes.
- [ ] **`python3 bootstrap.py check --strict` exits 0.**
- [ ] **No publish surface touched.** No OWNER-QUEUE row added, no owner-action
      click-script run, no external post — a free article is not a priced SKU.
- [ ] **Diff is the intended files only** — the article, the drafts edit, the
      CATALOG edit, the README link, plus the slice's own session card / heartbeat.

---

## 4. OWNER-ACTION handoff (paste-ready, never auto-published)

**This is owner-gated publishing. The seat's work ends at paste-ready. The
following are the owner's actions, and only the owner's — the doc never
auto-publishes, the same rule every launch asset in this repo follows.**

What the owner does to actually post it:

1. **Post the article as content**, from the owner's own account, to one or more
   of the channels the article header and the channel-draft section name (dev.to
   / Hashnode as the canonical home; a Show HN and/or the two subreddit teasers as
   discovery). Post it as an *article*, not a sales post — let its soft footer do
   the funnel.
2. **Capture the canonical URL** of the posted article and fill `<ARTICLE_URL>`
   in the channel drafts (and `<ARTICLE_TITLE>` in the article header) so the
   remaining channel posts point at the live piece.
3. **Fill `<PRODUCT_URL>`** with the storefront/product link once the funnel
   targets are live (after the relevant ⚑B/⚑D owner publish clicks in
   [`../publishing/OWNER-QUEUE.md`](../publishing/OWNER-QUEUE.md)).
4. **Post the remaining channel drafts** from
   [`distribution-drafts.md`](distribution-drafts.md), spaced sanely across
   channels, each from the owner's own account.

The seat performs **none** of the above. It writes the article, the drafts, the
CATALOG registration, and this handoff — all reversible, in-repo — and stops.
Posting, account use, and any spend are owner clicks.

---

## Worked examples

Two full, shipped instances of this recipe to read alongside the skeleton:

- **PR #243** — [`api-robustness-lead-magnet.md`](api-robustness-lead-magnet.md):
  the dev/webhook + API-robustness cluster. Six failure modes (replay-unsafe
  webhook handlers, forged events, retry storms, offset-pagination drift, a 429
  with no Retry-After, the CORS/Authorization footgun), funnelling Webhook
  Verifier + API Robustness bundles → singles → The False-Green Test Trap.
- **PR #246** — [`agent-ops-lead-magnet.md`](agent-ops-lead-magnet.md): the
  agent-ops / fleet cluster. Six fleet-operating failures (self-certified "tests
  pass," self-certified "done," parallel-session collisions, the green PR that
  can't self-merge, the ungated spend/publish, the undiscoverable artifact),
  funnelling the Agent Fleet Field Manual umbrella → the supporting SKUs mapped
  to each failure → The False-Green Test Trap.

Both are cited in [`CATALOG.md`](CATALOG.md)'s Cross-sell clusters section as
their clusters' funnel-top assets — the exact registration Step 3 above
reproduces for the next cluster.

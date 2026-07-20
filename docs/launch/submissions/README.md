# Distribution submission pack — paste-and-post the free lead magnets

> **Status:** `reference`

This directory turns the four free lead-magnet articles into **paste-and-post-ready
submissions** — one file per channel where the article honestly fits — so each
external post is ONE owner paste + click with **zero reformatting**. Every file
carries the platform structure (front-matter / tags / title / canonical rule /
subreddit + submit URL) and the exact URL to open.

**Nothing here is published or spent by the seat.** Posting is an owner
paste-and-post (OWNER-ACTION), same as every launch asset. Each file names where to
click; the owner posts from their own account.

**Honesty rules baked into every file (do not undo them):**

- **No fabricated stats, metrics, testimonials, or "used by N" claims.** The bodies
  reproduce the source articles' honest voice; reformatting = platform structure,
  never new claims.
- **Every owner-fill link is marked `⟨owner: …⟩`** (e.g. `⟨owner: your Gumroad link⟩`).
  No URL is invented. Replace each marker with your real link *before* publishing.
  (The double-square-bracket `fill` marker is reserved for session cards and must never appear here.)
- **The product footer is soft and last** — bundles/umbrella first, then singles.
  The article is content, not a sales post; its footer does the funnel.

---

## The canonical-URL rule (this lab has no live blog and ~0 traffic)

There is no pre-existing canonical home, so **you** choose one per article. Concrete
rule — follow it exactly, it is stated once here and echoed in each dev.to/Hashnode file:

1. **Pick ONE platform to publish each article on first.** That post becomes the
   article's canonical home.
2. **On that first platform, leave `canonical_url` BLANK.** A blank canonical means
   "this platform is the original."
3. **When you cross-post the SAME article to the OTHER platform(s), set that
   platform's canonical URL to the URL of the first post.** (dev.to: the
   `canonical_url:` front-matter field. Hashnode: post settings → "Canonical URL".)
   This tells search engines the first post is the original and avoids a
   duplicate-content penalty.
4. **Exception:** if you instead publish the article on your own website/blog first,
   set `canonical_url` to that site URL on **both** dev.to and Hashnode.
5. **Never leave `canonical_url` blank on more than one platform for the same
   article** — that is the one mistake this rule exists to prevent.

Reddit self-posts have no canonical field; the teaching text *is* the post, so there
is nothing to point back at.

---

## Index — article × channel → paste-ready file

| Article (cluster) | Channel | Paste-ready file | Where to click | CTA reminder |
| --- | --- | --- | --- | --- |
| Agent-ops / fleet discipline | dev.to | [agent-ops--devto.md](agent-ops--devto.md) | https://dev.to/new | Soft footer; Agent Fleet Field Manual (umbrella) first |
| Agent-ops / fleet discipline | Hashnode | [agent-ops--hashnode.md](agent-ops--hashnode.md) | https://hashnode.com/create/story | Soft footer; Field Manual first, then mapped SKUs |
| Agent-ops / fleet discipline | Reddit · r/LLMDevs | [agent-ops--reddit.md](agent-ops--reddit.md) | https://www.reddit.com/r/LLMDevs/submit | Value-first; one soft product line at the very end |
| API robustness / webhooks | dev.to | [api-robustness--devto.md](api-robustness--devto.md) | https://dev.to/new | Soft footer; Webhook Verifier + API Robustness bundles first |
| API robustness / webhooks | Hashnode | [api-robustness--hashnode.md](api-robustness--hashnode.md) | https://hashnode.com/create/story | Soft footer; bundles before singles |
| API robustness / webhooks | Reddit · r/webdev | [api-robustness--reddit.md](api-robustness--reddit.md) | https://www.reddit.com/r/webdev/submit | Value-first; one soft product line at the very end |
| Membership / Stripe | dev.to | [membership--devto.md](membership--devto.md) | https://dev.to/new | Soft footer; Ship-It Bundle first, then single kits |
| Membership / Stripe | Hashnode | [membership--hashnode.md](membership--hashnode.md) | https://hashnode.com/create/story | Soft footer; bundle before singles |
| Membership / Stripe | Reddit · r/SaaS | [membership--reddit.md](membership--reddit.md) | https://www.reddit.com/r/SaaS/submit | Value-first; one soft product line at the very end |
| AI-novella production line | Reddit · r/selfpublishing | [ai-novella--reddit-selfpublishing.md](ai-novella--reddit-selfpublishing.md) | https://www.reddit.com/r/selfpublishing/submit | Value-first; one soft product line at the very end |
| AI-novella production line | Reddit · r/writing | [ai-novella--reddit-writing.md](ai-novella--reddit-writing.md) | https://www.reddit.com/r/writing/submit | **No CTA / no link** — strict self-promo sub; pure discussion post |

### Channels skipped on purpose (honest fit)

- **AI-novella → dev.to and Hashnode: skipped.** Both are developer platforms; a
  fiction-production piece is off-audience there, and the thin "writing-as-a-system"
  angle doesn't justify posting it over the two on-topic writing subreddits above.
  Post it where the readers are (r/selfpublishing, r/writing), not where the article
  merely *could* technically go.
- **All four articles → r/programming: not used.** r/programming removes self-posts
  and self-promotion; it is not a self-promo-tolerant home for these. The dev-tooling
  clusters use r/LLMDevs / r/webdev / r/SaaS instead — genuinely on-topic and
  tolerant of substantive, teach-first write-ups.

---

## How to use a file

1. Open the file for the article + channel you want to post.
2. Read the short header (where to click, CTA reminder, canonical rule).
3. Copy the fenced paste block (for Reddit, the Title + Body blocks) exactly.
4. Open the "where to click" URL, paste, replace every `⟨owner: …⟩` marker with your
   real link, set the canonical field per the rule above (dev.to/Hashnode only), and
   post — as an *article*, not a sales post.

Source articles these are built from:
[`agent-ops-lead-magnet.md`](../agent-ops-lead-magnet.md) ·
[`ai-novella-lead-magnet.md`](../ai-novella-lead-magnet.md) ·
[`api-robustness-lead-magnet.md`](../api-robustness-lead-magnet.md) ·
[`membership-lead-magnet.md`](../membership-lead-magnet.md).
The channel doctrine and OWNER-ACTION handoff live in
[`../DISTRIBUTION-PLAYBOOK.md`](../DISTRIBUTION-PLAYBOOK.md) and
[`../distribution-drafts.md`](../distribution-drafts.md).

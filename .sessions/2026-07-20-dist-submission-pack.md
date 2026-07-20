# Session — Distribution submission pack (paste-and-post the 4 lead magnets)

> **Status:** `complete`

- **📊 Model:** opus-4.8 · high · distribution submission pack

- **started (date -u):** Mon Jul 20 04:13 UTC 2026
- **branch:** `claude/dist-submission-pack`
- **base:** `main@1fdbc4f`
- **purpose:** attack the venture's binding constraint (1 live SKU, ~0 traffic) by
  turning the four existing **free lead-magnet articles** into **paste-and-post-ready
  submissions** — one file per channel where the article honestly fits — so each
  external post becomes ONE owner paste+click with zero reformatting. The four
  magnets already exist as raw markdown
  ([`agent-ops-lead-magnet.md`](../docs/launch/agent-ops-lead-magnet.md),
  [`ai-novella-lead-magnet.md`](../docs/launch/ai-novella-lead-magnet.md),
  [`api-robustness-lead-magnet.md`](../docs/launch/api-robustness-lead-magnet.md),
  [`membership-lead-magnet.md`](../docs/launch/membership-lead-magnet.md)); this
  slice does NOT rewrite their claims — it reformats them for each platform
  (front-matter, tags, canonical rule, subreddit + submit URL) and states the
  canonical-honesty rule for a lab with no live blog. Reversible docs only;
  **posting stays owner-gated** (each file names the exact URL to open, but the
  seat posts nothing).
- **scope (files):** NEW `docs/launch/submissions/` — a per-article × per-channel
  paste-ready file set (dev.to / Hashnode / a fitting subreddit for the three
  dev-tooling clusters; two writing subreddits for the AI-novella cluster, with
  dev.to/Hashnode skipped and the reason noted) plus `submissions/README.md`
  (index table + canonical-url doctrine); NEW
  `control/claims/dist-submission-pack.md`; this card. No SKU, no OWNER-QUEUE row,
  no publish surface, no generated file, and none of the reserved lanes
  (OWNER-START-HERE, control/status.md, docs/current-state.md, CATALOG.md, the SKU
  registry, candidates/**) touched.

## Work log

- 2026-07-20 — Isolated worktree on `claude/dist-submission-pack` from
  `origin/main` (`1fdbc4f`). Read the four lead magnets in full and skimmed the
  channel doctrine (`DISTRIBUTION-PLAYBOOK.md`, `distribution-channels.md`,
  `distribution-drafts.md`) to reuse the existing honest-voice framing and the
  OWNER-ACTION handoff. Confirmed the docs-gate mechanics: every new `docs/` doc
  needs a `> **Status:**` badge in its first 12 lines, all relative links must
  resolve, and every doc must be reachable — and `check_reachable` seeds a root
  from every `README.md` under `docs/`, so `submissions/README.md` makes the whole
  subtree reachable without touching CATALOG or the launch README. Born-red card +
  claim committed FIRST; the `in-progress` Status holds the merge-on-green gate red
  by design.
- 2026-07-20 — Built the submission pack: **11** channel files across the four
  clusters + the index README (12 files total under `docs/launch/submissions/`).
  Channels placed by honest fit — the three dev-tooling clusters (agent-ops,
  api-robustness, membership) each got dev.to + Hashnode + one on-topic subreddit
  (r/LLMDevs / r/webdev / r/SaaS); the AI-novella cluster got r/selfpublishing +
  r/writing and **skipped** dev.to/Hashnode (developer platforms, off-audience for
  a fiction-production piece). r/programming deliberately avoided (self-post +
  self-promo removals). No fabricated stats/metrics/testimonials; every owner-fill
  link marked `⟨owner: …⟩`, never an invented URL. Content committed (`9976995`).
- 2026-07-20 — Pre-flip `python3 bootstrap.py check --strict`: red on the born-red
  HOLD only — the docs-gate (badge/link/reachable), `check_docs_links`,
  `check_funnel_assets`, and `check_catalog_drefs` all green; the only remaining
  advisories (seat-digest, model-line) are pre-existing and non-gating. Every new
  `docs/launch/submissions/*.md` carries a `reference` badge and is reachable — the
  `README.md` seeds a reachability root and links every file. Flip to `complete`
  (this commit): Status badge flipped, all five auto-draft `[[fill:]]` slots
  resolved, the four byte-markers present (`**Status:**`, `💡`,
  `previous-session review`, `📊 Model:`). Re-ran `check --strict` → **exit 0**
  (born-red HOLD cleared). PR opened READY immediately after this flip, base `main`.

## 💡 Session idea

💡 **A `scripts/check_submission_pack.py` advisory that keeps each submission file
honest against its source magnet.** The pack I just built is a hand-maintained
projection of the four `*-lead-magnet.md` articles onto platforms: each dev.to /
Hashnode / Reddit file reproduces a magnet's body, and each carries owner-fill
`⟨owner: …⟩` markers plus a "where to click" URL. Two invariants silently rot the
moment a magnet is edited or a URL is fixed: (a) a submission file drifts from the
magnet it mirrors (a failure mode added to the article never reaches the posted
copy), and (b) a real URL leaks in where an `⟨owner: …⟩` placeholder belongs, or a
stray `<PRODUCT_URL>`/`[[fill:]]` token (reserved for cards, not submissions)
survives into a paste-ready file. A tiny advisory — same non-gating class as the
seat-digest / model-line warnings — could parse `docs/launch/submissions/*.md`,
assert every file names a source magnet that still exists, warn when a submission's
failure-mode headings diverge from its source's, and flag any `http(s)://` literal
in a CTA slot or any surviving `<…>`/`[[fill:]]` token. It is the natural sibling
of the proposed `series-hook-chain` and `check_planning_conveyor` advisories — the
same "a hand-maintained artifact drifts from its source" shape, applied to the
distribution projection.

## previous-session review

previous-session review: the newest prior card
(`.sessions/2026-07-19-veto-menu-roadmap.md`, PR #259) groomed the 64-item veto
menu into a prioritized execution roadmap and named **distribution** as standing
constraint #1 — new SKUs/books don't move revenue without an owner-gated
publish+distribution path. This slice acts on exactly that constraint: it does not
add inventory, it lowers the friction on the *distribution* half by making the four
existing free magnets one-paste-per-channel. I carried three disciplines forward
from that card: (1) the one-writer diff — this pack *reproduces* the magnets and
*references* the channel doctrine rather than rewriting CATALOG or the drafts doc;
(2) the honesty bar held hard — no invented metrics, owner-fill links left as
`⟨owner: …⟩` rather than guessed; (3) the born-red landing recipe reused verbatim
(card + claim first, flip last on green). Its 💡 proposed a `check_planning_conveyor`
advisory that keeps the planning chain self-reconciling; my 💡 above proposes the
sibling that keeps the *distribution* projection self-reconciling — same drift
shape, different artifact.

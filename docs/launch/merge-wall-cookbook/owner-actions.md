# The Agent Merge-Wall Cookbook — owner publish click-script

> **Status:** `reference`

QUEUED (2026-07-13, ORDER 008 night run, PRODUCT #9). No freeze applies:
this is a guide + workflow-YAML cookbook with no Stripe/payment-path
dependency of its own, so the ORDER 003 gate (lifted 2026-07-11 by PR #22)
never attached to it. Honest caveat: a live purchase of ANY catalog
product besides SWTK remains unverified — QUEUED means the owner may
click, not that this product's delivery is live-proven. This is a
click-script for the owner, not a request to any agent; no agent performs
publish/spend/account actions.

### ⚑ — Publish "The Agent Merge-Wall Cookbook" at $19 (one-time)
- **WHAT:** Create a $19 one-time digital product on your own no-code
  storefront, selling
  `candidates/merge-wall-cookbook/dist/merge-wall-cookbook-v0.1.zip`,
  using `docs/launch/merge-wall-cookbook/listing-copy.md`.
- **WHERE:** gumroad.com → *New product* → *Digital product* (price $19),
  or lemonsqueezy.com equivalent, in your own account.
- **HOW:** 1) Sign in. 2) New product → Digital product. 3) Name = "The
  Agent Merge-Wall Cookbook". 4) Price = $19 one-time. 5) Upload the dist
  zip. 6) Paste the listing copy (Title / Short / Long / Bullets / FAQ).
  7) Publish. 8) Copy the public product URL.
- **WHY:** Narrow but real, high-intent pain (agent-fleet builders whose
  green PRs cannot land) with few alternatives; the catalog's strongest
  production-evidence mechanic — the primary recipe is adapted from this
  repo's own live enabler workflow, and the guide cites verifiable
  merged_by github-actions[bot] events (PR #104, PR #128, 2026-07-13).
  Intake scored 3.55 weighted; distribution axis capped by a small TAM on
  the same saturated community funnel as the rest of the catalog.
  Conservative expectation: 0–3 sales in 90 days, $0–$57; zero
  distribution = $0 (the intake's own line).
- **UNBLOCKS:** First infrastructure-recipe sale; the agent-builder
  audience surface shared with the Field Manual ($39) and the False-Green
  Test Trap ($15) — natural cross-sell copy already exists in the guide's
  citations.
- **VERIFIED-WHEN:** The public URL loads a purchasable $19 page and a
  preview/test purchase delivers the zip whose sha256 matches the
  ARTIFACT line below. (The intake's original CI-lint clause is superseded
  honestly: recipes are parse-verified from the packaged bundle + the
  enabler pattern is production-evidenced by real merge events; the
  never-run status of Recipe 2 is disclosed in the listing FAQ, the
  recipe header, and guide ch. 7 — not asserted as CI-verified.)
- **ARTIFACT (verified 2026-07-13):** upload exactly
  `candidates/merge-wall-cookbook/dist/merge-wall-cookbook-v0.1.zip` @
  sha256 `8d12a4371850689ed7f1be5b7f13fa0017db98bfa163bc6570edca1306a3c2b0`
  (25,629 bytes; byte-reproducible via `package.sh` — double rebuild
  produced the identical sha; the committed dist IS that build). Executed
  verification from the extracted bundle in a clean dir: all 4 recipe
  YAMLs parse via `yaml.safe_load` (and pass the shipped stdlib
  structural check); inventory 14/14 vs INCLUDED.md; all files valid
  UTF-8 non-empty, all 10 markdown files H1-headed with balanced fences;
  real-secret-shape scan **0 hits** — the recipes' 9 `${{ secrets.* }}`
  occurrences are GitHub Actions template-variable REFERENCES (variable
  names, no values), documented here as the allowlisted remainder; no
  `.DS_Store`, no `__pycache__`, no junk entries in the archive listing.

## Price precedent chain

$19 one-time — set at intake
(`candidates/merge-wall-cookbook/INTAKE.md`: "Conservative revenue
estimate: $19 one-time") and recorded identically in the listing copy,
the §7 packet, and this script. Precedent rung: the Agent-Workflow
Template Pack sells at the same $19 price point (PWYW floor, PR #108) —
runnable-artifact packs for the same builder audience. Chain: Kill-Rule
Intake Kit $15 = False-Green Test Trap $15 < **$19 this cookbook** =
template-packs $19 PWYW < SWTK $29 (live, PR #86) < Field Manual $39
(PR #110) < Membership Kit $49 (PR #106). A recipe cookbook that ships
runnable, production-cited YAML prices above the bottom guide rung and at
parity with the template pack, honestly below the tool-kit rungs.

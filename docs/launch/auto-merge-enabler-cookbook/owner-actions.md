# The Auto-Merge Enabler Cookbook — owner publish click-script

> **Status:** `reference`

QUEUED (2026-07-17, ORDER 016 overnight run). No freeze applies: this is a
guide + workflow-YAML cookbook with no Stripe/payment-path dependency of
its own, so the ORDER 003 gate (lifted 2026-07-11 by PR #22) never attached
to it. Honest caveat: a live purchase of ANY catalog product besides the
live Stripe Webhook Test Kit remains unverified — QUEUED means the owner
may click, not that this product's delivery is live-proven. This is a
click-script for the owner, not a request to any agent; no agent performs
publish/spend/account actions.

### ⚑ — Publish "The Auto-Merge Enabler Cookbook" at $19 (one-time)
- **WHAT:** Create a $19 one-time digital product on your own no-code
  storefront, selling
  `candidates/auto-merge-enabler-cookbook/dist/auto-merge-enabler-cookbook-v0.1.zip`,
  using `docs/launch/auto-merge-enabler-cookbook/listing-copy.md`.
- **WHERE:** gumroad.com → *New product* → *Digital product* (price $19),
  or lemonsqueezy.com equivalent, in your own account.
- **HOW:** 1) Sign in. 2) New product → Digital product. 3) Name = "The
  Auto-Merge Enabler Cookbook". 4) Price = $19 one-time. 5) Upload the dist
  zip. 6) Paste the listing copy (Title / Short / Long / Bullets / FAQ /
  the "what it does NOT do" honesty section). 7) Publish. 8) Copy the public
  product URL.
- **WHY:** The catalog's strongest production-evidence mechanic — the two
  primary recipes are the EXACT live workflows this repo runs, and the guide
  cites five verifiable `github-actions[bot]` merge events (PRs #219–#223,
  2026-07-17) plus the `do-not-automerge` counter-example (#218). Narrow but
  real, high-intent pain (agent-fleet builders who want PRs to land on green
  without a human) with few alternatives. Natural cross-sell with the Agent
  Merge-Wall Cookbook ($19, conflict-avoidance sibling) and the Field Manual
  ($39). Conservative expectation: 0–3 sales in 90 days, $0–$57; zero
  distribution = $0 (the intake's own line).
- **UNBLOCKS:** A second infrastructure-recipe sale on the agent-builder
  surface; the "CI/CD for agent fleets" bundle idea pairing this + the
  Merge-Wall Cookbook + Field Manual.
- **VERIFIED-WHEN:** The public URL loads a purchasable $19 page and a
  preview/test purchase delivers the zip whose sha256 matches the ARTIFACT
  line below. The recipes are parse-verified from the packaged bundle AND
  the two production recipes are byte-identical to this repo's live
  workflows (cmp-verifiable); the minimal variant's parse-verified-only
  status is disclosed in the listing FAQ, the recipe header, and guide ch. 8
  — not asserted as production-run.
- **ARTIFACT (verified 2026-07-17):** upload exactly
  `candidates/auto-merge-enabler-cookbook/dist/auto-merge-enabler-cookbook-v0.1.zip`
  @ sha256 `3deceb46b587f8d24899c63cba7ce58d0a41aae564b2dfeabe5b80135bfdd703`
  (36,456 bytes; byte-reproducible via `package.sh` — double rebuild
  produced the identical sha; the committed dist IS that build). Executed
  verification from the extracted bundle in a clean dir: all 3 recipe YAMLs
  parse via `yaml.safe_load` (and pass the shipped stdlib structural check);
  inventory 15/15 vs INCLUDED.md; all 12 markdown files valid UTF-8
  non-empty, H1-headed with balanced fences; real-secret-shape scan
  **0 hits** — the 12 `${{ secrets.* }}` occurrences (6 `GITHUB_TOKEN` +
  6 `ROUTINE_PAT`) are GitHub Actions template-variable REFERENCES (variable
  names, no values), documented here as the allowlisted remainder; the two
  production recipes are byte-identical (`cmp`) to
  `.github/workflows/auto-merge-enabler.yml` and `substrate-gate.yml`; no
  `.DS_Store`, no `__pycache__`, no junk entries in the archive listing.

## Price precedent chain

$19 one-time — set at intake
(`candidates/auto-merge-enabler-cookbook/INTAKE.md`: "Conservative revenue
estimate: $19 one-time") and recorded identically in the listing copy, the
§7 packet, and this script. Precedent rung: the **Agent Merge-Wall
Cookbook** sells at the same $19 price point (PR-landed, `docs/publishing/
vetting/merge-wall-cookbook.md`) — a runnable, production-cited GitHub
Actions cookbook for the same agent-builder audience, and this product's
nearest sibling (enable mechanism vs. its conflict-avoidance scope). Chain:
Kill-Rule Intake Kit $15 = False-Green Test Trap $15 < **$19 this cookbook**
= merge-wall-cookbook $19 = template-packs $19 PWYW < SWTK $29 (live) <
Field Manual $39 < Membership Kit $49. A recipe cookbook that ships
runnable, production-cited YAML prices at parity with its Merge-Wall sibling
and above the bottom guide rung, honestly below the tool-kit rungs.

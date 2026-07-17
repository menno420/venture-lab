# The Auto-Merge Enabler Cookbook — listing copy

> **Status:** `reference`

Ready-to-paste copy for a Gumroad / Lemon Squeezy digital-product page.

## Title
```
The Auto-Merge Enabler Cookbook — land your AI agents' pull requests on green with no human clicking merge
```

## Short description (≤ 200 chars)
```
The exact merge-on-green enabler workflow this repo runs in production — annotated line by line, plus the required-check gate and born-red HOLD that make it safe. Five citable github-actions[bot] merges.
```

## Long description
```
An agent fleet that opens its own pull requests wants them to land the moment they go green — no human clicking merge at 3am, no queue of finished-but-unlanded work. But the obvious approach is a trap: have the agent merge its own PR and a policy layer denies it (self-approval defeats two-party review), retrying through a different API path is denied again, and even arming GitHub-native auto-merge from the agent's own seat is recognized as the same act and denied.

This cookbook is the landing path that works, taken from a public repository whose agent fleet runs it in production. The trust move is one sentence: the agent never merges and never even arms auto-merge — a repo-owned workflow arms GitHub-native auto-merge at PR open, and GitHub itself squash-merges the moment your required check goes green. Arming is not merging, so the server-side arm+merge under the workflow's own token sails past the policy layer that denies the agent. The merging identity is the workflow (github-actions[bot]), never the agent's seat.

Eight compact chapters (~10 pages): the merge-on-green model; the enabler workflow annotated guard by guard (the synchronize re-arm, the refuse-to-arm-on-zero-required-contexts guard, the stale-payload label re-read); required-checks gating and the zero-required-checks trap (count contexts, not rules); the born-red HOLD that makes "not finished yet" a red check so a pre-armed auto-merge can't land an unfinished session; the do-not-automerge opt-out and the two one-time repo settings; why the agent is classifier-barred from self-arming and why that's correct; a troubleshooting flow for why a green PR didn't land (the MCP-created-PR-fires-no-workflow gotcha, pending-forever required checks, GraphQL quota at fleet scale, and why github-actions[bot] squashes suppress on:push CI on main); and the copy-paste recipe set with a per-file honesty ledger.

Three GitHub Actions files, ready for .github/workflows/: the auto-merge enabler and the substrate-gate born-red HOLD are the EXACT production workflows this repo runs, copied byte-for-byte; a minimal enabler variant reduces it to the load-bearing skeleton for reading. Every recipe parses with a stock YAML loader and the QUICKSTART ships the verification commands.

Provenance is the product. The subject is this repo's own live infrastructure, so the evidence class is verified-by-production, not a synthetic test: every chapter ends with a Sources footer citing file @ commit in the public repo, and the guide cites five real merge events (PRs #219–#223, each merged_by github-actions[bot] on 2026-07-17) you can verify from the public GitHub API — including PR #223, opened READY and auto-merged 48 seconds later. The honesty ledger states exactly which files are production-proven verbatim and which one is a parse-verified distillation.
```

## Bullets
```
- The trust move, in one sentence: the agent never merges or arms — a repo-owned workflow arms native auto-merge at open; GitHub squash-merges on green (merged_by github-actions[bot], not the agent)
- The EXACT production enabler workflow this repo runs, copied verbatim and annotated guard by guard — synchronize re-arm, refuse-to-arm on zero required contexts, stale-payload label re-read
- The born-red HOLD gate (also verbatim): makes an unfinished session a RED check, so a pre-armed auto-merge can't land half-done work — with the documented 24-second false-green incident it prevents
- Required-checks gating done right: count contexts not rules, always report (never paths-ignore), verify from the API not the settings page
- The do-not-automerge opt-out — proven by PR #218, which carried the label and was merged_by the human owner while five sibling PRs auto-merged
- Troubleshooting: MCP-created PRs fire no workflow at open (push once to arm); pending-forever required checks; GraphQL quota at fleet scale; why github-actions[bot] squashes suppress on:push CI on main
- ~10 pages + ~450 lines of commented YAML; every chapter cites file @ commit in a public repo you can audit; five API-verifiable merge events
```

## FAQ
```
Q: Are the merges and incidents real?
A: Yes, and auditably so. The five auto-merges (PRs #219–#223, merged_by github-actions[bot], 2026-07-17) and the do-not-automerge counter-example (PR #218, merged_by the human owner) are verifiable from the public menno420/venture-lab GitHub API; every chapter ends with a Sources footer citing the exact file @ commit. This is verified-by-production evidence — the cookbook's subject is this repo's own live merge infrastructure.

Q: Are the recipes actually used in production?
A: Labeled per file, honestly. The auto-merge-enabler.yml and substrate-gate.yml recipes are copied BYTE-FOR-BYTE from the workflows this repo runs — the enabler squash-merged five agent PRs in a single night. The third file (auto-merge-enabler-minimal.yml) is a readability distillation of the enabler that drops the label-race re-read; it was parse-verified, not production-run, and its header says so.

Q: Will this bypass my code review or policy layer?
A: No, and it doesn't try. The whole design is the opposite: the agent never merges. Merging is done by GitHub's native auto-merge under a repo-owned token, gated by a required check you control. If your org requires human review, that requirement still holds — these recipes land PRs whose required checks pass, nothing else. The do-not-automerge label (and a branch-namespace filter) take any PR off the auto-merge path for a human to land.

Q: How is this different from the Agent Merge-Wall Cookbook?
A: Different scope, same audience. The Merge-Wall Cookbook is conflict AVOIDANCE — the walls a self-merging fleet hits and the fallbacks (including a REST merge-on-green recipe). THIS cookbook is the merge-on-green ENABLE mechanism — the enabler workflow itself, deep, annotated guard by guard, with the born-red HOLD that makes it safe. They cross-sell; they don't overlap. If you want the runnable REST fallback, that's the Merge-Wall Cookbook.

Q: Is this specific to Claude/one vendor's agents?
A: The branch-namespace filter in the recipes is claude/* because that's what this repo runs — it's one string to change. The mechanics (auto-merge arming, required-check behavior, the GITHUB_TOKEN recursion guard, the self-approval policy denial pattern) are GitHub platform behavior plus a policy-layer pattern any autonomous-agent stack reproduces.

Q: What was NOT machine-verified?
A: The prose chapters are verified by citation to committed material and by the real merge events, not by re-running the workflows on a fresh repo. The two production recipes are the exact bytes this repo runs (cmp-verifiable against a clone); the minimal variant is parse-verified only. A REST merge-on-green fallback is NOT shipped here as a production recipe — this repo lands via the native arm. Platform workarounds also rot; GitHub changes its API and UI — re-verify before betting a fleet.

Q: Who should NOT buy this?
A: If your agents' PRs are merged by humans and that's fine, you don't have this problem. If you already run a repo-owned enabler that arms native auto-merge, gated by a required check with a work-in-progress hold, you own this discipline — buy nothing.

Q: License?
A: Single-user license; use the recipes in as many of your own projects as you like. v0.1 — free updates to the v0.x line.

Q: Support?
A: Best-effort, community-level. It's a cookbook, not a managed service.
```

## What this does NOT do (honesty section — keep in the listing)

- It does **not** bypass code review or your policy layer. The agent never
  merges; GitHub's native auto-merge does, under a repo-owned token, gated
  by a required check you control.
- It does **not** ship a runnable REST merge-on-green fallback. This repo
  lands via the native arm; if the arm is structurally refused on your repo
  shape you need that fallback — it's in the companion Merge-Wall Cookbook.
- It is **not** the Agent Merge-Wall Cookbook. That's conflict avoidance +
  fallbacks; this is the enable mechanism itself. Sibling audience,
  non-overlapping scope.
- It cannot promise identical behavior on your repo shape, GitHub plan, or
  org policy — the recipes' guards exist because behavior varies.

---

**PROVENANCE-FOOTER** — every claim above traces to the buyer bundle and
committed repo material: `.github/workflows/auto-merge-enabler.yml` @
`aa04700` · `.github/workflows/substrate-gate.yml` @ `aa04700` ·
`.github/workflows/main-verify.yml` @ `f8ccc60` · `docs/current-state.md` @
`4e0a37c` · merge events #219 `389ab6e` / #220 `4e0a37c` / #221 `12498f4` /
#222 `37cf9fd` / #223 `f0511ae` (all `github-actions[bot]`, 2026-07-17) ·
opt-out #218 `do-not-automerge` → `merged_by menno420` · buyer bundle
`candidates/auto-merge-enabler-cookbook/dist/auto-merge-enabler-cookbook-v0.1.zip`
@ sha256 `3deceb46b587f8d24899c63cba7ce58d0a41aae564b2dfeabe5b80135bfdd703`
(36,456 bytes, 15 content files) · repo `menno420/venture-lab` @ `f0511ae`.

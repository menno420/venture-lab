# The Agent Merge-Wall Cookbook — listing copy

> **Status:** `reference`

Ready-to-paste copy for a Gumroad / Lemon Squeezy digital-product page.

## Title
```
The Agent Merge-Wall Cookbook — land your AI agents' pull requests without a human clicking merge
```

## Short description (≤ 200 chars)
```
Your agent's PR is green and still can't land: self-merge denied, auto-merge won't arm. Four runnable GitHub Actions recipes + the verbatim walls, from a repo whose fleet lands 10+ PRs a night.
```

## Long description
```
An agent fleet that opens its own pull requests hits a wall no amount of prompting fixes: the direct self-merge is denied by policy ("[Self-Approval] … defeating two-party review"), retrying through a different API path is denied again, and GitHub-native auto-merge refuses to arm because the branch has zero required checks — so a green PR sits agent-unlandable, one human click from done.

This cookbook is the landing path, taken from a public repository whose agent fleet hit every one of those walls, recorded each denial verbatim in a committed platform-limits ledger, and then landed 13 agent PRs green in a single night with the workflows this bundle ships.

Seven compact chapters (~3,500 words, ~8 pages): the self-merge wall with the actual denial texts and the first-denial-is-terminal rule; why auto-merge won't arm (the zero-required-checks trap, and why a required_status_checks rule with an empty context list is still a hole); the enabler pattern that arms native auto-merge at PR open so GitHub itself performs the merge; the born-red HOLD gate that keeps work-in-progress PRs red by design (including the documented incident where a card-only PR merged 24 seconds after open); the fast-lane rule that a required check must always report (never paths-ignore it); advisory checks double-guarded so they can never block a merge; and the GITHUB_TOKEN REST merge-on-green fallback for repo shapes where the arm is structurally refused.

Four runnable GitHub Actions recipes, ready for .github/workflows/: the auto-merge enabler (adapted near-verbatim from the live production workflow, with two merge events you can verify from the public GitHub API — merged_by: github-actions[bot]); the born-red HOLD gate with the fast-lane short-circuit; the never-red advisory check; and the REST merge-on-green fallback. Every recipe parses with a stock YAML loader and the QUICKSTART includes the exact verification commands.

Provenance is the product: every chapter ends with a Sources footer citing file @ commit in the public repo, and a per-recipe honesty ledger states exactly which recipes are production-proven and which one is assembled from documented doctrine and parse-verified only.
```

## Bullets
```
- The walls, verbatim: real self-merge denial texts from a committed platform-limits ledger — no invented cases
- Recipe 1: auto-merge enabler — arm at PR open, refuse-to-arm on zero required contexts, label carve-out with a stale-payload race guard (production-proven: verifiable merged_by github-actions[bot] events)
- Recipe 2: GITHUB_TOKEN REST merge-on-green fallback — every-check-green verification, sha-pinned merge (honesty-labeled: parse-verified, not production-run)
- Recipe 3: born-red HOLD gate — work-in-progress PRs red by design, so pre-armed auto-merge can't land an unfinished session (the 24-second false-green incident, documented)
- Recipe 4: the advisory check that can never turn red — exit-0 contract + continue-on-error, deliberately redundant
- The required-check rules that keep it all landing: always report (never paths-ignore), count contexts not rules, verify from the API not the settings page
- ~8 pages + ~330 lines of commented YAML; every chapter cites file @ commit in a public repo you can audit
```

## FAQ
```
Q: Are the walls and incidents real?
A: Yes, and auditably so. The denial texts, the zero-required-checks diagnosis, and the 24-second false-green incident are quoted from committed files in the public menno420/venture-lab repo; every chapter ends with a Sources footer citing the exact file @ commit.

Q: Are the recipes actually used in production?
A: Labeled per recipe, honestly. The enabler is adapted near-verbatim from the workflow live in that repo — it landed 13 agent PRs on 2026-07-13 alone, and the guide cites two merge events (PR #104, PR #128, merged_by github-actions[bot]) you can verify from the public GitHub API. The born-red gate and advisory check are distillations of live production jobs. The REST merge-on-green fallback is NOT production-run in the source repo (it lands via the native arm) — its header and chapter 7's honesty ledger say so, and tell you to trial it on a scratch repo.

Q: Will this bypass my policy layer / code review requirements?
A: No, and it doesn't try. The whole design is the opposite: the agent never merges. Merging is done by GitHub's native auto-merge or a repo-owned workflow identity, gated by a required check you control. If your org requires human review, that requirement still holds — these recipes land PRs whose required checks pass, nothing else.

Q: Is this specific to Claude/one vendor's agents?
A: The branch-namespace filter in the recipes is claude/* because that's what the source repo runs — it's one string to change. The walls (self-approval policy denials, auto-merge arming mechanics, required-check behavior) are GitHub platform behavior plus a policy-layer pattern any autonomous-agent stack reproduces.

Q: What was NOT machine-verified?
A: The prose chapters are verified by citation to committed material, not by execution. All four YAML recipes were parse-verified with a stock YAML loader from the packaged bundle; the enabler pattern is additionally backed by real production merge events. Recipe 2 was never run in production by the authors. Platform workarounds also rot — GitHub changes its API and UI; re-verify before betting a fleet.

Q: Who should NOT buy this?
A: If your agents' PRs are merged by humans and that's fine, you don't have this problem. If you already run a merge-on-green workflow with a required gate, a WIP hold, and never-red advisories, you own this discipline — buy nothing.

Q: License?
A: Single-user license; use the recipes in as many of your own projects as you like. v0.1 — free updates to the v0.x line.

Q: Support?
A: Best-effort, community-level. It's a cookbook, not a managed service.
```

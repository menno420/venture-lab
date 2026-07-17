# What's in this bundle (v0.1)

15 files:

```
auto-merge-enabler-cookbook-v0.1/
├── README.md                            — what this is + honesty box + "what it does NOT do"
├── QUICKSTART.md                        — verify, the two settings, install order, choreography
├── INCLUDED.md                          — this manifest
├── PROVENANCE.md                        — file@sha citations + the real merge event IDs
├── guide/
│   ├── 01-merge-on-green-model.md       — the model: the agent never merges
│   ├── 02-the-enabler-annotated.md      — the enabler workflow, guard by guard
│   ├── 03-required-checks-gating.md     — the zero-required-checks trap; contexts not rules
│   ├── 04-born-red-hold.md              — make "not finished" a red check
│   ├── 05-do-not-automerge-optout.md    — the opt-out label + the two one-time settings
│   ├── 06-seats-cant-self-arm.md        — the classifier caveat: why the workflow merges, not the seat
│   ├── 07-troubleshooting.md            — why a green PR didn't auto-merge
│   └── 08-recipes.md                    — install guide + per-file honesty ledger
└── recipes/
    ├── auto-merge-enabler.yml           — arm native auto-merge at open (production-proven, verbatim)
    ├── substrate-gate.yml               — required gate + born-red HOLD (production-proven, verbatim)
    └── auto-merge-enabler-minimal.yml   — the enabler skeleton for reading (distillation, parse-verified)
```

Guide length: ~4,300 words (~10 pages) across 8 chapters, each with a
Sources footer citing `file @ commit` in the public `menno420/venture-lab`
repo. Plus ~1,300 words of README/QUICKSTART/PROVENANCE and 3 GitHub
Actions files (~450 lines of commented YAML) — two of them the exact
production workflows this repo runs.

Evidence class: **verified-by-production**. The subject is this repo's own
live infrastructure, so the guide cites `file@sha` + real merge event IDs
(the five 2026-07-17 `github-actions[bot]` squashes) rather than an HTTP
test. See `PROVENANCE.md`.

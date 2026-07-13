# What's in this bundle (v0.1)

14 files:

```
merge-wall-cookbook-v0.1/
├── README.md                          — what this is + honesty box
├── QUICKSTART.md                      — verify, settings, install order, choreography
├── INCLUDED.md                        — this manifest
├── guide/
│   ├── 01-the-wall.md                 — the self-merge wall, denials verbatim
│   ├── 02-why-auto-merge-wont-arm.md  — the zero-required-checks trap
│   ├── 03-the-enabler.md              — Recipe 1 walkthrough + production merge events
│   ├── 04-born-red-hold.md            — Recipe 3: WIP PRs red by design
│   ├── 05-fast-lane.md                — required checks must always report
│   ├── 06-advisory-checks.md          — Recipe 4: checks that can never red
│   └── 07-rest-merge-on-green.md      — Recipe 2 + the per-recipe honesty ledger
└── recipes/
    ├── auto-merge-enabler.yml         — arm native auto-merge at open (production-proven)
    ├── merge-on-green.yml             — GITHUB_TOKEN REST fallback (parse-verified only)
    ├── born-red-hold-gate.yml         — born-red HOLD + fast lane (distilled from live gate)
    └── advisory-check.yml             — double-guarded never-red advisory (production-proven)
```

Guide length: ~3,500 words (~8 pages) across 7 chapters, each with a
Sources footer citing `file @ commit` in the public `menno420/venture-lab`
repo. Plus ~950 words of README/QUICKSTART and 4 runnable recipes
(~330 lines of commented YAML).

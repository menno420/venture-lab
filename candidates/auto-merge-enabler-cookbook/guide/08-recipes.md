# 8 · The recipes: copy-paste set + the honesty ledger

Three files ship in `recipes/`. Two are the **exact production workflows**
from the source repo, copied byte-for-byte; one is a minimal reading of the
enabler for people who want the skeleton first. This chapter is the install
guide and the per-file honesty statement — read the ledger before you trust
any of it with a fleet.

## What's in `recipes/`

| File | What it is | Provenance |
|------|-----------|------------|
| `auto-merge-enabler.yml` | The live enabler — arms native auto-merge on agent PRs at open. | **Production-proven, verbatim.** The exact file this repo runs. |
| `substrate-gate.yml` | The live required gate — born-red HOLD + control fast lane + append-only inbox gate. | **Production-proven, verbatim.** The exact file this repo runs. |
| `auto-merge-enabler-minimal.yml` | The enabler reduced to its load-bearing skeleton, for reading. | **Distillation, parse-verified.** Drops the label-race re-read; header says so. |

## Install order

1. **`substrate-gate.yml` → `.github/workflows/`.** This is your required
   check. Make it a **required context** on the default branch (chapters
   3-4). Adjust to your repo: the journal path (`.sessions/*.md`), the
   coordination prefix (`control/`), and swap this repo's
   `bootstrap.py check` invocations for your own test/lint commands at the
   marked steps. The load-bearing rule to preserve is the born-red HOLD:
   an added journal declaring an unfinished status is a designed red.
2. **`auto-merge-enabler.yml` → `.github/workflows/`.** The landing path.
   Adjust: your agent branch namespace (`claude/*` → yours); optionally add
   a `ROUTINE_PAT`/`MERGE_PAT` secret so merges attribute to a real user
   instead of `github-actions[bot]`. Confirm the gate name it waits on
   matches your required context (`substrate-gate` in both files here).
3. **Turn on the two repo settings** (chapter 5): "Allow auto-merge" = ON,
   and make your gate a required check. Verify from the API, not the UI.
4. **`auto-merge-enabler-minimal.yml`** is optional — install the full
   `auto-merge-enabler.yml` in production. Use the minimal file to
   understand the shape, or as a starting point if you are certain none of
   your PRs get their opt-out label after open (its header states the
   condition).

Don't run the minimal file *and* the full enabler together — two workflows
arming the same PR is harmless (arming is idempotent) but noisy. Pick one.

## Verify the recipes parse (one minute, no network)

Every recipe is plain GitHub Actions YAML. Prove they parse with a stock
loader:

```sh
python3 -c "import yaml,glob; [yaml.safe_load(open(p)) for p in sorted(glob.glob('recipes/*.yml'))]; print('3 recipes parse OK')"
```

No PyYAML? The stdlib structural check (weaker — verifies UTF-8 + required
top-level keys, not full grammar):

```sh
python3 - <<'EOF'
import glob
for p in sorted(glob.glob('recipes/*.yml')):
    t = open(p, encoding='utf-8').read()
    assert all(k in t for k in ('name:', 'on:', 'jobs:')), p
    print(p, 'structural OK')
EOF
```

## The honesty ledger (read before you ship any of this)

This cookbook's credibility mechanic is that its claims trace to committed
material in a public repo, and that the subject **is this repo's own live
infrastructure**. So the evidence class is *verified-by-production*, not an
HTTP test — but here is exactly what that does and does not mean:

- **`auto-merge-enabler.yml`: production-proven, verbatim.** It is the file
  this repo runs. On 2026-07-17 it squash-merged five agent PRs
  (`github-actions[bot]`: #219 `389ab6e`, #220 `4e0a37c`, #221 `12498f4`,
  #222 `37cf9fd`, #223 `f0511ae`), verifiable from the public GitHub API.
  What is *not* claimed: that it will behave identically on your repo shape,
  plan, or org policy — the guards exist precisely because behavior varies.
- **`substrate-gate.yml`: production-proven, verbatim.** The live required
  gate. Its born-red HOLD is what held this cookbook's own PR red until the
  session card flipped `complete`. What is *not* claimed: that the shipped
  `bootstrap.py check` commands run in *your* repo — they call this repo's
  engine; swap in your own test steps (the file marks where).
- **`auto-merge-enabler-minimal.yml`: distillation, parse-verified only.**
  It is a readability reduction of the enabler and drops the label-race
  re-read. It was parse-checked, not run in production. Its own header
  states the one condition under which it is safe to prefer over the full
  file.
- **The REST merge-on-green fallback is NOT shipped here as a production
  recipe.** This repo lands via the native arm, so the REST path exists as
  documented doctrine (chapter 7). If you need a runnable one, the companion
  Agent Merge-Wall Cookbook ships a parse-verified version — trial it on a
  scratch repo first.
- **Platform workarounds rot.** GitHub changes its API and UI; required-check
  mechanics, auto-merge arming, and the `GITHUB_TOKEN` recursion guard are
  all platform behavior that can shift. Re-verify against current GitHub
  docs before betting a fleet on any of this.

That is the standard: the two production files are the exact bytes this
repo runs, cited to real merge events; the one distillation says it's a
distillation; and the path this repo doesn't run isn't dressed up as one it
does.

**Sources** (public repo `menno420/venture-lab`):
`.github/workflows/auto-merge-enabler.yml` @ `aa04700` and
`.github/workflows/substrate-gate.yml` @ `aa04700` (the two verbatim
production recipes); merge events verified via the GitHub API on
2026-07-17 (the five `github-actions[bot]` squashes above); PR #223
created 23:05:38Z, merged 23:06:26Z.

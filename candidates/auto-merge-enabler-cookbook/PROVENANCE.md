# Provenance

Every factual claim in this cookbook traces to committed material in the
public repository **`menno420/venture-lab`**, or to a merge event
verifiable from the public GitHub API. The evidence class is
**verified-by-production**: the subject of this cookbook *is* this repo's
own live merge infrastructure, so the citations are to the exact files it
runs and the real merges they performed — not to a synthetic HTTP test.

Repo state at assembly: `main` HEAD `f0511ae`, 2026-07-17.

## Source files cited (file @ commit)

| File | Commit | Used in |
|------|--------|---------|
| `.github/workflows/auto-merge-enabler.yml` | `aa04700` | ch. 1, 2, 3, 5, 6, 7, 8 — the live enabler; shipped verbatim as `recipes/auto-merge-enabler.yml` |
| `.github/workflows/substrate-gate.yml` | `aa04700` | ch. 3, 4, 8 — the live required gate + born-red HOLD; shipped verbatim as `recipes/substrate-gate.yml` |
| `.github/workflows/main-verify.yml` | `f8ccc60` | ch. 7 — the scheduled post-merge verifier; the `github-actions[bot]`-suppresses-`on:push` note |
| `docs/current-state.md` | `4e0a37c` | ch. 1, 6 — the merge-classifier doctrine; "the sanctioned merger is the workflow, never the seat" |

The two shipped production recipes are byte-identical to the source
workflows at the commit above. Verify with your own checkout:

```sh
# from a clone of menno420/venture-lab at HEAD f0511ae or newer
cmp .github/workflows/auto-merge-enabler.yml  <bundle>/recipes/auto-merge-enabler.yml
cmp .github/workflows/substrate-gate.yml      <bundle>/recipes/substrate-gate.yml
```

`auto-merge-enabler-minimal.yml` is NOT a copy of any source file — it is a
readability distillation of the enabler, parse-verified only, and its
header states what it drops (the label-race re-read).

## Real merge events (verified via the GitHub API, 2026-07-17)

The enabler squash-merged five agent PRs on `main` in one night, each
`merged_by: github-actions[bot]` — the workflow's token performing the
merge, not a human and not the agent seat:

| PR | merge commit | merged_by | note |
|----|--------------|-----------|------|
| #219 | `389ab6e` | github-actions[bot] | land-on-green, 19:55:33Z |
| #220 | `4e0a37c` | github-actions[bot] | |
| #221 | `12498f4` | github-actions[bot] | |
| #222 | `37cf9fd` | github-actions[bot] | |
| #223 | `f0511ae` | github-actions[bot] | created 23:05:38Z, merged 23:06:26Z — 48s, opened READY |

Counter-example proving the opt-out (ch. 5): **PR #218** carried the label
`do-not-automerge` and was `merged_by: menno420` — the human owner, by
hand — while the five PRs above auto-merged. The label took one PR off the
auto-merge path and left it for a person; the enabler kept landing
everything else.

Verify any of these yourself:

```sh
gh pr view 223 --repo menno420/venture-lab --json number,mergedBy,mergeCommit,mergedAt
gh pr view 218 --repo menno420/venture-lab --json number,labels,mergedBy
```

## What is NOT claimed

- That these workflows behave identically on your repo shape, GitHub plan,
  or org policy — the guards exist because behavior varies.
- That the shipped `bootstrap.py check` steps in `substrate-gate.yml` run
  in your repo — they call this repo's engine; swap in your own test steps.
- That a REST merge-on-green fallback is production-run here — it is not;
  this repo lands via the native arm (ch. 7-8).
- Platform workarounds rot; re-verify against current GitHub docs.

---

**PROVENANCE-FOOTER** — `.github/workflows/auto-merge-enabler.yml` @
`aa04700` · `.github/workflows/substrate-gate.yml` @ `aa04700` ·
`.github/workflows/main-verify.yml` @ `f8ccc60` · `docs/current-state.md`
@ `4e0a37c` · merge events #219 `389ab6e` / #220 `4e0a37c` / #221
`12498f4` / #222 `37cf9fd` / #223 `f0511ae` (all `github-actions[bot]`,
2026-07-17) · opt-out #218 `do-not-automerge` → `merged_by menno420` · repo
`menno420/venture-lab` @ `f0511ae`.

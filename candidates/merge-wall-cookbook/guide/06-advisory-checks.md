# 6 · Recipe 4: advisory checks that can never red

An auto-merging fleet changes the economics of CI checks. In a
human-merged repo, a flaky informational check is an annoyance someone
clicks past. In a fleet where merges happen at 3am with nobody watching,
**any check that can red can stall a merge**, and an informational check
that stalls merges is paying rent it doesn't earn.

So the production repo splits its checks into exactly two castes, with
nothing in between:

- **Required checks** (chapters 4–5): always report, never path-filtered,
  red means "do not merge," including designed reds.
- **Advisory checks**: pure signal. May path-filter freely, may skip, may
  crash — and can *never* turn red.

## The double guard

"Can never turn red" is enforced twice in the production advisory job,
deliberately redundantly, per its own comment:

> ADVISORY ONLY — never a required gate. Double-guarded against ever
> turning red: the script exits 0 on EVERY path (in-sync, trailing, skip,
> parse failure) AND the step is continue-on-error.

Guard 1 is a **contract on the script**: it exits 0 unconditionally — on
success, on the drift it exists to detect, on skip, even on its own parse
failure. Its stdout line is the signal; its exit code is constitutionally
green. Guard 2 is `continue-on-error: true` on the step, so even an
interpreter crash or missing file cannot red the check. One guard is a
promise; two is a property — the belt survives the suspenders' bug.

What the production instance does with its green-always slot: prints one
ledger-drift line comparing the repo's "recently shipped" doc against the
newest merged PR — a nagging signal the next session reads, costing the
merge path nothing.

## The asymmetry that makes both castes work

Notice the mirror-image rules:

| | Required check | Advisory check |
|---|---|---|
| May `paths-ignore` / path-filter | **Never** (pending-forever trap, ch. 5) | Freely |
| May turn red | Yes — that's its job | **Never** (double guard) |
| Belongs in branch protection | Yes | **Never** |

A required advisory is a contradiction: either it reds (and blocks merges
on signal noise) or it can't (and gates nothing while occupying a required
slot). The moment an advisory earns the right to block merges, it isn't
advisory — promote it into the required gate and give it the always-report
treatment.

`recipes/advisory-check.yml` ships the pattern with the double guard in
place and a stub where your signal script goes.

**Sources** (public repo `menno420/venture-lab`):
`.github/workflows/kit-tests.yml` @ `838b46e` (`ledger-drift-advisory`
job: the double-guard comment, exit-0-on-every-path contract,
`continue-on-error: true`); `.github/workflows/substrate-gate.yml` @
`4776045` (the required-side rules the asymmetry table mirrors).

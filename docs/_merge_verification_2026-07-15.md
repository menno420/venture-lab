# Merge-on-green verification probe (2026-07-15)

> **Status:** `historical`
>
> ⚠️ **HISTORICAL — one-off probe artifact.** The `auto-merge-enabler.yml`
> mechanism this probe confirmed is being retired in the wind-down (agent seats
> no longer arm/self-merge; the owner merges). Kept as a record only; safe to
> delete at relaunch.

This file is a merge-automation verification probe for a fleet-wide audit session on
2026-07-15. It is a plain, inert content-only addition (no `.github/workflows/**`
changes) intended to confirm that ordinary code/doc PRs in this repo land on green
CI with zero human click, via the existing `auto-merge-enabler.yml` mechanism. It is
safe to keep or delete; it carries no functional meaning for the app.

# 2026-07-11 — Venture candidate: photo-packs (photography wallpaper / stock packs)

> **Status:** `in-progress`

## 💡 Session idea
Build the owner-directed photography venture candidate "photo-packs" end-to-end under `candidates/photo-packs/` — a line of downloadable wallpaper/stock packs (nature environments, macro bugs/insects, sunsets) sold as cheap digital bundles. Deliver an honest kill-rule INTAKE, a RESEARCHED + CITED MARKET-PLAN covering Gumroad/Ko-fi, stock-licensing, print-on-demand, and a differentiated macro-bug niche, a PACK-SPEC with a LOUD public-repo safety rule (no full-res originals — only downsized ≤2048px watermarked samples), a `packs.json` registry modeled on Bababoefoe's `editions.json`, and a stdlib-only `validate_samples.py` CI-cheap validator that degrades gracefully with no samples. No spend, no accounts, no publishing, no secrets — every revenue step is an owner-gated six-field OWNER-ACTION.

## Previous-session review
The prior physical/creative owner-directed candidate slice landed Bababoefoe (plush IP, PR-tracked under `candidates/bababoefoe/`), which established the local pattern this slice mirrors: a stdlib-only static-site `build.py`, a JSON registry as source of truth (`editions.json`), a phased money-protocol plan, and an honest INTAKE scored against venture-eval-001. photo-packs reuses that skeleton for a digital-download photography line. This slice touches only NEW files under `candidates/photo-packs/` plus this card; it does not touch control/, .github/workflows/, docs/launch/, or other candidates.

## Model
- **📊 Model:** opus-4.8 · worker · venture/build

## Deliverables
- candidates/photo-packs/INTAKE.md — kill-rule fields, honest cold-start read
- candidates/photo-packs/MARKET-PLAN.md — researched + CITED channel economics, six-field OWNER-ACTIONs
- candidates/photo-packs/PACK-SPEC.md — public-repo safety rule, curation, tiers, watermark policy, themes
- candidates/photo-packs/packs.json — registry seed modeled on editions.json
- candidates/photo-packs/validate_samples.py — stdlib-only, CI-cheap samples validator (graceful with no samples)
- candidates/photo-packs/site/build.py — stdlib gallery generator mirroring bababoefoe/site/build.py

## Outcome
_(pending — this card is born-red; it flips to `complete` in the final commit once all deliverables are built, `check --strict` is green, and `validate_samples.py` exits 0.)_

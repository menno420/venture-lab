# 2026-07-11 — Venture candidate: photo-packs (photography wallpaper / stock packs)

> **Status:** `complete`

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
Built the photo-packs candidate end-to-end under `candidates/photo-packs/` (NEW files
only; did not touch control/, .github/workflows/, docs/launch/, or other candidates):
- `INTAKE.md` — kill-rule fields, honest cold-start read, scored 2.35 against
  venture-eval-001; kill threshold ≤80k tokens incl. CI; conservative revenue
  $0–30/90d without an audience, stated plainly; blunt "why this might fail" (wallpapers
  compete with FREE; macro-bug niche + "shot on a real camera by a human" are the wedge).
- `MARKET-PLAN.md` — RESEARCHED + CITED channel economics: Gumroad (10% + $0.50),
  Ko-fi (5%/0% Gold), Adobe Stock (33%, ~$0.99/license), Shutterstock (15–40%, ~$0.10
  entry), Alamy (40% Gold), POD ($2–6/order, ~20% poster margin), plus the AI-ban /
  authentic-human tailwind and the macro-bug niche. Each channel ends in a six-field
  OWNER-ACTION. Unverifiable numbers marked "(not verified)".
- `PACK-SPEC.md` — LOUD top-of-file public-repo safety rule (full-res originals NEVER
  committed; only ≤2048px watermarked samples), curation + licensing-safety criteria,
  resolution tiers (phone 1290×2796, 4K 3840×2160, 5K 5120×2880, ultrawide 3440×1440),
  watermark policy, naming/metadata schema, 6 proposed themes.
- `packs.json` — registry seed modeled on Bababoefoe `editions.json`; 5 example packs
  with empty `samples` arrays so real previews slot in.
- `validate_samples.py` — STDLIB-ONLY, CI-cheap; header-only PNG/JPEG dimension reads,
  ≤2048px + size caps, naming + cross-reference checks; degrades gracefully to exit 0
  with "no samples yet".
- `site/build.py` (+ generated `dist/`) — stdlib gallery mirroring bababoefoe/site/build.py,
  previews-only, "samples coming" state when empty.
`check --strict` green after this flip; `validate_samples.py` exits 0 ("no samples yet").
No spend, no accounts, no publishing, no supplier contact, no secrets. First commit was
this card born-red; this final commit flips it complete.

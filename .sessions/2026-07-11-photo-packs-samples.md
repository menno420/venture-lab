# 2026-07-11 — photo-packs: compliant watermarked preview samples

> **Status:** `complete`

## 💡 Session idea
Turn the owner's 10 oversized full-res originals (posted to PR #51 on branch
`menno420-patch-1`, which violates the public-repo rule that only ≤2048px
watermarked previews may ever be committed) into COMPLIANT preview derivatives:
downsize each to longest edge ≤ 2048px, apply a visible crop-resistant watermark,
register the good ones into `packs.json` under two packs (Golden Hours — Waterside
and Dutch Skies), rebuild the gallery, and harden `validate_samples.py` to close the
root-level gap that let PR #51's full-res dump through. No full-res bytes committed;
originals stay OFF-repo. No spend, no publish, no self-merge; PR #51 and the owner's
branch are left untouched (owner's cleanup).

## Previous-session review
The photo-packs candidate previously shipped its spec (`PACK-SPEC.md`), a stdlib
registry (`packs.json`) with empty `samples` arrays, a stdlib gallery
(`site/build.py`), and a header-only `validate_samples.py` — all staged for real
previews to drop in. The owner then posted 10 full-res originals to PR #51 at repo
ROOT, which is exactly what the safety rule forbids. This slice supplies the missing
compliant previews and closes the validator gap that failed to catch the root-level
originals. It touches ONLY `candidates/photo-packs/**` and this card — not `control/`,
`docs/launch/`, `.github/workflows/`, or other candidates.

## Model
- **📊 Model:** opus-4.8 · worker · venture/build

## Deliverables
- candidates/photo-packs/samples/*.jpg — 7 watermarked ≤2048px previews (2 packs)
- candidates/photo-packs/packs.json — golden-hours + dutch-skies registered
- candidates/photo-packs/site/dist/ — gallery rebuilt with the previews
- candidates/photo-packs/validate_samples.py — repo-wide oversize guard + wider header read
- candidates/photo-packs/PACK-SPEC.md — v1 curation log, exclusions, validator-hardening note

## Outcome
Produced **7 compliant watermarked previews** (all longest edge exactly 2048px,
150–483 KB each) from the owner's 10 full-res originals using **Pillow 12.3.0**
(no ImageMagick/ffmpeg on host; Pillow pip-installed — free, no spend). Pipeline:
EXIF auto-orient → LANCZOS downscale to ≤2048px → tiled crop-resistant body
watermark (`© menno420 — PREVIEW — not for use`) + solid corner mark → JPEG q82,
EXIF stripped. Originals were fetched to an off-repo scratch dir and **never entered
the repo tree**; verified every staged blob ≤2048px before committing.

Registered two packs in `packs.json` — **golden-hours** ("Golden Hours — Waterside",
4 previews) and **dutch-skies** ("Dutch Skies", 3 previews) — rebuilt `site/dist/`.
`validate_samples.py` passes (exit 0) on the 7 samples.

Exclusions: **#7 cat dropped** (no theme fit), **#3 corporate signage held**
(licensing risk — not registered/committed), **#4 theme-ambiguous held** (processed
to a compliant derivative in scratch but not registered, to avoid an orphan-fail and
pending an owner theme call). **#5/#6 read sideways (EXIF orientation 6) and were
auto-oriented** via `ImageOps.exif_transpose` — upright, no manual rotation needed.

Hardened `validate_samples.py` to close the PR #51 root-level gap: a **repo-wide
oversize scan** now fails the build on ANY tree image (excl. `.git`) with longest
edge > 2048px (no sanctioned oversize location), and the header read window was
raised 64 KiB → 4 MiB so a large-EXIF phone JPEG's SOF is still parsed (fail-closed
on unreadable). Proven to catch an 11720px root-level dump, then cleaned. CI wiring
left as a follow-up (no photo-packs check exists in workflows; kit-owned
`substrate-gate.yml` not hand-edited).

No spend, no publish, no self-merge. PR #51 and branch `menno420-patch-1` untouched
(owner's cleanup). First commit born-red; this final commit flips the card complete.

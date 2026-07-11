# 2026-07-11 — photo-packs: compliant watermarked preview samples

> **Status:** `in-progress`

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
_(to be filled on close-out)_

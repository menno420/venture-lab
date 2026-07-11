<!-- ============================================================= -->
<!--  ⚠️  PUBLIC REPO — READ THIS BEFORE ADDING ANY IMAGE  ⚠️     -->
<!-- ============================================================= -->

> # ⚠️ STOP — PUBLIC REPO SAFETY RULE (read before committing any image)
>
> **This repository is PUBLIC. Full-resolution original photographs must NEVER be
> committed here — committing a full-res original gives it away for free and destroys
> the product you are trying to sell.**
>
> **ONLY downsized, watermarked SAMPLE images may ever be committed, and only if
> they satisfy ALL of:**
> 1. **≤ 2048 px on the longest edge** (preview resolution, never a usable wallpaper),
> 2. **visibly watermarked** (see Watermark policy below),
> 3. **placed under `candidates/photo-packs/samples/`** and registered in `packs.json`.
>
> **Full-res originals and any sellable file live OFF this repo** — on the owner's
> storefront (Gumroad/Ko-fi), stock platform, or private storage. `validate_samples.py`
> enforces the ≤2048px and size caps mechanically, but it cannot know a file is an
> original — **the human committing is responsible.** When in doubt, do NOT commit it.

<!-- ============================================================= -->

# photo-packs — pack specification

Defines how photography packs are curated, sized, named, watermarked, and registered.
The registry (`packs.json`) is the source of truth, modeled on Bababoefoe's
`editions.json` (see `candidates/bababoefoe/site/editions.json`).

## Curation criteria
A photo qualifies for a pack only if it clears all of:
- **Sharpness:** critically sharp at the intended subject (pixel-peep the focal
  plane; reject motion blur / missed focus). Wallpapers are viewed full-screen.
- **Subject interest:** a clear, compelling subject — for the differentiated packs,
  that means genuine macro detail or a distinct natural moment, not a generic scene.
- **Licensing-safety (owner homework, not agent-checkable):**
  - **No recognizable people** without a model release (avoid faces entirely for
    stock/wallpaper use).
  - **No trademarked logos / brands** in frame.
  - **No private-property or protected-location issues** (some landmarks/venues
    restrict commercial use; property releases may be required).
  - Macro bug/insect shots are the lowest-risk here; sunsets/landscapes need a
    people-and-property pass before sale.

## Resolution tiers (exact pixel dimensions)
Each sold pack ships these tiers (built from the full-res original, OFF-repo):

| Tier | Dimensions (px) | Notes |
|---|---|---|
| Phone | 1290 × 2796 | iPhone 15/16 Pro Max class; portrait. A 1080 × 2340 variant covers common Android. |
| Desktop 4K | 3840 × 2160 | 16:9 UHD — the standard desktop wallpaper tier. |
| Desktop 5K | 5120 × 2880 | 16:9 5K — for high-DPI/Retina displays. |
| Ultrawide | 3440 × 1440 | 21:9 — ultrawide monitors. A 5120 × 1440 variant covers 32:9 super-ultrawide. |

**Sample/preview tier (the ONLY tier that may enter this repo):** longest edge
**≤ 2048 px**, watermarked. This is a preview, deliberately too small and too marked
to use as a real wallpaper.

## Watermark policy (public previews)
- Every committed sample carries a **visible watermark** — a semi-transparent mark
  across the image body (not just a corner, which is easily cropped).
- Suggested text: the pack/brand name + "PREVIEW — not for use".
- Watermarking is done by the owner in their editor before committing; it is a
  **policy + human step**, not automated by this repo. `validate_samples.py` verifies
  size/dimensions/naming but **cannot detect a watermark** — do not rely on it for that.

## Naming + metadata schema
**File naming (samples):** `<pack-id>__<seq>__<tier>.<ext>`
e.g. `small-worlds__01__preview.jpg`. Lowercase, hyphen/underscore only, no spaces.
- `<pack-id>` matches a pack `id` in `packs.json`.
- `<seq>` is a zero-padded index (`01`, `02`, …).
- `<tier>` for committed files is always `preview` (the ≤2048px watermarked tier).
- `<ext>` is `jpg`, `jpeg`, or `png`.

**`packs.json` registry (source of truth, modeled on `editions.json`):**
top-level object with `brand`, `tagline`, a `//` note, `base_url`, `sample_dir`,
`watermark_note`, and a `packs` array. Each pack entry has:

| Field | Meaning |
|---|---|
| `id` | stable slug/id (e.g. `small-worlds`); matches sample filenames + never changes once published |
| `title` | display title (e.g. "Small Worlds") |
| `theme` | short theme key (e.g. `macro`, `sunset`, `nature`) |
| `description` | one-line description for the gallery / listing |
| `tiers` | list of resolution-tier keys shipped in the SOLD pack (`phone`, `desktop-4k`, `desktop-5k`, `ultrawide`) — NOT committed here, listed for the storefront |
| `samples` | list of committed sample filenames (under `sample_dir`), each ≤2048px + watermarked |
| `price_usd` | suggested list price (e.g. 5) — informational, real price set on storefront |
| `count` | number of photos in the full sold pack (informational) |
| `watermark` | note confirming samples are watermarked previews |

The seed file `packs.json` ships with example pack entries and **empty `samples`
arrays** so real sample filenames slot in when the owner adds files.

## Suggested pack themes (from owner's subjects)
Proposed starting line-up (4–6 themes). The macro packs are the differentiated wedge;
the sunset pack is included but flagged as the weak, saturated one.

1. **Small Worlds** — macro bugs/insects, extreme detail. *The strongest wedge:
   differentiated subject + educational/blog audience.*
2. **Six-Legged Neighbours** — macro of common garden insects (bees, beetles,
   spiders, dragonflies); pairs with the entomology-education outreach channel.
3. **Wild Ground** — nature environments / landscapes (forests, wetlands, dunes),
   the owner's "nature environments" subject.
4. **Dutch Skies** — big-sky / cloud / weather scenes over open landscape (the
   owner's environment); more distinctive than generic sunsets.
5. **Golden Hours** — sunsets / golden-hour light. *Included for completeness but the
   most-saturated, least-differentiated pack — do not lead with it.*
6. **After Rain** — dew, water droplets, wet-leaf macro (bridges macro + nature; high
   visual appeal, still differentiated). *(optional 6th)*

## Site / gallery
A stdlib-only gallery generator lives at `candidates/photo-packs/site/build.py`,
mirroring the style of `candidates/bababoefoe/site/build.py`. It reads `packs.json`
and renders a preview gallery ready for samples; with no samples yet it renders the
pack cards and a "samples coming" state. It intentionally shows only the watermarked
preview tier — never a sellable file.

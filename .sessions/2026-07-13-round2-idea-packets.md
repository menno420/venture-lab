# 2026-07-13 — Day run: round-2 book concept vetting packets (BOOKS lane)

> **Status:** `complete`

Started 2026-07-13T09:26:39Z · closed 2026-07-13T09:37:46Z (`date -u`).
Day-run BOOKS-lane slice: a SECOND round of new book concepts as
concept-stage mini vetting packets (the night run's
`.sessions/2026-07-13-night-book-idea-packets.md` delivered round one).
Each packet follows `docs/publishing/CHECKLIST.md` §1–§7 in the
`the-paper-orange.md` concept-stage format, with REAL dated collision
scans, and reserves its niche name-level only in
`docs/publishing/keyword-map.md` §3. Fills catalog gaps outside every
owned/reserved register (C1–C4 respected; no Night Kiln / `en/` manuscript
files touched — sibling worker owns those).

## Outcome

- Six concept-stage packets under `docs/publishing/vetting/`, each per
  CHECKLIST §1–§7 with a REAL web collision scan quoted + "accessed
  2026-07-13", cited §3 comps, price band from the plan's verified §1
  table (KDP 70% tier noted), §6 marked PROVISIONAL/name-level, and a §7
  ⚑ OWNER-GATE block in the paper-orange format:
  - `the-marmalade-post.md` — adult contemporary cozy mystery, series-native
    (one misdelivered parcel per book) — collision **Low**; first cozy shelf,
    register-distinct from Weigh House's procedural rows.
  - `the-glass-rectory.md` — adult Victorian gothic ghost novella —
    collision **Low**; distinct from both reserved dark niches (Hollowtide
    folk-dark, Undertow coastal-psychological).
  - `the-seed-catalogue-courtship.md` — adult epistolary romance (clean,
    later-in-life) — collision **None found → Low**; the catalog's first
    Romance-storefront title; Catalogue/Catalog spelling fork handled in §1.
  - `the-salvage-orchard.md` — adult solarpunk novella — collision **Low**;
    second SF shelf, zero stem overlap with Slow Word's owned register or
    Last Good Frequency's reserved radio niche, by construction.
  - `the-halfway-ferry.md` — middle-grade portal-fantasy series (first MG
    title; one crossing per book) — collision **Low**, after a same-day
    rename OFF the occupied Thistlewick stem (honest scan, dropped it).
  - `the-twelfth-cake.md` — adult seasonal Twelfth Night (Jan 5) historical
    novella — collision **Moderate** (common-noun search crowding, not a
    competing novel); mitigation locked now (mandatory subtitle,
    fiction-marked keywords); first seasonal/holiday shelf.
- `docs/publishing/keyword-map.md` §3: six NAME-LEVEL reservation rows
  (no ownership rows — those come at graduation), each recording its
  register constraints vs C1–C4 and the reserved niches.
- Honest nulls: no manuscript exists for any concept (each parks at "no
  manuscript" §3/§5); no spend, no accounts, no publishing; base case ≈ $0
  in every §3; the plan's §1 price table has no MG-ebook row — flagged in
  the Halfway Ferry packet rather than invented.
- Ritual: claim `control/claims/round2-idea-packets.md` live from commit 1;
  PR #143 opened READY; keyword-map re-fetched against main before close
  (unchanged on main — no merge needed).

## 💡 Session idea
💡 **Keyword-register linter.** The map's registers (C1–C4 + the reserved
niches) are enforced today by each packet author re-reading §3 prose — this
slice had to hand-check six packets against a dozen forbidden stems (radio/
signal, widow, Amsterdam, Golden Age, bedtime, space...). A ~40-line
advisory checker (same tolerant/exit-0 contract as `derive_owner_queue.py`)
that greps every packet's §6 keyword block against a small per-owner
stem-list derived from the map's §1 rows would catch a register violation
at commit time instead of at map-review time — complementary to the
graduation checker idea (which checks row SPECIES; this checks row
CONTENT).

## Previous-session review
previous-session review: `.sessions/2026-07-13-night-book-idea-packets.md`
(PR — night run, round 1) — the concept-stage packet format it locked
(paper-orange §1–§7 + name-level-only §3 rows) made this round mostly
mechanical, which is the point; genuinely good was the honest-collision
discipline (its Windmill Mouse Moderate), which this round copied twice
(Thistlewick rename, Twelfth Cake Moderate); honest nit: its packets'
§3 comps lean on the plan's inherited price table where this round added
per-packet cited comps — round 1's packets could be retrofitted cheaply.

## Model
- **📊 Model:** fable-5 · worker · BOOKS lane, day run

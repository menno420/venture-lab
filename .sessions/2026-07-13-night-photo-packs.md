# Session — Night run: photo-packs driven to the owner gate, honestly (ORDER 008, PRODUCT #5)

> **Status:** `complete`

- **📊 Model:** fable-5 · worker slice · ORDER 008 night-run product lane
- **session:** PRODUCT #5 of the 2026-07-13 night run — photo packs
  (`candidates/photo-packs/`) driven as far as agent-doable WITHOUT faking
  readiness: executed assessment (validator, registry, samples), pricing
  recommendation from MARKET-PLAN evidence, listing copy for the two packs
  with committed previews, and a §7 packet whose artifact-build rows are
  HARD-GATED owner rows — the sellable zips cannot be built in-repo because
  full-res originals are owner-held off-repo. NO publish click is queued
  ungated; the product is NOT claimed publish-READY.
- **started (date -u):** Sun Jul 13 01:56:27 UTC 2026
- **closed (date -u):** Sun Jul 13 02:12 UTC 2026

## ⟲ Previous-session review

Previous session (`.sessions/2026-07-13-night-queue-done-disposition.md`,
PR #116, merged): the DONE-disposition slice held its bar — the both-marks
rule (checked box AND `— DONE <date>`) plus the regression test pinning the
legacy tolerance meant this session could add a 15th packet without touching
the script and trust the totals arithmetic (9/74/13 → 11/82/14, verified by
diff, not assumed). Its guard recipe ("never flip a DONE row back") was
copied into this packet's post-click seat row verbatim. Two observations:
(1) its 💡 (a `⏲ <date>` / KILL-CHECK token rendering a "next checkpoint"
column in the Live section) remains unbuilt and is now MORE valuable — with
photo-packs the queue carries three different row temporalities (pending,
blocked-pending, DONE) and still no time dimension; SWTK's 2026-07-19
checkpoint is 6 days out and invisible in the derived file. (2) The blocked
rendering says "(a D-item above blocks this sequence)" — true for the book
packets whose blocker IS a decision, but photo-packs' blocker is a hand-off
step, not a D-item; harmless wording drift in a generated file, noted here
rather than hand-edited (the file is script-owned).

## 💡 Session idea

`derive_owner_queue.py`'s `blocked` flag is group-level, so a HARD-GATED
sequence renders every row identically even though only the first rows are
the gate. Cheap upgrade, same tolerant bar: rows carrying "blocking" render
with a distinct marker (e.g. `- [ ] ⛔`) and the group header names the gate
("HARD-GATED on: hand off full-res originals…" — first blocking row's first
clause) instead of the generic D-item wording. Then the owner reads WHAT
blocks a sequence from the queue itself, without opening the packet — and
the wording drift noted in the review above disappears for free.

## Scope

- Executed assessment (read-only on `candidates/photo-packs/`):
  `validate_samples.py`, packs.json JSON + PACK-SPEC conformance, sample
  dims/watermark/EXIF checks.
- `docs/launch/photo-packs/listing-copy.md` — NEW, dutch-skies +
  golden-hours at catalog parity, PREVIEW-ONLY header.
- `docs/publishing/vetting/photo-packs.md` — NEW §7 packet, blocking owner
  rows first; `docs/publishing/OWNER-QUEUE.md` regenerated;
  `docs/publishing/README.md` index row.
- `docs/current-state.md` — products section updated to tonight's reality
  (SWTK live, 3 click-queued, photo packs gated) + missing photo-packs row.
- NOT touched: `candidates/photo-packs/site/` (site-shaped = Websites lane;
  WEBSITE-IDEA flagged in the run report, not here).

## Work log — executed evidence (all 2026-07-13, base `d01dacd`)

1. **Validator:** `python3 candidates/photo-packs/validate_samples.py` →
   exit 0: "packs.json valid and 7 sample file(s) pass all checks (<= 2048px,
   size cap, naming, cross-referenced); repo-wide oversize scan clean"
   (7 image files scanned repo-wide).
2. **Registry:** packs.json valid JSON; 5 packs (not 7 — 7 is the sample
   count); all required top-level + per-pack fields present; tier keys
   canonical; all sample names match `<id>__<seq>__preview.jpg` with
   matching ids; count==samples for both preview packs (3 / 4).
3. **Samples:** dims header-parsed (stdlib) — all 7 at longest edge exactly
   2048px; watermark visually confirmed on one sample per pack (tiled
   "© menno420 — PREVIEW — not for use" + corner mark); EXIF: no
   `Exif\x00\x00` APP1 segment in any file (byte scan; Pillow unavailable,
   honest limitation — but no segment means no tags, GPS included).
4. **Queue delta proven:** baseline regen at HEAD byte-identical to
   committed (9 decisions / 74 clicks / 13 sequences); after adding the
   packet: 16/16 inputs clean, 11 / 82 / 14, manual-review none; diff vs
   baseline = ONLY photo-packs D3+D4 (renumbering D5–D11) + one new
   HARD-GATED 8-row group. No other group changed.
5. **Not done, on purpose:** no zip, no sha, no publish click, no
   publish-READY claim — the artifact cannot exist in this public repo.

## Guard recipe

Never queue an ungated photo-packs publish click: the §7 blocking rows
(originals hand-off + licensing pass) must flip to DONE before the seat
build row, and the seat build row must pin per-zip sha256s in §1 before any
upload/publish row is actionable. Full-res originals NEVER enter this repo
under any workflow — the validator's repo-wide oversize scan is the
mechanical backstop, but the PACK-SPEC human rule is the real gate.

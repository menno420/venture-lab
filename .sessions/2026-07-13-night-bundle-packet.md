# Session — Night run: $59 Ship-It Bundle as an honest HARD-GATED packet (ORDER 008, PRODUCT #6)

> **Status:** `complete`

- **📊 Model:** fable-5 · worker slice · ORDER 008 night-run product lane
- **session:** PRODUCT #6 of the 2026-07-13 night run — the $59 bundle
  (Membership-Site Kit $49 + Agent-Workflow Template Pack $19 PWYW,
  `candidates/BUNDLE-LISTING.md`) driven to the owner gate HONESTLY: a
  Gumroad bundle references existing live products, so there is no new
  zip/sha to build (stage-6 N/A-with-reason per `docs/products/TEMPLATE.md`
  honest-null discipline — the re-verified component shas ARE the artifact
  pins), and the bundle cannot exist until the ⚑B and ⚑D component publish
  clicks are executed — so the §7 packet's first rows are BLOCKING owner
  rows and NO ungated bundle click is queued. Also: the stale "nothing
  published" line in BUNDLE-LISTING.md fixed with citations (SWTK live
  PR #86; components click-queued PR #106/#108), and the PACK-SPEC
  follow-up standalone CI workflow for
  `candidates/photo-packs/validate_samples.py` landed.
- **started (date -u):** Sun Jul 13 02:11:32 UTC 2026
- **closed (date -u):** Sun Jul 13 02:24 UTC 2026

## ⟲ Previous-session review

Previous session (`.sessions/2026-07-13-night-photo-packs.md`, PR #120,
merged): the first HARD-GATED packet held its bar and made this one cheap —
its "blocking rows first, no ungated click" §7 shape was reused wholesale;
its baseline-then-delta queue-regen proof (regen at HEAD byte-identical,
then diff = only the new group) was repeated here verbatim and caught
nothing drifting (9→11→11 decisions across the two slices, this one adds
zero by construction). Two of its observations paid off tonight: (1) its
review noted the generated "(a D-item above blocks this sequence)" wording
is drift when the blocker isn't a D-item — this packet hits the same drift
(its blockers are component *clicks*), confirming the photo-packs 💡 (row
level "blocking" markers + gate-naming headers) is now the queue's most
valuable pending upgrade, still unbuilt along with the older ⏲/KILL-CHECK
column idea. (2) Its guard recipe ("the validator's repo-wide oversize scan
is the mechanical backstop") became executable tonight — the PACK-SPEC CI
follow-up it left on the table is landed here as the standalone
`photo-samples-validate.yml`. One miss found while building on it: nothing
in the photo-packs slice fixed the BUNDLE-LISTING staleness it walked past;
that lag between catalog reality and candidate docs is exactly what this
slice's staleness fix closes.

## 💡 Session idea

The §7 grammar now encodes three distinct blocker *kinds* with one word
("blocking"): missing artifact (photo-packs), missing referent (this
bundle: components not live), missing decision (illustration gates). A
cheap, tolerant extension: let a blocking row name its gate type and
release condition machine-readably — `blocking[until: ⚑B DONE]` — and have
`derive_owner_queue.py` render a "clears when" clause per gated group and,
once the DONE disposition flips ⚑B/⚑D, AUTOMATICALLY drop the satisfied
blocking rows from the bundle group at the next regen. Then a component
going live un-gates its dependents in the derived queue with zero packet
edits — the queue becomes a real dependency graph instead of prose.

## Scope

- `docs/launch/bundle-starter/` — NEW: `listing-copy.md` (refreshed from
  `candidates/BUNDLE-LISTING.md` to catalog parity, Title / short 190≤200 /
  long / bullets / FAQ, $59 vs $68-separate cited) + `owner-actions.md`
  (six-field WHAT/WHERE/HOW/WHY/UNBLOCKS/VERIFIED-WHEN, HARD-GATED).
- `candidates/BUNDLE-LISTING.md` — stale "Nothing here has been published"
  header replaced with cited catalog reality.
- `docs/publishing/vetting/bundle-starter.md` — NEW §7 packet, blocking
  component-click rows first; `docs/publishing/OWNER-QUEUE.md` regenerated;
  index rows in `docs/publishing/README.md`, `docs/launch/README.md`,
  `docs/current-state.md`.
- `.github/workflows/photo-samples-validate.yml` — NEW standalone workflow
  (PACK-SPEC follow-up); NO existing workflow touched.

## Work log — executed evidence (all 2026-07-13, base `cf4f17e`)

1. **Sha pins re-verified** (not copied): `sha256sum` on both committed
   dists → `9f262fc8…d5d3e1` (membership-kit-v0.2.zip) and
   `d65d4c9e…3a2b3` (template-packs-v0.1.zip), matching the component
   packets' pins exactly; verbatim output in the packet §1.
2. **Stage-6 honest null:** no new artifact built ON PURPOSE — a Gumroad
   bundle references the components' own uploads; zipping the zips would
   fork a second artifact chain that isn't what the buyer receives.
   Rationale written into packet §1 per TEMPLATE.md.
3. **Queue delta proven:** baseline regen with the new packet moved aside →
   byte-identical to committed (11 decisions / 82 clicks / 14 sequences);
   with the packet → 17/17 inputs clean, 11 / 88 / 15, manual-review none;
   diff vs committed = ONLY one new HARD-GATED 6-row Ship-It Bundle group
   (+9 lines, no other hunk). Zero D-items added by construction.
4. **Parser lessons hit and fixed same session:** (a) a ⚑ inside a numbered
   step makes the tolerant parser demand a default (manual-review nag) —
   flag tokens moved to checkbox rows only; (b) markdown links in checkbox
   rows propagate verbatim into the generated file one directory up →
   dead links (caught by `bootstrap.py check --strict`) — plain-text
   packet refs instead.
5. **CI follow-up:** `python3 candidates/photo-packs/validate_samples.py`
   re-run → exit 0 ("7 sample file(s) pass all checks … repo-wide oversize
   scan clean"); new workflow YAML parses (`yaml.safe_load` ok),
   path-filtered to `candidates/photo-packs/**`, one job, no secrets.
6. **Not done, on purpose:** no bundle click queued ungated, no
   publish-READY claim (the packet verdict is "NOT actionable yet —
   HARD-GATED"), field manual NOT added (v2 only, after v1 signal).

## Guard recipe

Never queue an ungated bundle click: the §7 blocking rows (⚑B + ⚑D
executed) must flip to DONE before the bundle-creation rows are actionable,
and the bundle price stays FIXED $59 (inheriting the pack's PWYW would let
the bundle undercut the $49 kit alone). The component sha pins in §1 are
re-verified against the committed dists — never copied forward from prose —
so a dist refresh in either component packet invalidates this packet's §1
until re-run.

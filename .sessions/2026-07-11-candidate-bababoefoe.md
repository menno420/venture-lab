# 2026-07-11 — Venture candidate: Bababoefoe (owner plushy brand)

> **Status:** `complete`

## 💡 Session idea
Build the owner-directed physical-product venture candidate "Bababoefoe" — a family of round ultra-fluffy costumed plush critters (Pirate, Chef, Police, Santa/Witch editions) whose physical features feed a fiction: magnetic hands that hold in a chain, a hidden keepsake pocket, and a per-edition QR tag opening that edition's origin-story page. Deliver a brand bible, sample stories, a working stdlib-only static site with a QR/edition registry, a phased money-protocol MAKE-IT-REAL plan, and an honest intake — every revenue step owner-gated, no spend.

## Previous-session review
Prior slices intook the digital-artifact candidates (stripe-webhook-test-kit, agent-fleet-field-manual, cc-cost-lens) and landed the round-2 close-out. This slice is the first PHYSICAL-product candidate and sits OUTSIDE the lane's proven one-click-digital path: every physical/revenue step is owner-gated, and it exists to be evaluated honestly against that constraint, not to claim the lane's usual buildability. It touches only NEW files under candidates/bababoefoe/ plus this card; it does not touch control/, .github/workflows/, docs/launch/, or other candidates.

## Model
- **📊 Model:** opus-4.8 · worker · venture/build

## Deliverables
- candidates/bababoefoe/BRAND-BIBLE.md
- candidates/bababoefoe/stories/*.md (4–5 sample edition stories)
- candidates/bababoefoe/site/ — editions.json, build.py (stdlib), generated pages, qr-urls.txt
- candidates/bababoefoe/MAKE-IT-REAL-PLAN.md (phased, money-protocol)
- candidates/bababoefoe/INTAKE.md

## Outcome
Built the Bababoefoe candidate end-to-end under candidates/bababoefoe/: BRAND-BIBLE.md
(universe, naming grammar, feature→fiction mapping, colorways), 5 kid-safe read-aloud
edition stories (Pirate, Chef, Police, Santa, Witch), a working stdlib-only static
site (editions.json registry + build.py → dist/ landing/collection/per-edition pages +
qr-urls.txt manifest), a phased money-protocol MAKE-IT-REAL-PLAN.md with CITED numbers
(Makeship/POD/plush-MOQ) and a safety/compliance section flagging the magnetic-hands
regulation, and an honest INTAKE.md scoring the candidate 2.20 (physical products are
outside the lane's proven digital path; every revenue step owner-gated). QR path: no
segno/qrcode installed and nothing installed (no-spend) → url-manifest path; segno is a
zero-cost owner/local step. No spend, no accounts, no publishing, no supplier contact,
no secrets. check --strict green. First commit born-red card; this final commit flips
it complete.

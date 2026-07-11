# Bababoefoe site

Working static site, plain HTML/CSS, **stdlib-only** build (no jinja, no external deps).

## Build
```
python3 build.py     # run from this dir; writes everything into dist/
```

## Files
- `editions.json` — the edition registry and **source of truth for printed QR tags**
  (id, name, colorway, slug, story path, stable url). Freeze `base_url` + `url`
  before printing any tag.
- `build.py` — reads `editions.json` + `../stories/*.md`, generates into `dist/`:
  - `index.html` — landing page
  - `collection.html` — registry page (mirrors `editions.json`)
  - `<slug>.html` — one page per edition story (the QR target)
  - `style.css` — shared stylesheet
  - `qr-urls.txt` — slug → full URL manifest (printable QR source of truth)
  - `qr/<slug>.svg` — only if `segno` or `qrcode` is importable

## QR path taken
Neither `segno` nor `qrcode` is installed here, and nothing was installed (no-spend
rule). `build.py` therefore emitted `dist/qr-urls.txt`. To render actual QR images
later at zero cost: `pip install segno` locally (pure-Python, MIT — NOT a repo
dependency) and re-run `python3 build.py`; SVGs appear in `dist/qr/` and are auto-
referenced on each edition page. No code change needed.

## Deploy
GitHub Pages, one owner click — see `../MAKE-IT-REAL-PLAN.md` → Phase 0 /
OWNER-ACTION 0.1. Served base: `https://menno420.github.io/venture-lab/candidates/bababoefoe/site/dist/`.

`dist/` is generated output committed for direct GitHub Pages serving.

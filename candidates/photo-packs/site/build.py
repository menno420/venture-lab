#!/usr/bin/env python3
"""photo-packs static gallery builder — STDLIB ONLY (no jinja, no external deps).

Mirrors the style of candidates/bababoefoe/site/build.py. Reads `../packs.json`
(the registry / source of truth) and generates, into `dist/`:
  - index.html    landing + a card per pack
  - <id>.html     one preview page per pack (its watermarked samples, if any)
  - style.css     shared stylesheet

PUBLIC REPO: this generator only ever references the watermarked PREVIEW samples
listed in packs.json (files under `sample_dir`, each <=2048px). It NEVER references
full-res originals or sold tiers — those never live in this repo. With no samples
yet, each pack page renders a "samples coming" state so the gallery is ready to
drop previews into.

Run:  python3 build.py        (from candidates/photo-packs/site/)
Output is self-contained in dist/ and opens directly in a browser (file://) or on
GitHub Pages at the base_url recorded in packs.json.
"""
from __future__ import annotations

import html
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DIST = HERE / "dist"
REGISTRY = HERE.parent / "packs.json"


# ---------- page shell ----------

def page(title: str, body: str, *, css_href: str = "style.css") -> str:
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<link rel="stylesheet" href="{css_href}">
</head>
<body>
<div class="wrap">
{body}
<footer><a href="index.html">photo-packs</a> &middot; real photos, shot on a real camera, by a human.</footer>
</div>
</body>
</html>
"""


CSS = """
:root { --bg:#0f1115; --card:#181c22; --ink:#e8eaed; --muted:#9aa1ab; --accent:#5ec8a0; --soft:#262c34; }
* { box-sizing: border-box; }
body { margin:0; font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  background: var(--bg); color: var(--ink); line-height: 1.6; }
.wrap { max-width: 860px; margin: 0 auto; padding: 2rem 1.2rem 3rem; }
h1 { font-size: 2rem; margin: .2rem 0 .3rem; }
h2 { margin-top: 2rem; }
a { color: var(--accent); }
.lede { font-size: 1.1rem; color: var(--muted); }
.tag { display:inline-block; background:var(--soft); border-radius:999px;
  padding:.15rem .7rem; font-size:.8rem; margin:.15rem .3rem .15rem 0; color:var(--muted); }
.grid { display:grid; gap:1rem; grid-template-columns:repeat(auto-fill,minmax(240px,1fr)); margin-top:1.2rem; }
.card { background:var(--card); border:1px solid var(--soft); border-radius:14px;
  padding:1.1rem; text-decoration:none; color:inherit; display:block; transition:transform .1s; }
.card:hover { transform: translateY(-3px); }
.card h3 { margin:.1rem 0 .3rem; }
.samples { display:grid; gap:.8rem; grid-template-columns:repeat(auto-fill,minmax(180px,1fr)); margin-top:1rem; }
.samples img { width:100%; height:auto; border-radius:10px; border:1px solid var(--soft); }
.empty { background:var(--card); border:1px dashed var(--soft); border-radius:14px;
  padding:1.4rem 1.6rem; margin-top:1rem; color:var(--muted); }
.warn { background:#2a1d1d; border:1px solid #5a2d2d; border-radius:12px;
  padding:.9rem 1.1rem; margin:1.2rem 0; font-size:.9rem; color:#f0c8c8; }
.back { display:inline-block; margin:1rem 0; }
footer { margin-top:2.5rem; padding-top:1rem; border-top:1px solid var(--soft); font-size:.85rem; color:var(--muted); }
"""


# ---------- build ----------

def sample_dir_rel(data: dict) -> str:
    """Path (relative to dist/) where sample files live. Samples sit at
    candidates/photo-packs/samples; dist/ is candidates/photo-packs/site/dist,
    so previews are two levels up."""
    return "../../samples"


def main() -> None:
    data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    packs = data.get("packs", [])
    DIST.mkdir(exist_ok=True)
    (DIST / "style.css").write_text(CSS, encoding="utf-8")
    samples_root = sample_dir_rel(data)

    # index / landing
    def card_html(p: dict) -> str:
        n = len(p.get("samples", []) or [])
        state = f'{n} preview(s)' if n else 'samples coming'
        return (
            f'<a class="card" href="{html.escape(p["id"])}.html">'
            f'<h3>{html.escape(p.get("title", p["id"]))}</h3>'
            f'<div class="tag">{html.escape(p.get("theme",""))}</div>'
            f'<div class="tag">{html.escape(state)}</div>'
            f'<p>{html.escape(p.get("description",""))}</p></a>'
        )

    cards = "".join(card_html(p) for p in packs)
    index_body = f"""
<h1>{html.escape(data.get("brand","photo-packs"))}</h1>
<p class="lede">{html.escape(data.get("tagline",""))}</p>
<div class="warn">Previews only. Every image shown here is a downsized, watermarked
preview (&le;2048px). Full-resolution wallpapers ship only from the storefront.</div>
<div class="grid">{cards}</div>
"""
    (DIST / "index.html").write_text(page(data.get("brand", "photo-packs"), index_body),
                                     encoding="utf-8")

    # per-pack pages
    for p in packs:
        samples = p.get("samples", []) or []
        if samples:
            imgs = "".join(
                f'<img src="{samples_root}/{html.escape(s)}" '
                f'alt="{html.escape(p.get("title", p["id"]))} preview" loading="lazy">'
                for s in samples if isinstance(s, str)
            )
            gallery = f'<div class="samples">{imgs}</div>'
        else:
            gallery = ('<div class="empty">No previews committed yet. Watermarked '
                       '&le;2048px previews will appear here once the owner adds them '
                       'under <code>samples/</code> and lists them in '
                       '<code>packs.json</code>.</div>')
        tiers = ", ".join(html.escape(t) for t in p.get("tiers", []) or [])
        price = p.get("price_usd")
        price_line = f'<div class="tag">~${html.escape(str(price))}</div>' if price else ""
        body = f"""
<p><a class="back" href="index.html">&larr; all packs</a></p>
<h1>{html.escape(p.get("title", p["id"]))}</h1>
<div class="tag">{html.escape(p.get("theme",""))}</div>{price_line}
<p class="lede">{html.escape(p.get("description",""))}</p>
<p>Sold tiers: {tiers or "(see storefront)"}.</p>
{gallery}
"""
        (DIST / f'{p["id"]}.html').write_text(page(p.get("title", p["id"]), body),
                                              encoding="utf-8")

    print(f"Built {len(packs)} pack pages -> {DIST}")
    print("Pages: index.html, " + ", ".join(f'{p["id"]}.html' for p in packs))


if __name__ == "__main__":
    main()

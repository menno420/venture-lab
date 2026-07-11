#!/usr/bin/env python3
"""Bababoefoe static-site builder — STDLIB ONLY (no jinja, no external deps).

Reads `editions.json` + the story markdown files and generates, into `dist/`:
  - index.html            landing page
  - collection.html       registry page: every edition, with links + keepsake
  - <slug>.html           one page per edition (its origin story = the QR target)
  - style.css             shared stylesheet
  - qr codes:
      * if `segno` OR `qrcode` is importable -> an SVG QR per edition (dist/qr/<slug>.svg),
        pointing at that edition's Pages URL, referenced on each edition page.
      * otherwise -> `dist/qr-urls.txt` (slug -> full URL). Zero-cost owner/local
        step to render QR images later: `pip install segno` (pure-python, MIT),
        then re-run this script. segno is NOT a repo dependency.

Run:  python3 build.py        (from candidates/bababoefoe/site/)
Output is self-contained in dist/ and opens directly in a browser (file://) or on
GitHub Pages at the base_url recorded in editions.json.
"""
from __future__ import annotations

import html
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
DIST = HERE / "dist"
REGISTRY = HERE / "editions.json"


# ---------- tiny markdown -> HTML (stdlib only) ----------

def _inline(text: str) -> str:
    """Escape, then apply bold/italic. Order matters: escape first."""
    text = html.escape(text, quote=False)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\*(.+?)\*", r"<em>\1</em>", text)
    return text


def md_to_html(md: str) -> str:
    """Minimal converter: #/## headings, --- rules, blank-line paragraphs."""
    out: list[str] = []
    para: list[str] = []

    def flush() -> None:
        if para:
            out.append("<p>" + _inline(" ".join(para)) + "</p>")
            para.clear()

    for raw in md.splitlines():
        line = raw.rstrip()
        if not line.strip():
            flush()
            continue
        if line.strip() == "---":
            flush()
            out.append("<hr>")
            continue
        m = re.match(r"^(#{1,4})\s+(.*)$", line)
        if m:
            flush()
            level = len(m.group(1))
            out.append(f"<h{level}>{_inline(m.group(2))}</h{level}>")
            continue
        para.append(line.strip())
    flush()
    return "\n".join(out)


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
<footer><a href="index.html">Bababoefoe</a> &middot; every edition carries its own story.</footer>
</div>
</body>
</html>
"""


CSS = """
:root { --bg:#fbf7f2; --card:#fff; --ink:#3a2f2a; --accent:#e08a52; --soft:#f0e6da; }
* { box-sizing: border-box; }
body { margin:0; font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  background: var(--bg); color: var(--ink); line-height: 1.6; }
.wrap { max-width: 720px; margin: 0 auto; padding: 2rem 1.2rem 3rem; }
h1 { font-size: 2rem; margin: .2rem 0 .3rem; }
h2 { margin-top: 2rem; }
a { color: var(--accent); }
.tag { display:inline-block; background:var(--soft); border-radius:999px;
  padding:.15rem .7rem; font-size:.8rem; margin:.15rem .3rem .15rem 0; }
.grid { display:grid; gap:1rem; grid-template-columns:repeat(auto-fill,minmax(220px,1fr)); margin-top:1.2rem; }
.card { background:var(--card); border:1px solid var(--soft); border-radius:14px;
  padding:1.1rem; text-decoration:none; color:inherit; display:block; transition:transform .1s; }
.card:hover { transform: translateY(-3px); }
.card h3 { margin:.1rem 0 .3rem; }
.swatch { display:inline-block; width:.9rem; height:.9rem; border-radius:50%; vertical-align:middle; margin-right:.4rem; border:1px solid rgba(0,0,0,.1); }
.story { background:var(--card); border:1px solid var(--soft); border-radius:14px; padding:1.4rem 1.6rem; margin-top:1rem; }
.story hr { border:none; border-top:1px dashed var(--soft); margin:1.4rem 0; }
.qr { margin-top:1.2rem; }
.qr img { width:150px; height:150px; image-rendering:pixelated; }
.back { display:inline-block; margin-top:1.2rem; }
footer { margin-top:2.5rem; padding-top:1rem; border-top:1px solid var(--soft); font-size:.85rem; opacity:.75; }
.lede { font-size:1.1rem; }
table { width:100%; border-collapse:collapse; margin-top:1rem; background:var(--card); border-radius:12px; overflow:hidden; }
th, td { text-align:left; padding:.6rem .7rem; border-bottom:1px solid var(--soft); font-size:.92rem; }
th { background:var(--soft); }
.color-teal{background:#3fb8b0}.color-orange{background:#e8863a}.color-pink{background:#e88fb0}
.color-green{background:#7bbf6a}.color-blue{background:#5a8fd6}.color-yellow{background:#e8cf4a}
.color-purple{background:#9b7bc8}.color-brown{background:#a9744f}
"""


def swatch(colorway: str) -> str:
    return f'<span class="swatch color-{html.escape(colorway)}"></span>'


# ---------- QR handling ----------

def qr_backend():
    """Return (name, module) for the first available QR lib, else (None, None)."""
    for name in ("segno", "qrcode"):
        try:
            mod = __import__(name)
            return name, mod
        except ImportError:
            continue
    return None, None


def make_qr_svg(name: str, mod, url: str, out: Path) -> None:
    if name == "segno":
        mod.make(url, error="m").save(str(out), scale=4)
    else:  # qrcode
        import qrcode.image.svg as svg  # type: ignore
        img = mod.make(url, image_factory=svg.SvgImage)
        img.save(str(out))


# ---------- build ----------

def main() -> None:
    data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    editions = data["editions"]
    DIST.mkdir(exist_ok=True)
    (DIST / "style.css").write_text(CSS, encoding="utf-8")

    qr_name, qr_mod = qr_backend()
    qr_dir = DIST / "qr"
    if qr_name:
        qr_dir.mkdir(exist_ok=True)
        print(f"QR: using '{qr_name}' -> SVG per edition in dist/qr/")
    else:
        print("QR: no segno/qrcode installed -> writing dist/qr-urls.txt (url manifest)")

    # index / landing
    def card_html(e: dict) -> str:
        seasonal = '<div class="tag">seasonal</div>' if e.get("seasonal") else ""
        return (
            f'<a class="card" href="{html.escape(e["slug"])}.html">'
            f'<h3>{swatch(e["colorway"])}{html.escape(e["name"])}</h3>'
            f'<div class="tag">{html.escape(e["colorway"])}</div>{seasonal}'
            f'<p>Carries {html.escape(e["keepsake"])}.</p></a>'
        )

    cards = "".join(card_html(e) for e in editions)
    index_body = f"""
<h1>Bababoefoe</h1>
<p class="lede">{html.escape(data.get("tagline",""))}</p>
<p>Round, ultra-fluffy little critters that hold hands in a chain, hide a tiny
keepsake in a secret pocket, and carry their own story on a QR tag. Meet the family:</p>
<div class="grid">{cards}</div>
<p style="margin-top:1.5rem"><a href="collection.html">See the full collection &rarr;</a></p>
"""
    (DIST / "index.html").write_text(page("Bababoefoe", index_body), encoding="utf-8")

    # per-edition story pages
    url_lines: list[str] = []
    for e in editions:
        story_md = (HERE / e["story"]).read_text(encoding="utf-8")
        story_html = md_to_html(story_md)
        url_lines.append(f'{e["slug"]}\t{e["url"]}')

        qr_block = ""
        if qr_name:
            out = qr_dir / f'{e["slug"]}.svg'
            make_qr_svg(qr_name, qr_mod, e["url"], out)
            qr_block = (
                f'<div class="qr"><p>Scan this edition&rsquo;s tag:</p>'
                f'<img src="qr/{html.escape(e["slug"])}.svg" alt="QR code for {html.escape(e["name"])}"></div>'
            )

        body = f"""
<p><a class="back" href="index.html">&larr; all editions</a></p>
<div class="story">
{story_html}
</div>
<p style="margin-top:1rem">{swatch(e["colorway"])}<strong>{html.escape(e["name"])}</strong>
&middot; colorway: {html.escape(e["colorway"])}
&middot; keepsake: {html.escape(e["keepsake"])}</p>
{qr_block}
"""
        (DIST / f'{e["slug"]}.html').write_text(page(e["name"], body), encoding="utf-8")

    # collection / registry page
    rows = "".join(
        f"<tr><td>{html.escape(e['id'])}</td>"
        f"<td><a href='{html.escape(e['slug'])}.html'>{swatch(e['colorway'])}{html.escape(e['name'])}</a></td>"
        f"<td>{html.escape(e['colorway'])}</td>"
        f"<td>{'seasonal' if e.get('seasonal') else 'core'}</td>"
        f"<td>{html.escape(e['keepsake'])}</td></tr>"
        for e in editions
    )
    coll_body = f"""
<p><a class="back" href="index.html">&larr; home</a></p>
<h1>The Collection</h1>
<p>Every Bababoefoe edition in the registry. Each row's QR tag opens that
edition's story page. This mirrors <code>editions.json</code> — the source of
truth physical tags are printed from.</p>
<table>
<thead><tr><th>ID</th><th>Edition</th><th>Colorway</th><th>Type</th><th>Pocket keepsake</th></tr></thead>
<tbody>{rows}</tbody>
</table>
"""
    (DIST / "collection.html").write_text(page("The Collection — Bababoefoe", coll_body), encoding="utf-8")

    # QR url manifest (always written; the printable source for tags even when SVGs also exist)
    manifest = "# slug<TAB>url — Bababoefoe QR targets (source of truth for printed tags)\n" + "\n".join(url_lines) + "\n"
    (DIST / "qr-urls.txt").write_text(manifest, encoding="utf-8")

    print(f"Built {len(editions)} editions -> {DIST}")
    print("Pages: index.html, collection.html, " + ", ".join(f'{e["slug"]}.html' for e in editions))


if __name__ == "__main__":
    main()

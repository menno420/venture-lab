#!/usr/bin/env python3
"""Build the Agent Fleet Field Manual into a single self-contained HTML file.

Stdlib only — no pip, no external CSS/JS/fonts/CDN. Reads chapters/*.md in
sorted order, converts each with a small purpose-built Markdown subset
converter (headings, paragraphs, bold, italic, inline code, fenced code
blocks, unordered/ordered lists, links, horizontal rules), auto-generates a
table of contents with anchor links, and marks the two FREE chapters with a
badge in both the TOC and the chapter header.

Output: dist/agent-fleet-field-manual-v0.1.html

Deliberately NOT a full CommonMark implementation — it handles exactly the
Markdown these chapters use. Keep the chapters within that subset.
"""
from __future__ import annotations

import html
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
CHAPTERS_DIR = HERE / "chapters"
DIST_DIR = HERE / "dist"
OUT_PATH = DIST_DIR / "agent-fleet-field-manual-v0.1.html"

FREE_MARKER = "**FREE CHAPTER**"

_CODE_SPAN = re.compile(r"`([^`]+)`")
_LINK = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
_BOLD = re.compile(r"\*\*([^*]+)\*\*")
_ITALIC = re.compile(r"(?<!\*)\*(?!\*)([^*]+?)\*(?!\*)")
_HEADING = re.compile(r"^(#{1,6})\s+(.*)$")
_ULIST = re.compile(r"^[-*]\s+(.*)$")
_OLIST = re.compile(r"^\d+\.\s+(.*)$")


def render_inline(text: str) -> str:
    """Convert inline Markdown to HTML on already-line-level text.

    Order matters: escape HTML, protect inline-code spans as placeholders so
    their contents are never re-processed, then links, bold, italic, then
    restore the code spans.
    """
    escaped = html.escape(text, quote=False)

    spans: list[str] = []

    def _stash(m: re.Match) -> str:
        spans.append(m.group(1))
        return f"\x00{len(spans) - 1}\x00"

    escaped = _CODE_SPAN.sub(_stash, escaped)
    escaped = _LINK.sub(
        lambda m: f'<a href="{html.escape(m.group(2), quote=True)}">{m.group(1)}</a>',
        escaped,
    )
    escaped = _BOLD.sub(r"<strong>\1</strong>", escaped)
    escaped = _ITALIC.sub(r"<em>\1</em>", escaped)

    def _restore(m: re.Match) -> str:
        idx = int(m.group(1))
        return f"<code>{spans[idx]}</code>"

    escaped = re.sub(r"\x00(\d+)\x00", _restore, escaped)
    return escaped


def md_to_html(md: str) -> str:
    """Convert a Markdown-subset document body to an HTML fragment."""
    lines = md.split("\n")
    out: list[str] = []
    i = 0
    n = len(lines)

    para: list[str] = []
    list_stack: str | None = None  # "ul" or "ol" when inside a list

    def flush_para() -> None:
        if para:
            joined = " ".join(s.strip() for s in para)
            # The header already renders a FREE badge for free chapters, so the
            # in-text marker line is suppressed to avoid a doubled badge.
            if joined.strip() != FREE_MARKER:
                out.append(f"<p>{render_inline(joined)}</p>")
            para.clear()

    def close_list() -> None:
        nonlocal list_stack
        if list_stack:
            out.append(f"</{list_stack}>")
            list_stack = None

    while i < n:
        line = lines[i]

        # Fenced code block: verbatim until the closing fence.
        if line.lstrip().startswith("```"):
            flush_para()
            close_list()
            code: list[str] = []
            i += 1
            while i < n and not lines[i].lstrip().startswith("```"):
                code.append(lines[i])
                i += 1
            i += 1  # consume closing fence
            body = html.escape("\n".join(code), quote=False)
            out.append(f"<pre><code>{body}</code></pre>")
            continue

        stripped = line.strip()

        if not stripped:
            flush_para()
            close_list()
            i += 1
            continue

        if stripped == "---":
            flush_para()
            close_list()
            out.append("<hr>")
            i += 1
            continue

        m = _HEADING.match(line)
        if m:
            flush_para()
            close_list()
            level = len(m.group(1))
            out.append(f"<h{level}>{render_inline(m.group(2).strip())}</h{level}>")
            i += 1
            continue

        mu = _ULIST.match(stripped)
        mo = _OLIST.match(stripped)
        if mu or mo:
            flush_para()
            want = "ul" if mu else "ol"
            if list_stack and list_stack != want:
                close_list()
            if not list_stack:
                out.append(f"<{want}>")
                list_stack = want
            item = (mu or mo).group(1)
            out.append(f"<li>{render_inline(item)}</li>")
            i += 1
            continue

        # Plain paragraph text.
        close_list()
        para.append(line)
        i += 1

    flush_para()
    close_list()
    return "\n".join(out)


def chapter_id(path: Path) -> str:
    m = re.match(r"(\d+)", path.stem)
    return f"ch-{m.group(1)}" if m else f"ch-{path.stem}"


def chapter_title(md: str, fallback: str) -> str:
    for line in md.split("\n"):
        m = _HEADING.match(line)
        if m and len(m.group(1)) == 1:
            return m.group(2).strip()
    return fallback


def is_free(md: str) -> bool:
    return FREE_MARKER in md


CSS = """
:root { color-scheme: light dark; }
* { box-sizing: border-box; }
body {
  margin: 0;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  line-height: 1.65;
  color: #1a1a1a;
  background: #fdfdfc;
}
.wrap { max-width: 46rem; margin: 0 auto; padding: 3rem 1.25rem 6rem; }
h1, h2, h3 { line-height: 1.25; font-weight: 700; }
h1 { font-size: 2rem; margin: 2.5rem 0 1rem; }
h2 { font-size: 1.4rem; margin: 2.25rem 0 0.75rem; }
h3 { font-size: 1.1rem; margin: 1.75rem 0 0.5rem; }
p { margin: 0 0 1rem; }
a { color: #0b5fff; }
code {
  font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  font-size: 0.9em;
  background: rgba(120,120,120,0.14);
  padding: 0.1em 0.35em;
  border-radius: 4px;
}
pre {
  background: #f4f4f2;
  border: 1px solid rgba(0,0,0,0.08);
  border-radius: 8px;
  padding: 1rem;
  overflow-x: auto;
}
pre code { background: none; padding: 0; font-size: 0.85em; }
hr { border: none; border-top: 1px solid rgba(0,0,0,0.12); margin: 2.5rem 0; }
ul, ol { margin: 0 0 1rem; padding-left: 1.5rem; }
li { margin: 0.35rem 0; }
.free-badge {
  display: inline-block;
  background: #1a7f37;
  color: #fff;
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  padding: 0.2rem 0.6rem;
  border-radius: 999px;
  margin: 0 0 1rem;
}
.book-title { font-size: 2.4rem; margin-bottom: 0.25rem; }
.book-sub { color: #666; margin-bottom: 2rem; }
.toc { background: rgba(120,120,120,0.07); border-radius: 10px; padding: 1.25rem 1.5rem; margin: 2rem 0 3rem; }
.toc h2 { margin-top: 0; }
.toc ol { list-style: none; padding-left: 0; }
.toc li { margin: 0.5rem 0; }
.toc a { text-decoration: none; }
.toc a:hover { text-decoration: underline; }
.toc .free-pill {
  display: inline-block; background: #1a7f37; color: #fff; font-size: 0.62rem;
  font-weight: 700; letter-spacing: 0.05em; text-transform: uppercase;
  padding: 0.05rem 0.4rem; border-radius: 999px; margin-left: 0.5rem; vertical-align: middle;
}
.chapter { border-top: 1px solid rgba(0,0,0,0.08); padding-top: 1rem; }
.chapter:first-of-type { border-top: none; }
.backlink { font-size: 0.8rem; }
footer { margin-top: 4rem; color: #777; font-size: 0.85rem; border-top: 1px solid rgba(0,0,0,0.1); padding-top: 1.5rem; }
@media (prefers-color-scheme: dark) {
  body { color: #e6e6e6; background: #16171a; }
  a { color: #6ea8ff; }
  pre { background: #1e1f23; border-color: rgba(255,255,255,0.1); }
  hr, .chapter { border-color: rgba(255,255,255,0.12); }
  .book-sub { color: #9aa0a6; }
  footer { color: #9aa0a6; border-color: rgba(255,255,255,0.12); }
}
"""


def build() -> Path:
    files = sorted(CHAPTERS_DIR.glob("*.md"))
    if not files:
        print("build: no chapters found", file=sys.stderr)
        raise SystemExit(1)

    chapters = []
    for path in files:
        md = path.read_text(encoding="utf-8")
        chapters.append(
            {
                "id": chapter_id(path),
                "title": chapter_title(md, path.stem),
                "free": is_free(md),
                "html": md_to_html(md),
            }
        )

    toc_items = []
    for ch in chapters:
        pill = '<span class="free-pill">Free</span>' if ch["free"] else ""
        toc_items.append(
            f'<li><a href="#{ch["id"]}">{html.escape(ch["title"], quote=False)}</a>{pill}</li>'
        )
    toc = "<ol>\n" + "\n".join(toc_items) + "\n</ol>"

    body_parts = []
    for ch in chapters:
        badge = '<div class="free-badge">Free chapter</div>' if ch["free"] else ""
        body_parts.append(
            f'<section class="chapter" id="{ch["id"]}">\n{badge}\n{ch["html"]}\n'
            f'<p class="backlink"><a href="#top">↑ Back to contents</a></p>\n</section>'
        )
    body = "\n\n".join(body_parts)

    doc = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Agent Fleet Field Manual v0.1</title>
<style>{CSS}</style>
</head>
<body>
<div class="wrap" id="top">
<h1 class="book-title">Agent Fleet Field Manual</h1>
<p class="book-sub">v0.1 — operating lessons for autonomous coding-agent fleets, each cited to a real repository artifact. Two chapters are free.</p>
<nav class="toc">
<h2>Contents</h2>
{toc}
</nav>
{body}
<footer>
Agent Fleet Field Manual v0.1 — $39 one-time. Conservative first-90-day: 0–4 sales ($0–$156). Zero distribution = $0.
Built from stdlib only; no external assets. Every lesson is cited to a real repository artifact.
</footer>
</div>
</body>
</html>
"""

    DIST_DIR.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(doc, encoding="utf-8")
    return OUT_PATH


if __name__ == "__main__":
    out = build()
    print(f"built: {out}")

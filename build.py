#!/usr/bin/env python3
"""Build the Windows 11 Built-In AI guide into a static HTML site.

Usage:
    python3 build.py           # render docs/*.md (+ README.md) into site/
    python3 build.py --check   # build, then verify pages, links, credits

No third-party dependencies. Requires Python 3.8+.
"""

import html
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DOCS = ROOT / "docs"
SITE = ROOT / "site"
ASSETS = SITE / "assets"

# Ordered chapter list: filename -> (nav label, short title for headers)
CHAPTERS = [
    ("index.html", "Home"),
    ("00-start-here.html", "Start Here"),
    ("01-copilot-chat.html", "Copilot Chat"),
    ("02-copilot-settings-and-privacy.html", "Copilot Settings & Privacy"),
    ("03-photos-ai.html", "Photos AI"),
    ("04-paint-ai.html", "Paint AI"),
    ("05-recall-and-privacy.html", "Recall & Privacy"),
    ("06-cloud-backup-and-auto-send.html", "Cloud & Auto-Send"),
    ("07-uncheck-checklist.html", "Uncheck Checklist"),
    ("08-troubleshooting.html", "Troubleshooting"),
]

CREDIT = "Copyright (c) 2026 Asdale Dynamics, LLC · Asdale Dynamics, LLC"
TAGLINE = "Windows 11's built-in AI, explained like a friend would."

CSS = """:root {
  --ink: #1f2430; --muted: #5c6472; --paper: #fbfaf7; --card: #ffffff;
  --accent: #2c6e63; --accent-2: #24534b; --line: #e3ddd2; --hi: #eef4f1;
}
* { box-sizing: border-box; }
body {
  margin: 0; background: var(--paper); color: var(--ink);
  font-family: Georgia, 'Times New Roman', serif; line-height: 1.7;
}
.layout { display: flex; max-width: 1100px; margin: 0 auto; min-height: 100vh; }
nav.toc {
  width: 250px; flex: none; padding: 2rem 1rem; border-right: 1px solid var(--line);
  font-family: 'Segoe UI', system-ui, -apple-system, sans-serif; font-size: 0.92rem;
}
@media (max-width: 800px) {
  .layout { display: block; }
  nav.toc { width: auto; border-right: 0; border-bottom: 1px solid var(--line); }
}
nav.toc .brand { font-weight: 700; color: var(--accent); margin-bottom: 0.25rem; }
nav.toc .brandline { color: var(--muted); font-size: 0.8rem; margin-bottom: 1.2rem; }
nav.toc ol { margin: 0; padding: 0; list-style: none; }
nav.toc li { margin: 0; }
nav.toc li a {
  display: block; padding: 0.4rem 0.6rem; border-radius: 6px; color: var(--ink);
  text-decoration: none;
}
nav.toc li a:hover { background: var(--hi); }
nav.toc li a.active { background: var(--accent); color: #fff; }
main { flex: 1; padding: 2.5rem 3rem 3rem; max-width: 800px; }
@media (max-width: 800px) { main { padding: 1.5rem 1.25rem 2.5rem; } }
h1, h2, h3 { font-family: 'Segoe UI', system-ui, -apple-system, sans-serif; line-height: 1.25; }
h1 { font-size: 1.9rem; color: var(--accent-2); margin: 0 0 1rem; }
h2 { font-size: 1.25rem; color: var(--accent-2); margin-top: 2.2rem; }
h3 { font-size: 1.05rem; margin-top: 1.6rem; }
p, li { font-size: 1.03rem; }
a { color: var(--accent); }
code {
  font-family: Consolas, 'Cascadia Mono', monospace; font-size: 0.9em;
  background: var(--hi); border: 1px solid var(--line);
  border-radius: 4px; padding: 0.1em 0.35em;
}
pre { background: var(--hi); border: 1px solid var(--line); border-radius: 8px;
  padding: 1rem; overflow-x: auto; white-space: pre-wrap; }
pre code { background: none; border: 0; padding: 0; }
blockquote {
  margin: 1.2rem 0; padding: 0.9rem 1.2rem; background: var(--card);
  border-left: 4px solid var(--accent); border-radius: 0 8px 8px 0;
  box-shadow: 0 1px 3px rgba(0,0,0,0.05);
}
blockquote p { margin: 0.3rem 0; }
table { border-collapse: collapse; width: 100%; margin: 1.2rem 0;
  font-family: 'Segoe UI', system-ui, sans-serif; font-size: 0.95rem; }
th, td { border: 1px solid var(--line); padding: 0.55rem 0.7rem;
  text-align: left; vertical-align: top; }
th { background: var(--hi); color: var(--accent-2); }
hr { border: 0; border-top: 1px solid var(--line); margin: 2.2rem 0; }
.pn { display: flex; justify-content: space-between; gap: 1rem; margin-top: 3rem;
  font-family: 'Segoe UI', system-ui, sans-serif; font-size: 0.95rem; }
.pn a { text-decoration: none; padding: 0.5rem 0.9rem; border: 1px solid var(--line);
  border-radius: 8px; background: var(--card); }
.pn a:hover { background: var(--hi); }
footer { margin-top: 3rem; padding-top: 1rem; border-top: 1px solid var(--line);
  color: var(--muted); font-size: 0.9rem;
  font-family: 'Segoe UI', system-ui, sans-serif; }
"""

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} · Windows 11's Built-In AI: A Plain-English Guide</title>
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
<div class="layout">
<nav class="toc">
<div class="brand">Windows 11's Built-In AI</div>
<div class="brandline">{tagline}</div>
<ol>
{nav}
</ol>
</nav>
<main>
{body}
<div class="pn">{prev}{next}</div>
<footer>
A guide by Asdale Dynamics, LLC · {credit}
<br>Educational content only — not medical, legal, or financial advice.
</footer>
</main>
</div>
</body>
</html>
"""


# --------------------------------------------------------------------------
# Inline rendering (bold / italic / code / links / backslash escapes)
# --------------------------------------------------------------------------

LINK_RE = re.compile(r"\[([^\]]*)\]\(([^)\s]+)\)")


def render_inline(text: str) -> str:
    out = []
    buf = []

    def flush():
        if buf:
            out.append(html.escape("".join(buf)))
            buf.clear()

    i, n = 0, len(text)
    while i < n:
        ch = text[i]
        if ch == "`":
            j = text.find("`", i + 1)
            if j != -1:
                flush()
                out.append("<code>%s</code>" % html.escape(text[i + 1:j]))
                i = j + 1
                continue
        if ch == "[":
            m = LINK_RE.match(text, i)
            if m:
                flush()
                out.append('<a href="%s">%s</a>' % (
                    html.escape(m.group(2), quote=True),
                    render_inline(m.group(1))))
                i = m.end()
                continue
        if ch == "*":
            if text[i:i + 2] == "**":
                j = text.find("**", i + 2)
                if j != -1:
                    flush()
                    out.append("<strong>%s</strong>" % render_inline(text[i + 2:j]))
                    i = j + 2
                    continue
            j = text.find("*", i + 1)
            if j != -1 and i + 1 < n and not text[i + 1].isspace() and text[i + 1] != "*":
                flush()
                out.append("<em>%s</em>" % render_inline(text[i + 1:j]))
                i = j + 1
                continue
        if ch == "_" and (i == 0 or not text[i - 1].isalnum()):
            j = text.find("_", i + 1)
            if j != -1 and i + 1 < n and not text[i + 1].isspace():
                flush()
                out.append("<em>%s</em>" % render_inline(text[i + 1:j]))
                i = j + 1
                continue
        if ch == "\\" and i + 1 < n and text[i + 1] in "*_`[]()-":
            buf.append(text[i + 1])
            i += 2
            continue
        buf.append(ch)
        i += 1
    flush()
    return "".join(out)


def slugify(text: str) -> str:
    text = re.sub(r"<[^>]+>", "", text).lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")
HR_RE = re.compile(r"^\s*(---+|\*\*\*+)\s*$")
UL_RE = re.compile(r"^(\s*)([-*+])\s+(.*)$")
OL_RE = re.compile(r"^(\s*)(\d+[.)])\s+(.*)$")
TABLE_SEP_RE = re.compile(r"^\s*\|?[\s:|\-]+\|?\s*$")
NON_PARA_PREFIXES = ("```", "#", ">", "|")


def is_marker(line):
    return bool(UL_RE.match(line) or OL_RE.match(line))


def render_markdown(src: str) -> str:
    lines = src.replace("\r\n", "\n").split("\n")
    out = []
    list_stack = []  # stack of 'ol'/'ul'

    def close_lists():
        while list_stack:
            out.append("</%s>" % list_stack.pop())

    def open_lists(tag, depth):
        while len(list_stack) < depth:
            list_stack.append(tag)
            out.append("<%s>" % tag)
        while len(list_stack) > depth:
            t = list_stack.pop()
            out.append("</%s>" % t)
        if list_stack and list_stack[-1] != tag:
            t = list_stack.pop()
            out.append("</%s>" % t)
            list_stack.append(tag)
            out.append("<%s>" % tag)

    def add_paragraph(parts):
        para = "<p>%s</p>" % render_inline(" ".join(x.strip() for x in parts))
        # lazy continuation of a list item: merge into previous <li>
        if out and out[-1].startswith("<li>") and out[-1].endswith("</li>"):
            out[-1] = out[-1][:-5] + " " + para[3:-4] + "</li>"
        else:
            close_lists()
            out.append(para)

    i = 0
    while i < len(lines):
        line = lines[i]

        if line.startswith("```"):
            close_lists()
            lang = line[3:].strip()
            code_lines = []
            i += 1
            while i < len(lines) and not lines[i].startswith("```"):
                code_lines.append(lines[i])
                i += 1
            i += 1
            cls = ' class="language-%s"' % html.escape(lang) if lang else ""
            out.append("<pre><code%s>%s</code></pre>"
                       % (cls, html.escape("\n".join(code_lines))))
            continue

        m = HEADING_RE.match(line)
        if m:
            close_lists()
            level, text = len(m.group(1)), m.group(2).strip()
            idattr = ' id="%s"' % slugify(text) if level <= 3 else ""
            out.append("<h%d%s>%s</h%d>"
                       % (level, idattr, render_inline(text), level))
            i += 1
            continue

        if HR_RE.match(line):
            close_lists()
            out.append("<hr>")
            i += 1
            continue

        if "|" in line and i + 1 < len(lines) and TABLE_SEP_RE.match(lines[i + 1]):
            close_lists()
            header = [c.strip() for c in line.strip().strip("|").split("|")]
            rows = []
            i += 2
            while i < len(lines) and "|" in lines[i] and lines[i].strip():
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            ths = "".join("<th>%s</th>" % render_inline(c) for c in header)
            trs = "".join(
                "<tr>%s</tr>" % "".join("<td>%s</td>" % render_inline(c) for c in r)
                for r in rows)
            out.append("<table><thead><tr>%s</tr></thead><tbody>%s</tbody></table>"
                       % (ths, trs))
            continue

        if line.startswith(">"):
            close_lists()
            paras, cur = [], []
            while i < len(lines) and lines[i].startswith(">"):
                q = lines[i][1:].lstrip(" ")
                if q.strip():
                    cur.append(q)
                elif cur:
                    paras.append(cur)
                    cur = []
                i += 1
            if cur:
                paras.append(cur)
            body = "".join("<p>%s</p>" % render_inline(" ".join(p)) for p in paras)
            out.append("<blockquote>%s</blockquote>" % body)
            continue

        om = OL_RE.match(line)
        um = UL_RE.match(line)
        if om:
            open_lists("ol", len(om.group(1)) // 2 + 1)
            out.append("<li>%s</li>" % render_inline(om.group(3).strip()))
            i += 1
            continue
        if um:
            open_lists("ul", len(um.group(1)) // 2 + 1)
            out.append("<li>%s</li>" % render_inline(um.group(3).strip()))
            i += 1
            continue

        if not line.strip():
            close_lists()
            i += 1
            continue

        # paragraph: absorb lines until blank line or a block start
        parts = [line]
        i += 1
        while i < len(lines):
            nxt = lines[i]
            if (not nxt.strip() or nxt.startswith(NON_PARA_PREFIXES)
                    or HR_RE.match(nxt) or is_marker(nxt)):
                break
            parts.append(nxt)
            i += 1
        add_paragraph(parts)

    close_lists()
    return "\n".join(out)


# --------------------------------------------------------------------------
# Site building
# --------------------------------------------------------------------------

# docs/ links in README/chapters become links to the generated pages
MD_LINK_RE = re.compile(r"\((docs/([0-9A-Za-z\-]+))\.md\)")


def map_links(src: str) -> str:
    return MD_LINK_RE.sub(lambda m: "(%s.html)" % m.group(2), src)


def source_pages():
    """Yield (output_name, title, raw_markdown)."""
    yields = []

    md_files = [Path("README.md").resolve()] + sorted(DOCS.glob("*.md"))
    for path in md_files:
        src = map_links(path.read_text(encoding="utf-8"))
        name = "index.html" if path.name == "README.md" else path.stem + ".html"
        title = None
        for line in src.replace("\r\n", "\n").split("\n"):
            if line.startswith("# "):
                title = line[2:].strip()
                break
        title = title or path.stem
        yield name, (title, src)


def build():
    if SITE.exists():
        shutil.rmtree(SITE)
    ASSETS.mkdir(parents=True)
    (ASSETS / "style.css").write_text(CSS, encoding="utf-8")

    rendered = {}
    for name, (title, src) in source_pages():
        rendered[name] = (title, render_markdown(src))

    for name, (title, body_html) in rendered.items():
        nav_rows = ['<li><a href="%s"%s>%s</a></li>'
                    % (target,
                       ' class="active"' if target == name else "",
                       label)
                    for target, label in CHAPTERS if target in rendered]
        idx = [t for t, _ in CHAPTERS].index(name)
        prev_html = next_html = ""
        if idx > 0:
            pt, pl = CHAPTERS[idx - 1]
            prev_html = '<a href="%s">&larr; %s</a>' % (pt, pl)
        if idx < len(CHAPTERS) - 1:
            nt, nl = CHAPTERS[idx + 1]
            next_html = '<a href="%s">%s &rarr;</a>' % (nt, nl)
        out = TEMPLATE.format(title=html.escape(title), tagline=TAGLINE,
                              nav="\n".join(nav_rows), body=body_html,
                              prev=prev_html, next=next_html,
                              credit=CREDIT)
        (SITE / name).write_text(out, encoding="utf-8")
    return rendered


# --------------------------------------------------------------------------
# Verification
# --------------------------------------------------------------------------

def check(rendered) -> int:
    errors = []
    print("Verifying built site…")

    for name in rendered:
        text = (SITE / name).read_text(encoding="utf-8")
        if CREDIT not in text:
            errors.append("%s: footer credit missing" % name)
        if '<link rel="stylesheet" href="assets/style.css">' not in text:
            errors.append("%s: stylesheet missing" % name)
        if not text.endswith("</html>\n") or "<title>" not in text:
            errors.append("%s: malformed HTML skeleton" % name)
        for tag in ("div", "main", "nav", "table", "ol", "ul", "p", "blockquote"):
            opens = len(re.findall(r"<%s[\s>]" % tag, text))
            closes = text.count("</%s>" % tag)
            if opens != closes:
                errors.append("%s: unbalanced <%s> (%d open vs %d close)"
                              % (name, tag, opens, closes))
        for href in re.findall(r'href="([^"]+)"', text):
            if href.startswith(("http://", "https://", "#", "mailto:", "me")):
                continue
            target = (SITE / href.split("#")[0]).resolve()
            if not target.exists():
                errors.append("%s: broken link -> %s" % (name, href))

    for target, _ in CHAPTERS:
        if target not in rendered:
            errors.append("required page missing: %s" % target)

    if errors:
        print("\nFAIL:")
        for e in errors:
            print("  -", e)
        return 1
    print("\nAll checks passed: %d pages; footer credit present; "
          "all internal links resolve; HTML tags balanced." % len(rendered))
    print(CREDIT)
    return 0


def main():
    rendered = build()
    print("Built %d pages into site/:" % len(rendered))
    for p in rendered:
        print("  site/" + p)
    if "--check" in sys.argv[1:]:
        sys.exit(check(rendered))


if __name__ == "__main__":
    main()

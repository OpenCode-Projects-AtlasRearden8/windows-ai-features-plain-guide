# STATUS.md

**Project:** windows-ai-features-plain-guide
**Built by:** Asdale Dynamics, LLC · "Explained like a friend would."
**Date finished:** 2026-11-06

## What was built

A substantive, plain-English walking guide to the AI already inside Windows 11:

- **docs/** — 9 Markdown chapters (the source of truth), each with numbered clicks,
  "What you'll see on your screen" descriptions in words (no screenshots on purpose),
  honest privacy notes, and "If it doesn't look right" fixes:
  - `00-start-here.md` — what built-in AI is, requirements, how to read the guide
  - `01-copilot-chat.md` — Copilot chat: front doors, first five minutes, everyday wins
  - `02-copilot-settings-and-privacy.md` — Copilot settings, auto-send-on-Enter,
    history deletion, Windows-level permissions, the Copilot key
  - `03-photos-ai.md` — Photos: background removal, object erase, Restyle, upscale;
    Snipping Tool text actions
  - `04-paint-ai.md` — Paint: Image Creator, Cocreator, Remover, and their privacy
    boundaries (cloud vs on-device)
  - `05-recall-and-privacy.md` — Recall: what it is, what it is not, off/on/filter/
    pause/delete, and a decision checklist
  - `06-cloud-backup-and-auto-send.md` — Windows Backup sync, OneDrive known-folder
    backup, Photos cloud gallery, Office AutoSave defaults
  - `07-uncheck-checklist.md` — the full consolidated "which box to uncheck" list,
    organized by Settings page (tables)
  - `08-troubleshooting.md` — eight common hiccups with calm fixes
- **build.py** — dependency-free (Python 3 stdlib only) Markdown → static HTML
  site generator: sidebar nav, prev/next chapter links, one shared stylesheet,
  footer credit on every page, and markdown source-link mapping (`docs/*.md` →
  generated pages) so the home page's chapter table works on both GitHub and the site.
- **site/** — the generated static site (10 pages + `assets/style.css`),
  committed so it can be opened or hosted directly without building.
- **README.md** — overview, what's inside, difference from the phone guide and the
  day-one setup guide, how to build/run, MIT + credit.
- **LICENSE** — MIT, copyright line exactly: `Copyright (c) 2026 Asdale Dynamics, LLC`

Guarantees honored: no registry editing anywhere in the guide; every step is
described in words; no screenshots required; no secrets, API keys, or personal data
in any file; Asdale Dynamics, LLC credited in README and on every page footer.

## How to run it

```bash
python3 build.py          # rebuild site/ from docs/ + README.md
python3 build.py --check  # build + verify pages, links, HTML balance, credits
python3 -m http.server --directory site 8000   # optional local preview
```

Or simply open `site/index.html` in any browser — the site is self-contained
(no JavaScript, no external requests).

## Verification results (all performed)

- `python3 build.py --check` — PASS: 10 pages built, footer credit present on all
  10, all internal links resolve, HTML tag balance verified (`div/main/nav/ol/ul/
  p/blockquote/table`).
- Local HTTP smoke test — `index`, `assets/style.css`, and chapter pages all
  HTTP 200 via `python3 -m http.server`.
- Content artifact scan — no unrendered Markdown markup, no stray backslash
  escapes, no unmapped `docs/*.md` links, no duplicate-word typos in docs/README.
- Inline renderer manually exercised for nested bold/italic (`**What is *not*
  true**`), list-item continuations, tables, fenced code, and blockquotes.

Bugs found and fixed during verification: lazy list continuations splitting into
paragraphs, an off-by-one in the `<li>` merge leaving stray `</p>` tags, README
`.md` links not mapping to HTML pages, and the checker verifying page names vs
labels. All fixed and re-verified green.

## Known gaps

- Content reflects Windows 11 as of writing (late 2026); Microsoft rearranges
  menus over time, so exact wording ("Send on Enter", "Show cloud gallery",
  Recall's filter rows) is deliberately hedged with "wording varies" phrasing.
  The `--check` only verifies the site's integrity, not Microsoft's UI.
- The guide covers Home/Pro/Copilot+ consumer paths; enterprise/MDM policies that
  can mark settings as managed (greyed out) are not covered.
- No screenshots by design; if the LLC later wants visual proof pages, that's an
  addition, not a change.
- The static site has no search box; browser Ctrl+F is the search mechanism.

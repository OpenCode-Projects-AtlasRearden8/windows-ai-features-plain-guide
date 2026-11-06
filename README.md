# Windows 11's Built-In AI: A Plain-English Walking Guide

**By Asdale Dynamics, LLC · "Explained like a friend would."**

A substantive, step-by-step manual for regular Windows 11 users who want to actually
use the AI that ships with Windows — Copilot chat, the AI features in the Photos and
Paint apps, and the newer, bigger privacy decisions (Recall, and the settings that
quietly send things to the cloud).

Everything here is:

- **Plain English.** No jargon left unexplained, no assumptions that you already know.
- **Step by step with words instead of screenshots.** Every step includes a short
  "What you'll see on your screen" description, so you can follow along even if your
  screen looks a little different than described.
- **Privacy-first.** This guide tells you honestly which features phone home, and gives
  you a plain checklist of exactly which boxes to uncheck (or turn off) if you'd rather
  keep things local.
- **No registry editing. Ever.** Nothing in this guide asks you to open the Registry
  Editor or run any command-line voodoo. Everything is buttons, toggles, and menus.

## How this is different from our other guides

- **New Windows computer, day one?** Use our *New Computer Setup Day Guide* first —
  that one walks you through unboxing and first-time setup.
- **Copilot on your *phone*?** That's our *AI on Your Phone Guide*.
- **This guide** covers the AI that is *already inside your Windows 11 PC* — the one
  on your laptop or desktop keyboard, in your Photos app, in your Paint app, and
  (if your PC is newer) in Recall.

If you've already set the computer up and you're just discovering "wait, there's AI
in here?" — you're in exactly the right place.

## What's inside

| Chapter | What it covers |
| --- | --- |
| [Start Here](docs/00-start-here.md) | What built-in AI is, what you need, how to use this guide |
| [Copilot Chat](docs/01-copilot-chat.md) | The Copilot side panel: asking questions, drafting, everyday wins |
| [Copilot Settings & Privacy](docs/02-copilot-settings-and-privacy.md) | Where Copilot sends your messages, and the settings worth changing |
| [AI in the Photos App](docs/03-photos-ai.md) | Erasing objects, Restyle Image, Copy Text, enhanced photos |
| [AI in the Paint App](docs/04-paint-ai.md) | Cocreator, generative fill, Image Creator basics |
| [Recall & Your Privacy Choices](docs/05-recall-and-privacy.md) | What Recall is, how to turn it off, filter apps, delete snapshots, pause it |
| [Cloud Backup & Auto-Send Settings](docs/06-cloud-backup-and-auto-send.md) | OneDrive auto-send, "Backup" vs. sync, what to keep local |
| [The Uncheck Checklist](docs/07-uncheck-checklist.md) | One printable list of every box this guide suggests unchecking |
| [If Something Goes Wrong](docs/08-troubleshooting.md) | Common hiccups and calm fixes |

## How to run this guide as a website

The manual lives as plain Markdown in `docs/`. A small, dependency-free Python script
turns it into a static HTML site in `site/`.

```bash
python3 build.py        # renders docs/*.md into site/*.html
# then open site/index.html in any browser, or:
python3 -m http.server --directory site 8000   # preview at http://localhost:8000
```

No Node, no npm install, no internet connection needed. The generated `site/` folder
is fully self-contained (one CSS file, plain URLs) and can be copied anywhere.

## Verification

Run the included check script — it rebuilds the site and verifies internal links,
required pages, and footer credits:

```bash
python3 build.py --check
```

## Credits

Written and maintained by **Asdale Dynamics, LLC** — the company behind
*The Massive AI Manual* and Dylan Asdale's plain-English AI guides. Educational
content only; never medical, legal, or financial advice.

Released under the MIT License (`LICENSE`). Copyright (c) 2026 Asdale Dynamics, LLC.

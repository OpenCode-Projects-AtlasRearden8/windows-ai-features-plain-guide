# Chapter 5 · Recall & Your Privacy Choices

*Time: 15 minutes to read, 5 minutes to configure · Difficulty: medium, high stakes, no registry*

This is the chapter to read slowly. **Recall** is the most privacy-meaningful AI
feature Windows has ever shipped: a background timeline of your screen activity that
AI-search indexes, so you can look back through "everything I saw on my computer
recently" like a DVR. For some people it's a life-changing tool. For others it
sounds scary-sounding. Both reactions come from the same place, and the good news is
that **you** get to decide — clearly, with toggles, no sysadmin degree required.

Here's how it fits together:

**What it actually is.** On specific new Windows 11 machines (the "Copilot+ PC" class
— newer laptops with a special Neural Processing Unit chip) your computer can take a
screenshot-like record of your screen every few seconds. Those records are called
*snapshots*. They are stored **on your PC**, encrypted with the kind of device
encryption that is already protecting your files, and opened only after proving
you're-you with Windows Hello (face, fingerprint, or PIN). You don't see this
timeline anywhere in normal use. To browse or search it, you open its dedicated app
timeline.

**What is *not* true**, worth saying out loud: snapshots do not float to Microsoft's
servers, do not ride along with OneDrive, and are not visible to apps. The
processing is local. Content that common filters recognize as sensitive (social
security numbers, financial card strings, and so on) is supposed to be filtered out
of the snapshots that get stored.

**The part that's actual up-to-you:** whether snapshots happen *at all*. This
feature is **opt-in** — the timeline stays off until you turn it on in Settings.
Microsoft ships it with the switch off; when you first use a Copilot+ machine, or
after major feature updates, a prompt lets you turn it on or decline. Plenty of
smart friends run with it declined; plenty of other smart friends are thrilled about
it. This chapter is a careful tour both ways.

## 5.1 · First: check whether your PC has Recall at all

**Step 1.** Press **Windows key + I** to open Settings. (Or **Start** > gear icon.)

**Step 2.** In the left rail, click **Privacy & security**.

**Step 3.** Scroll the middle list and look for **Recall & snapshots**. If you don't
see it anywhere in the list, your PC doesn't have Recall, and this chapter ends for
you feeling prematurely brief. Skip to Chapter 6 with peace of mind.

> **What you'll see** (for those with it): a page whose top section is titled
> something like **"Save snapshots"** with a single large toggle pill, and below it
> rows for filtering, deleting snapshots, and some informational text about
> encryption and Windows Hello. We'll walk through each row, top to bottom.

## 5.2 · Decide: "Do I want this?"

A friend-level decision tree, no judgment attached:

**Turn it ON if…** you often riffle through old browser tabs, PDFs, emails, chat
windows saying *"where was that thing I saw?"* Recall's search is genuinely
uncanny for that. Nurses, students, resale inventory people, and chronic 40-tab-open
folks *love* it, and for some ADHD friends it's the accessibility win of the decade.

**Turn it OFF if…** you don't want your screen recorded even on-device; if others
share your Windows account loosely (a PIN is technically a secret anyone can watch
being typed); if an employer policy, a court matter, a support group, or a household
privacy arrangement makes a screen timeline a bad idea. Then leave the toggle off
and move on with your life. Nothing else needed.

**Turn it ON then carefully filter it…** if you want the upside but with guardrails
— this is Section 5.3.

## 5.3 · Configure Recall with guardrails

With the **Save snapshots** toggle **on**, work down the rows on the same
**Recall & snapshots** Settings page:

**Row: "Filter apps" / "Exclude apps".** Add apps whose windows should never be
snapshotted — banking apps, password managers, medical-record software at home, VPN
apps, HR portals, messages with private groups (pick your own). Click **Add**, and
pick apps from the popup and confirm.

> **What you'll see:** a small Windows-standard "pick an app" style list of your
> installed apps with checkbox-style rows. Select apps (for example your browser, if
> even web browsing is off-limits) and click **Confirm**/**Save**. Names appear in a
> list below the row, each with a trash icon to remove it later.

**Row: "Filter websites".** Some builds let you filter by website or domain (for
example your bank's and benefits portals) — a text-field style row where you add
entries one per click. Add the ones you want permanently un-recorded in Recall.
Not every build has this (earlier versions filter apps; newer ones also do website
filtering). If it isn't there, the app-level filter is your lever.

**Row: "Words I don't want included" / "Sensitive information filtering".** If your
build shows it: a list where you add words or phrases (like a rare last name, a
project codename, a lease number) to block from snapshots when recognized as
sensitive — one row at a time. It is not perfect keyword filtering; treat it as
an extra layer, not the whole defense.

**Row: "Save activity" range / " Automatically delete after …".** You may see how
many days of snapshots are kept (30, 60, 90). Lower is fewer files to worry about;
most people are fine at the default.

## 5.4 · Pause and delete, whenever you feel like it

Two safety valves exist, and you should know both are within two clicks:

**Pause.** In the Recall app itself (or in the same Settings rows) there's a
**pause** control that stops recording while you do something sensitive, then let
you unpause. If you finish your overdue paperwork for ten minutes tomorrow, this is
how you undo worry legally. When you finish, unpause — nothing was lost.

**Delete.** On the **Recall & snapshots** settings page you'll find
**"Delete all snapshots"** (or **Delete snapshots** with a date range picker in
newer versions). Clicking it wipes every stored snapshot **immediately and
permanently**, before you can confirm in a small dialog.

> **What you'll see:** a confirmation dialog with the word **Delete** — the kind of
> button that actually means it. Afterward the space used clears; if you had
> snapshots spanning months, you'll notice timeline sizes reset.

Third valve worth knowing: **turn Recall off entirely** (the main *Save snapshots*
toggle off gains nothing — the timeline just stops being recorded). Existing
snapshots stay on disk until deleted, so when you turn off in Settings, the page
will guide you through deleting afterwards. Deleting is the real ending, not just
unchecking.

## 5.5 · The Recall checklist, if you turn it on

A calm pre-flight checklist from one friend to another. If any of these feel
under-considered, consider whether maybe it should stay turned off for you:

- [ ] I know where the OFF switch is (Privacy & security > Recall & snapshots > Save
      snapshots), and so does a housemate who might need to turn it off for me.
- [ ] My Windows account uses a strong Windows Hello PIN, not a shared password.
- [ ] I have Windows Hello device encryption working (Settings > Privacy &
      security > Device encryption should say it's on — it is on most Copilot+ PCs
      already).
- [ ] I have added my sensitive apps to **Filter apps**: banking, health, password
      manager, certain message apps.
- [ ] I know how to hit **Pause** for anything sensitive I need to handle.
- [ ] I know **Delete all snapshots** exists and is one click.
- [ ] Deciding who will see it: if my machine is used by anyone besides me with
      **their own** secure Windows account, Recall stays per-account (other users
      can't browse my snapshot timeline), but the machine itself now stores more
      history than it used to — worth telling them, honestly, even if they can't open it.

Keep Recall or skip it — either way, by the end of this chapter, you've *decided*,
you've *seen* how it works, and you can find every switch without help. That's all
this chapter was ever going to ask of you.

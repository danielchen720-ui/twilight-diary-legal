---
layout: default
title: Export and import your diary — Diary BFF help
description: How to export your Diary BFF diary to one file, protect it with a password, import it again, and move in from Day One or Apple Journal.
---

<!-- #2899 市场部 11-06：出处 = project-163rel 7f4985fe7 src/lib/strings.ts（settings.export* / move.*）。零脚本。 -->

# Export and import your diary

<!-- 支持回复模板 -->
**Short answer:** Go to **Settings → Export and import → Export backup**. You get one file with your entries, timestamps, your diary BFF's replies, Sunday letters and your chats. You can add a password. Export is free.

## What goes in the file

<!-- settings.exportIntro -->
Every entry — the writing, timestamps, your diary BFF's replies, Sunday letters and your chats — packed into one JSON file you keep. Use it to move to a new phone or to reinstall.

## Adding a password

<!-- settings.encryptPwdOptional「Password (optional)」· settings.encryptNote -->
The password is optional. With a password, only someone who knows it can open the file. Lose it and the backup can't be opened, so keep it somewhere you'll find it.

## Importing a backup

<!-- lock.importBackup「Import from a backup」· settings.importDiary「Import a diary」（SettingsScreen.tsx:2102 那一组） -->
On a new phone, choose **Import from a backup** when the app opens. On a phone that already has the diary, go to Settings and look under **Import a diary**.

## Moving in from Day One or Apple Journal

<!-- move.header「From another app」（SettingsScreen.tsx:2120，紧跟 Import a diary 组）· move.howDayOne · move.howJournal（逐字） -->
In Settings, under **From another app**:

- **Day One:** In Day One, open Settings, tap Export and choose JSON. Save the zip to Files, then choose it in Diary BFF.
- **Apple Journal:** In Journal, tap the More button and choose Export. On iOS 18, go to Settings, then Apps, Journal, Export All Journal Entries. Save the zip to Files, then choose it in Diary BFF. If it saved as a folder, long-press it in Files and choose Compress first.

<!-- move.footer / move.footerMulti：照片张数走 {max}，不写数字 -->
Your entries come over, with their photos up to the limit shown on that screen.

## Is export free?

<!-- /support/「Export is free, as often as you like」；CLAUDE.md §1 写作永远免费 -->
Yes, as often as you like.

---

Something didn't come over? Write to **hello@diarybff.app**. You don't need to send the file. · [All help](../) · [Diary BFF on the App Store](https://apps.apple.com/app/apple-store/id6811528172?pt=129391747&ct=help-export&mt=8)

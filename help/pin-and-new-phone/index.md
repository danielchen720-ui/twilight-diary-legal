---
layout: default
title: Forgot your PIN, or got a new phone — Diary BFF help
description: How to reset your Diary BFF PIN, bring your diary to a new phone, and open it again after reinstalling.
---

<!-- #2899 市场部 11-06：出处 = project-163rel 7f4985fe7（1.6.3 build 96）src/lib/strings.ts + supabase/functions/pin-recovery/index.ts；与 /support/ 同段逐句对过。零脚本。 -->

# Forgot your PIN, or got a new phone

<!-- 支持回复模板：下面「Short answer」整段可直接贴进回信 -->
**Short answer:** On the lock screen, tap **Forgot PIN**, then **Ask to reset the PIN**. Your entries are not lost. They stay locked, and after 10 days you can set a new PIN. If the diary is still open on another phone of yours, you can approve it there and skip the wait.

## I forgot my PIN

<!-- lock.forgotPin「Forgot PIN?」/ lock.forgotPasscode「Forgot PIN」（v7）· lock.resetAsk · pin-recovery RESET_WAIT_DAYS = 10 · lock.onlyYou -->
Tap **Forgot PIN** on the lock screen, then **Ask to reset the PIN**. Your entries stay locked while you wait, and after 10 days you can set a new PIN. The wait is on purpose. The diary has its own lock, separate from your phone's, and the lock screen says it plainly: "Only you can open this."

<!-- lock.resetPendingUnknown / lock.resetNotMeArmed（同 /support/） -->
If you didn't ask for a reset, open the diary with your PIN. You'll see the request and can cancel it.

## Skip the wait from another phone

<!-- lock.approveTitle「New phone waiting」/ lock.approveBody / lock.approveYes「It was me」 -->
If the diary is still open on another phone of yours, that phone shows **New phone waiting**. Tap **It was me** there, and the new phone opens right away.

## I want a different PIN

<!-- settings.passcode「PIN」· settings.changePasscode「Change PIN」；改 PIN 先验当前 PIN（CLAUDE.md §2） -->
If you remember your PIN, go to **Settings → PIN → Change PIN**. You'll enter the current PIN first.

## Bring your diary to a new phone

<!-- link.settingsRow「Keep it when you change phones」· lock.useAppleId「Use your Apple ID」 -->
On your old phone, go to **Settings → Keep it when you change phones** and connect your Apple ID. On the new phone, install Diary BFF, tap **Use your Apple ID**, and use the same Apple ID. Your entries come back. Enter the PIN from your old phone and it opens.

<!-- lock.fromOldPhoneForgot「I don't remember it」 -->
Don't remember that PIN? Tap **I don't remember it**. Your entries stay locked, and you can ask to reset the PIN as above.

<!-- lock.importBackup「Import from a backup」· settings.exportBackup -->
Didn't connect an Apple ID? Make a backup on the old phone first (see [Export and import](../export-and-import/)), move the file over, and choose **Import from a backup** on the new phone.

## I deleted the app and installed it again

<!-- 隐私页「Kept only on your phone」：Keychain 登录钥匙（同 /support/） -->
On the same phone, your account comes back. The app keeps a sign-in key in the iPhone's Keychain for this. For a different phone, use your Apple ID or a backup.

---

Still stuck? Write to **hello@diarybff.app** and tell us which iPhone and iOS version you have. · [All help](../) · [Diary BFF on the App Store](https://apps.apple.com/app/apple-store/id6811528172?pt=129391747&ct=help-pin&mt=8)

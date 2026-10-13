---
layout: default
title: Support — Diary BFF
description: Help with your PIN, a new phone, export, deleting your account, and subscriptions.
---

<!--
  #497（后端部 10-12 23:0x）：逐句对 App 现版（release/1.5.1 树 `src/lib/strings.ts` + `config/legal-urls.json` +
  `supabase/functions/pin-recovery/index.ts` + 本站隐私页）重写。每段上面那行注释 = 出处。
  原来那一版写着「PIN 找不回、重装就丢」—— 那是 1.0 的事，现在有 10 天重设、Apple ID 换机、旧手机批准。
  按总经理令不写：no one / never / encrypted / 治疗 / 医疗。
-->

# Support

_Last updated: 2026-10-13_

Something broken, confusing, or missing? Write to the person who makes Diary BFF:

<!-- config/legal-urls.json primary.contactEmail -->
**hello@diarybff.app**

A person reads every message. Tell us which iPhone and which iOS version you have. It usually saves a round trip.

## Your PIN

### I forgot my PIN.

<!-- strings.ts lock.forgotPin / lock.resetAsk / lock.onlyYou 3563；pin-recovery RESET_WAIT_DAYS = 10 -->
On the lock screen, tap **Forgot PIN?** and then **Ask to reset the PIN**. Your entries are not lost. They stay locked, and after 10 days you can set a new PIN. The wait is on purpose: the app says it on the lock screen, "Only you can open this. Forget your PIN and even you wait 10 days."

<!-- strings.ts lock.resetAnswerDays / lock.resetPendingUnknown / lock.resetNotMeArmed -->
If you didn't ask for a reset, open the app with your PIN. You'll see the request and can cancel it.

<!-- strings.ts settings.passcode / settings.changePasscode / settings.currentPasscode -->
If you remember your PIN and just want a different one, go to **Settings → PIN → Change PIN**.

### Is there a faster way?

<!-- strings.ts lock.approveTitle / lock.approveBody / lock.approveYes -->
If the diary is still open on another phone of yours, that phone shows **New phone waiting**. Tap **It was me** there, and the new phone can open right away instead of waiting 10 days.

## A new phone

### How do I bring my diary to a new phone?

<!-- strings.ts link.settingsRow / link.recoverBody / lock.useAppleId / lock.fromOldPhone；privacy「Account and identity」 -->
On your old phone, go to **Settings → Keep it when you change phones** and connect your Apple ID. On the new phone, install Diary BFF, tap **Use your Apple ID**, and use the same Apple ID. Your entries come back. Enter the PIN from your old phone and it opens right away.

<!-- strings.ts lock.fromOldPhoneForgot / lock.fromOldPhoneForgotWhy -->
Don't remember that PIN? Tap **I don't remember it**. Your entries stay locked, and you can ask to reset the PIN. The new phone opens in 10 days, or right away if you approve it from the old phone (see above).

<!-- strings.ts lock.importBackup / settings.exportBackup / settings.backupWarning -->
Didn't connect an Apple ID? Make a backup on the old phone (**Settings → Export and import → Export backup**, with a password), move the file over, and choose **Import from a backup** on the new phone.

### I deleted the app and installed it again on the same phone.

<!-- privacy「Kept only on your phone」：Keychain 里的登录钥匙 lets the app reopen your account if you delete and reinstall it -->
Your account comes back. The app keeps a sign-in key in the iPhone's Keychain for exactly this. That key stays on this phone. For a different phone, use your Apple ID or a backup (above).

## Your writing

### How do I get my writing out?

<!-- strings.ts settings.exportIntro 1610 / settings.backupPwd；backup.ts 读 companion_chat_messages（导出含聊天页，1.5 A② 363dc7fd 起） -->
**Settings → Export and import → Export backup.** You get one file you keep, with your entries, the timestamps, your diary BFF's replies, Sunday letters, and your chats. You can add a password to it. Export is free, as often as you like.

### Can I move in from Day One or Apple Journal?

<!-- strings.ts move.howDayOne / move.howJournal（1.5.1 起） -->
Yes. In Day One, open Settings, tap Export and choose JSON. In Journal, tap the More button and choose Export. Save the zip to Files, then in Diary BFF go to **Settings → Export and import** and choose it.

### Is writing free?

<!-- strings.ts paywall.freeForever 2130（Writing stays free；对外不说 forever） -->
Yes. Writing stays free. A subscription buys more replies and the full Sunday letter.

## Replies

### What gets sent when I ask for a reply?

<!-- strings.ts aiConsent.what / aiConsent.who / aiConsent.ifNot -->
Before the first reply, the app shows you what gets sent: that entry, plus short notes from earlier nights (with their dates), not your name. It goes to Anthropic, the company whose model writes back. They do not train on it. Say no and the diary works the same. It writes, saves, and locks. Your diary BFF just stays quiet.

### Can I turn the replies off?

<!-- strings.ts settings.aiReplies（「{Name} writes back」）/ settings.aiRepliesNote -->
Yes. In Settings, turn off the "writes back" switch next to your diary BFF's name, and nothing more is sent. The full detail is in the [privacy policy](../privacy/).

## Subscriptions and deleting

### How do I cancel a subscription?

<!-- strings.ts sub.trialHowToCancel 2412 / paywall.timelineStarts 2151 -->
Apple handles subscriptions. Open **iPhone Settings → your name → Subscriptions**, pick Diary BFF, and cancel. Cancel at least 24 hours before your plan renews and you won't be charged for the next period.

### How do I delete everything?

<!-- strings.ts settings.deleteAccount / settings.deleteAccountIntro 1885 / settings.exportFirstHint 1890 / settings.deletePermanently -->
**Settings → Delete account → Delete for good.** It erases your entries, letters, chats, photos, and the account, and it cannot be undone. Export a copy first if you want to keep any of it.

<!-- strings.ts 1906 -->
**Deleting your account does not cancel your subscription.** Cancel it separately in iPhone Settings → your name → Subscriptions, or you'll keep being charged.

## Reporting a problem

Tell us what you did, what you expected, and what happened instead. You don't need to send anything you wrote. A description is enough.

The privacy policy is [here](../privacy/).

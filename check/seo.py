#!/usr/bin/env python3
"""#2320 + #2341（+ #2454 第 5–6 篇 · #2487 第 9–10 篇）：SEO 文章挂站 + 免费渠道分账 ct。只读，本机没有 jekyll 也能跑（JS 那一格要 node）。

    python3 check/seo.py      → 退出 0 = 全对；1 = 哪一条不对印出来

核的是源，不是 build 出来的页（本机没有 jekyll）：
① 每篇各在 <篇名>/index.md，layout: article，ct = seo-<短篇名>（表在 PAGES；≤ 30 字符），title / description 都有、description ≤ 155 字符
② _layouts/article.html：每个 App Store 链接 ct 只读 page.ct（不给默认值）、带 pt；canonical 指本页；不带 noindex
③ 正文里没有自己写死的 App Store 链接（按钮只在 layout 里一处）、没有孤零零的 he / him / his（老板 10-08 he/she 规矩）、
   没有比 App 走得远的那几句（「Two to four sentences」= 提示词定的是 1–2 句最多 3；「neutral count … nothing else」=
   日记本上还有一句 `{n} nights in a row.`；`No streaks` = App 那边 paywallNoStreakClaim 明令不许这么扩写）
④ sitemap：_config.yml 开 jekyll-sitemap；/tiktok/ 是 noindex 的那一页，sitemap: false
⑥ #2414（总经理裁：同题两页互抢）：旧 /rosebud/（Q128 草稿）不再是一页，改成跳到 /rosebud-alternative/ ——
   GitHub Pages 发不了 HTTP 301，用 jekyll-redirect-from 的 redirect_from 出一张即时 meta refresh 页；
   Google 原句「Google Search interprets instant meta refresh redirects as permanent redirects」
   （https://developers.google.com/search/docs/crawling-indexing/301-redirects）。那张跳转页插件自己标 sitemap: false。
⑤ 首页（ct = site）带 ?ref= / ?utm_source= 进来 → 下载链接 ct 改成 dir-<站名>（只 [a-z0-9-]，ct ≤ 30 字符）；
   /tiktok/ 不改；没带参数不改。这一格把 home.html 里那段脚本原样拿出来在 node 里跑，喂假的 location / 链接
推完之后的那一半：`curl -fsSL https://diarybff.app/sitemap.xml | grep -c '<loc>'`、每篇各 `curl -fsSL … | grep -c 'ct=seo-'`（部署卡上那几格）。
"""
import json
import os
import re
import shutil
import subprocess
import sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
# 目录名（= 网址）→ 按钮 ct。ct 用短篇名不用目录名：Apple 的 campaign token 最多 30 个字符
# （https://developer.apple.com/help/app-store-connect/view-app-analytics/manage-campaigns 原句
# "You can use up to 30 alphanumeric characters"），seo-journal-app-that-replies-to-you 是 35。
PAGES = {
    "ai-diary-that-writes-back": "seo-writes-back",
    "journal-app-that-replies-to-you": "seo-replies",
    "private-diary-with-pin-lock": "seo-pin-lock",
    "rosebud-alternative": "seo-rosebud",
    # #2454（市场部 #2451 第 5–6 篇）：和第 4 篇分开讲 —— 第 4 篇讲「为什么锁要和手机分开」，
    # 这两篇一篇讲 PIN 本身、一篇讲「锁有三种」
    "diary-with-pin": "seo-pin",
    "journal-with-lock": "seo-lock",
    # #2487（市场部 #2478 第 9–10 篇）：第 9 篇是宽词 private diary app（五个问题，PIN 只占第 1 问，和第 3 篇不撞）；
    # 第 10 篇主词 diary app no account，但标题 / H1 只说 no sign-up（claims C26：底下有匿名 ID）
    "private-diary-app": "seo-private",
    "diary-app-no-account": "seo-noaccount",
}
CT_RE = re.compile(r"^[a-z0-9-]{1,30}$")
STALE = (
    (re.compile(r"two to four sentences", re.I), "「Two to four sentences」—— 提示词是 One or two sentences, three at most（prompts.ts）"),
    (re.compile(r"neutral count[^.]*\b(nothing else|that's all|that's it)\b", re.I), "「neutral count … nothing else」—— 日记本上还有 `{n} nights in a row.`"),
    (re.compile(r"\bno streaks\b", re.I), "`No streaks` —— App 那边 paywallNoStreakClaim 不许这么扩写；商店原句是 no streak to keep and nothing to break"),
    (re.compile(r"\bforever\b", re.I), "forever —— 10-03 老板定对外不说"),
)
LONE_HE = re.compile(r"\b(he|him|his)\b(?!\s*/\s*(she|her))", re.I)


def read(p):
    try:
        with open(os.path.join(ROOT, p), encoding="utf-8") as f:
            return f.read()
    except OSError:
        return None


def split_front(s):
    if s is None or not s.startswith("---\n"):
        return None, s
    end = s.index("\n---", 4)
    head = s[4:end]
    pairs = (l.split(":", 1) for l in head.splitlines() if ":" in l)
    return {k.strip(): v.strip().strip('"') for k, v in pairs}, s[end + 4:]


def check_pages(out):
    for slug, want_ct in PAGES.items():
        p = f"{slug}/index.md"
        fm, body = split_front(read(p))
        if fm is None:
            out.append(f"{p}：不在，或没有 front matter")
            continue
        if fm.get("layout") != "article":
            out.append(f"{p}：layout 不是 article（{fm.get('layout')!r}）")
        ct = fm.get("ct", "")
        if ct != want_ct:
            out.append(f"{p}：ct 应是 {want_ct}，是 {ct!r}")
        if not CT_RE.match(ct):
            out.append(f"{p}：ct {ct!r} 不是 [a-z0-9-]、≤30 字符")
        if not fm.get("title"):
            out.append(f"{p}：没有 title")
        d = fm.get("description", "")
        if not d or len(d) > 155:
            out.append(f"{p}：description 空或超 155 字符（{len(d)}）")
        if "apps.apple.com" in body:
            out.append(f"{p}：正文里自己写了 App Store 链接（按钮只许在 layout 里）")
        for rx, why in STALE:
            if rx.search(body):
                out.append(f"{p}：{why}")
        m = LONE_HE.search(body)
        if m:
            out.append(f"{p}：孤零零的 {m.group(0)!r}（he/she 规矩）")


def check_layout(out):
    lay = read("_layouts/article.html")
    if lay is None:
        out.append("_layouts/article.html 不在")
        return
    links = re.findall(r'href="(https://apps\.apple\.com/[^"]+)"', lay)
    if not links:
        out.append("article layout 里一个 App Store 链接都没有")
    for l in links:
        if "ct={{ page.ct }}" not in l:
            out.append(f"article layout 有一个 App Store 链接 ct 不是 page.ct：{l}")
        if "pt=129391747" not in l:
            out.append(f"article layout 有一个 App Store 链接没带 pt：{l}")
    if '<link rel="canonical" href="{{ site.url }}{{ page.url }}">' not in lay:
        out.append("article layout 的 canonical 不是指本页")
    if "noindex" in lay:
        out.append("article layout 带了 noindex（文章要进索引）")


def check_sitemap(out):
    cfg = read("_config.yml") or ""
    if not re.search(r"^plugins:[\s\S]*?^  - jekyll-sitemap$", cfg, re.M):
        out.append("_config.yml 没开 jekyll-sitemap")
    fm, _ = split_front(read("tiktok/index.html"))
    if not fm or fm.get("sitemap") != "false":
        out.append("tiktok/index.html 没写 sitemap: false（那一页 noindex，不该进 sitemap）")


JS_HARNESS = r"""
const vm = require('vm');
const [script, cases] = [process.argv[1], JSON.parse(process.argv[2])];
const res = cases.map(([search, href]) => {
  const a = { href };
  const ctx = {
    URL, URLSearchParams, location: { search },
    document: { querySelectorAll: (sel) => (sel === 'a[href^="https://apps.apple.com/"]' ? [a] : []) },
  };
  vm.runInNewContext(script, ctx);
  return new URL(a.href).searchParams.get('ct');
});
console.log(JSON.stringify(res));
"""
APP = "https://apps.apple.com/app/apple-store/id6811528172?pt=129391747&ct=site&mt=8"
JS_CASES = (
    ("?ref=theresanaiforthat.com", "dir-theresanaiforthat-com"),
    ("?utm_source=ProductHunt", "dir-producthunt"),
    ("?ref=www.saashub.com&utm_source=x", "dir-saashub-com"),
    ("?ref=%3Cscript%3E", "dir-script"),
    ("?ref=" + "a" * 60, "dir-" + "a" * 26),
    ("?ref=theresanaiforthat-com-directory", "dir-theresanaiforthat-com-dire"),
    ("", "site"),
    ("?ref=", "site"),
    ("?ref=---", "site"),
)


def check_home_js(out):
    lay = read("_layouts/home.html") or ""
    m = re.search(r"\{% unless page\.ct and page\.ct != \"site\" %\}\s*<script>([\s\S]*?)</script>\s*\{% endunless %\}", lay)
    if not m:
        out.append("home layout 里没有只在 ct = site 那一页跑的 dir- 改写脚本")
        return
    node = shutil.which("node")
    if not node:
        out.append("没有 node：dir- 改写脚本这一格没跑（没跑 ≠ 过）")
        return
    r = subprocess.run([node, "-e", JS_HARNESS, m.group(1), json.dumps([[s, APP] for s, _ in JS_CASES])],
                       capture_output=True, text=True)
    if r.returncode != 0:
        out.append(f"dir- 改写脚本在 node 里跑挂了：{r.stderr.strip()[:200]}")
        return
    got = json.loads(r.stdout)
    for (search, want), g in zip(JS_CASES, got):
        if g != want:
            out.append(f"首页 {search or '（没带参数）'} → ct 应是 {want}，是 {g}")
        elif not CT_RE.match(g):
            out.append(f"首页 {search} → ct {g!r} 不是 [a-z0-9-]、≤30 字符")


def check_rosebud_redirect(out):
    if read("rosebud/index.html") is not None or read("rosebud/index.md") is not None:
        out.append("rosebud/index.*：旧 /rosebud/ 还是一页 —— 和 /rosebud-alternative/ 同题互抢（#2414），删掉、交给 redirect_from")
    fm, _ = split_front(read("rosebud-alternative/index.md"))
    if not fm or fm.get("redirect_from") != "/rosebud/":
        out.append("rosebud-alternative/index.md：front matter 没有 redirect_from: /rosebud/（#2414）")
    if "jekyll-redirect-from" not in (read("_config.yml") or ""):
        out.append("_config.yml：plugins 里没有 jekyll-redirect-from，redirect_from 不生效")


def problems():
    out = []
    check_pages(out)
    check_layout(out)
    check_sitemap(out)
    check_home_js(out)
    check_rosebud_redirect(out)
    return out


if __name__ == "__main__":
    p = problems()
    for x in p:
        print("✗ " + x)
    print(f"✓ {len(PAGES)} 篇挂好、按钮 ct=seo-<篇名>、sitemap 开、首页 ref → ct=dir-<站名>、/rosebud/ → /rosebud-alternative/" if not p else f"#2320/#2341 核：{len(p)} 处不对")
    sys.exit(1 if p else 0)

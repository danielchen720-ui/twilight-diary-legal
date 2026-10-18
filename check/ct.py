#!/usr/bin/env python3
"""#1461：官网两页 App Store 按钮的 ct 不一样（首页 site / TikTok 主页来的 /tiktok/ = tiktok）。只读，本机没有 jekyll 也能跑。

    python3 check/ct.py      → 退出 0 = 全对；1 = 哪一条不对印出来

核的是源，不是 build 出来的页（本机没有 jekyll）：
① 首页和 /tiktok/ 都走 `_layouts/home.html`，front matter 里的 ct 各是 site / tiktok（不一样）
② 那个 layout 里每一个 App Store 链接的 ct 都是 `{{ page.ct | default: 'site' }}`，一个写死的都没有
③ layout 里 canonical 永远指首页；ct 不是 site 的那一页带 noindex（搜索引擎只认首页一份）
④ 这个目录不发到站上（_config.yml 的 exclude）
推完之后的那一半：`curl -fsSL https://diarybff.app/tiktok/ | grep -c 'ct=tiktok'` ≥ 1（推送卡上那一格）。
"""
import os
import re
import sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
CT_LIQUID = "{{ page.ct | default: 'site' }}"


def read(p):
    try:
        with open(os.path.join(ROOT, p), encoding="utf-8") as f:
            return f.read()
    except OSError:
        return None


def front(p):
    s = read(p)
    if s is None or not s.startswith("---\n"):
        return None
    head = s[4:s.index("\n---", 4)]
    pairs = (l.split(":", 1) for l in head.splitlines() if ":" in l)
    return {k.strip(): v.strip().strip('"') for k, v in pairs}


def problems():
    out = []
    pages = {"index.html": "site", "tiktok/index.html": "tiktok"}
    for p, want in pages.items():
        fm = front(p)
        if fm is None:
            out.append(f"{p}：没有 front matter（要 layout: home + ct: {want}）")
            continue
        if fm.get("layout") != "home":
            out.append(f"{p}：layout 不是 home（{fm.get('layout')!r}）")
        if fm.get("ct") != want:
            out.append(f"{p}：ct 应是 {want}，是 {fm.get('ct')!r}")
    lay = read("_layouts/home.html")
    if lay is None:
        out.append("_layouts/home.html 不在")
    else:
        links = re.findall(r'href="(https://apps\.apple\.com/[^"]+)"', lay)
        if not links:
            out.append("_layouts/home.html 里一个 App Store 链接都没有")
        for l in links:
            if f"ct={CT_LIQUID}" not in l:
                out.append(f"layout 里有一个 App Store 链接的 ct 不是页面变量：{l}")
        if not re.search(r'<link rel="canonical" href="\{\{ site\.url \}\}/">', lay):
            out.append("layout 里没有指首页的 canonical")
        if not re.search(r'\{% if page\.ct and page\.ct != "site" %\}<meta name="robots" content="noindex">\{% endif %\}', lay):
            out.append("layout 里没有「ct 不是 site 就 noindex」那一句")
    cfg = read("_config.yml") or ""
    if not re.search(r"^exclude:[\s\S]*^  - check$", cfg, re.M):
        out.append("_config.yml 没把 check/ 排出去（会发到站上）")
    return out


if __name__ == "__main__":
    p = problems()
    for x in p:
        print("✗ " + x)
    print("✓ 两页按钮 ct 不同，/tiktok/ canonical 指首页 + noindex" if not p else f"#1461 ct 核：{len(p)} 处不对")
    sys.exit(1 if p else 0)

#!/usr/bin/env python3
"""#2940 ②（后端部 11-06）：build 出来的站逐页查站内链接 + /help/ 五页的零脚本 / ct。只读。

    jekyll build -d <OUT> && python3 check/links.py <OUT>   → 0 = 全对；1 = 哪一条不对印出来

为什么查 build 出来的页、不只查源（seo.py 查源）：死链只在 build 之后才看得见 ——
`../export-and-import/` 这种相对链接、`/assets/...` 图、`.md` 版，源里写对写错长得一样。
① 每个 <a href> / <img src> / <link href> 指向本站的（/x、../x、https://diarybff.app/x），build 里都有那个文件（目录 = 目录/index.html）
② /help/ 下每页：没有 <script；恰好 1 个 App Store 链接，ct=help-<名>（表在 HELP）、带 pt=129391747
③ /llms.txt 在，里面列的每个 https://diarybff.app/ 地址 build 里都有
"""
import os
import re
import sys
from urllib.parse import urlparse, unquote

HELP = {
    "help/index.html": "help-index",
    "help/pin-and-new-phone/index.html": "help-pin",
    "help/export-and-import/index.html": "help-export",
    "help/delete-account/index.html": "help-delete",
    "help/free-and-paid/index.html": "help-plans",
    "help/replies/index.html": "help-replies",
}
LINK_RE = re.compile(r'(?:href|src)="([^"]+)"')
APPSTORE_RE = re.compile(r'href="(https://apps\.apple\.com/[^"]+)"')


def exists(out, path):
    p = os.path.join(out, unquote(path).lstrip("/"))
    if path.endswith("/"):
        return os.path.isfile(os.path.join(p, "index.html"))
    return os.path.isfile(p) or os.path.isfile(os.path.join(p, "index.html"))


def target(page_rel, href):
    """站内链接 → 站根下的路径；站外 / 锚点 / mailto → None"""
    if href.startswith(("mailto:", "#", "tel:", "data:")):
        return None
    u = urlparse(href)
    if u.scheme in ("http", "https"):
        if u.netloc != "diarybff.app":
            return None
        return u.path or "/"
    if u.scheme:
        return None
    if href.startswith("/"):
        return u.path
    base = "/" + os.path.dirname(page_rel)
    return os.path.normpath(os.path.join(base, u.path)) + ("/" if u.path.endswith("/") else "")


def problems(out):
    bad = []
    pages = []
    for root, _, files in os.walk(out):
        for f in files:
            if f.endswith(".html"):
                pages.append(os.path.relpath(os.path.join(root, f), out))
    for rel in sorted(pages):
        s = open(os.path.join(out, rel), encoding="utf-8").read()
        for href in LINK_RE.findall(s):
            t = target(rel, href.replace("&amp;", "&"))
            if t is not None and not exists(out, t):
                bad.append(f"{rel}：死链 {href}")
    for rel, ct in HELP.items():
        p = os.path.join(out, rel)
        if not os.path.isfile(p):
            bad.append(f"{rel}：不在")
            continue
        s = open(p, encoding="utf-8").read()
        if "<script" in s:
            bad.append(f"{rel}：有 <script（help 页要零脚本）")
        links = APPSTORE_RE.findall(s)
        if len(links) != 1:
            bad.append(f"{rel}：App Store 链接 {len(links)} 个（要恰好 1 个）")
        for l in links:
            if f"ct={ct}&" not in l.replace("&amp;", "&") + "&":
                bad.append(f"{rel}：App Store 链接 ct 不是 {ct}：{l}")
            if "pt=129391747" not in l:
                bad.append(f"{rel}：App Store 链接没带 pt：{l}")
    llms = os.path.join(out, "llms.txt")
    if not os.path.isfile(llms):
        bad.append("llms.txt：不在")
    else:
        for u in re.findall(r"https://diarybff\.app(/[^\s)<>]*)", open(llms, encoding="utf-8").read()):
            if not exists(out, u):
                bad.append(f"llms.txt：死链 https://diarybff.app{u}")
    return bad, len(pages)


if __name__ == "__main__":
    if len(sys.argv) != 2 or not os.path.isdir(sys.argv[1]):
        sys.exit("用法：python3 check/links.py <jekyll build 出来的目录>")
    p, n = problems(sys.argv[1])
    for x in p:
        print("✗ " + x)
    print(f"✓ {n} 页站内链接全通、/help/ 六页零脚本 + ct=help-*、llms.txt 全通" if not p else f"#2940 链接核：{len(p)} 处不对")
    sys.exit(1 if p else 0)

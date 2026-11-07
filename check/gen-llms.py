#!/usr/bin/env python3
"""#2940 ② 后端部：从市场部 #2818 那份拷来，多认 help/<页>/index.md（列进 About the app）。落站前：提交正文 → python3 check/gen-llms.py . HEAD .
#2818 官网 /llms.txt + 每篇 .md 版。只读一个 legal-site checkout，写到 OUT 目录（不改 checkout）。
  python3 gen-md-and-llms.py <legal-site 路径> <git ref> <OUT> [覆盖目录…]
覆盖目录 = 本夹里还没上站的篇（<slug>/index.md），同名的以它为准。
.md 版没有 front matter（Jekyll 当静态文件原样发），第一段是 URL / 日期 / 作者。"""
import os, re, subprocess, sys
site, ref, out, *over = sys.argv[1:]
SKIP = {'check', 'assets', 'tiktok', '_layouts'}
def git(*a): return subprocess.run(['git', '-C', site, *a], capture_output=True, text=True).stdout
pages = {}
for f in git('ls-tree', '-r', '--name-only', ref).split():
    m = re.match(r'^([a-z0-9-]+(?:/[a-z0-9-]+)?)/index\.md$', f)
    if m and '/' in m.group(1) and not m.group(1).startswith('help/'): continue
    if m and m.group(1) not in SKIP:
        pages[m.group(1)] = (git('show', f'{ref}:{f}'), git('log', '-1', '--format=%cs', ref, '--', f).strip())
for d in over:
    for slug in os.listdir(d):
        p = os.path.join(d, slug, 'index.md')
        if os.path.isfile(p): pages[slug] = (open(p, encoding='utf8').read(), '2026-11-04')
os.makedirs(out, exist_ok=True)
arts, other = [], []
for slug, (t, date) in sorted(pages.items()):
    m = re.match(r'---\n(.*?)\n---\n', t, re.S)
    if not m: continue
    fm, body = m.group(1), t[m.end():]
    g = lambda k: (re.search(r'^' + k + r':\s*"?(.*?)"?\s*$', fm, re.M) or [None, ''])[1]
    if 'article' not in g('layout'):
        other.append((slug, g('title'), g('description'))); continue
    arts.append((slug, g('title'), g('description')))
    url = f'https://diarybff.app/{slug}/'
    head = f'URL: {url}\nDate: {date}\nAuthor: Daniel Chen, founder of Diary BFF\nPublished by Diary BFF\n\n'
    body = re.sub(r'\]\(/', '](https://diarybff.app/', body.lstrip('\n'))
    open(os.path.join(out, f'{slug}.md'), 'w', encoding='utf8').write(head + body)
L = ["# Diary BFF", "",
     "> Diary BFF is a private iPhone diary that writes back when you ask. You write; when you tap Ask, your diary BFF answers in a few sentences under your entry and, when it brings up an earlier night, adds the date. The diary has its own PIN, separate from the phone's passcode, and entries are not used to train AI.",
     "", "Published by Diary BFF. Author: Daniel Chen, founder of Diary BFF. App Store: https://apps.apple.com/app/id6811528172", "",
     "## Articles", "", "Each article also has a plain Markdown copy at https://diarybff.app/<slug>.md", ""]
L += [f'- [{t}](https://diarybff.app/{s}/): {d}' for s, t, d in arts]
L += ["", "## About the app", ""] + [f'- [{t or s}](https://diarybff.app/{s}/)' + (f': {d}' if d else '') for s, t, d in other]
open(os.path.join(out, 'llms.txt'), 'w', encoding='utf8').write('\n'.join(L) + '\n')
print(f'{len(arts)} 篇 .md + llms.txt → {out}')

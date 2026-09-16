# twilight-diary-legal

Diary BFF (iOS) 的**隐私政策**和**支持页**。

| 页面 | 新地址（自定义域名生效后） | 过渡地址（现在） |
|---|---|---|
| 隐私政策 | https://diarybff.app/privacy/ | https://danielchen720-ui.github.io/twilight-diary-legal/privacy/ |
| 支持页 | https://diarybff.app/support/ | https://danielchen720-ui.github.io/twilight-diary-legal/support/ |
| 根地址 | 跳转到 `/privacy/` | 同左 |

隐私政策的源文件在主仓库 `docs/privacy-policy-1.0.2.md`，改那边之后同步到这里的
`privacy/index.md`。

## 站内链接一律写成**相对**路径

`support/index.md` 指向隐私政策用的是 `../privacy/`，不是 `/privacy/`。
理由：自定义域名生效之前，这个站挂在 `…github.io/twilight-diary-legal/` 下面，
**绝对路径在那个地址上会 404**。相对路径在两个地址上都对，所以搬家那天
不需要有人记得回来改链接。

## ⚠️ `CNAME` 还没进 `main` —— 它在 `custom-domain` 分支上等着

自定义域名是**一条命令就能落地**的：

```
git fetch origin && git merge --ff-only origin/custom-domain && git push
```

**但是在 Porkbun 的 DNS 指到 GitHub Pages 之前不要合。** 原因：

`CNAME` 一进 `main`，GitHub Pages 就把自定义域名打开，
于是 `…github.io/twilight-diary-legal/` 会 **301 跳到 `diarybff.app`**。
DNS 还没通的话那个域名解析不出来 —— 也就是说**老地址会当场变成一个死链**，
而 App Store Connect 上现在挂的隐私政策 URL 正是老地址。
GitHub 自己的文档也是这个顺序：先配 DNS，再设自定义域名。

所以顺序是：

1. Porkbun 配 A 记录（`185.199.108-111.153`）+ `www` 的 CNAME
2. `dig diarybff.app +short` 能看到那四个 IP
3. 合 `custom-domain`（上面那条命令），GitHub Pages 设置里勾 Enforce HTTPS
4. `curl -sI https://diarybff.app/privacy/` 是 200
5. **这一步之后**才去改 App Store Connect 上的隐私政策 URL

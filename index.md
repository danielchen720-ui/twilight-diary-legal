---
layout: default
title: Diary BFF
redirect_to: ./privacy/
---

<!--
  这一页只做一件事：把根地址送到 /privacy/。

  它有两道，因为两道各自会在对方还活着的场景里失效：

  - `redirect_to`（上面的 front matter）来自 jekyll-redirect-from，
    GitHub Pages 自带。它生效时会整页换成自己的跳转页，下面的正文根本不渲染。
  - 下面的 meta refresh 是它**没**生效时的那一半 —— 插件没加载的话
    `redirect_to` 是一行没人读的 YAML，页面会静默地变成一张空白页，
    而空白的隐私政策首页和"跳转坏了"从外面看长得一模一样。

  两处的目标地址都是**相对**的 `./privacy/`，不是 `/privacy/`：
  这个仓库在自定义域名生效之前挂在 `…github.io/twilight-diary-legal/` 下面，
  绝对路径在那个地址上会 404。相对路径两个地址都对。
-->
<meta http-equiv="refresh" content="0; url=./privacy/">

# Diary BFF

[Privacy Policy](./privacy/) · [Support](./support/)

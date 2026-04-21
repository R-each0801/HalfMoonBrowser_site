# HalfMoonBrowser_site

HalfMoon Browser の公式サイト（マニュアル / 利用規約 / プライバシーポリシー）を配信するリポジトリです。

**公開 URL**: <https://r-each0801.github.io/HalfMoonBrowser_site/>

## 構成

- `index.md` — ランディング (マニュアル目次)
- `01-setup.md` 〜 `18-faq.md` — マニュアル本編
- `terms.md` — 利用規約
- `privacy.md` — プライバシーポリシー
- `_layouts/` / `_includes/` / `_data/` / `assets/` — Jekyll テンプレート
- `screenshots/` — 各章に埋め込むスクリーンショット

## ローカルプレビュー

```bash
bundle install
bundle exec jekyll serve
```

`http://127.0.0.1:4000/` でサイトが開きます。

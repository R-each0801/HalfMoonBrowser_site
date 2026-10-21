---
layout: default
title: 困ったとき
prev:
  title: 設定ガイド
  url: /settings/
---

# 困ったとき

よくある質問と、解決しないときのお問い合わせ先です。

## よくある質問

### ダイヤルが開かない

画面のふちから内側へスワイプしてください。ふちより少し内側から指を動かすと反応しません。ダイヤルの大きさは {% include path.html id="dialEdit.size" %} で変えられます。

ダイヤルの項目をすべて外してしまったときは、画面の右下に歯車のボタンが表示されます。そこから設定を開き、{% include path.html id="dialEdit.reset" %} で初期配置に戻せます。

### 広告が消えないサイトがある

1. {% include path.html id="adblock.strong" %} がオンか確認します
2. それでも残る広告は、ダイヤルの「広告を消す」でタップして消せます（[やり方]({{ '/features/#adblock' | relative_url }})）

### ページが真っ白になる・表示が崩れる

1. ダイヤルの「更新」で読み込み直します
2. 改善しないときは、ダイヤルの「サイト別広告ブロック」でそのサイトだけ広告ブロックをオフにします
3. それでも直らないときは、{% include path.html id="adblock.strong" %} を一時的にオフにして確かめてください

### 動画が再生されない・操作しにくい

{% include path.html id="media.player" %} をオフにすると、iOS 標準のプレイヤーで再生します。切り替えは次にページを読み込んだときから反映されます。

### ログインしたままにならない

プライベートブラウザではログイン情報が残りません。通常のブラウザでログインしてください。ダイヤルの「データ消去」や {% include path.html id="data.siteData" %} で Cookie を消した場合も、ログインし直しが必要です。

### リンクを HalfMoon で開きたい

iOS の設定で HalfMoon をデフォルトのブラウザに選んでください。{% include path.html id="app.defaultBrowser" %} から iOS の設定を開けます。

### Pro 版の購入を復元したい

{% include path.html id="app.restore" %} をタップします。購入したときと同じ Apple ID で App Store にサインインしている必要があります。

### アプリが落ちる・不具合を報告したい

まず iOS とアプリを最新版にしてから、アプリを開き直してください。それでも起きるときは、下のお問い合わせ先にお知らせください。調査用の情報（デバッグ情報）の取り方をご案内することがあります。

## お問い合わせ

### GitHub Issues

公開の報告窓口です。同じ問題がすでに報告されていないかも確認できます。

- [HalfMoon Browser — Issues](https://github.com/R-each0801/HalfMoonBrowser/issues)

次の内容を添えていただけると、原因を早く特定できます。

1. 起きたこと
2. 起きるまでの手順
3. 端末と iOS のバージョン（例: iPhone 15, iOS 18.1）
4. アプリのバージョン（{% include path.html id="app.version" %}）
5. 起きたページの URL

### メール

- **サポート全般 / プライバシー関連**: [reach.app.support@gmail.com](mailto:reach.app.support@gmail.com)

原則 5 営業日以内にご返信します。個人で開発しているため、遅れる場合があります。

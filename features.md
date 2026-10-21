---
layout: default
title: 機能ガイド
prev:
  title: ダイヤル操作
  url: /dial/
next:
  title: 設定ガイド
  url: /settings/
---

# 機能ガイド

やりたいことから探せるように、機能ごとにまとめています。設定の場所は「設定 › …」の道順で示しています。

<nav class="hm-toc hm-toc-inline" aria-label="このページの目次">
  <ul>
    <li><a href="#adblock">広告をなくす</a></li>
    <li><a href="#tabs">タブを使う</a></li>
    <li><a href="#search">検索とお気に入り</a></li>
    <li><a href="#reading">読みやすくする</a></li>
    <li><a href="#media">動画と SNS</a></li>
    <li><a href="#private">プライベートブラウザ</a></li>
    <li><a href="#data">履歴とデータ</a></li>
    <li><a href="#apps">他のアプリとの連携</a></li>
    <li><a href="#pro">Pro 版</a></li>
  </ul>
</nav>

<h2 id="adblock">広告をなくす</h2>

広告ブロックは最初からオンになっています。特に何もしなくても、ページを開いた時点で多くの広告が消えます。

| しくみ | 内容 |
|---|---|
| 広告ブロック | 広告の配信元への通信を止め、広告の枠を画面から隠します |
| 強力ブロック | 「広告ブロックを解除してください」と表示するサイトや、画面に追従する広告にも対応します |
| 広告を消す | それでも残った広告を、指でタップして消します |

どちらのブロックも {% include path.html page="adblock" %} で切り替えられます。

### 残った広告をタップで消す

<ol class="hm-steps">
  <li>
    <p class="hm-step-title">「広告を消す」を選ぶ</p>
    <p>左ダイヤルの「サブメニュー」から <span class="hm-ui">広告を消す</span> を選びます。画面の下に操作ボタンが表示されます。</p>
  </li>
  <li>
    <p class="hm-step-title">消したい広告をタップ</p>
    <p>タップした部分が枠で囲まれます。広告の一部しか囲まれないときは <span class="hm-ui">親へ</span> を押すと、範囲がひと回り広がります。</p>
  </li>
  <li>
    <p class="hm-step-title">「消す」で確定</p>
    <p><span class="hm-ui">消す</span> で非表示にします。やめるときは <span class="hm-ui">取消</span> を押します。</p>
  </li>
</ol>

消した広告はサイトごとに記憶され、次にそのサイトを開いたときも消えたままになります。元に戻したいときは {% include path.html id="adblock.hidden" %} から、要素ごと、またはサイトごとに戻せます。

### 表示が崩れるサイトがあるとき

広告ブロックの影響でページが正しく表示されないときは、ダイヤルの <span class="hm-ui">サイト別広告ブロック</span> で、そのサイトだけブロックをオフにできます。オフにしたサイトは {% include path.html id="adblock.sites" %} で確認し、元に戻せます。

自分でブロックしたい URL がある場合は {% include path.html id="adblock.filters" %} に追加します。

<h2 id="tabs">タブを使う</h2>

- **新しいタブ** — ダイヤルの <span class="hm-ui">新規タブ</span>
- **タブの切り替え** — <span class="hm-ui">タブ一覧</span> で一覧から選ぶか、<span class="hm-ui">タブ移動</span> で次のタブへ
- **タブを閉じる** — <span class="hm-ui">タブを閉じる</span>
- **リンクを新しいタブで開く** — リンクを長押しして「新しいタブで開く」

タブ一覧は、円状に並べる **円環カルーセル** と、横一列に並べて操作を画面の下にまとめる **横並び** から選べます。大きい iPhone を片手で使うなら横並びがおすすめです。
{% include path.html id="tabs.style" %}

画面の下に、前後のタブを並べた帯や「戻る・検索・ホーム・共有・進む」の操作バーを常に出しておくこともできます。
{% include path.html page="tabs" %}

<h2 id="search">検索とお気に入り</h2>

### 検索する

右ダイヤルの <span class="hm-ui">検索・URL</span> を選ぶと入力欄が開きます。言葉を入れると検索、URL を入れるとそのページを開きます。入力欄が空のときは、右側のボタンで QR コードを読み取れます。

- 使う検索サイトは Google・DuckDuckGo・Bing・Yahoo! Japan・Ecosia から選べます。{% include path.html id="search.engine" %}
- 最近の検索と URL は入力候補として表示されます。プライベートブラウザでの入力は残りません。{% include path.html id="search.history" %}

### スタートページとお気に入り

新しいタブを開くと表示されるのがスタートページです。よく見るサイトをお気に入りとして並べておけます。

- 開いているページを追加するには、ダイヤルの <span class="hm-ui">ブックマーク追加</span>
- お気に入りはフォルダにまとめられます
- 他のブラウザのブックマークは、書き出した HTML ファイルから取り込めます。{% include path.html id="search.import" %}

スタートページ上部の検索バーとタブの一覧は、不要なら隠せます。{% include path.html page="search" %}

<h2 id="reading">読みやすくする</h2>

### 夜に見やすくする

| 機能 | 内容 | 切り替え |
|---|---|---|
| ダーク | 明るいページを暗い配色に変換します。写真と動画は元の色のままです | ダイヤルの <span class="hm-ui">ライト/ダーク切替</span> |
| 自動 (Pro) | 端末の設定・時間帯・画面の明るさに合わせてライトとダークを切り替えます | 設定のみ |
| スーパーダーク | 画面全体を暗幕で覆い、まぶしさを抑えます。暗さは 10%〜85% で調整できます | ダイヤルの <span class="hm-ui">スーパーダーク</span> |

設定は {% include path.html page="display" %} にまとめています。

### 文章を読みやすくする

- <span class="hm-ui">リーダー</span> — 広告やメニューを省き、本文だけを表示します。読み上げもできます
- <span class="hm-ui">翻訳</span> — 開いているページを Google 翻訳で表示します
- <span class="hm-ui">拡大</span> / <span class="hm-ui">縮小</span> — ページを拡大・縮小します。倍率はサイトごとに記憶されます
- <span class="hm-ui">PC 表示切替</span> — スマホ向けとパソコン向けの表示を切り替えます。サイトごとに記憶されます
- <span class="hm-ui">自動スクロール</span> — ページをゆっくり自動でスクロールします。画面をタップすると止まります。速さは {% include path.html id="dial.autoScrollSpeed" %} で変えられます

<h2 id="media">動画と SNS</h2>

ページに埋め込まれた動画は、片手で操作しやすい専用のプレイヤーで再生します。横長の動画を全画面にすると、画面が自動で横向きになります。うまく再生できない動画があるときは、専用プレイヤーをオフにすると iOS 標準のプレイヤーで再生します。
{% include path.html id="media.player" %}

X・Instagram・TikTok のリンクは、端末に入っている公式アプリで開きます。ブログなどに埋め込まれた投稿の画像は、公式アプリを開かずにその場で拡大できます。
{% include path.html page="media" %}

<h2 id="private">プライベートブラウザ</h2>

ダイヤルの <span class="hm-ui">プライベート切替</span> で、閲覧の記録を残さないプライベートブラウザに切り替わります。

- 閲覧履歴、Cookie、ログイン情報はこの端末に残りません
- 入力した語句は検索の入力候補に残りません
- 初期設定では、開くときに Face ID・Touch ID・パスコードで本人確認します

ロックや次回起動時の再開などは {% include path.html page="private" %} で変えられます。Pro 版では、プライベート専用のお気に入りを通常と分けて持てます。

<h2 id="data">履歴とデータ</h2>

| やりたいこと | 場所 |
|---|---|
| 見たページを探す・消す | {% include path.html id="data.history" %} |
| ダウンロードしたファイルを見る | {% include path.html id="data.downloads" %} |
| サイトの Cookie やキャッシュを消す | {% include path.html id="data.siteData" %} |
| すべてのタブと Cookie・キャッシュをまとめて消す | ダイヤルの <span class="hm-ui">データ消去</span> |

PDF や ZIP などのファイルをダウンロードすると、ダウンロードの画面に一覧で表示されます。そこから共有メニューで他のアプリに送ったり「ファイル」App に保存したりできます。

パスワードは iOS の自動入力（iCloud キーチェーン）に保存されます。HalfMoon 独自のパスワード保存はありません。

<h2 id="apps">他のアプリとの連携</h2>

- **デフォルトのブラウザにする** — iOS の設定で HalfMoon をデフォルトのブラウザに選ぶと、メールや SNS のリンク、カメラで読み取った QR コードが HalfMoon で開きます。{% include path.html id="app.defaultBrowser" %}
- **共有から開く** — 他のアプリの共有メニューで「HalfMoon で開く」を選ぶと、そのページを HalfMoon で開きます
- **ページを共有** — ダイヤルの <span class="hm-ui">共有</span> で、開いているページを他のアプリに送れます

<h2 id="pro">Pro 版</h2>

Pro 版は買い切りです（定期的な支払いはありません）。購入すると次の機能が使えます。

- ダイヤルとサブメニューに 12 項目まで並べられる
- 表示モードの「自動」
- プライベート専用のお気に入り

購入は {% include path.html id="app.pro" %}、機種変更や再インストールのあとは {% include path.html id="app.restore" %} から行います。

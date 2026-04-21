---
layout: default
title: 広告ブロックと機能
prev:
  title: ダイヤルとカスタマイズ
  url: /dial/
---

# 広告ブロックと機能

## 広告ブロック — 3 層構造で、強力に

HalfMoon の広告ブロックは、3 つの層が重なって動作します。
どれか 1 つだけで対処しきれない広告も、層を組み合わせることで
ほとんど残さず除去できます。

<div class="hm-card-grid">
  <div class="hm-card hm-card-static">
    <span class="hm-card-num">層 1</span>
    <span class="hm-card-title">URL フィルタ</span>
    <span class="hm-card-desc">
      Google Ads / Criteo / Taboola / Microad など、200 を超える
      広告配信ドメインへの通信そのものを遮断。ページ表示も軽くなります。
    </span>
  </div>
  <div class="hm-card hm-card-static">
    <span class="hm-card-num">層 2</span>
    <span class="hm-card-title">CSS 非表示</span>
    <span class="hm-card-desc">
      通信は必要だが画面から消したい広告コンテナを、CSS セレクタで
      非表示に。ネイティブ広告やアフィリエイトリンクに対応します。
    </span>
  </div>
  <div class="hm-card hm-card-static">
    <span class="hm-card-num">層 3</span>
    <span class="hm-card-title">検知バイパス</span>
    <span class="hm-card-desc">
      「広告ブロックを解除してください」の警告表示や、広告が読み込め
      ないと自動リロードして戻してくるサイトに対抗します。
    </span>
  </div>
</div>

設定 → 広告ブロック → **「強力ブロック」** を ON にすると層 3 も有効化。
表示が崩れるサイトだけを **ダイヤルからワンタップで OFF** にでき、
後で管理画面から復元できます。

<div class="hm-adblock-compare">
  <div class="hm-adblock-compare-item">
    <div class="hm-adblock-compare-label">🔴 ブロックなし</div>
    <img src="{{ '/assets/images/adblock-none.png' | relative_url }}" alt="広告ブロックなしの状態">
    <div class="hm-adblock-compare-note">広告で画面が埋め尽くされ、本文がほぼ見えない</div>
  </div>
  <div class="hm-adblock-compare-item">
    <div class="hm-adblock-compare-label">🟡 通常ブロック</div>
    <img src="{{ '/assets/images/adblock-standard.png' | relative_url }}" alt="通常ブロック適用後">
    <div class="hm-adblock-compare-note">目立つ広告は消えるが、本文中になお残る</div>
  </div>
  <div class="hm-adblock-compare-item">
    <div class="hm-adblock-compare-label">🟢 強力ブロック</div>
    <img src="{{ '/assets/images/adblock-strong.png' | relative_url }}" alt="強力ブロック適用後">
    <div class="hm-adblock-compare-note">本文だけが残り、スッキリ読める</div>
  </div>
</div>

## 広告ピッカー — 残った広告を、指でタップして消す

フィルタで消しきれなかった広告は、サブメニューの **「広告を消す」** から
手動で非表示にできます。

1. サブメニュー → 「広告を消す」を起動
2. 画面下に操作バーが表示される
3. 消したい広告を **指でタップ**
4. 狙いより狭い範囲が選ばれたら「親」ボタンで 1 階層広げる
5. 「非表示」で確定

非表示にしたセレクタは **サイトごとに記憶** されます。
同じサイトを次に開いたときは最初から消えた状態になり、
毎回操作し直す必要はありません。

管理は 設定 → 広告ブロック → **「消した広告の管理」** から。
復元したくなったセレクタは 1 つずつ、または
サイトごとに一括で戻せます。

![広告ピッカー起動中]({{ '/assets/images/adblock-picker.png' | relative_url }})

## プライベートブラウザ

Face ID / Touch ID / パスコードで保護された閲覧モードです。
閲覧履歴・Cookie・ログイン情報を端末に残しません。
一度アプリをバックグラウンドに送って戻したときも、再度認証を求めます。

Pro 版では、プライベート専用のスタートページを通常モードと分離して持てます。
仕事用と趣味用、というような使い分けに。

## 表示のカスタマイズ

<div class="hm-card-grid">
  <div class="hm-card hm-card-static">
    <span class="hm-card-num">🌗</span>
    <span class="hm-card-title">強制ダークモード</span>
    <span class="hm-card-desc">
      白背景のサイトを暗く反転表示。画像・動画は自動で再反転されるので、
      写真はそのままの色で表示されます。
    </span>
  </div>
  <div class="hm-card hm-card-static">
    <span class="hm-card-num">🌑</span>
    <span class="hm-card-title">スーパーダーク</span>
    <span class="hm-card-desc">
      画面全体に半透明の暗幕をかけて輝度を下げる機能。
      10〜85% で調整でき、夜間の目の負担を軽減します。
    </span>
  </div>
</div>

![ダークモード適用中]({{ '/assets/images/dark-mode.png' | relative_url }})

## データ管理

- **パスワード保存** — iOS Keychain に暗号化保存し、サイトに自動入力
- **サイトデータ管理** — Cookie / キャッシュ / LocalStorage をサイト単位で削除
- **ダウンロード** — PDF / ZIP / 画像を iOS「ファイル」App に保存
- **履歴** — 日付別に整理、まとめて削除も可能 (プライベート中は記録しない)

## iOS との連携

| 機能 | 内容 |
|---|---|
| iCloud 同期 | 表示設定や検索エンジンを他の iPhone / iPad と自動同期 |
| 標準ブラウザ指定 | iOS 設定から HalfMoon をデフォルトブラウザに |
| 共有シート | Safari などから「HalfMoon で開く」で受け取り |
| URL スキーム | `halfmoon://open?url=...` で他アプリからの呼び出しに対応 |

## Pro 版

<div class="hm-card-grid">
  <div class="hm-card hm-card-static">
    <span class="hm-card-num">+6</span>
    <span class="hm-card-title">ダイヤル 12 項目まで</span>
    <span class="hm-card-desc">
      通常版の 6 項目から、各方向 12 項目に拡張。
      すべての操作をダイヤル上に置けるようになります。
    </span>
  </div>
  <div class="hm-card hm-card-static">
    <span class="hm-card-num">🎭</span>
    <span class="hm-card-title">プライベート専用お気に入り</span>
    <span class="hm-card-desc">
      通常モードと完全に分離したタイル一覧を、
      プライベートモード側に持てるようになります。
    </span>
  </div>
</div>

App Store 経由の **買い切り課金** です (サブスクリプションではありません)。
Family Sharing に対応しているので、同じ Apple ID グループのご家族とも共有できます。

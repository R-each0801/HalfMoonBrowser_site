---
layout: default
title: ホーム
next:
  title: ダイヤルとカスタマイズ
  url: /dial/
---

<div class="hm-hero">
  <div class="hm-hero-glyph">{% include halfmoon-glyph.html %}</div>
  <h1>HalfMoon Browser</h1>
  <p class="hm-hero-lead">
    片手で、すべて完結。<br>
    iPhone のために作った、軽快なブラウザ。
  </p>
</div>

## 3 つの特徴

<div class="hm-card-grid">
  <div class="hm-card hm-card-static">
    <span class="hm-card-num">01</span>
    <span class="hm-card-title">片手で完結する操作性</span>
    <span class="hm-card-desc">
      戻る・検索・タブ切替まで、よく使う操作はすべて画面の端から呼び出せるダイヤルに集約。親指 1 本で届きます。
    </span>
  </div>
  <div class="hm-card hm-card-static">
    <span class="hm-card-num">02</span>
    <span class="hm-card-title">自分仕様に作り込めるカスタマイズ</span>
    <span class="hm-card-desc">
      ダイヤルの項目、順番、操作モードまで自由に変更可能。Pro 版なら各方向 12 項目まで拡張できます。
    </span>
  </div>
  <div class="hm-card hm-card-static">
    <span class="hm-card-num">03</span>
    <span class="hm-card-title">かつてない強力な広告ブロック</span>
    <span class="hm-card-desc">
      URL フィルタ + CSS 非表示 + 検知回避の 3 層構造。消えない広告も、指でタップするだけで消せて、サイト単位で記憶します。
    </span>
  </div>
</div>

## 操作は、すべて親指の届く場所に

iPhone の標準ブラウザでは、戻るボタン・タブ切替・URL 入力などの操作が
画面のあちこちに分かれています。HalfMoon では、**画面の左右の端から
半円状に開くダイヤル** に、よく使う操作をすべて集約しました。

指を画面の端に置くだけでダイヤルが出て、上下にスライドして指を離すと実行。
端末を持ち替えず、片手のまま:

- ページを **戻る / 進む**
- タブを **開く / 切り替える / 閉じる**
- **検索バー** を呼び出す
- **広告を消す**
- **ダークモード** に切り替える

すべて完結します。

![右ダイヤルを展開した状態]({{ '/assets/images/dial-right.png' | relative_url }})

## 自分の手に、馴染ませていく

ダイヤルに配置するのは、あなたがよく使う操作だけで十分です。
使わない項目は外し、必要なものを足す。順番も、上から使いやすい順に並べる。
設定 → **ダイヤル編集** からいつでも調整できます。

- **通常版**: 左・右・サブメニュー 各 6 項目
- **Pro 版**: 各 12 項目に拡張
- **2 つの操作モード**: ホールド＆リリース / タップ切替
- **サイズ調整**: 0.8x 〜 1.8x
- **左右入れ替え**: 利き手切替も 1 タップ

![ダイヤル編集画面]({{ '/assets/images/dial-edit.png' | relative_url }})

## 広告は、ほぼゼロに

HalfMoon には、日本で広く使われている広告配信ネットワークを
**200 以上** カバーする URL フィルタと、広告コンテナを CSS で
非表示にする仕組みを内蔵しています。

それでも残ってしまう広告は、サブメニューの **「広告を消す」** を選んで、
**指でタップするだけで非表示** にできます。非表示にしたセレクタは
サイトごとに記憶されるので、次回以降は最初から消えた状態で開きます。

<div class="hm-adblock-compare">
  <div class="hm-adblock-compare-item">
    <div class="hm-adblock-compare-label">🔴 ブロックなし</div>
    <img src="{{ '/assets/images/adblock-none.png' | relative_url }}" alt="広告ブロックなしの状態">
    <div class="hm-adblock-compare-note">広告で埋め尽くされ、本文がほぼ見えない</div>
  </div>
  <div class="hm-adblock-compare-item">
    <div class="hm-adblock-compare-label">🟡 通常ブロック</div>
    <img src="{{ '/assets/images/adblock-standard.png' | relative_url }}" alt="通常ブロック適用後">
    <div class="hm-adblock-compare-note">目立つ広告は消えるが、まだ残る</div>
  </div>
  <div class="hm-adblock-compare-item">
    <div class="hm-adblock-compare-label">🟢 強力ブロック</div>
    <img src="{{ '/assets/images/adblock-strong.png' | relative_url }}" alt="強力ブロック適用後">
    <div class="hm-adblock-compare-note">本文だけが残り、快適に読める</div>
  </div>
</div>

<div class="hm-card-grid">
  <a class="hm-card" href="{{ '/dial/' | relative_url }}">
    <span class="hm-card-num">GUIDE</span>
    <span class="hm-card-title">ダイヤルとカスタマイズ</span>
    <span class="hm-card-desc">片手操作の全体像と、自分仕様への作り込み方。</span>
  </a>
  <a class="hm-card" href="{{ '/features/' | relative_url }}">
    <span class="hm-card-num">FEATURES</span>
    <span class="hm-card-title">広告ブロックと機能一覧</span>
    <span class="hm-card-desc">3 層の広告ブロックと、ダーク・プライベート等の機能。</span>
  </a>
</div>

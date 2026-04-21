---
layout: default
title: iOS との連携
prev:
  title: データ管理
  url: /15-data-management
next:
  title: Pro 版
  url: /17-pro
---

# 16. iOS との連携

## iCloud 同期（設定のみ）

設定 → **「iOS」→ iCloud 同期** を ON にすると、以下の **設定** を同じ Apple ID の
他の iPhone / iPad と同期します:

- 既定の検索エンジン
- ダークモード / スーパーダークの設定
- 触覚フィードバックの設定
- 広告ブロックの ON / OFF

最終同期時刻は同じ画面に表示されます。

![iCloud 同期トグル + 最終同期](/screenshots/s43-icloud-sync.png)

### 有効化に必要なもの

- iCloud にサインイン済み（設定アプリ → Apple ID）
- iCloud Drive が ON
- HalfMoon の iCloud アクセスを許可

## 標準の Web ブラウザに設定

iOS 14 以降では、Safari 以外のブラウザをデフォルトに設定できます:

1. iOS の **「設定」→ HalfMoon** を開く
2. **「デフォルトの Web ブラウザ App」** → **HalfMoon** を選択
3. 他アプリから URL をタップすると HalfMoon で開くようになります

設定 → 「iOS」→ **「iOS の設定を開く」** から 1 タップで iOS 設定へ飛べます。

![iOS 設定のデフォルトブラウザ欄](/screenshots/s44-default-browser.png)

## Share Extension（共有シートから開く）

HalfMoon は iOS の **共有シート** にも対応しています。Safari や他アプリで URL を
共有 → **「HalfMoon で開く」** を選ぶと、HalfMoon が起動してそのページを開きます。

![共有シートに HalfMoon が並ぶ](/screenshots/s45-share-extension.png)

## カスタム URL スキーム

以下の URL を他アプリから開くと HalfMoon が起動します:

```
halfmoon://open?url=https://example.com
```

ショートカット App や他アプリとの連携に使えます。

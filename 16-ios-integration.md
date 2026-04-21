# 16. iOS との連携

> ← [15. データ管理](15-data-management.md) | 次へ → [17. Pro 版](17-pro.md)

---

## iCloud 同期（設定のみ）

設定 → **「iOS」→ iCloud 同期** を ON にすると、以下の **設定** を同じ Apple ID の
他の iPhone / iPad と同期します:

- 既定の検索エンジン
- ダークモード / スーパーダークの設定
- 触覚フィードバックの設定
- 広告ブロックの ON / OFF
- ダイヤル項目の配置（予定）

**タブ・履歴・お気に入り・パスワード** の同期は今後のバージョンで対応予定です。

最終同期時刻は同じ画面に表示されます。

> 📸 **スクリーンショット S-43**: iCloud 同期トグル + 最終同期
> 置き場所: `screenshots/s43-icloud-sync.png`

### 有効化に必要なもの

- iCloud にサインイン済み（設定アプリ → Apple ID）
- iCloud Drive が ON
- HalfMoon の iCloud アクセスを許可

### 注意

- Apple Developer で iCloud エンタイトルメントを有効化したビルドで動作します
- Beta / 開発ビルドでは iCloud アイコンがグレーで動作しない場合があります

## 標準の Web ブラウザに設定

iOS 14+ では、Safari 以外のブラウザをデフォルトに設定できます:

1. iOS の **「設定」→ HalfMoon** を開く
2. **「デフォルトの Web ブラウザ App」** → **HalfMoon** を選択
3. 他アプリから URL をタップすると HalfMoon で開くようになります

設定 → 「iOS」→ **「iOS の設定を開く」** から 1 タップで iOS 設定へ飛べます。

> 📸 **スクリーンショット S-44**: iOS 設定のデフォルトブラウザ欄
> 置き場所: `screenshots/s44-default-browser.png`

### ⚠️ 注意

Apple の **web-browser entitlement の承認** が必要です。未承認の配布ビルドでは
デフォルト設定の項目が表示されません。承認ステータスはバージョンごとに異なります。

## Share Extension（共有シートから開く）

HalfMoon は iOS の **共有シート** にも対応しています。Safari や他アプリで URL を
共有 → **「HalfMoon で開く」** を選ぶと、HalfMoon が起動してそのページを開きます。

> 📸 **スクリーンショット S-45**: 共有シートに HalfMoon が並ぶ
> 置き場所: `screenshots/s45-share-extension.png`

## カスタム URL スキーム

以下の URL を他アプリから開くと HalfMoon が起動します:

```
halfmoon://open?url=https://example.com
```

ショートカット App や他アプリとの連携に使えます。

---

→ [17. Pro 版について](17-pro.md)

"""
manual の .md を Jekyll 向けに一括変換するユーティリティ。

変換内容:
  1. "📸 スクリーンショット" の blockquote 形式を `![alt](src)` に変換
  2. ページ末尾の重複する「→ 次へ」手書きナビを削除
     (Jekyll の prev/next 自動生成に置き換えるため)
  3. 冒頭の "← [XX] | 次へ → [YY]" 手書きナビも削除
  4. 開発者向けメタ文言を削除
  5. 各ページに front matter (title + prev/next) を付与

このスクリプトは 1 度だけ実行する前提。再実行は冪等。
"""
from __future__ import annotations
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# ページ順 (prev/next 自動化のため)
ORDER = [
    ("index.md",                     "HalfMoon Browser マニュアル"),
    ("01-setup.md",                  "インストールと初回起動"),
    ("02-dial-concept.md",           "ダイヤルの基本"),
    ("03-practice-url.md",           "URL・検索バーを呼び出す"),
    ("04-practice-navigation.md",    "戻る・進む・ホーム・タブ開閉"),
    ("05-practice-submenu.md",       "サブメニューを開く"),
    ("06-practice-bookmark-scroll.md","ブックマーク追加とページ内ジャンプ"),
    ("07-practice-adblock-select.md","広告を手動で消す"),
    ("08-practice-autoscroll.md",    "自動スクロール"),
    ("09-practice-findinpage.md",    "ページ内検索"),
    ("10-dial-customize.md",         "ダイヤルを編集する"),
    ("11-startpage.md",              "スタートページ"),
    ("12-private.md",                "プライベートブラウザ"),
    ("13-adblock-settings.md",       "広告ブロックの詳細設定"),
    ("14-display.md",                "表示 (ダークモード)"),
    ("15-data-management.md",        "データ管理"),
    ("16-ios-integration.md",        "iOS との連携"),
    ("17-pro.md",                    "Pro 版"),
    ("18-faq.md",                    "よくある質問"),
]

# 手書きナビの削除パターン: 先頭の "> ← [XX] | 次へ → [YY]" 行 (および周辺の水平線 / 空行)
HEADER_NAV_RE = re.compile(
    r"^>\s*(?:←|次へ|\[目次|目次へ|\|)[^\n]*\n",
    re.MULTILINE,
)
HEADER_HR_AFTER_NAV_RE = re.compile(r"^---\s*\n(?=\n)", re.MULTILINE)

# 末尾の手書きナビ (→ [XX. ...](path)) ブロック
FOOTER_NAV_BLOCK_RE = re.compile(
    r"\n+(?:→\s*\[[^\]]+\]\([^)]+\)|\[目次へ戻る\]\([^)]+\))\s*\n*$"
)

# "📸 スクリーンショット S-XX" blockquote → ![alt](src)
#
# パターン:
# > 📸 **スクリーンショット S-07**: 右端にタッチした瞬間
# > 置き場所: `screenshots/s07-touch-right-edge.png`
SCREENSHOT_RE = re.compile(
    r"^>\s*📸\s*\*\*スクリーンショット\s*(S-\d+)\*\*:\s*([^\n]+?)\s*\n"
    r"^>\s*置き場所:\s*`([^`]+)`\s*\n",
    re.MULTILINE,
)

# meta 文言 (pre-release notes など)
META_PATTERNS = [
    r"^>\s*📦[^\n]*\n(?:>[^\n]*\n)*",   # "📦 このマニュアルは…" ブロック
    r"^---\n+© 20\d{2} HalfMoon[^\n]*\n",  # README 末尾のライセンス (旧 README 用)
]


def strip_header_nav(text: str) -> str:
    # 最初の見出し (# ...) の直後に手書きナビがある → 削除
    lines = text.splitlines(keepends=True)
    out = []
    i = 0
    while i < len(lines):
        line = lines[i]
        # "> ← ..." や "> 次へ → ..." を含む blockquote を削除
        if re.match(r"^>\s*(?:←|次へ|\||\[目次へ)", line):
            # その直後が "---" と空行ならそれも削除
            i += 1
            while i < len(lines) and (re.match(r"^---\s*$", lines[i]) or lines[i].strip() == ""):
                i += 1
            continue
        out.append(line)
        i += 1
    return "".join(out)


def convert_screenshots(text: str) -> str:
    def repl(m: re.Match) -> str:
        sn, alt, src = m.group(1), m.group(2).strip(), m.group(3).strip()
        return f"![{alt}]({{ '/{src}' | relative_url }})\n"
    # Jekyll の relative_url filter を使うには `{% raw %}` / Liquid tag が必要だが
    # kramdown は alt テキスト内の `{}` を普通に解釈するので普通の相対パスを使う
    def simple_repl(m: re.Match) -> str:
        alt, src = m.group(2).strip(), m.group(3).strip()
        return f"![{alt}](/{src})\n"
    return SCREENSHOT_RE.sub(simple_repl, text)


def strip_meta(text: str) -> str:
    for pat in META_PATTERNS:
        text = re.sub(pat, "", text, flags=re.MULTILINE)
    return text


def strip_footer_nav(text: str) -> str:
    # 末尾の "→ [次へ](...)" 行を削除
    lines = text.rstrip().splitlines()
    while lines and (
        re.match(r"^→\s*\[[^\]]+\]\([^)]+\)\s*$", lines[-1])
        or re.match(r"^\[目次へ戻る\]\([^)]+\)\s*$", lines[-1])
        or lines[-1].strip() == ""
        or re.match(r"^---+\s*$", lines[-1])
    ):
        lines.pop()
    return "\n".join(lines) + "\n"


def build_front_matter(filename: str, title: str) -> str:
    # prev / next を ORDER から決める
    idx = next((i for i, (fn, _) in enumerate(ORDER) if fn == filename), -1)
    fm_lines = ["---", f"title: {title}"]
    if idx > 0:
        prev_fn, prev_title = ORDER[idx - 1]
        prev_url = "/" if prev_fn == "index.md" else "/" + prev_fn.replace(".md", "")
        fm_lines.append(f"prev:\n  title: {prev_title}\n  url: {prev_url}")
    if 0 <= idx < len(ORDER) - 1:
        next_fn, next_title = ORDER[idx + 1]
        next_url = "/" if next_fn == "index.md" else "/" + next_fn.replace(".md", "")
        fm_lines.append(f"next:\n  title: {next_title}\n  url: {next_url}")
    fm_lines.append("---\n\n")
    return "\n".join(fm_lines)


def has_front_matter(text: str) -> bool:
    return text.lstrip().startswith("---")


def transform(path: Path, title: str) -> None:
    text = path.read_text(encoding="utf-8")
    if has_front_matter(text):
        print(f"  skip (already has front matter): {path.name}")
        return

    text = strip_header_nav(text)
    text = strip_meta(text)
    text = convert_screenshots(text)
    text = strip_footer_nav(text)
    text = build_front_matter(path.name, title) + text.lstrip("\n")

    path.write_text(text, encoding="utf-8", newline="\n")
    print(f"  transformed: {path.name}")


def main() -> None:
    # index.md は後で別途作成するのでスキップ対象
    for fn, title in ORDER:
        if fn == "index.md":
            continue
        p = ROOT / fn
        if not p.exists():
            print(f"  missing: {fn}")
            continue
        transform(p, title)

    # terms / privacy も front matter を付与
    for fn, title in [("terms.md", "利用規約"), ("privacy.md", "プライバシーポリシー")]:
        p = ROOT / fn
        if p.exists():
            text = p.read_text(encoding="utf-8")
            if has_front_matter(text):
                continue
            text = strip_meta(text)
            fm = f"---\ntitle: {title}\n---\n\n"
            p.write_text(fm + text.lstrip("\n"), encoding="utf-8", newline="\n")
            print(f"  transformed: {fn}")


if __name__ == "__main__":
    main()

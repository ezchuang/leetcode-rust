#!/usr/bin/env python3
"""
build_readme.py — 自動生成 README.md

說明:
1. 掃描所有解題檔案 (sXXXX_slug.py/.go/.rs)，聚合各語言完成狀態。
2. 根據 problems 目錄下的 .md / .todo.md 檔案決定【Desc】欄連結或 TODO 標記。
3. 讀取 premium_overrides.json 與 source_urls_cache.json，決定【Source】欄的最終 URL。
4. 輸出 Markdown 表格，其中每個 ✅ 都是可點擊的超連結；未完成則顯示 ✏️。

用法:
  python scripts/build_readme.py

依賴:
  無額外套件，僅使用 pathlib、re、json、collections。

作者: Ezra Chuang
版本: 1.0
"""
from __future__ import annotations
import json
import pathlib
import re
from collections import defaultdict

# 定義專案根目錄與快取檔路徑
ROOT = pathlib.Path(__file__).resolve().parents[1]
SCR  = ROOT / "scripts"
PREM_MAP  = json.loads((SCR / "premium_overrides.json").read_text()) if (SCR / "premium_overrides.json").exists() else {}
CACHE_MAP = json.loads((SCR / "source_urls_cache.json").read_text()) if (SCR / "source_urls_cache.json").exists() else {}

# 表格欄位與提示文字
LANGS = ["PY", "GO", "RS"]
TIPS  = {"PY": "Python", "GO": "Go", "RS": "Rust"}

# 匹配解題檔案的正規表達式：s0001_slug.ext
SRC_RX = re.compile(r"s(\d{4})_([\w_]+)\.(py|go|rs)$", re.I)

# 匹配 problems 下的 .md / .todo.md 檔
DESC_OK = re.compile(r"(\d{4})_.*\.md$")
DESC_TD = re.compile(r"(\d{4})_.*\.todo\.md$")

# 聚合資料結構：rows[pid] = { title, PY, GO, RS, desc, todo, src }
rows = defaultdict(dict)

# 1. 掃描所有語言解答檔案，記錄完成狀態與 slug → Title Case
for fp in ROOT.rglob("s????_*.*"):
    m = SRC_RX.match(fp.name)
    if not m:
        continue
    pid, slug, ext = m.groups()
    rec = rows[pid]
    # 題目顯示文字：slug 轉 Title Case
    rec["title"] = slug.replace("_", " ").title()
    # 標記各語言是否完成，並存相對路徑
    rec[ext.upper()] = fp.relative_to(ROOT).as_posix()
    # 來源 URL：優先 premium override，再 source cache，最後預設 LeetCode
    rec["src"] = PREM_MAP.get(pid) or CACHE_MAP.get(pid) or f"https://leetcode.com/problems/{slug.replace('_','-')}/"

# 2. 掃描 problems 資料夾下的 Markdown 敘述檔
for fp in (ROOT / "problems").glob("*.md"):
    if m := DESC_TD.match(fp.name):
        pid = m.group(1)
        rows[pid]["todo"] = fp.relative_to(ROOT).as_posix()
    elif m := DESC_OK.match(fp.name):
        pid = m.group(1)
        rows[pid]["desc"] = fp.relative_to(ROOT).as_posix()
    

# 3. 定義「鏈結或圖示」函式
def get_icon(
        path: str | None, 
        title: str | None = None, 
        show_edit: bool = False) -> str:
    """
    如果傳入的 path (或 URL) 存在，就回傳可點擊的 ✅ / 🔗；
    否則回傳 ✏️，表示尚未完成。
    可透過 title 參數設定 link title。
    """
    if path:
        if title == "Link":
            return f"[🔗]({path} \"{title}\")"
        if title:
            return f"[✅]({path} \"{title}\")"
        return f"[✅]({path})"
    return "✏️" if show_edit else ""

# 4. 組裝 Markdown 表格
lines = [
    "# LeetCode Progress",
    "",
    "| # | Problem | " + " | ".join(LANGS) + " | Desc | Source |",
    "|----|---------|" + "|".join([":--:" for _ in LANGS]) + "|:---:|:----:|"
]

# 依題號排序，每一行生成表格列
for pid in sorted(rows):
    rec = rows[pid]
    # 基本欄位
    row = [pid, rec.get("title", "")]  
    # 各語言欄位
    for lang in LANGS:
        row.append(get_icon(rec.get(lang), TIPS.get(lang)))
    # Desc 欄 (優先 desc，再 todo)
    if rec.get("desc"):
        row.append(get_icon(rec.get("desc"), "Description"))
    elif rec.get("todo"):
        row.append(f"[✏️]({rec.get('todo')})")
    else:
        row.append("✏️")
    # Source 欄
    row.append(get_icon(rec.get("src"), "Link"))
    lines.append("| " + " | ".join(row) + " |")

# 5. 輸出 README.md
README = ROOT / "README.md"
README.write_text("\n".join(lines) + "\n", encoding="utf-8")
print("✅ README rebuilt successfully.")
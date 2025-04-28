#!/usr/bin/env python3
"""
Re-generate README.md for multi-language LeetCode solutions.

* 集合語言欄位固定為 Py | Go | RS
* 同題多語言合併成單列
* front-matter 例:

// ---                # Rust / Go
// id: 1
// problem: Two Sum
// source: https://leetcode.com/problems/two-sum
// ---

# ---                 # Python
# id: 1
# problem: Two Sum
# source: https://leetcode.com/problems/two-sum
# ---

author: ezchuang
"""

from __future__ import annotations

import pathlib
import re
import sys
from collections import defaultdict
from typing import Dict, List

try:
    import yaml
except ModuleNotFoundError:
    sys.exit("❌  請先 pip install pyyaml")

# -------- 可自行調整的常數 -------- #
LANG_COLS = ["PY", "GO", "RS"]                     # 表格語言欄順序
LANG_TOOLTIP = {"PY": "Python", "GO": "Go", "RS": "Rust"}
ROOT = pathlib.Path(__file__).resolve().parents[1]  # 專案根目錄
CODE_DIRS = [
    ("rust/src",   ".rs"),
    ("go/pkg",     ".go"),
    ("python",     ".py"),
]

# ^---/---^ 允許行前有 // 或 # （含空白）
HEADER_RX = re.compile(
    r"""^[ \t]*(?://|#)?\s*---\s*$      # 起始線
        (.*?)                           # 內文 (非貪婪)
        ^[ \t]*(?://|#)?\s*---\s*$      # 結束線
    """, re.M | re.S | re.VERBOSE
)

# ========= 掃描並聚合 =========
problems: Dict[str, Dict[str, str]] = defaultdict(dict)

for subdir, ext in CODE_DIRS:
    for path in (ROOT / subdir).rglob(f"*{ext}"):
        txt = path.read_text(encoding="utf-8", errors="ignore")
        m = HEADER_RX.search(txt)
        if not m:
            continue

        # ----  Strip 註解前綴  ----
        raw = []
        for ln in m.group(1).splitlines():
            ln = ln.lstrip()
            if ln.startswith("//"):
                ln = ln[2:]
            elif ln.startswith("#"):
                ln = ln[1:]
            raw.append(ln.lstrip())
        try:
            meta = yaml.safe_load("\n".join(raw))
        except yaml.YAMLError as e:
            print(f"⚠️  YAML 解析失敗 → {path}\n{e}", file=sys.stderr)
            continue

        prob = str(meta.get("problem", "")).strip()
        if not prob:
            print(f"⚠️  缺少 problem 欄位 → {path}", file=sys.stderr)
            continue

        lang = ext.lstrip(".").upper()
        problems[prob][lang] = path.relative_to(ROOT).as_posix()
        if "id" not in problems[prob] and "id" in meta:
            problems[prob]["id"] = int(meta["id"])
        if "source" not in problems[prob] and "source" in meta:
            problems[prob]["source"] = str(meta["source"]).strip()

# ========= 產生 README =========
lines: List[str] = [
    "# Solutions",
    "",
    "| # | Problem | " + " | ".join(LANG_COLS) + " | Source |",
    "|---|---------|" + "|".join(["----"] * len(LANG_COLS)) + "|--------|",
]

def sort_key(item):                        # 先 id 再題名
    prob, info = item
    return (info.get("id", 10**9), prob.lower())

for idx, (prob, info) in enumerate(sorted(problems.items(), key=sort_key), 1):
    row = [str(idx), prob]
    for col in LANG_COLS:
        p = info.get(col, "")
        row.append(f"[{col}]({p} \"{LANG_TOOLTIP[col]}\")" if p else "")
    src = info.get("source", "")
    row.append(f"[link]({src})" if src else "")
    lines.append("| " + " | ".join(row) + " |")

README = ROOT / "README.md"
README.write_text("\n".join(lines) + "\n", encoding="utf-8")
print(f"✅  README.md 已更新，共 {len(problems)} 題。")

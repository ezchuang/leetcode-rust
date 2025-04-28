#!/usr/bin/env python3
"""重建 README (改用『題目』欄 & .md 連結)"""
from __future__ import annotations
import json, pathlib, re
from collections import defaultdict

ROOT = pathlib.Path(__file__).resolve().parents[1]
HTML_DIR = ROOT / "question_html"
MD_DIR   = ROOT / "problems"

LANGS = ["PY", "GO", "RS"]
EXTMAP = {".py": "PY", ".go": "GO", ".rs": "RS"}
TIP    = {"PY": "Python", "GO": "Go", "RS": "Rust"}
FNAME  = re.compile(r"s(\d{4})_([\w_]+)\.(py|go|rs)$", re.I)

PREM = json.loads((ROOT/"scripts/premium_overrides.json").read_text()) if (ROOT/"scripts/premium_overrides.json").exists() else {}
SRC_CACHE = json.loads((ROOT/"scripts/source_urls_cache.json").read_text()) if (ROOT/"scripts/source_urls_cache.json").exists() else {}

problems = defaultdict(dict)

for p in ROOT.rglob("s????_*.*"):
    m = FNAME.match(p.name)
    if not m: continue
    pid, slug, ext = m.groups()
    lang = EXTMAP[p.suffix]
    title = slug.replace("_", " ").title()

    info = problems[pid]
    info["problem"] = title
    info[lang] = p.relative_to(ROOT).as_posix()
    info["md"] = f"problems/{pid}.md" if (MD_DIR/f"{pid}.md").exists() else ""
    info["source"] = PREM.get(pid) or SRC_CACHE.get(pid) or f"https://leetcode.com/problems/{slug.replace('_','-')}/"

out = [
    "# Solutions", "",
    "| # | Problem | " + " | ".join(LANGS) + " | 題目 | Source |",
    "|----|---------|" + "|".join(["----"]*len(LANGS)) + "|------|--------|",
]

for pid in sorted(problems):
    info = problems[pid]
    row = [pid, info["problem"]]
    for lang in LANGS:
        path = info.get(lang, "")
        row.append(f"[{lang}]({path} \"{TIP[lang]}\")" if path else "")
    row.append(f"[題目]({info['md']})" if info["md"] else "")
    row.append(f"[link]({info['source']})")
    out.append("| " + " | ".join(row) + " |")

(ROOT/"README.md").write_text("\n".join(out) + "\n", encoding="utf-8")
print("✅ README 完成")

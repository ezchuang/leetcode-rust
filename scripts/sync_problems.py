#!/usr/bin/env python3
"""
Minimal LeetCode fetcher (requests + GraphQL).
- 解析 sXXXX_slug.* 用 pid、slug
- 下載 HTML (非付費) → problems/XXXX.md
"""
import os, json, re, pathlib, requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md

ROOT = pathlib.Path(__file__).resolve().parents[1]
MD_OUT = ROOT / "problems"; MD_OUT.mkdir(exist_ok=True)
PREM = (ROOT/"scripts/premium_overrides.json")
SESSION = os.getenv("LC_SESSION")      # export LC_SESSION=xxxx
CSRF    = os.getenv("LC_CSRF")

S = requests.Session()
S.headers.update({"Content-Type":"application/json"})
S.cookies.update({"LEETCODE_SESSION":SESSION, "csrftoken":CSRF})

slug_map = {str(q["stat"]["frontend_question_id"]).zfill(4): q["stat"]["question__title_slug"]
            for q in S.get("https://leetcode.com/api/problems/all").json()["stat_status_pairs"]}  # :contentReference[oaicite:15]{index=15}

def grab(pid:str):
    slug = slug_map[pid]
    q = {"query":"query($s:String!){question(titleSlug:$s){content isPaidOnly}}",
         "variables":{"s":slug}}
    data = S.post("https://leetcode.com/graphql", json=q).json()["data"]["question"]  # :contentReference[oaicite:16]{index=16}
    if data["isPaidOnly"]: return None
    html = data["content"]
    node = BeautifulSoup(html,"html.parser").select_one('[data-key="description-content"]') \
           or BeautifulSoup(html,"html.parser").select_one('div.question-content')
    md_file = MD_OUT / f"{pid}.md"
    md_file.write_text(md(str(node), heading_style="ATX"), encoding="utf-8")
    return md_file

for path in ROOT.rglob("s????_*.*"):
    m = re.match(r"s(\d{4})_", path.name)
    if not m: continue
    pid = m.group(1)
    out = MD_OUT / f"{pid}.md"
    if out.exists(): continue
    if grab(pid) is None:
        print(f"💰 {pid} premium，請在 premium_overrides.json 填入替代網址")

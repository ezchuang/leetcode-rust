#!/usr/bin/env python3
"""
sync_problems.py — 下載並轉換 LeetCode 題目敘述為 Markdown

功能說明: 
1. 掃描 repo 根目錄，收集所有符合 sXXXX_slug.py/.go/.rs 的檔案。
2. 透過 LeetCode REST API 一次取得題號 ↔ slug 對照表。
3. 使用 GraphQL 查詢免費題 (非 Premium) 之 title 與 content。
   • 成功: 將 HTML 內容轉為 Markdown，並寫入 problems/0009_palindrome_number.md
   • 失敗 (Premium 或錯誤) : 產生 problems/0009_palindrome_number.todo.md 以供手動補充
4. 更新 premium_overrides.json (記錄 Premium 題) 與 source_urls_cache.json (記錄官方鏈結) 

使用方式: 
  $ pip install requests beautifulsoup4 markdownify
  $ export LC_SESSION=<你的 LeetCode Session>    # 可選，登入狀態下可抓需登入之題目
  $ export LC_CSRF=<你的 csrftoken>
  $ python scripts/sync_problems.py

依賴套件: requests | beautifulsoup4 | markdownify
作者: Ezra Chuang  
版本: 1.0
"""
from __future__ import annotations
import json
import os
import pathlib
import re
import sys
import time
import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md

# ---------- 常數與路徑設定 ----------
ROOT = pathlib.Path(__file__).resolve().parents[1]
PROB = ROOT / "problems"                 # Markdown 輸出目錄
SCR  = ROOT / "scripts"                  # 快取與覆寫設定目錄
PROB.mkdir(exist_ok=True)

PREM_FILE  = SCR / "premium_overrides.json"     # Premium 題手動覆寫網址
CACHE_FILE = SCR / "source_urls_cache.json"     # 題號 ↔ 官方鏈結快取

# 讀取或初始化快取資料
PREM_MAP  = json.loads(PREM_FILE.read_text())  if PREM_FILE.exists()  else {}
CACHE_MAP = json.loads(CACHE_FILE.read_text()) if CACHE_FILE.exists() else {}

# Optional: 若需抓取會員限定或每日一題，可設定以下兩個環境變數
SESSION = os.getenv("LC_SESSION", "")  # LeetCode 登入 Session cookie
CSRF    = os.getenv("LC_CSRF", "")     # LeetCode csrftoken

# 設置 HTTP Session
S = requests.Session()
S.headers.update({"Content-Type": "application/json"})
if SESSION and CSRF:
    S.cookies.update({"LEETCODE_SESSION": SESSION, "csrftoken": CSRF})

# 解析檔名之正則: 捕捉題號與 slug
SRC_RX = re.compile(r"s(\d{4})_([\w_]+)\.(py|go|rs)$", re.I)

# GraphQL 查詢語句，含 title + content + isPaidOnly flag
GRAPHQL_URL = "https://leetcode.com/graphql"
QUERY = '''
query($slug:String!){
  question(titleSlug:$slug){
    title
    content
    isPaidOnly
  }
}'''

# ---------- 1. 收集已提交題目 ----------
# solved: { '0009': 'palindrome_number', ... }
solved: dict[str,str] = {}
for fp in ROOT.rglob("s????_*.*"):
    m = SRC_RX.match(fp.name)
    if not m:
        continue
    pid, slug, _ = m.groups()
    # 優先保留第一個語言對應的 slug
    solved.setdefault(pid, slug)

if not solved:
    sys.exit("⚠️ 未偵測到任何 sXXXX_slug.* 檔案，請確認檔名格式")

# ---------- 2. 取得題號 → slug 對照表 ----------
try:
    resp = S.get("https://leetcode.com/api/problems/all", timeout=10)
    resp.raise_for_status()
    stats = resp.json()["stat_status_pairs"]  # 包含每題數據
    slug_map = {str(q["stat"]["frontend_question_id"]).zfill(4): q["stat"]["question__title_slug"]
                for q in stats}
except Exception as e:
    sys.exit(f"❌ 無法取得 REST slug 對照: {e}")

# ---------- 3. 定義抓取並轉 Markdown 的函式 ----------

def html_to_markdown(html: str) -> str:
    """
    擷取題目敘述區塊，轉為 GFM Markdown。
    適配舊版 (div.question-content) 與新版 (data-key="description-content").
    """
    soup = BeautifulSoup(html, "html.parser")
    node = (soup.select_one('[data-key="description-content"]')  # 新版 UI
            or soup.select_one('div.question-content')            # 舊版 UI
            or soup)
    return md(str(node), heading_style="ATX")


def fetch_markdown(pid: str, slug: str) -> tuple[str|None,str|None]:
    """
    向 GraphQL 查詢題目資料，回傳 (title, markdown_body)。
    若 isPaidOnly=True 或發生錯誤，回傳 (None, None)。
    """
    try:
        payload = {"query": QUERY, "variables": {"slug": slug}}
        r = S.post(GRAPHQL_URL, json=payload, timeout=10)
        r.raise_for_status()
        data = r.json()
        if errors := data.get("errors"):
            print(f"✘ [{pid}] GraphQL 錯誤: {errors[0]['message']}")
            return None, None
        q = data["data"]["question"]
    except Exception as exc:
        print(f"✘ [{pid}] HTTP/解析失敗: {exc}")
        return None, None

    # Premium 題跳過
    if q is None or q.get("isPaidOnly"):
        print(f"💰 [{pid}] Premium 題，略過")
        return None, None

    # 轉 Markdown
    md_body = html_to_markdown(q["content"])
    return q.get("title"), md_body

# ---------- 4. 同步流程 ----------
for pid in sorted(solved):
    # 使用 REST map 或 slug fallback
    slug = slug_map.get(pid, solved[pid].replace('_','-'))
    if not slug:
        print(f"❓ [{pid}] 無 slug，跳過")
        continue

    # 檔名格式: 0009_palindrome-number.md
    fn_base = f"{pid}_{slug}.md"
    ok_path   = PROB / fn_base
    todo_path = PROB / fn_base.replace(".md", ".todo.md")

    # 已存在則跳過
    if ok_path.exists():
        continue

    title, body = fetch_markdown(pid, slug)
    if title and body:
        # 內文開頭加入標題
        ok_path.write_text(f"# {int(pid)}. {title}\n\n{body}", encoding="utf-8")
        CACHE_MAP[pid] = f"https://leetcode.com/problems/{slug}/"
        print(f"✅ [{pid}] 已儲存 Markdown: {ok_path.name}")
    else:
        # 生成 TODO 樣板
        todo_path.write_text(f"# {pid} **TODO**: paste description here\n", encoding="utf-8")
        PREM_MAP.setdefault(pid, "")
        print(f"✏️  [{pid}] 需手動補充: {todo_path.name}")

    time.sleep(0.6)  # 禮貌限速

# ---------- 5. 寫回快取設定 ----------
PREM_FILE.write_text(json.dumps(PREM_MAP,  indent=2, ensure_ascii=False))
CACHE_FILE.write_text(json.dumps(CACHE_MAP, indent=2, ensure_ascii=False))
print("🔄 同步完成: problems 目錄已更新、快取檔已寫入。")

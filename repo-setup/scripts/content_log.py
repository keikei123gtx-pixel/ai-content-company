"""
content_log.py — 投稿ログの記録・分析
使い方:
  python scripts/content_log.py add "タイトル" "https://youtu.be/xxx" "lofi,bgm,study"
  python scripts/content_log.py summary
"""
import sys, csv
from datetime import datetime
from pathlib import Path

LOG_FILE = Path("logs/upload_history.csv")
HEADERS  = ["date", "title", "youtube_url", "genre", "tags", "views_7d", "views_30d", "notes"]

def ensure_log():
    LOG_FILE.parent.mkdir(exist_ok=True)
    if not LOG_FILE.exists():
        with open(LOG_FILE, "w", newline="", encoding="utf-8") as f:
            csv.writer(f).writerow(HEADERS)

def add_entry(title, url, tags="", genre="BGM", notes=""):
    ensure_log()
    with open(LOG_FILE, "a", newline="", encoding="utf-8") as f:
        csv.writer(f).writerow([
            datetime.now().strftime("%Y-%m-%d"),
            title, url, genre, tags, 0, 0, notes
        ])
    print(f"✅ ログに追加: {title}")

def show_summary():
    ensure_log()
    with open(LOG_FILE, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    if not rows:
        print("ログがまだありません")
        return
    print(f"\n📊 投稿サマリー（合計 {len(rows)} 本）")
    print("-" * 40)
    for r in rows[-10:]:  # 直近10件
        print(f"  {r['date']} | {r['title'][:30]} | 再生: {r['views_7d']}")

if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "summary"
    if cmd == "add" and len(sys.argv) >= 4:
        add_entry(sys.argv[2], sys.argv[3],
                  sys.argv[4] if len(sys.argv) > 4 else "")
    else:
        show_summary()

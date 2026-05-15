import os, sys, json
from datetime import datetime
from pathlib import Path

API_KEY = os.environ.get("GEMINI_API_KEY", "")
MODEL   = "gemini-1.5-flash"

try:
    import google.generativeai as genai
except ImportError:
    print("pip install google-generativeai")
    sys.exit(1)

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel(MODEL)

def research(topic: str) -> dict:
    prompt = f"""
あなたはYouTube BGMチャンネルのSEOと競合分析の専門家です。
トピック「{topic}」について調査し、以下のJSON形式で回答してください。
JSON以外は不要です。

{{
  "recommended_titles": ["タイトル案1", "タイトル案2", "タイトル案3"],
  "tags": ["タグ1", "タグ2", "タグ3", "タグ4", "タグ5"],
  "description_template": "説明欄テンプレート（300文字）",
  "trending_keywords": ["キーワード1", "キーワード2", "キーワード3"],
  "competitor_insight": "競合の傾向（200文字）",
  "content_angle": "差別化の提案"
}}"""
    res = model.generate_content(prompt)
    text = res.text.strip()
    if "```json" in text:
        text = text.split("```json")[1].split("```")[0].strip()
    elif "```" in text:
        text = text.split("```")[1].split("```")[0].strip()
    try:
        return json.loads(text)
    except:
        return {"raw": text}

def save(topic: str, data: dict) -> Path:
    out = Path("results")
    out.mkdir(exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    fp = out / f"{ts}_{topic[:20].replace(' ','_')}.md"
    lines = [f"# Gemini Research: {topic}", f"日時: {datetime.now():%Y-%m-%d %H:%M}", ""]
    if "recommended_titles" in data:
        lines += ["## タイトル案"] + [f"- {t}" for t in data["recommended_titles"]] + [""]
    if "tags" in data:
        lines += ["## タグ", ", ".join(data["tags"]), ""]
    if "trending_keywords" in data:
        lines += ["## トレンドキーワード", ", ".join(data["trending_keywords"]), ""]
    if "description_template" in data:
        lines += ["## 説明欄テンプレート", data["description_template"], ""]
    if "competitor_insight" in data:
        lines += ["## 競合分析", data["competitor_insight"], ""]
    if "content_angle" in data:
        lines += ["## 差別化提案", data["content_angle"], ""]
    fp.write_text("\n".join(lines), encoding="utf-8")
    return fp

if __name__ == "__main__":
    topic = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "lofi hip hop BGM 作業用"
    print(f"🔍 リサーチ中: {topic}")
    data = research(topic)
    fp = save(topic, data)
    print(f"✅ 保存: {fp}")
    if "recommended_titles" in data:
        print("\nタイトル案:")
        for t in data["recommended_titles"]: print(f"  • {t}")

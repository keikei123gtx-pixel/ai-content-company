# 🏢 AI Content Company

Claude × GitHub × Gemini で動くコンテンツ自動生成システム

## 体制
| 役割 | 担当 |
|------|------|
| 司令塔・制作実行 | Claude（Cowork） |
| トレンドリサーチ | Gemini API |
| 自動化・記録管理 | GitHub Actions |

## フォルダ構成
```
ai-content-company/
├── prompts/          ← Claudeへの指示テンプレート
├── scripts/          ← 自動化スクリプト
├── results/          ← Geminiリサーチ結果（自動蓄積）
├── logs/             ← 投稿履歴ログ
└── .github/workflows ← 週次自動実行
```

## 使い方
1. Claudeに「今週の動画を作って」と話しかけるだけ
2. Geminiがトレンドを調査 → Claudeが企画・制作 → YouTubeに投稿
3. 結果はGitHubに自動保存・蓄積される

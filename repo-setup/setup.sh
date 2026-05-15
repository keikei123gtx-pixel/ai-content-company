#!/bin/bash
# ==============================================
# AI Content Company — GitHubセットアップスクリプト
# 使い方:
#   1. GitHubからリポをclone:
#      git clone https://github.com/あなたのユーザー名/ai-content-company.git
#   2. このスクリプトをリポのルートに置く
#   3. bash setup.sh
# ==============================================

set -e
echo "🚀 AI Content Company セットアップ開始..."
echo ""

# フォルダ作成
echo "📁 フォルダ構造を作成中..."
mkdir -p prompts scripts results logs .github/workflows

# .gitkeep（空フォルダをGitで追跡するため）
touch results/.gitkeep

echo "✅ フォルダ作成完了"
echo ""

# Gemini APIキーの設定
echo "🔑 GitHubのSecretsにGemini APIキーを設定してください:"
echo "   https://github.com/$(git remote get-url origin | sed 's/.*github.com[:/]//' | sed 's/\.git$//')/settings/secrets/actions"
echo "   キー名: GEMINI_API_KEY"
echo ""

# Pythonパッケージ確認
echo "🐍 Pythonパッケージを確認中..."
if python3 -c "import google.generativeai" 2>/dev/null; then
    echo "   ✅ google-generativeai インストール済み"
else
    echo "   📦 google-generativeai をインストール中..."
    pip install google-generativeai --quiet
    echo "   ✅ インストール完了"
fi

echo ""
echo "✅ セットアップ完了！"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📌 次のステップ:"
echo "  1. GitHubのSecretsにGEMINI_API_KEYを設定"
echo "  2. Claudeに「今週の動画を作って」と話しかける"
echo "  3. 毎週月曜に自動でトレンドリサーチが走ります"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

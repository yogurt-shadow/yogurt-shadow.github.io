#!/bin/bash
# 快速部署脚本
# 用法: ./quick_deploy.sh [提交信息]

COMMIT_MSG="${1:-Update blog}"

echo "=== Fast Blog Deployment ==="

# 进入blog目录
cd "$(dirname "$0")" || exit 1

# 1. Generate static files
echo "1. Generating static files..."
hexo clean
hexo generate

# 1.5 Fix thumbnails
echo "1.5. Fixing thumbnails..."
python3 tools/fix-thumbnails.py || python tools/fix-thumbnails.py

# 1.6 Force light theme
echo "1.6. Forcing light theme..."
python3 tools/force-light.py || python tools/force-light.py

# 2. Copy to blog directory
echo "2. Copying files..."
cp -r public/* ./

# 3. Commit to Git
echo "3. Committing to Git..."
cd ..
git add .
git commit -m "$COMMIT_MSG"

# 4. Push to GitHub
echo "4. Pushing to GitHub..."
git push origin master

echo ""
echo "=== Deployment completed ==="
echo "Blog updated: https://yogurt-shadow.github.io/blog/"

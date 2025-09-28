#!/bin/bash
# 快速部署脚本
# 用法: ./quick_deploy.sh [提交信息]

COMMIT_MSG="${1:-Update blog}"

echo "=== 快速部署博客 ==="

# 进入blog目录
cd "$(dirname "$0")" || exit 1

# 1. 生成静态文件
echo "1. 生成静态文件..."
hexo clean
hexo generate

# 2. 复制到blog目录
echo "2. 复制文件..."
cp -r public/* ./

# 3. 提交到Git
echo "3. 提交到Git..."
cd ..
git add .
git commit -m "$COMMIT_MSG"

# 4. 推送到GitHub
echo "4. 推送到GitHub..."
git push origin master

echo ""
echo "=== 部署完成 ==="
echo "博客已更新: https://yogurt-shadow.github.io/blog/"

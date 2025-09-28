#!/bin/bash
# 预览博客的脚本
# 用法: ./preview.sh

echo "=== 启动博客预览服务器 ==="

# 进入blog目录
cd "$(dirname "$0")" || exit 1

echo "正在启动本地服务器..."
echo "博客将在 http://localhost:4000 打开"
echo "按 Ctrl+C 停止服务器"
echo ""

# 启动Hexo服务器
hexo server

#!/bin/bash
# 创建新文章的脚本
# 用法: ./new_post.sh "文章标题"

TITLE="$1"
if [ -z "$TITLE" ]; then
    echo "用法: $0 \"文章标题\""
    exit 1
fi

echo "=== 创建新文章: $TITLE ==="

# 进入blog目录
cd "$(dirname "$0")" || exit 1

# 创建新文章
hexo new "$TITLE"

echo "✓ 文章已创建"
echo "请编辑文件: source/_posts/$TITLE.md"
echo "编辑完成后运行: ./deploy.sh 来部署"

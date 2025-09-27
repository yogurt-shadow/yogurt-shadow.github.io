#!/bin/bash
# blog/new_post.sh
# 用法: ./new_post.sh "文章标题"
# 仅创建新文章的 Markdown 文件

TITLE="$1"
if [ -z "$TITLE" ]; then
    echo "Usage: $0 \"Post Title\""
    exit 1
fi

HEXODIR="$(cd "$(dirname "$0")"; pwd)"
cd "$HEXODIR" || exit 1

echo "Creating new post Markdown: $TITLE"
hexo new "$TITLE"

echo "Done! Edit the Markdown file in 'source/_posts/' before generating."

#!/bin/bash
# 创建新博客文章的脚本
# 用法: ./create_post.sh "文章标题" [分类] [标签]

TITLE="$1"
CATEGORY="${2:-General}"
TAGS="${3:-blog}"

if [ -z "$TITLE" ]; then
    echo "用法: $0 \"文章标题\" [分类] [标签]"
    echo ""
    echo "示例:"
    echo "  $0 \"我的新文章\""
    echo "  $0 \"研究进展\" \"Research\" \"formal-methods,SMT\""
    echo "  $0 \"技术分享\" \"Tech\" \"programming,algorithms\""
    exit 1
fi

echo "=== 创建新博客文章 ==="
echo "标题: $TITLE"
echo "分类: $CATEGORY"
echo "标签: $TAGS"
echo ""

# 进入blog目录
cd "$(dirname "$0")" || exit 1

# 创建新文章
echo "正在创建文章..."
hexo new "$TITLE"

# 获取生成的文件名（使用实际创建的文件）
POST_FILE=$(find source/_posts -name "*.md" -newer /tmp 2>/dev/null | head -1)

if [ -f "$POST_FILE" ]; then
    echo "✓ 文章文件已创建: $POST_FILE"
else
    # 如果找不到新文件，尝试使用标题作为文件名
    FILENAME=$(echo "$TITLE" | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9]/-/g' | sed 's/--*/-/g' | sed 's/^-\|-$//g')
    POST_FILE="source/_posts/$FILENAME.md"
    
    if [ -f "$POST_FILE" ]; then
        echo "✓ 文章文件已创建: $POST_FILE"
    else
        echo "✗ 文章文件创建失败"
        echo "请检查 source/_posts/ 目录"
        exit 1
    fi
fi

# 更新文章的前置信息
echo "正在更新文章配置..."
cat > "$POST_FILE" << EOF
---
title: $TITLE
date: $(date '+%Y-%m-%d %H:%M:%S')
tags: [$TAGS]
categories: [$CATEGORY]
---

# $TITLE

在这里开始写你的文章内容...

## 概述

在这里写文章的概述。

## 主要内容

在这里写文章的主要内容。

## 总结

在这里写文章的总结。

EOF

echo "✓ 文章配置已更新"
echo ""
echo "=== 下一步操作 ==="
echo "1. 编辑文章内容: $POST_FILE"
echo "2. 预览博客: hexo server"
echo "3. 部署到网站: ./deploy.sh"
echo ""
echo "文章已创建完成！"

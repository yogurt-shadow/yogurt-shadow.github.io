#!/bin/bash
# blog/new_public.sh
# 用法: ./new_public.sh
# 清理并生成 Hexo 静态文件，并同步到仓库根目录的 blog/

HEXODIR="$(cd "$(dirname "$0")"; pwd)"
cd "$HEXODIR" || exit 1

echo "Cleaning and generating static files..."
hexo clean
hexo g

# -----------------------------
# 同步 public/ 到 ../blog/
# -----------------------------
DEPLOY_DIR="../blog"
if [ ! -d "$DEPLOY_DIR" ]; then
    echo "Deploy directory $DEPLOY_DIR does not exist. Creating..."
    mkdir -p "$DEPLOY_DIR"
fi

echo "Copying generated static files to $DEPLOY_DIR ..."
cp -r public/* "$DEPLOY_DIR/"

echo "Done! Static files updated in '$DEPLOY_DIR'."

#!/bin/bash
# 自动化部署脚本
# 用法: ./deploy.sh

echo "=== Hexo 博客自动化部署 ==="

# 进入blog目录
cd "$(dirname "$0")" || exit 1

echo "当前目录: $(pwd)"

# 1. 清理旧文件
echo "1. 清理旧文件..."
hexo clean

# 2. 生成静态文件
echo "2. 生成静态文件..."
hexo generate

# 3. 检查生成结果
if [ ! -f "public/index.html" ]; then
    echo "错误: 无法生成静态文件"
    exit 1
fi

echo "✓ 静态文件生成成功"

# 4. 复制文件到blog目录（覆盖旧文件）
echo "3. 复制文件到blog目录..."
echo "复制所有静态文件..."

# 复制所有生成的文件到当前目录
cp -r public/* ./

# 5. 验证部署结果
echo "4. 验证部署结果..."
if [ -f "index.html" ]; then
    echo "✓ 主页面部署成功"
else
    echo "✗ 主页面部署失败"
fi

if [ -d "style" ]; then
    echo "✓ CSS文件部署成功"
else
    echo "✗ CSS文件部署失败"
fi

if [ -d "js" ]; then
    echo "✓ JS文件部署成功"
else
    echo "✗ JS文件部署失败"
fi

# 6. 显示文件结构
echo "5. 当前文件结构:"
ls -la | grep -E "\.(html|css|js)$|^d.*"

echo "=== 部署完成 ==="
echo "博客已成功部署到blog目录"
echo "现在可以访问: https://yogurt-shadow.github.io/blog/"

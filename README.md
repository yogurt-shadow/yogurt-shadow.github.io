# 个人主页项目

个人主页 + Hexo博客系统

## 🚀 创建新帖子

### 1. 创建新文章
```bash
cd blog
./create_post.sh "文章标题"
```

### 2. 编辑文章
编辑 `blog/source/_posts/文章标题.md` 文件

### 3. 预览博客
```bash
cd blog
./preview.sh
```
访问 http://localhost:4000

### 4. 部署到网站
```bash
cd blog
./quick_deploy.sh "更新博客"
```

## 🗑️ 删除帖子

### 删除文章
```bash
cd blog
rm source/_posts/文章标题.md
./quick_deploy.sh "删除文章"
```

## 📝 高级用法

### 指定分类和标签
```bash
cd blog
./create_post.sh "研究进展" "Research" "formal-methods,SMT"
```

### 常用分类
- `Research` - 研究相关
- `Tech` - 技术分享
- `General` - 一般内容

### 常用标签
- `formal-methods` - 形式化方法
- `SMT` - SMT求解
- `programming` - 编程
- `algorithms` - 算法

## 🔗 访问链接
- **主页**: https://yogurt-shadow.github.io/
- **博客**: https://yogurt-shadow.github.io/blog/
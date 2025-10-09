# Personal Website Project

Personal homepage + Hexo blog system

## 🚀 Creating New Posts

### 1. Create New Article
```bash
cd blog
./create_post.sh "Article Title"
```

### 2. Edit Article
Edit the `blog/source/_posts/Article Title.md` file

### 3. Preview Blog
```bash
cd blog
./preview.sh
```
Visit http://localhost:4000

### 4. Deploy to Website
```bash
cd blog
./quick_deploy.sh "Update blog"
```

Note:
- Hexo 生成的列表页缩略图可能与各 `post` 中 front matter 的 `img` 字段不一致。
- `blog/quick_deploy.sh` 在生成静态文件后，会自动调用 Python 脚本 `tools/fix-thumbnails.py` 批量修复 `public/**/*.html` 中的缩略图为对应 `post` 的 `img` 链接。
- 若服务端或本地环境未安装 Python3，可自行安装或手动跳过该步骤后再部署。

## 🗑️ Deleting Posts

### Delete Article
```bash
cd blog
rm source/_posts/Article Title.md
./quick_deploy.sh "Delete article"
```

## 📝 Advanced Usage

### Specify Categories and Tags
```bash
cd blog
./create_post.sh "Research Update" "Research" "formal-methods,SMT"
```

### Common Categories
- `Research` - Research related
- `Tech` - Technical sharing
- `General` - General content

### Common Tags
- `formal-methods` - Formal methods
- `SMT` - SMT solving
- `programming` - Programming
- `algorithms` - Algorithms

## 🔗 Access Links
- **Homepage**: https://yogurt-shadow.github.io/
- **Blog**: https://yogurt-shadow.github.io/blog/
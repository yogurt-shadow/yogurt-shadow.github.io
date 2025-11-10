"""
This script is used to fix the thumbnails in the blog posts.
"""

import os, sys, re
import html

class PostInfo:
    def __init__(self, date: str, title: str, img: str, tags: list[str], categories: list[str]):
        self.date = date
        self.title = title
        self.img = img
        self.tags = tags
        self.categories = categories

    def __str__(self):
        return f"PostInfo(date={self.date}, title={self.title}, img={self.img}, tags={self.tags}, categories={self.categories})"

    def __repr__(self):
        return self.__str__()

def scan_posts(posts_dir: str) -> dict:
    res = {}
    for file in os.listdir(posts_dir):
        if file.endswith(".md"):
            lines = open(os.path.join(posts_dir, file), "r", encoding="utf-8").readlines()
            date = None
            title = None
            img = None
            tags = None
            categories = None
            for line in lines:
                if "date:" in line:
                    date = line.replace("date: ", "").strip()
                elif "title:" in line:
                    title = line.replace("title: ", "").strip()
                elif "img:" in line:
                    img = line.replace("img: ", "").strip()
                elif "tags:" in line:
                    tags = line.replace("tags: ", "").strip()
                elif "categories:" in line:
                    categories = line.replace("categories: ", "").strip()
            res[file] = PostInfo(date, title, img, tags, categories)
    return res

html_paths = {
    "main": "../index.html",
    "tags": "../tags/",
    "public": "../public/index.html",
    "public_tags": "../public/tags/",
}

def fix_html_file(html_file: str, title_to_post: dict) -> bool:
    """
    修复单个 HTML 文件中的图片路径
    返回 True 如果文件被更新，False 如果无需更新
    """
    if not os.path.exists(html_file):
        print(f"文件不存在: {html_file}")
        return False
    
    # 读取 HTML 内容
    with open(html_file, "r", encoding="utf-8") as f:
        html_content = f.read()
    
    # 使用正则表达式找到每个 post-item section 中的标题和图片
    # 匹配模式：<h2 class="post-title">标题</h2> 和 <div class="feature-container" style="background-image: url('...');"></div>
    # 先找到所有 post-item sections
    section_pattern = r'(<section class="post-item">.*?</section>)'
    
    def replace_section(match):
        section = match.group(1)
        
        # 提取标题
        title_match = re.search(r'<h2 class="post-title">(.*?)</h2>', section)
        if not title_match:
            return section  # 如果没有标题，返回原内容
        
        title = title_match.group(1).strip()
        # 解码 HTML 实体（如 &#39; -> '）
        title_decoded = html.unescape(title)
        
        # 查找匹配的帖子（先尝试解码后的标题，再尝试原始标题）
        matched_post = None
        if title_decoded in title_to_post:
            matched_post = title_to_post[title_decoded]
        elif title in title_to_post:
            matched_post = title_to_post[title]
        
        if not matched_post:
            print(f"  警告: 未找到标题为 '{title}' (解码后: '{title_decoded}') 的帖子")
            return section
        
        post = matched_post
        if not post.img:
            print(f"  警告: '{title_decoded}' 没有图片信息")
            return section
        
        # 替换图片 URL
        # 匹配 background-image: url('...') 或 url("...")
        # 捕获引号类型（单引号或双引号）
        img_pattern = r'(<div class="feature-container" style="background-image: url\()([\'"])([^\'"]+)(\2)(\);"></div>)'
        
        def replace_img_url(img_match):
            prefix = img_match.group(1)
            quote = img_match.group(2)  # 引号类型（' 或 "）
            old_url = img_match.group(3)  # URL（不含引号）
            suffix = img_match.group(5)
            print(f"  替换 '{title_decoded}' 的图片: {old_url} -> {post.img}")
            # 使用相同的引号类型包裹新 URL
            return prefix + quote + post.img + quote + suffix
        
        new_section = re.sub(img_pattern, replace_img_url, section)
        return new_section
    
    # 执行替换
    new_html_content = re.sub(section_pattern, replace_section, html_content, flags=re.DOTALL)
    
    # 写回文件
    if new_html_content != html_content:
        with open(html_file, "w", encoding="utf-8") as f:
            f.write(new_html_content)
        print(f"已更新: {html_file}")
        return True
    else:
        print(f"无需更新: {html_file}")
        return False

def fix_html_directory(dir_path: str, title_to_post: dict):
    """
    递归处理目录下所有 HTML 文件
    """
    if not os.path.exists(dir_path):
        print(f"目录不存在: {dir_path}")
        return
    
    html_files = []
    # 递归查找所有 HTML 文件
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if file.endswith(".html"):
                html_files.append(os.path.join(root, file))
    
    if not html_files:
        print(f"目录中没有找到 HTML 文件: {dir_path}")
        return
    
    print(f"\n处理目录: {dir_path} (找到 {len(html_files)} 个 HTML 文件)")
    for html_file in html_files:
        fix_html_file(html_file, title_to_post)

def fix_all_html(post_info: dict):
    """
    处理所有路径下的 HTML 文件
    """
    # 创建一个标题到 PostInfo 的映射
    title_to_post = {}
    for file, info in post_info.items():
        if info.title:
            title_to_post[info.title] = info
    
    # 处理所有路径
    for key, path in html_paths.items():
        print(f"\n=== 处理路径: {key} ===")
        if os.path.isfile(path):
            # 单个文件
            fix_html_file(path, title_to_post)
        elif os.path.isdir(path):
            # 目录
            fix_html_directory(path, title_to_post)
        else:
            print(f"路径不存在: {path}")

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    print(f"工作目录: {os.getcwd()}")
    post_info = scan_posts(os.path.join(os.getcwd(), "../source", "_posts"))
    print(f"扫描到 {len(post_info)} 个帖子")
    fix_all_html(post_info)
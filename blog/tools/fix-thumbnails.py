#!/usr/bin/env python3
import re
import sys
from pathlib import Path


def build_slug_to_img_map(posts_dir: Path) -> dict:
    slug_to_img = {}
    if not posts_dir.exists():
        return slug_to_img
    for md_path in posts_dir.glob("*.md"):
        try:
            text = md_path.read_text(encoding="utf-8")
        except Exception:
            continue

        fm_match = re.search(r"^---\s*([\s\S]*?)\s*---", text, flags=re.MULTILINE)
        if not fm_match:
            continue
        front_matter = fm_match.group(1)

        slug = md_path.stem
        img_match = re.search(r"^\s*img:\s*(.+)$", front_matter, flags=re.MULTILINE)
        if not img_match:
            continue
        img_url = img_match.group(1).strip()
        slug_to_img[slug] = img_url
    return slug_to_img


def replace_thumbnails_in_html(public_dir: Path, slug_to_img: dict) -> int:
    replaced = 0
    for html_path in public_dir.rglob("*.html"):
        try:
            html = html_path.read_text(encoding="utf-8")
        except Exception:
            continue

        original_html = html

        for m in re.finditer(r"href=\"/blog/\d{4}/\d{2}/\d{2}/([^/]+)/\"", html):
            slug = m.group(1)
            if slug not in slug_to_img:
                continue
            img_url = slug_to_img[slug]
            html = re.sub(r'(class="feature-container"[^>]*background-image:\s*url\()([\'\"]?)([^)\'\"]+)([\'\"]?)(\))',
                          lambda mm: mm.group(1) + mm.group(2) + img_url + mm.group(4) + mm.group(5),
                          html)

        if html != original_html:
            try:
                html_path.write_text(html, encoding="utf-8")
                replaced += 1
            except Exception:
                pass

    return replaced


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    posts_dir = repo_root / "source" / "_posts"
    public_dir = repo_root / "public"

    slug_to_img = build_slug_to_img_map(posts_dir)
    if not slug_to_img:
        print("No posts with img found; nothing to replace.")
        return 0

    count = replace_thumbnails_in_html(public_dir, slug_to_img)
    print(f"Updated thumbnails in {count} HTML files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())



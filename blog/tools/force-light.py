#!/usr/bin/env python3
import re
from pathlib import Path


def force_light_in_html(public_dir: Path) -> int:
    replaced = 0
    pattern = re.compile(r"<script>!function\(\)\{var e=window\.matchMedia&&window\.matchMedia\(\(\"prefers-color-scheme: dark\"\)\)\.matches,t=localStorage\.getItem\(\"use-color-scheme\"\)\|\|\"auto\";\(\"dark\"===t\|\|e&&\"light\"!==t\)&&document\.documentElement\.classList\.toggle\(\"dark\",!0\)\}\<\)/script>")
    # Use a more lenient pattern due to minified differences
    fuzzy = re.compile(r"<script>!function\(\)\{var e=window\.matchMedia[\s\S]*?document\.documentElement\.classList\.toggle\(\"dark\",!0\)\}\(\)\)</script>")
    replacement = '<script>document.documentElement.classList.remove("dark");try{localStorage.setItem("use-color-scheme","light")}catch(e){}</script>'

    for html_path in public_dir.rglob("*.html"):
        try:
            html = html_path.read_text(encoding="utf-8")
        except Exception:
            continue

        new_html = fuzzy.sub(replacement, html)
        if new_html != html:
            try:
                html_path.write_text(new_html, encoding="utf-8")
                replaced += 1
            except Exception:
                pass
    return replaced


def main() -> int:
    public_dir = Path(__file__).resolve().parents[1] / "public"
    count = force_light_in_html(public_dir)
    print(f"Forced light mode in {count} HTML files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())



#!/usr/bin/env python3
import re
from pathlib import Path


def force_light_in_html(public_dir: Path) -> int:
    updated = 0
    injection = '\n<script>try{localStorage.setItem("use-color-scheme","light");}catch(e){};document.documentElement.classList.remove("dark");</script>\n'
    head_close_re = re.compile(r"</head>", re.IGNORECASE)

    for html_path in public_dir.rglob("*.html"):
        try:
            html = html_path.read_text(encoding="utf-8")
        except Exception:
            continue

        # If already contains our injection, skip
        if 'localStorage.setItem("use-color-scheme","light")' in html:
            continue

        # Insert just before </head>
        new_html, count = head_close_re.subn(injection + '</head>', html, count=1)
        if count:
            try:
                html_path.write_text(new_html, encoding="utf-8")
                updated += 1
            except Exception:
                pass
    return updated


def main() -> int:
    public_dir = Path(__file__).resolve().parents[1] / "public"
    count = force_light_in_html(public_dir)
    print(f"Forced light mode in {count} HTML files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())



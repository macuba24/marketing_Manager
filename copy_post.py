#!/usr/bin/env python3
"""Copy next unpublished LinkedIn post body to the clipboard (Windows-friendly).

Usage:
  python copy_post.py           # next unpublished → clipboard
  python copy_post.py --list    # show queue
  python copy_post.py --done    # mark last copied post as published
  python copy_post.py --file 2026-09-01_post-01.md
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
POSTS = ROOT / "marketing" / "posts"
PUBLISHED = POSTS / ".published"
LAST = POSTS / ".last_copied"
POST_RE = re.compile(r"^\d{4}-\d{2}-\d{2}_post-\d+\.md$", re.I)


def list_post_files() -> list[Path]:
    if not POSTS.is_dir():
        raise SystemExit(f"Missing folder: {POSTS}")
    files = [p for p in POSTS.iterdir() if p.is_file() and POST_RE.match(p.name)]
    return sorted(files, key=lambda p: p.name)


def load_published() -> set[str]:
    if not PUBLISHED.exists():
        return set()
    return {
        line.strip()
        for line in PUBLISHED.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.strip().startswith("#")
    }


def mark_published(name: str) -> None:
    done = load_published()
    done.add(name)
    lines = ["# Published LinkedIn posts (one filename per line)", *sorted(done)]
    PUBLISHED.write_text("\n".join(lines) + "\n", encoding="utf-8")


def next_unpublished() -> Path | None:
    published = load_published()
    for path in list_post_files():
        if path.name not in published:
            return path
    return None


def extract_body(markdown: str) -> str:
    """Prefer section '## Fertig zum Posten'; else strip metadata headers."""
    marker = re.search(r"^##\s+Fertig zum Posten\s*$", markdown, re.M | re.I)
    if marker:
        rest = markdown[marker.end() :]
        next_h2 = re.search(r"^##\s+", rest, re.M)
        body = rest[: next_h2.start()] if next_h2 else rest
        return body.strip() + "\n"

    # Fallback: drop leading YAML/meta until first blank line after title block
    lines = markdown.splitlines()
    out: list[str] = []
    started = False
    for line in lines:
        if not started:
            if line.startswith("#") or line.startswith("**") or line.strip() == "---" or not line.strip():
                continue
            started = True
        out.append(line)
    return "\n".join(out).strip() + "\n"


def copy_to_clipboard(text: str) -> None:
    """Windows: clip.exe (UTF-16). Fallback: PowerShell Set-Clipboard."""
    try:
        subprocess.run(
            ["clip"],
            input=text.encode("utf-16le"),
            check=True,
        )
        return
    except (FileNotFoundError, subprocess.CalledProcessError):
        pass

    # PowerShell fallback (handles Unicode well)
    ps = (
        "Set-Clipboard -Value ([Console]::In.ReadToEnd())"
    )
    subprocess.run(
        ["powershell", "-NoProfile", "-Command", ps],
        input=text.encode("utf-8"),
        check=True,
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Copy next LinkedIn post to clipboard")
    parser.add_argument("--list", action="store_true", help="Show published / pending queue")
    parser.add_argument("--done", action="store_true", help="Mark last copied post as published")
    parser.add_argument("--file", metavar="NAME", help="Copy a specific post filename")
    parser.add_argument("--dry-run", action="store_true", help="Print body, do not copy")
    args = parser.parse_args()

    if args.list:
        published = load_published()
        print("Pending:")
        for p in list_post_files():
            flag = "✓" if p.name in published else "·"
            print(f"  {flag} {p.name}")
        return 0

    if args.done:
        if not LAST.exists():
            print("Nothing to mark — run copy_post.py first.", file=sys.stderr)
            return 1
        name = LAST.read_text(encoding="utf-8").strip()
        mark_published(name)
        print(f"Marked published: {name}")
        return 0

    if args.file:
        path = POSTS / args.file
        if not path.is_file():
            print(f"Not found: {path}", file=sys.stderr)
            return 1
    else:
        path = next_unpublished()
        if path is None:
            print("All posts are marked published. Add new files under marketing/posts/")
            return 0

    body = extract_body(path.read_text(encoding="utf-8"))
    if args.dry_run:
        print(f"--- {path.name} ---")
        print(body, end="")
        return 0

    copy_to_clipboard(body)
    LAST.write_text(path.name + "\n", encoding="utf-8")
    print(f"Copied to clipboard: {path.name}")
    print("Paste into LinkedIn, then run:  python copy_post.py --done")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Repository sweep: internal links, anchors, and orphans.

Run from the repository root:  python3 check_links.py

Checks every markdown file in the tree for
  1. relative links whose target file does not exist,
  2. anchors whose target heading or explicit <a id> does not exist,
  3. markdown files nothing else links to (orphans).

Stdlib only; deterministic; no network. A finding here is a defect worth fixing
before a push, not an opinion.
"""
import io, os, re, sys, urllib.parse

SKIP_DIRS = {".git", "_site", "node_modules", ".jekyll-cache"}

# Files that are deliberately reachable from nowhere, with the reason. A tombstone that
# explains itself is not an orphan; anything else in this list needs justifying here.
ALLOWED_UNLINKED = {
    os.path.normpath("./OUTLINE.md"):
        "tombstone: the outline moved into MAP.md Part I on 23 August 2026; the path is kept "
        "so the working folder explains itself, and is deliberately linked from nowhere.",
}

def md_files():
    out = []
    for root, dirs, files in os.walk("."):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for f in files:
            if f.endswith(".md"):
                out.append(os.path.normpath(os.path.join(root, f)))
    return sorted(out)

def slug(h):
    """GitHub's heading-anchor rule, near enough for this repository."""
    s = h.strip().lower()
    s = re.sub(r"`([^`]*)`", r"\1", s)
    s = re.sub(r"\*\*|\*|__|_", "", s)
    s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)
    s = re.sub(r"[^\w\s-]", "", s, flags=re.UNICODE)
    s = s.replace(" ", "-")
    return s

def anchors_of(path):
    try:
        t = io.open(path, encoding="utf-8").read()
    except OSError:
        return set()
    a = set()
    seen = {}
    for m in re.finditer(r"(?m)^(#{1,6})\s+(.*)$", t):
        base = slug(m.group(2))
        # GitHub disambiguates repeated headings by appending -1, -2, ...
        k = seen.get(base, 0)
        a.add(base if k == 0 else f"{base}-{k}")
        seen[base] = k + 1
    for m in re.finditer(r'<a\s+id=["\']([^"\']+)["\']', t):
        a.add(m.group(1))
    for m in re.finditer(r'\bid=["\']([^"\']+)["\']', t):
        a.add(m.group(1))
    return a

LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")

def main():
    files = md_files()
    known = {f: anchors_of(f) for f in files}
    linked = set()
    dead_files, dead_anchors = [], []

    for f in files:
        t = io.open(f, encoding="utf-8").read()
        base = os.path.dirname(f)
        for m in LINK.finditer(t):
            href = m.group(1)
            if href.startswith(("http://", "https://", "mailto:", "tel:", "data:")):
                continue
            line = t[:m.start()].count("\n") + 1
            path, _, frag = href.partition("#")
            path = urllib.parse.unquote(path)
            frag = urllib.parse.unquote(frag)
            if not path:                       # same-file anchor
                target = f
            else:
                target = os.path.normpath(os.path.join(base, path))
                # the site serves .html; the repository holds .md
                cand = [target]
                if target.endswith(".html"):
                    cand.append(target[:-5] + ".md")
                if os.path.isdir(target):
                    cand.append(os.path.join(target, "README.md"))
                hit = next((c for c in cand if os.path.exists(c)), None)
                if hit is None:
                    dead_files.append((f, line, href))
                    continue
                target = hit
                linked.add(target)
            if frag:
                if target.endswith(".md") and frag not in known.get(target, set()):
                    dead_anchors.append((f, line, href))

    orphans = [f for f in files
               if f not in linked
               and os.path.basename(f) not in ("README.md",)
               and f not in ALLOWED_UNLINKED
               and not f.startswith(os.path.join(".", "archive"))]

    print("REPOSITORY LINK SWEEP")
    print(f"  markdown files ......... {len(files)}")
    print(f"  dead file links ........ {len(dead_files)}")
    print(f"  dead anchors ........... {len(dead_anchors)}")
    print(f"  unlinked markdown ...... {len(orphans)}")
    for label, rows in (("DEAD FILE LINK", dead_files), ("DEAD ANCHOR", dead_anchors)):
        for f, line, href in rows:
            print(f"  [{label}] {f}:{line} -> {href}")
    for f in orphans:
        print(f"  [UNLINKED] {f}")
    for f, why in sorted(ALLOWED_UNLINKED.items()):
        if os.path.exists(f):
            print(f"  [unlinked, allowed] {f} - {why}")
    return 1 if (dead_files or dead_anchors) else 0

if __name__ == "__main__":
    sys.exit(main())

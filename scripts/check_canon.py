#!/usr/bin/env python3
"""Doc checks for the workspace canon. Stdlib only.

Three checks over tracked files:

  em-dash   no U+2014 in any tracked .md file
  links     every relative markdown link resolves to a tracked file or directory
  index     the "Rules of record" section of CLAUDE.md and AGENTS.md is identical

Run `python scripts/check_canon.py` from the repository root. Exit status 1 when
any check finds a problem; every problem prints as `path:line: message`.
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote

EM_DASH = chr(0x2014)
INDEX_HEADING = "## Rules of record"
INDEX_FILES = ("CLAUDE.md", "AGENTS.md")

FENCE = re.compile(r"^\s*(```|~~~)")
INLINE_LINK = re.compile(r"!?\[[^\]]*\]\(\s*(<[^>]*>|[^)\s]*)[^)]*\)")
REFERENCE_DEF = re.compile(r"^\s{0,3}\[[^\]]+\]:\s*(<[^>]*>|\S+)")
INLINE_CODE = re.compile(r"`[^`]*`")
SCHEME = re.compile(r"^[a-zA-Z][a-zA-Z0-9+.-]*:")


def tracked(root: Path) -> list[str]:
    out = subprocess.run(
        ["git", "ls-files", "-z"], cwd=root, check=True, capture_output=True, text=True
    ).stdout
    return [name for name in out.split("\0") if name]


def read_lines(path: Path) -> list[str]:
    return path.read_text(encoding="utf-8").replace("\r\n", "\n").split("\n")


def check_em_dash(root: Path, markdown: list[str]) -> list[str]:
    problems = []
    for name in markdown:
        for number, line in enumerate(read_lines(root / name), 1):
            if EM_DASH in line:
                problems.append(f"{name}:{number}: em-dash (U+2014)")
    return problems


def link_targets(line: str) -> list[str]:
    targets = [m.group(1) for m in INLINE_LINK.finditer(INLINE_CODE.sub("", line))]
    reference = REFERENCE_DEF.match(line)
    if reference:
        targets.append(reference.group(1))
    return [t.strip("<>") for t in targets]


def resolves(root: Path, source: str, target: str, files: set[str], dirs: set[str]) -> bool:
    path = unquote(target.split("#", 1)[0].split("?", 1)[0])
    if not path:
        return True
    base = Path(source).parent
    joined = (base / path.lstrip("/")) if not path.startswith("/") else Path(path.lstrip("/"))
    parts: list[str] = []
    for part in joined.as_posix().split("/"):
        if part in ("", "."):
            continue
        if part == "..":
            if not parts:
                return False
            parts.pop()
        else:
            parts.append(part)
    resolved = "/".join(parts)
    return resolved == "" or resolved in files or resolved in dirs


def check_links(root: Path, markdown: list[str], all_files: list[str]) -> list[str]:
    files = set(all_files)
    dirs = {"/".join(f.split("/")[:i]) for f in all_files for i in range(1, len(f.split("/")))}
    problems = []
    for name in markdown:
        in_fence = False
        for number, line in enumerate(read_lines(root / name), 1):
            if FENCE.match(line):
                in_fence = not in_fence
                continue
            if in_fence:
                continue
            for target in link_targets(line):
                if not target or target.startswith("#") or SCHEME.match(target) or target.startswith("//"):
                    continue
                if not resolves(root, name, target, files, dirs):
                    problems.append(f"{name}:{number}: relative link does not resolve to a tracked file: {target}")
    return problems


def index_section(root: Path, name: str) -> list[str] | None:
    lines = read_lines(root / name)
    for start, line in enumerate(lines):
        if line.strip() == INDEX_HEADING:
            end = next((i for i in range(start + 1, len(lines)) if lines[i].startswith("## ")), len(lines))
            return lines[start:end]
    return None


def check_index(root: Path) -> list[str]:
    sections = {name: index_section(root, name) for name in INDEX_FILES}
    problems = [f"{n}:1: no '{INDEX_HEADING}' section" for n, s in sections.items() if s is None]
    if problems:
        return problems
    first, second = (sections[n] for n in INDEX_FILES)
    assert first is not None and second is not None
    if first == second:
        return []
    for offset, (a, b) in enumerate(zip(first, second)):
        if a != b:
            return [
                f"{INDEX_FILES[0]} and {INDEX_FILES[1]}: '{INDEX_HEADING}' sections differ at "
                f"section line {offset + 1}",
                f"  {INDEX_FILES[0]}: {a[:120]}",
                f"  {INDEX_FILES[1]}: {b[:120]}",
            ]
    return [
        f"{INDEX_FILES[0]} and {INDEX_FILES[1]}: '{INDEX_HEADING}' sections differ in length "
        f"({len(first)} vs {len(second)} lines)"
    ]


def main() -> int:
    root = Path(subprocess.run(["git", "rev-parse", "--show-toplevel"], check=True, capture_output=True, text=True).stdout.strip())
    all_files = tracked(root)
    markdown = [f for f in all_files if f.lower().endswith(".md")]
    results = {
        "em-dash": check_em_dash(root, markdown),
        "links": check_links(root, markdown, all_files),
        "index": check_index(root),
    }
    failed = False
    for name, problems in results.items():
        print(f"{name}: {'FAIL' if problems else 'ok'} ({len(markdown)} markdown files)")
        for problem in problems:
            print(f"  {problem}")
        failed = failed or bool(problems)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())

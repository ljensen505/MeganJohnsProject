#!/usr/bin/env python3

from pathlib import Path
from subprocess import run

UTF8 = "utf-8"


def bump():
    tags = [int(tag) for tag in find_tags() if tag.isnumeric()]
    tag_name = max(tags) + 1
    cmds = [f"git tag {tag_name}", f"git push origin tag {tag_name}"]
    for cmd in cmds:
        cmd = cmd.split(" ")
        output = run(cmd, capture_output=True, encoding=UTF8)
        if output.stdout:
            print(output.stdout)
        if output.stderr:
            print(output.stderr)


def find_tags() -> list[str]:
    dot_git = find_git_dir()
    tags_dir = dot_git / "refs" / "tags"
    for _, _, files in tags_dir.walk():
        return files
    raise Exception("Error parsing tags")


def find_git_dir() -> Path:
    dot_git = ".git"

    def _find_git_dir(cwd: Path = Path(__file__)) -> Path:
        for _, dirs, _ in cwd.walk(top_down=False):
            if dot_git in dirs:
                return cwd / dot_git
        return _find_git_dir(cwd.parent)

    return _find_git_dir()


if __name__ == "__main__":
    bump()

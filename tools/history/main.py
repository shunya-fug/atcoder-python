import subprocess
from dataclasses import dataclass
import re
from collections import defaultdict
from datetime import date


@dataclass
class Message:
    status: str
    branch: str
    problem: str

    def __init__(self, message: str):
        self.status, self.branch, self.problem = re.split(r"[： ]", message)


@dataclass
class Commit:
    day: str
    message: Message

    def __init__(self, row: str):
        self.day, message = row.split(",", 1)
        self.message = Message(message)


def print_date(day: str):
    diff = (date.today() - date.fromisoformat(day)).days
    if diff >= 7:
        print("\033[31m", end="")
    elif diff >= 3:
        print("\033[33m", end="")

    print(f"# {day} ({diff} days ago)", end="\033[0m\n")


if __name__ == "__main__":
    # ブランチ名一覧取得(main, settingは除外)
    branches = subprocess.run(
        "git branch | sed 's/^\* //' | tr -d ' ' | grep -vE '^(main|setting)$' | tr '\n' ',' | sed 's/,$//'",
        shell=True,
        capture_output=True,
        text=True,
    ).stdout.split(",")

    # key: 日付, value: Commitのリスト
    history = defaultdict(list)
    for branch in branches:
        log = subprocess.run(
            f"git log --no-merges --pretty=format:'%cs,%s' --first-parent {branch} --grep='[✅|📌]'",
            shell=True,
            capture_output=True,
            text=True,
        ).stdout.split("\n")
        log.reverse()
        h = {commit.message.problem: commit for commit in map(Commit, log)}
        h = {k: v for k, v in h.items() if v.message.status == "📌"}
        for _, commit in h.items():
            history[commit.day].append(commit)

    for day, commits in sorted(history.items()):
        print_date(day)
        for commit in commits:
            print(f"- {commit.message.branch} {commit.message.problem}")
        print("")

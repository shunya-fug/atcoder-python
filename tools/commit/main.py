import argparse
import questionary
import subprocess
from questionary import Choice
from pathlib import Path

def get_branch_name(filepath: str) -> str:
    """ ファイルパスからブランチ名を取得する

    Examples:
        `/workspaces/atcoder-python/contest/abc297/a/main.py`
        -> `abc297`
    """
    p = Path(filepath)
    return p.parent.parent.name

def get_problem_name(filepath: str) -> str:
    """ ファイルパスから問題名を取得する

    Examples:
        `/workspaces/atcoder-python/contest/abc297/a/main.py`
        -> `abc297 a`
    """
    p = Path(filepath)
    return f"{get_branch_name(filepath)} {p.parent.name.upper()}"


parser = argparse.ArgumentParser()
parser.add_argument("filepath")
problem_name = get_problem_name(parser.parse_args().filepath)

icon = questionary.select(
    "結果を選択",
    choices=[
        Choice(title="🚧: WA", value="🚧"),
        Choice(title="📌: AC(要復習)", value="📌"),
        Choice(title="✅: AC", value="✅"),
    ],
    use_shortcuts=True,
).ask()

subprocess.run(["git", "checkout", f"{get_branch_name(parser.parse_args().filepath)}"])
subprocess.run(["git", "add", parser.parse_args().filepath])
subprocess.run(["git", "commit", "-m", f"{icon}：{problem_name}", "--", parser.parse_args().filepath])

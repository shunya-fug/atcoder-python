"""
abc300 C
"""
from itertools import product


def correct(section):
    """区間がバツ印かどうか

    Args:
        section (list): 区間

    Returns:
        bool: バツ印かどうか
    """
    for i, j in product(range(len(section)), range(len(section[0]))):
        if (i == j or len(section) - i - 1 == j) and section[i][j] != "#":
            return False
    return True


H, W = map(int, input().split())
C = [input() for _ in range(H)]

N = min(H, W)
searched = set()
ans = [0 for _ in range(N)]
for n in reversed(range(1, N + 1)):
    for i, j in product(range(n, H - n), range(n, W - n)):
        section = [c[j - n : j + n + 1] for c in C[i - n : i + n + 1]]
        if correct(section) and (i, j) not in searched:
            ans[n - 1] += 1
            searched.add((i, j))

print(" ".join(map(str, ans)))

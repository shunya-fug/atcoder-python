"""
abc298 A
"""
N = int(input())
S = input()


def is_ok(s: str):
    if s.count("x") >= 1:
        return False
    elif s.count("o") == 0:
        return False
    else:
        return True


print("Yes" if is_ok(S) else "No")

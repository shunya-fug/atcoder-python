"""
abc293 C
"""
H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

ans = []


def rec(i, j, history: set):
    if i == H - 1 and j == W - 1:
        ans.append(history)
        return

    if i + 1 < H and A[i + 1][j] not in history:
        rec(i + 1, j, history | {A[i + 1][j]})
    if j + 1 < W and A[i][j + 1] not in history:
        rec(i, j + 1, history | {A[i][j + 1]})


rec(0, 0, {A[0][0]})

print(len(ans))

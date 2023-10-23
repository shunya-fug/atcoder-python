"""
abc325 b
"""
N = int(input())
W, X = [], []
for _ in range(N):
    w, x = map(int, input().split())
    W.append(w)
    X.append(x)

ans: int = 0
for t_g in range(24):
    total: int = 0
    for w, x in zip(W, X):
        t_l = (t_g + x) % 24
        if 9 <= t_l < 18:
            total += w
    ans = max(ans, total)

print(ans)

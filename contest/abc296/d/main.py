"""
abc296 D
"""
from math import inf

N, M = map(int, input().split())

ans = inf
for i in range(1, N + 1):
    x = (M + i - 1) // i
    if x <= N:
        ans = min(ans, i * x)
    if i > x:
        break

print(ans if ans != inf else -1)

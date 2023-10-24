"""
abc301 B
"""
from more_itertools import windowed

N = int(input())
A = list(map(int, input().split()))

ans = []
for l, r in windowed(A, 2):
    for n in range(l, r, 1 if l < r else -1):
        ans.append(n)
ans.append(A[-1])

print(" ".join(map(str, ans)))

"""
abc297 A
"""
from itertools import pairwise

N, D = map(int, input().split())
T = list(map(int, input().split()))

for t1, t2 in pairwise(T):
    if t2 - t1 <= D:
        print(t2)
        exit()

print(-1)

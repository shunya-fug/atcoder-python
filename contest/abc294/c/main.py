"""
abc294 C
"""
from bisect import bisect_left

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

l = A + B
l.sort()
print(" ".join([str(bisect_left(l, a) + 1) for a in A]))
print(" ".join([str(bisect_left(l, b) + 1) for b in B]))

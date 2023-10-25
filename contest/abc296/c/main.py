"""
abc296 C
"""
from bisect import bisect_left

N, X = map(int, input().split())
A = list(map(int, input().split()))

A.sort()
for j in range(N):
    i = bisect_left(A, A[j] + X)
    if i != len(A) and A[i] - A[j] == X:
        print("Yes")
        exit()

print("No")

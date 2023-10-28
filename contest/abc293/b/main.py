"""
abc293 B
"""
from sortedcontainers import SortedList

N = int(input())
A = list(map(int, input().split()))

A_sorted = SortedList(range(1, N + 1))
called = set()
for i, a in enumerate(A, 1):
    if i not in called:
        called.add(a)
        A_sorted.discard(a)

print(len(A_sorted))
print(" ".join(map(str, A_sorted)))

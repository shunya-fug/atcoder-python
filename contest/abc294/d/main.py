"""
abc294 D
"""
from collections import deque
from sortedcontainers import SortedList

N, Q = map(int, input().split())

waiting = deque([n for n in range(1, N + 1)])
called = SortedList()
for _ in range(Q):
    query = list(map(int, input().split()))
    match query[0]:
        case 1:
            called.add(waiting.popleft())
        case 2:
            x = query[1]
            called.remove(x)
        case 3:
            print(called[0])

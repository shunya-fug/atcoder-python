"""
abc293 D
"""
from collections import deque

N, M = map(int, input().split())
G = [[] for _ in range(N + 1)]
deg = [0 for _ in range(N + 1)]
for _ in range(M):
    a, b, c, d = input().split()
    G[int(a)].append(int(c))
    G[int(c)].append(int(a))
    deg[int(a)] += 1
    deg[int(c)] += 1

x, y = 0, 0
used = set()
for i in range(1, N + 1):
    if i in used:
        continue

    Q = deque()
    Q.append(i)
    used.add(i)
    f = True
    while Q:
        元 = Q.popleft()
        if deg[元] != 2:
            f = False

        for 先 in G[元]:
            if 先 in used:
                continue

            Q.append(先)
            used.add(先)

    if f:
        x += 1
    else:
        y += 1

print(x, y)

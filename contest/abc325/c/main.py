"""
abc325 c
"""
from collections import deque
from itertools import product

H, W = map(int, input().split())
S = [input() for _ in range(H)]

DX = [-1, 0, 1, -1, 1, -1, 0, 1]
DY = [-1, -1, -1, 0, 0, 1, 1, 1]

ans: int = 0
searched = [[False for _ in range(W)] for _ in range(H)]
for y, x in product(range(H), range(W)):
    if S[y][x] == '#' and searched[y][x] is False:
        ans += 1
        q = deque([(y, x)])
        while len(q) > 0:
            y, x = q.pop()
            for dy, dx in product(DY, DX):
                ny, nx = y + dy, x + dx
                if 0 <= nx < W and 0 <= ny < H and searched[ny][nx] is False:
                    searched[ny][nx] = True
                    if S[ny][nx] == '#':
                        q.append((ny, nx))

print(ans)

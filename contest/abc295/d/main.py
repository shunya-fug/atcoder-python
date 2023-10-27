"""
abc295 D
"""
from collections import Counter
from math import comb

S = input()

history = [0]
for c in S:
    history.append(history[-1] ^ (1 << int(c)))

ans = 0
for v in Counter(history).values():
    ans += comb(v, 2)

print(ans)

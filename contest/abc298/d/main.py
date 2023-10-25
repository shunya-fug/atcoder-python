"""
abc298 D
"""
from collections import deque

MOD = 998244353

Q = int(input())
query = [[int(i) for i in input().split()] for _ in range(Q)]

s = deque([1])
n = 1
for q in query:
    match q[0]:
        case 1:
            x = q[1]
            s.append(x)
            n = n * 10 + x
            n %= MOD
        case 2:
            l = s.popleft()
            n -= l * pow(10, len(s), MOD)
            n %= MOD
        case 3:
            print(n)

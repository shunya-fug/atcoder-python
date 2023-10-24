"""
abc299 B
"""
N, T = map(int, input().split())
C = list(map(int, input().split()))
R = list(map(int, input().split()))

t = T if T in C else C[0]
ans = C.index(t) + 1
for i, (c, r) in enumerate(zip(C, R), 1):
    if c == t and r > R[ans - 1]:
        ans = i

print(ans)

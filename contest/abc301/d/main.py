"""
abc301 D
"""
S = input()
N = int(input())

s = int(S.replace("?", "0"), 2)
if s > N:
    print(-1)
else:
    S_rev = S[::-1]
    for i in reversed(range(len(S))):
        if S_rev[i] == "?" and (s | 1 << i) <= N:
            s |= 1 << i
    print(s)

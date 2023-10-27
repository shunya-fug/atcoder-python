"""
abc294 B
"""
from string import ascii_uppercase

H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

S = "." + ascii_uppercase
for a in A:
    print("".join(map(lambda x: S[x], a)))

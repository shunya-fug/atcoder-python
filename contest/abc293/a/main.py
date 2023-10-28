"""
abc293 A
"""
from more_itertools import chunked

S = input()

ans = ""
for s in chunked(S, 2):
    ans += s[1] + s[0]

print(ans)

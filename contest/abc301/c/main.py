"""
abc301 C
"""
from collections import Counter
from string import ascii_lowercase

S = input()
T = input()

c_s = Counter(S)
c_t = Counter(T)

for c in "atcoder":
    if c_t[c] > c_s[c]:
        c_s["@"] -= c_t[c] - c_s[c]
        c_s[c] += c_t[c] - c_s[c]
    elif c_s[c] > c_t[c]:
        c_t["@"] -= c_s[c] - c_t[c]
        c_t[c] += c_s[c] - c_t[c]

if c_s["@"] < 0 or c_t["@"] < 0:
    print("No")
else:
    for c in ascii_lowercase + "@":
        if c_s[c] != c_t[c]:
            print("No")
            exit()
    print("Yes")

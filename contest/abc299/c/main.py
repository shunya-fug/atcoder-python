"""
abc299 C
"""
N = int(input())
S = input()

if S.find("o") == -1 or S.find("-") == -1:
    print(-1)
else:
    ans, count = 0, 0
    for c in S:
        if c == "o":
            count += 1
        else:
            count = 0
        ans = max(ans, count)
    print(ans)

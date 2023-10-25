"""
abc297 C
"""
H, W = map(int, input().split())
S = [input() for _ in range(H)]

for i in range(H):
    for j in range(len(S[i]) - 1):
        if S[i][j] == S[i][j + 1] == "T":
            S[i] = S[i][:j] + "PC" + S[i][j + 2 :]

print("\n".join(S))

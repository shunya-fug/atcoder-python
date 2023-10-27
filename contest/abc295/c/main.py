"""
abc295 C
"""
N = int(input())
A = list(map(int, input().split()))

A.sort()

ans = 0
for i in range(N - 1):
    if A[i] == A[i + 1]:
        A[i] = A[i + 1] = 0
        ans += 1

print(ans)

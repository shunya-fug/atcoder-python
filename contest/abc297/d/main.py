"""
abc297 D
"""
A, B = map(int, input().split())

ans = 0
while A != B:
    if A < B:
        A, B = B, A

    n = (A - B) // B
    if A - B * n == B:
        A = A - B * n
        ans += n
    else:
        A = A - B * (n + 1)
        ans += n + 1

print(ans)

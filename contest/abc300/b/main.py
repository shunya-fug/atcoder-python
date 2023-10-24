"""
abc300 B
"""
H, W = map(int, input().split())
A = [input() for _ in range(H)]
B = [input() for _ in range(H)]

A_rotate = A
for _ in range(H):
    A_rotate = A_rotate[1:] + A_rotate[:1]
    for _ in range(W):
        A_rotate = [A_rotate[i][1:] + A_rotate[i][:1] for i in range(H)]
        if A_rotate == B:
            print("Yes")
            exit()
print("No")

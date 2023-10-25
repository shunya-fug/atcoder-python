"""
abc298 B
"""
from itertools import product

N = int(input())
A = [[int(i) for i in input().split()] for _ in range(N)]
B = [[int(i) for i in input().split()] for _ in range(N)]


def rotate(A: list[list[int]]) -> list[list[int]]:
    return [[A[N - 1 - j][i] for j in range(N)] for i in range(N)]


def is_correct(A: list[list[int]], B: list[list[int]]) -> bool:
    for i, j in product(range(N), range(N)):
        if A[i][j] == 1 and B[i][j] != 1:
            return False
    return True


for _ in range(4):
    if is_correct(A, B):
        print("Yes")
        exit()
    A = rotate(A)

print("No")

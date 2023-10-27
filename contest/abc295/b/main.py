"""
abc295 B
"""
from copy import deepcopy
from itertools import product


def explode(board, i, j, power):
    for x, y in product(range(-power, power + 1), repeat=2):
        if abs(x) + abs(y) <= power and 0 <= i + x < R and 0 <= j + y < C:
            board[i + x][j + y] = "."

    return board


R, C = map(int, input().split())
B = [list(input()) for _ in range(R)]

ans = deepcopy(B)
for i, j in product(range(R), range(C)):
    if "1" <= B[i][j] <= "9":
        ans = explode(ans, i, j, int(B[i][j]))

for row in ans:
    print("".join(row))

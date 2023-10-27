"""
abc294 A
"""


N = int(input())
A = list(map(int, input().split()))

print(" ".join(map(str, filter(lambda a: a % 2 == 0, A))))

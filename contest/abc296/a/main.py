"""
abc296 A
"""
from itertools import pairwise

N = int(input())
S = input()

for a, b in pairwise(S):
    if a == b:
        print("No")
        exit()

print("Yes")

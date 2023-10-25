"""
abc298 C
"""
from collections import defaultdict
from sortedcontainers import SortedSet, SortedList

N = int(input())
Q = int(input())
query = [[int(i) for i in input().split()] for _ in range(Q)]

hbox = defaultdict(SortedList)
number = defaultdict(SortedSet)
for q in query:
    match q[0]:
        case 1:
            i, j = q[1:]
            hbox[j].add(i)
            number[i].add(j)
        case 2:
            i = q[1]
            print(" ".join(map(str, hbox[i])))
        case 3:
            i = q[1]
            print(" ".join(map(str, number[i])))

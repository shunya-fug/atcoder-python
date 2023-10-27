"""
abc295 A
"""
N = int(input())
W = input().split()

targets = ["and", "not", "that", "the", "you"]
for w in W:
    if w in targets:
        print("Yes")
        exit()

print("No")

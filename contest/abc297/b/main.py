"""
abc297 B
"""
S = input()

x = S.find("B")
y = S.rfind("B")

correct = x % 2 != y % 2 and S.find("R") < S.find("K") < S.rfind("R")
print("Yes" if correct else "No")

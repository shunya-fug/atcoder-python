"""
abc301 A
"""
N = int(input())
S = input()

a, t = S.count("A"), S.count("T")
if a == t:
    print("T" if S[-1] == "A" else "A")
else:
    print("T" if t > a else "A")

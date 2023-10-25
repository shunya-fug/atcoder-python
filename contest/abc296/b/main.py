"""
abc296 B
"""
from string import ascii_lowercase

S = [input() for _ in range(8)]

for i in range(len(S)):
    j = S[i].find("*")
    if j != -1:
        print(ascii_lowercase[j] + str(len(S) - i))
        exit()

"""
abc300 D
"""
import math
from bisect import bisect_left


def sieve_of_eratosthenes(x):
    nums = [i for i in range(x + 1)]

    root = int(pow(x, 0.5))
    for i in range(2, root + 1):
        if nums[i] != 0:
            for j in range(i, x + 1):
                if i * j >= x + 1:
                    break
                nums[i * j] = 0

    primes = sorted(list(set(nums)))[2:]

    return primes


def calc(a, b, c):
    return a**2 * b * c**2


N = int(input())

ans = 0
primes = sieve_of_eratosthenes(int(math.sqrt(N)))
for b_i in range(1, len(primes) - 1):
    for a_i in range(b_i):
        p = bisect_left(
            primes, int(math.sqrt(N / (primes[a_i] ** 2 * primes[b_i]))), lo=b_i
        )
        if p == b_i:
            break
        ans += (
            p - b_i if calc(primes[a_i], primes[b_i], primes[p]) <= N else p - b_i - 1
        )

print(ans)

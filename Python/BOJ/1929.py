import sys

def findPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True
N, M = map(int, sys.stdin.readline().split())

for i in range(N, M + 1):
    if findPrime(i):
        print(i)
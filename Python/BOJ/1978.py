import sys


def findPrime(n):
    if n < 2:
        return False
    for i in range(2, n - 1):
        if n % i == 0:
            return False

    return True
        
N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

count = 0

for n in num:
    if findPrime(n):
        count += 1

print(count)
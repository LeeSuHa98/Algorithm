import sys


def gcd(a, b):
    if b == 0: return a
    else: return gcd(b, a%b)
    
N, M = map(int, sys.stdin.readline().split())

gcd = gcd(N,M)

print(gcd)
print(int(N*M/gcd))
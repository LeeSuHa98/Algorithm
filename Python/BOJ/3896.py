import sys

# 합성수 인지 ( 소수가 아닌지 체크 )
MAX = 13000001
prime = []
a = [0] * (MAX)

def findPrime():
    for i in range(2, MAX - 1):
        if a[i]:
            continue
        else:
            prime.append(i)
            for j in range(2 * i, MAX - 1, i):
               a[j] = 1    

    # return prime, a
def binarySearch(n):
    l = 2
    r = len(prime) - 1
    while(l <= r):
        mid = (l + r) // 2
        if prime[mid] >= n:
            r = mid - 1
        else:
            l = mid + 1
    return l

T = int(input())

findPrime()

for i in range(T):
    N = int(input())
    
    if a[N] != True:
        print(0)
    else:
        index = binarySearch(N)
        print(prime[index] - prime[index - 1])
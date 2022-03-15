def findPrime(n):
    a = [False, False] + [True] * (n - 1)
    prime = []
    
    for i in range(2, n + 1):
        if a[i]:
            prime.append(i)
            for j in range(2 * i, n + 1, i):
                a[j] = False
    return prime

N = int(input())

prime = findPrime(N)
result = 0
start = 0
end = 0

while end <= len(prime):
    temp = sum(prime[start:end])
    if temp == N:
        result += 1
        end += 1
    elif temp < N:
        end += 1
    else:
        start += 1
        
print(result)
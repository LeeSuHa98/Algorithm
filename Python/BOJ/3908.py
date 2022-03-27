import sys

dp = [[0 for i in range(15)] for j in range(1130)]
prime = [True for i in range(1121)]   
p = []

for i in range(2, int(1121 ** 0.5) + 1):
    prime[0] = prime[1] = False
    if prime[i]:
        for j in range(i * i, 1121, i):
            prime[j] = False

for i in range(2, 1121):
    if prime[i]:
        p.append(i)
        
dp[0][0] = 1
for i in range(1, len(p)):
    for j in range(1120, p[i], -1):
        for k in range(1, 15):
            dp[j][k] = min(dp[j][k], dp[j][k] + dp[j-p[i]][k-1])
print(dp)

T = int(input())

for i in range(T):
    N, K = map(int, input().split())

    print(dp[N][K])
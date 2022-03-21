import sys

N, M = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))

dp = [0 for i in range(N)]

for i in range(N):
    if i == 0:
        dp[i] = array[i]
    else:
        dp[i] = dp[i-1] + array[i]

for i in range(M):
    X, Y = map(int, sys.stdin.readline().split())
    
    if X == 1:
        print(dp[Y-1])
    else:
        print(dp[Y-1] - dp[X-2])
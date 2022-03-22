import sys

N, M = map(int, sys.stdin.readline().split())

arr = []
for i in range(N):
    arr.append(list(map(int, sys.stdin.readline().strip())))
    
dp = [[0 for i in range(M+1)] for j in range(N+1)]

count = 0
for i in range(1, N+1):
    for j in range(1, M+1):
        if arr[i-1][j-1] == 1:
            dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) +1
            
            count = max(dp[i][j], count)
                         
print(count ** 2)
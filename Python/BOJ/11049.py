import sys

N = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))
for i in range(N-1):
    r, c = map(int, sys.stdin.readline().split())
    arr.append(c)
    
dp = [[0 for i in range(N)] for j in range(N)]

for i in range(1, N):
    for j in range(N-i):
        if i == 1:
            dp[j][j+i] = arr[j] * arr[j+i] * arr[j+i+1]
            continue
        
        dp[j][j+i] = 2 ** 32
        for k in range(j, j+i):
            dp[j][j+i] = min(dp[j][j+i], dp[j][k] + dp[k+1][j+i] + arr[j] * arr[k+1] * arr[j+i+1])
print(dp[0][N-1])
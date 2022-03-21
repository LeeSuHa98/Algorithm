N = int(input())

array = []
for i in range(N):
    array.append(list(map(int, input().split())))
  
dp = [[0]*i for i in range(1, N + 1)]

for i in range(N):
    for j in range(i+1):
        if j == 0:
            dp[i][j] = dp[i-1][j] + array[i][j]
        elif j == i:
            dp[i][j] = dp[i-1][j-1] + array[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + array[i][j]

print(max(dp[N-1]))
import sys


# def dfs(level, begin):
#     global count
#     if level == K:
#         if sum(result) == N:
#             count += 1
#         return count
#     for i in range(begin, len(prime)):
#         result[level] = prime[i]
#         dfs(level + 1, i + 1)]


            
T = int(sys.stdin.readline())

for i in range(T):
    N, K = map(int, sys.stdin.readline().split())

    print(dp[N][K])


import math
import sys
input = sys.stdin.readline


N, K = map(int, input().split())
arr = [[0] * 7 for i in range(2)]

for i in range(N):
    S, Y = map(int, input().split())
    arr[S][Y] += 1

result = 0
for i in range(2):
    for j in arr[i]:
        result += math.ceil(j/K)
        
print(result)
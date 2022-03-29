import math
import sys
input = sys.stdin.readline


N, K = map(int, input().split())
arr = [[0]*7 for i in range(2)]

for i in range(N):
    S, Y = map(int, input().split())
    arr[S][Y] += 1

room = 0
for i in arr:
    for j in i:
        room += math.ceil(j/K)
print(room)
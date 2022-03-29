import sys
input = sys.stdin.readline


N = int(input())
arr = [[] for i in range(N)]

for i in range(N):
    x, y = map(int, input().split())
    
    arr[i].append(y)
    arr[i].append(x)

arr = sorted(arr)
for i in range(N):
    print(arr[i][1], arr[i][0])
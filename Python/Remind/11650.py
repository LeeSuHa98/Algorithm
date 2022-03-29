import sys
input = sys.stdin.readline


N = int(input())
arr = [[] for i in range(N)]

for i in range(N):
    x, y = map(int, input().split())
    
    arr[i].append(x)
    arr[i].append(y)

arr = sorted(arr)
for i in range(N):
    print(' '.join(map(str, arr[i])))
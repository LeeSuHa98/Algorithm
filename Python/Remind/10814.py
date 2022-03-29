import sys
input = sys.stdin.readline


N = int(input())
arr = [[] for i in range(N)]

for i in range(N):
    age, name = map(str, input().split())

    arr[i].append(int(age))
    arr[i].append(name)

result = sorted(arr, key=lambda x : x[0])
for i in range(N):
    print(result[i][0], result[i][1])
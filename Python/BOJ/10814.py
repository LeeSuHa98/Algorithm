import sys

N = int(sys.stdin.readline())

array = []
for i in range(N):
    age, name = map(str, sys.stdin.readline().split())
    array.append([int(age), name])

array = sorted(array, key=lambda x: x[0])

for i in range(N):
    print(array[i][0], array[i][1])
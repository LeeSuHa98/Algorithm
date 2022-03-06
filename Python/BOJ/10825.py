import sys

N = int(sys.stdin.readline())

array = []
for i in range(N):
    name, koean, english, math = map(str, sys.stdin.readline().split())
    array.append([name, int(koean), int(english), int(math)])

array = sorted(array, key=lambda x: (-x[1], x[2], -x[3], x[0]))

for i in range(N):
    print(array[i][0])
import sys

N = int(input())
word = [sys.stdin.readline() for _ in range(N)]
new = []
for i in word:
    if i not in new:
        new.append(i)

arr = sorted(new)
result = sorted(arr, key=len)

for i in range(len(result)):
    sys.stdout.write(result[i])

import sys
input = sys.stdin.readline


arr = [0] * 26
S = list(map(str, input().strip()))

for i in S:
    arr[ord(i) - 97] += 1

print(' '.join(map(str, arr)))
import sys

S = list(map(str, sys.stdin.readline().strip()))
arr = [0] * 26

for i in set(S): arr[ord(i) - 97] = S.count(i)

print(' '.join(map(str, arr)))
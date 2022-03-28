import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
v = int(sys.stdin.readline())

count = 0
for i in range(N):
    if v == arr[i]: count += 1
    
print(count)
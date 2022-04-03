from collections import deque
import sys

N = int(sys.stdin.readline())
arr = deque([i for i in range(1, N+1)])

while len(arr) > 1:
    arr.popleft()
    arr.append(arr.popleft())
    
print(arr[0])
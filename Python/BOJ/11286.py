import heapq
import sys
input = sys.stdin.readline

            
N = int(input())
h = []
for i in range(N):
    x = int(input())
    
    if x != 0:
        heapq.heappush(h, (abs(x), x))
    elif x == 0 and len(h) != 0:
        print(heapq.heappop(h)[1])
    else:
        print(0)
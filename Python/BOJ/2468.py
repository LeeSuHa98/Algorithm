from collections import deque
import sys
from trace import Trace 
sys.setrecursionlimit(100000)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, check):

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and graph[nx][ny] > check:
            visited[nx][ny] = True
            bfs(nx, ny, check)

N = int(sys.stdin.readline())

graph = [list(map(int, sys.stdin.readline().split())) for i in range(N)]

#count 배열에 담아서 max(count) 구해야함
result = 0
for k in range(max(map(max, graph))):
    visited = [[False]*N for i in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and graph[i][j] > k:
                count += 1
                visited[i][j] = True
                bfs(i, j, k)
    result = max(result, count)
    
print(result)
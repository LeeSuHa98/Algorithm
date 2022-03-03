# RecursionError 해결 방법
# sys.setrecursionlimt 제한 설정

from collections import deque
import sys
sys.setrecursionlimit(10000)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    visited[x][y] = True
    checkColor = graph[x][y]
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and graph[nx][ny] == checkColor:
            bfs(nx, ny)
                
N = int(input())

graph = [list(map(str, sys.stdin.readline().strip())) for i in range(N)]
visited = [[False]*N for i in range(N)]

count = 0
countBlind = 0

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j)
            count += 1
            
for i in range(N):
    for j in range(N):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'     

#bfs 함수를 사용하기 위한 visited 초기화
visited = [[False]*N for i in range(N)]

for i in range(N):
    for j in range(N):
        if not visited[i][j]:            
            bfs(i, j)
            countBlind += 1

print(count, countBlind)

# sys.setsrecursiinlimit 설정 필요성은 
# 최대 재귀 깊이를 인위로 늘려줘서 recursion error를 막는 방법
# deque를 사용해서 재귀는 한번만 요청

from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    checkColor = graph[x][y]
    
    while queue:
        xx, yy = queue.popleft()
        
        for i in range(4):
            nx = xx + dx[i]
            ny = yy + dy[i]
            
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and graph[nx][ny] == checkColor:
                visited[nx][ny] = True
                queue.append([nx, ny])
                
N = int(input())

graph = [list(map(str, input().strip())) for i in range(N)]
visited = [[False]*N for i in range(N)]

count = 0
countBlind = 0

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j)
            count += 1
            
for i in range(N):
    for j in range(N):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

#bfs 함수를 사용하기 위한 visited 초기화
visited = [[False]*N for i in range(N)]

for i in range(N):
    for j in range(N):
        if not visited[i][j]:            
            bfs(i, j)
            countBlind += 1

print(count, countBlind)
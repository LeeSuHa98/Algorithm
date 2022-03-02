#계속 입력받고 끝내고 싶으면 0 0 입력
#상하좌우 + 대각선까지 체크

from collections import deque

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, 1, -1, -1, 1]

def bfs(i, j):
    queue = deque()
    queue.append([i, j])
    visited[i][j] == True
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append([nx, ny])

island = []

while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break
    
    visited = [[False]*w for i in range(h)]
    graph = [list(map(int, input().split())) for i in range(h)]

    count = 0
    
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1 and not visited[i][j]:
                bfs(i,j)
                count += 1
    print(count)
    
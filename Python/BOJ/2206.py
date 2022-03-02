from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(startX, startY, isCheck, visitied, graph):
    queue = deque()
    queue.append([startX, startY, isCheck])
    visitied[startX][startY][isCheck] = 1
    
    while queue:
        x, y, isCheck = queue.popleft()
        
        if x == N - 1 and y == M -1:
            return visitied[x][y][isCheck]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 > nx or N <= nx or 0 > ny or M <= ny:
                continue
            if graph[nx][ny] == 0 and visitied[nx][ny][isCheck] == 0:
                queue.append([nx, ny, isCheck])
                visitied[nx][ny][isCheck] = visitied[x][y][isCheck] + 1
            if graph[nx][ny] == 1 and isCheck == 0:
                queue.append([nx, ny, isCheck + 1])
                visitied[nx][ny][isCheck + 1] = visitied[x][y][isCheck] + 1
                
    return -1

N, M = map(int, input().split())

graph = [list(map(int, input().strip())) for i in range(N)]
visitied = [[[0]*2 for i in range(M)] for j in range(N)]

print(bfs(0,0,0,visitied,graph))
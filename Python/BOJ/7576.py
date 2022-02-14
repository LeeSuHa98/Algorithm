from collections import deque

def bfs(x, y):
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < M and gragh[nx][ny] == 0:
                gragh[nx][ny] = gragh[x][y] + 1
                queue.append([nx, ny])
                
M, N = map(int, input().split())

gragh = [list(map(int, input().split())) for _ in range(N)]

queue = deque()

for i in range(N):
    for j in range(M):
        if gragh[i][j] == 1:
            queue.append([i, j])
    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0
bfs(0, 0)

for i in gragh:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)

    result = max(result, max(i))
print(result - 1)
from collections import deque


def bfs(i, j):
    queue = deque()
    queue.append([i,j])
    graph[i][j] = 0
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append([nx, ny])
        
    return

T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(T):
    M, N, K = map(int, input().split())
    graph = [[0]*N for i in range(M)]
    
    count = 0
    
    for j in range(K):
        X, Y = map(int, input().split())
        graph[X][Y] = 1

    for i in range(M):
        for j in range(N):
            if graph[i][j] == 1:
                bfs(i, j)
                count += 1

    print(count)   
# bfs로 블록 그룹화
def bfs(i, j, count):
    

N, M, K = map(int, input().split())

graph = [list(map(str, input().strip())) for i in range(2*M + 1)]

visited = [[False]*(2*N + 1) for i in range(2*M + 1)]

count = 0
#블록 그룹화 call
for i in range(2*M + 1):
    for j in range(2*N + 1):
        if not visited[i][j] and graph[i][j] == 'B':
            count += 1
            bfs(i, j, count)
from collections import deque


def bfs(start):
    queue = deque()
    visited[start] = True
    queue.append(start)
    
    while queue:
        search = queue.popleft()
        for i in graph[search]:
            if not visited[i]:
                visited[i] = visited[search] + 1
                queue.append(i)
    return sum(visited)

N, M = map(int, input().split())

graph = [[] for i in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
result = []
for i in range(1, N+1):
    visited = [False]*(N+1)
    result.append(bfs(i))
    
print(result.index(min(result)) + 1)
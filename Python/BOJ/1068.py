import sys
input = sys.stdin.readline


def dfs(graph, v):
    global count
    if not graph[v]:
        count += 1
        return

    for i in graph[v]:
        dfs(graph, i)
                
N = int(input())
d = list(map(int, input().split()))
K = int(input())

graph = [[] for i in range(N+1)]
count = 0
root = -1

for i in range(N):
    if d[i] == -1:
        root = i
        continue
    if K == i:
        continue
    graph[d[i]].append(i)

if K == root:
    print(0)
else:
    dfs(graph, root)
    print(count)
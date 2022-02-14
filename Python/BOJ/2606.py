#dfs

def dfs(gragh, v, visited):
    visited[v] = True
    global count
    for i in gragh[v]:
        if not visited[i]:
            dfs(gragh, i, visited)
            count += 1
            
N = int(input())
network = int(input())

gragh = [[]*N for i in range(N+1)]

#[0][i] 는 리스트 번호
#[j][i]는 j 리스트 번호에 들어갈 배열
for i in range(network):
    a, b = map(int, input().split())
    gragh[a].append(b)
    gragh[b].append(a)
    
count = 0
visited = [False]*(N+1)

dfs(gragh, 1, visited)
print(count)
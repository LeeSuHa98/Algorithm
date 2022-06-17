import sys
input=sys.stdin.readline

N = int(input())
result = [1]*N
graph = {}
visited = {}

def gcd(a, b):
    return b if a%b == 0 else gcd(b, a%b)

def bfs(a, b, edge):
    global visited
    
    if (a, edge) in visited: 
        return
    
    visited[(a, edge)]=True
    result[a] *= edge
    
    for i in graph[a]:
        if i != b: 
            bfs(i, a, edge)

for i in range(N): 
    graph[i] = []
    
check=[]
for _ in range(N-1):
    a, b, p, q=map(int, input().split())
    graph[a].append(b); 
    graph[b].append(a)
    check.append([a, b, p, q])

for i in range(N-1):
    a, b, p, q=check[i]
    visited={}
    bfs(a, b, p)
    bfs(b, a, q)

num = result[0]
for i in range(N):
    num = gcd(g, result[i])
    
for i in range(N): 
    result[i]//=num
    
print(*result)
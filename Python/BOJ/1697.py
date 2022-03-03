from collections import deque

def bfs(N,K):
    queue = deque([[N, 0]])
    visited = {N}
    
    while queue:
        pre, count = queue.popleft()
        
        if pre == K:
            return count
        if pre + 1 <= 100000 and pre + 1 not in visited:
            queue.append([pre + 1, count + 1])
            visited.add(pre + 1)
        if pre -1 >= 0 and pre -1 not in visited:
            queue.append([pre - 1, count + 1])
            visited.add(pre - 1)
        if pre*2 <= 100000 and pre * 2 not in visited:
            queue.append([pre * 2, count + 1])
            visited.add(pre * 2)
    
N, K = map(int, input().split())

print(bfs(N, K))
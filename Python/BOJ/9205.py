from collections import deque


def bfs():
    queue = deque()
    queue.append([home[0], home[1]])
    
    while queue:
        x, y = queue.popleft()
        
        if abs(x - destination[0]) + abs(y - destination[1]) <= 1000:
            print("happy")
            return
        for i in range(n):
            if not visited[i]:
                nx, ny = case[i]
                if abs(x - nx) + abs(y - ny) <= 1000:
                    queue.append([nx, ny])
                    visited[i] = 1
    print("sad")
    return

t = int(input())

for i in range(t):
    n = int(input())
    home = [int(x) for x in input().split()]
    
    case = []
    for i in range(n):
        x, y = map(int, input().split())
        case.append([x,y])
        
    destination = [int(x) for x in input().split()]
    
    visited = [0 for i in range(n+1)]
    bfs()
import sys
input = sys.stdin.readline


N = int(input())
queue = []
for i in range(N):
    command = input().split()
    
    if command[0] == 'push':
        queue.append(command[1])
    if command[0] == 'pop':
        if len(queue) == 0: print(-1)
        else: print(queue.pop(0))
    if command[0] == 'size':
        print(len(queue))
    if command[0] == 'empty':
        if len(queue) == 0: print(1)
        else: print(0)
    if command[0] == 'front':
        if len(queue) == 0: print(-1)
        else: print(queue[0])
    if command[0] == 'back':
        if len(queue) == 0: print(-1)
        else: print(queue[-1])
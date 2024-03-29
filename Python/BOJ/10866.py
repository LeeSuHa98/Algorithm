import sys
input = sys.stdin.readline


N = int(input())
deque = []
for i in range(N):
    command = input().split()
    
    if command[0] == 'push_front':
        deque.insert(0, command[1])
    if command[0] == 'push_back':
        deque.append(command[1])
    if command[0] == 'pop_front':
        if len(deque) == 0: print(-1)
        else: print(deque.pop(0))
    if command[0] == 'pop_back':
        if len(deque) == 0: print(-1)
        else: print(deque.pop(len(deque)-1))
    if command[0] == 'size':
        print(len(deque))
    if command[0] == 'empty':
        if len(deque) == 0: print(1)
        else: print(0)
    if command[0] == 'front':
        if len(deque) == 0: print(-1)
        else: print(deque[0])
    if command[0] == 'back':
        if len(deque) == 0: print(-1)
        else: print(deque[len(deque)-1])
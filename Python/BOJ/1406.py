import sys
input = sys.stdin.readline


N = list(map(str, input().strip()))
M = int(input())

stack = []
for i in range(M):
    command = input().split()
    
    if command[0] == 'P':
        N.append(command[1])
    elif command[0] == 'L':
        if N: stack.append(N.pop())
    elif command[0] == 'B':
        if N: N.pop()
    elif command[0] == 'D':
        if stack: N.append(stack.pop())

N.extend(reversed(stack))
print(''.join(N))

'''
구현
'''


import sys
input = sys.stdin.readline

r1, c1, r2, c2 = map(int, input().split())

board = [[0]*(c2-c1+1) for i in range(r2-r1+1)]

x = y = 0
num = level = 1
count = max_num = direc = num_count =  0

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

while True:
    if r1 <= y <= r2 and c1 <= x <= c2:
        board[y-r1][x-c1] = str(num)
        max_num = max(len(str(num)), max_num)
        num_count += 1
        
        if num_count == (c2-c1+1)*(r2-r1+1):
            break
    num += 1
    count += 1
    
    y = y + dy[direc]
    x = x + dx[direc]
    
    if count == level:
        count = 0
        direc = (direc+3)%4
        if direc == 0 or direc == 2:
            level += 1

max_num_len = len(str(max_num-1))

for i in range(r2-r1+1):
    for j in range(c2-c1+1):
        print(' '*(max_num-len(board[i][j])) + board[i][j], end=' ')
    print()

from collections import deque

def bfs(x, y, char):
    visited = [[0]*6 for i in range(12)]
    queue = deque()
    queue.append([x, y])
    bomb = 1
    visited[x][y] = bomb
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < 12 and 0 <= ny < 6 and field[nx][ny] == field[x][y] and visited[nx][ny] == 0:
                bomb += 1
                visited[nx][ny] = 1
                queue.append([nx, ny])
    
    #
    if bomb >= 4:
        char += 1
        for i in range(12):
            for j in range(6):
                if visited[i][j] == 1:
                    field[i][j] = '.'
    return char
# 뿌요가 터졌을 때 뿌요가 있을 때 까지 아래로 떨어지는 함수
def checkFall():
    for i in range(10, -1, -1):
        for j in range(6):
            if field[i][j] != '.' and field[i+1][j] == '.':
                for k in range(i+1, 12):
                    if k == 11 and field[k][j] == '.':
                        field[k][j] = field[i][j]
                    elif field[k][j] != '.':
                        field[k-1][j] = field[i][j]
                        break
                field[i][j] = '.'
                
#한문자씩 입력받아 field 에 저장
field = [list(map(str, input().strip())) for i in range(12)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

flag = 0
while True:
    # 뿌요가 4개 이상일 때 1로 변경되며 터트림과 동시에 . 으로 변경
    count = 0
    for i in range(12):
        for j in range(6):
            if field[i][j] != '.':
                count = bfs(i, j, count)
    if count == 0:
        print(flag)
        break
    else:
        flag += 1
    checkFall()

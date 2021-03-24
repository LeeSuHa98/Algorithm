N = int(input())
trip = input().split()

#(1,1) 부터 시작
x, y = 1, 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

move_type = ['L', 'R', 'U', 'D']

for step in trip:
    for i in range(len(move_type)):
        if step == move_type[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or nx > N or ny < 1 or ny > N:
        continue
    x, y = nx, ny

print(x, y)
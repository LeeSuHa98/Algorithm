N = int(input())

point = []

for i in range(N):
    x, y = map(int, input().split())
    point.append((x,y))

point = sorted(point)

for i in range(N):
    print(point[i][0], point[i][1])
    
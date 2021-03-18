N = int(input())

point = []

for i in range(N):
    x, y = map(int, input().split())
    point.append((y,x))

point = sorted(point)

for i in range(N):
    print(point[i][1], point[i][0])
    
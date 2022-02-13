X, Y = map(int, input().split())
N = int(input())

preTotal = (1000*X)/Y

for i in range(N):
    gimbabX, gimbabY = map(int, input().split())

    total = (1000*gimbabX)/gimbabY
    preTotal = min(preTotal, total)

print(f"{preTotal:.2f}")
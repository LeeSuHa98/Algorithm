#baekjoon 7568

N = int(input())
human = []

for i in range(N):
    width, height = map(int, input().split())
    human.append((width, height))

for i in human:
    count = 1
    for j in human:
        if(i[0] < j[0] and i[1] < j[1]):
            count += 1
    print(count, end=" ")


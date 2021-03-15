#baekjoon

N = int(input())
sort = []

for i in range(N):
    sort.append(int(input()))

result = sorted(sort)

for i in range(len(sort)):
    print(result[i])
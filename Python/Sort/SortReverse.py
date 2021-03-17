N = int(input())

arr = []

for i in str(N):
    arr.append(i)


result = sorted(arr)

print(''.join(reversed(result)))
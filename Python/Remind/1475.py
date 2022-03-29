import sys
input = sys.stdin.readline


N = list(map(int, input().strip()))
arr = [0] * 10

for i in range(len(N)):
    index = N[i]

    if index == 6 or index == 9:
        if arr[6] <= arr[9]:
            arr[6] += 1
        else:
            arr[9] += 1
    else:
        arr[index] += 1
    print(arr)
print(max(arr))
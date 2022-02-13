A, B, C = map(int, input().split())

array = []
array.extend([A, B, C])
array.sort()

if array[1] - array[0] == array[2] - array[1]:
    print(array[2] + array[2] - array[1])
elif array[1] - array[0] < array[2] - array[1]:
    print(array[1] + array[1] - array[0])
else:
    print(array[0] + array[2] - array[1])
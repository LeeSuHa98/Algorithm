from itertools import combinations
# 9난쟁이의 총 합은 100 + 알파
# 합 - 100 의 값을 가진 두 인자를 배열에서 제외
# 9C2의 조합으로 찾아내면 해결

from ntpath import join


array = []

for i in range(9):
    hat = int(input())
    array.append(hat)

total = sum(array) - 100

for i in combinations(array, 2):
    if sum(i) == total:
        array.remove(i[0])
        array.remove(i[1])

result = '\n'.join(map(str, array))
print(result)
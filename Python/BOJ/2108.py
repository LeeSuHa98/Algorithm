N = int(input())

array = []
for i in range(N):
    array.append(int(input()))

array.sort()
# 산술평균
def mean():
    return round(sum(array)/N)
    
# 중앙값
def mid():
    return array[N//2]
    
# 최빈값
def mode():
    less = list(set(array))
    max = []
    maxCount = 0
    for i in less:
        if maxCount >= array.count(i):
            max.append(i)
        elif maxCount < array.count(i):
            max = []
            max.append(i)
            maxCount = array.count(i)
    if len(max) > 1:
        max.sort()
        return max[1]
    else:
        return max[0]
# 범위
def range():
    return max(array)-min(array)
    
print(mean())
print(mid())
print(mode())
print(range())
from typing import Counter
import sys

N = int(sys.stdin.readline())
arr = []

for i in range(N):
    arr.append(int(sys.stdin.readline()))

def Mean(arr):
    return round(sum(arr)/len(arr))

def Median(arr):
    length = len(arr)
    tmp = sorted(arr)
    return tmp[length >> 1] if length & 1 else (tmp[length >> 1] + tmp[length >> 1 -1])/2

def Mode(arr):
    arrCount = Counter(sorted(arr))
    modes = arrCount.most_common()

    if len(arr) > 1:
        if modes[0][1] == modes[1][1]:
            modeResult = modes[1][0]
        else:
            modeResult = modes[0][0]
    else:
        modeResult = modes[0][0]
    
    return modeResult

def MinMax(arr):
    return max(arr) - min(arr)

print(Mean(arr))
print(Median(arr))
print(Mode(arr))
print(MinMax(arr))
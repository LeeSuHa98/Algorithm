#baekjoon 2798

'''
#sol 1 

N, M = map(int, input().split())
arr = list(map(int, input().split()))

similar = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if arr[i]+arr[j]+arr[k] > M:
                continue
            else:
                similar = max(similar, arr[i]+arr[j]+arr[k])

print(similar)
'''

#sol 2 use combination
from itertools import combinations

N, M = map(int, input().split())
arr = list(map(int, input().split()))

similar = 0

for i in combinations(arr, 3):
    temp = sum(i)
    if similar < temp <= M:
        similar = temp

print(similar)
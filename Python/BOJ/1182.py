import sys

# solve 1 재귀함수

def dfs(index, sum):
    global count
    
    if index >= N:
        return 
    
    sum += array[index]
    
    if sum == S:
        count += 1
        
    dfs(index+1, sum - array[index])
    dfs(index+1, sum)
    
N, S = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))

count = 0
dfs(0, 0)
print(count)

# solve 2 브루트포스 이진법

N, K = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))
count = 0

for i in range(1, 1 << N):
    t = 0
    for j in range(N):
        if i & 1 << j: t += array[j]
    if t == K: count += 1
print(count)
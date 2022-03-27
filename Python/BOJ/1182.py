import sys

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
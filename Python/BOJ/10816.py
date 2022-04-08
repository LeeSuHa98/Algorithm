import sys
input = sys.stdin.readline


def binary_search(arr, i, start, end):
    mid = (start+end)//2
    
    if start > end:
        return 0
    if arr[mid] == i:
        return arr[start:end+1].count(i)
    elif arr[mid] > i:
        return binary_search(arr, i, start, mid-1)
    else:
        return binary_search(arr, i, mid+1, end)
    
N = input()
n = sorted(map(int, input().split()))
M = input()
m = map(int, input().split())

check = {}
for i in n:
    if i not in check:
        check[i] = binary_search(n, i, 0, len(n)-1)
        
print(' '.join(str(check[i]) if i in check else '0' for i in m))
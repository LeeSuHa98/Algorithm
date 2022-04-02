import sys
input = sys.stdin.readline


N = int(input())
n = sorted(map(int, input().split()))
M = int(input())
m = map(int, input().split())

def binary_search(n, i, start, end):
    mid = (start+end)//2
    if start > end:
        return 0
    elif n[mid] == i:
        return 1
    elif n[mid] > i:
        return binary_search(n, i, start, mid-1)
    else:
        return binary_search(n, i, mid+1, end)

for i in m:
    start = 0
    end = len(n)-1
    print(binary_search(n, i, start, end), end=' ')
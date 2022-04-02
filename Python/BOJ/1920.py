import sys
input = sys.stdin.readline


# 집합 자료형
N = int(input())
A = set(input().split())
M = int(input())
check = input().split()

print(A)
print(check)
for i in check:
    if i in A:
        sys.stdout.write('1'+'\n')
    else:
        sys.stdout.write('0'+'\n')
        
# 이분탐색
N = int(input())
A = sorted(map(int, input().split()))
M = int(input())
check = map(int, input().split())

def binary_search(A, l, start, end):
    mid = (start + end)//2
    
    if start > end:
        return 0
    elif A[mid] == l:
        return 1
    elif A[mid] > l:
        return binary_search(A, l, start, mid-1)
    else:
        return binary_search(A, l, mid+1, end)
for l in check:
    start = 0
    end = len(A)-1
    
    print(binary_search(A, l, start, end))
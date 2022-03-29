import sys
input = sys.stdin.readline


A = int(input())
B = int(input())
C = int(input())

arr = [0] * 10
check = list(map(int, str(A*B*C)))

for i in check:
    arr[i] += 1
        
print('\n'.join(map(str, arr)))
import sys
input = sys.stdin.readline


A, B, C, N = map(int, input().split())

count = 0
for i in range(N//A+1):
    for j in range(N//B+1):
        for k in range(N//C+1):
            if A*i + B*j + C*k == N:
                count = 1
                
print(count)
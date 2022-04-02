import sys
input = sys.stdin.readline

# solve 1
# 정렬과 그리디
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A = sorted(A)
B = sorted(B, reverse=True)

result = 0
for i in range(N):
    result += A[i] * B[i]
print(result)

# solve 2
# 재배열 없이 푼 방법
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

result = 0
for i in range(N):
    result += min(A)*max(B)
    A.pop(A.index(min(A)))
    B.pop(B.index(max(B)))
print(result)
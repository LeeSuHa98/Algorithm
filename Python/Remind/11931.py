import sys
input = sys.stdin.readline


N = int(input())
arr = [int(input()) for i in range(N)]

print('\n'.join(map(str, sorted(arr, reverse=True))))
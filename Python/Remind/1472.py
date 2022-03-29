import sys
input = sys.stdin.readline


N = list(map(int, input().strip()))

print(''.join(map(str, sorted(N, reverse=True))))
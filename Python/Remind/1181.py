import sys
input = sys.stdin.readline


N = int(input())
word = [input().strip() for i in range(N)]

print('\n'.join(map(str, sorted(sorted(set(word)), key=len))))
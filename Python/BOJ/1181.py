import sys
input = sys.stdin.readline

N = int(input())

word = []
for i in range(N):
    word.append(input().strip())

result = sorted(sorted(set(word)), key=len)

print('\n'.join(map(str, result)))
from itertools import permutations
N, M = map(int, input().split())

p = permutations(range(1, N+1), M)

for i in p:
    print(' '.join(map(str, i)))
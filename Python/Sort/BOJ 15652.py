N, M = map(int, input().split())

result = []

def backTracking(depth, idx, N, M):
    if depth == M:
        print(' '.join(map(str, result)))
        return
    for i in range(idx, N):
        result.append(i+1)
        backTracking(depth+1, i, N, M)
        result.pop()

backTracking(0, 0, N, M)
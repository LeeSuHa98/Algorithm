N, M = map(int, input().split())

result = []

def backTracking(depth, N, M):
    if depth == M:
        print(' '.join(map(str, result)))
        return
    for i in range(N):
        result.append(i+1)
        backTracking(depth+1, N, M)
        result.pop()

backTracking(0, N, M)
#baekjoon 1018

N, M = list(map(int, input().split()))
chess = []

for i in range (N):
    chess.append(input())

result = []

for i in range(N-7):
    for j in range(M-7):
        firstW = 0;
        firstB = 0;
        for a in range(i, i+8):
            for b in range(j, j+8):
                if((a+b) % 2 == 0):
                    #짝수일 때 
                    if(chess[a][b] != "W"):
                        firstW += 1
                    if(chess[a][b] != "B"):
                        firstB += 1
                else:
                    #홀수일 때
                    if(chess[a][b] != "B"):
                        firstW += 1
                    if(chess[a][b] != "W"):
                        firstB += 1

            print(a, "+", firstW)
            print(a, "+",firstB)
        result.append(firstW)
        result.append(firstB)

print(min(result))

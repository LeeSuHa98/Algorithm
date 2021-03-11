#baekjoon 1018

N, M = list(map(int, input().split()))
chess = []

for i in range (N):
    chess.append(input())

result = []

for i in range(N-7):
    for j in range(M-7):
        changeW = 0;
        changeB = 0;
        for a in range(i, i+8):
            for b in range(j, j+8):
                if((a+b) % 2 == 0):
                    #짝수일 때 
                    if(chess[a][b] != "W"):
                        changeW += 1
                    if(chess[a][b] != "B"):
                        changeB += 1
                else:
                    #홀수일 때
                    if(chess[a][b] != "B"):
                        changeW += 1
                    if(chess[a][b] != "W"):
                        changeB += 1
        result.append(changeW)
        result.append(changeB)

print(min(result))

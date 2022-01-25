# solve 1
# sort code and effective
N = int(input())

for i in range(N):
    quize = input()

    sum = 0
    score = 0
    
    for j in quize:
        if j == 'O':
            score += 1
            sum += score
        elif j == 'X':
            score = 0
    print(sum)
    
# solve 2
# first code uneffective
N = int(input())

quize = []
result = []

for i in range(N):
    quize = input()
    result.append(list(quize))

for i in range(N):
    sum = 0
    score = 0
    for j in range(0, len(result[i])):
        if result[i][j] == 'O' and result[i][j-1] == 'O':
            score += 1
            sum += score
        elif result[i][j] == 'O':
            score = 1
            sum += score
        elif result[i][j] == 'X':
            score = 0
    print(sum)
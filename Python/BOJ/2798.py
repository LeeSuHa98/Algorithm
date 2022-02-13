from itertools import combinations

N, M =  input().split()
total = []

card = map(int, input().split())
M = int(M)

maxCard = 0
for i in combinations(card, 3):
    if sum(i) <= M:
        if maxCard < sum(i):
            maxCard = sum(i)
print(maxCard)
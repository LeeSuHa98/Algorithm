N = int(input())

playerList = []
for i in range(N):
    player = input()
    playerList.append(player[0])

count = {}
playerList.sort()

for i in playerList:
    try:
        count[i] += 1
    except:
        count[i] = 1


playerExcept = 0
for key, value in count.items():
    if value >= 5:
        playerExcept += 1
        print(key, end='')
        
if playerExcept == 0:
    print("PREDAJA")
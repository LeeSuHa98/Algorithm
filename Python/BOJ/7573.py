N, L, M = map(int, input().split())

# M 만큼 물고기 좌표 입력받기
fish = []
for i in range(M):
    xFish, yFish = map(int, input().split())
    fish.append([xFish, yFish])

def getNet(L):
    netList = []
    for l1 in range(1, L//2):
        l2 = L//2 - l1
        netList.append([l1, l2])      
    return netList

def checkNet(x, y, net):
    if x + net[0] > N or y + net[1] > N:
        return False
    else:
        return True
    
def countFish(x, y, net):
    if not checkNet(x, y, net):
        return 0
    
    count = 0
    
    for fishes in fish:
        fx, fy = fishes
        if x <= fx <= x + net[0] and y <= fy <= y + net[1]:
            count += 1
            
    return count

def getFish(nets):
    # nets = (x, y)
    maxFish = 0
    
    for fishes in fish:
        fx, fy = fishes
        
        for x in range(fx, fx - nets[0] - 1, -1):
            maxFish = max(maxFish, countFish(x, fy, nets))
        for y in range(fy, fy - nets[1] - 1, -1):
            maxFish = max(maxFish, countFish(fx, y, nets))
    return maxFish

net = getNet(L)
result = 0
for i in net:
    result = max(result, getFish(i))
print(result)
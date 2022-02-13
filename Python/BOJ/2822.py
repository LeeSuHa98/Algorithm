array = []
for i in range(8):
    score = int(input())
    array.append(score)
    
newList = sorted(array, reverse = True)[0:5]

result = []
for i in newList[0:5]:
    for j in range(8):
        if array[j] == i:
            result.append(j+1)
            
result.sort()
index = ' '.join(map(str, result))
print(sum(newList))
print(index)
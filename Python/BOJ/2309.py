import sys
    
array = [int(sys.stdin.readline()) for i in range(9)]

temp, temp2 = 0, 0
for i in range(len(array)):
    for j in range(i+1, len(array)):
        if sum(array) - (array[i] + array[j]) == 100:
            temp = array[i]
            temp2 = array[j]
            
array.remove(temp)
array.remove(temp2)

print('\n'.join(map(str, sorted(array))))
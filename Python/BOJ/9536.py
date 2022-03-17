import sys

T = int(sys.stdin.readline())

for i in range(T):
    sentence = sys.stdin.readline().split()
    array = []
    
    while True:
        animal = sys.stdin.readline().split()
        if len(animal) > 3:
            break
        array.append(animal[2])
    
    result = []
    for i in sentence:
        if i not in array:
            result.append(i)
    
    print(' '.join(result))
T = int(input())

for i in range(T):
    k = int(input())
    n = int(input())
    
    array = [i for i in range(1, n+1)]

    for i in range(k):
        for j in range(1, n):
            array[j] += array[j-1]

    print(array[n-1])
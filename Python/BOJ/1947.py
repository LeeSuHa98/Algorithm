array = list(map(int, input().split()))

def sort(array):
    n = len(array)
    
    while True:
        for i in range(n - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                print(' '.join(map(str, array)))
            if array == sorted(array):
                return False
sort(array)
import sys
input = sys.stdin.readline


def twopointer(arr):
    left = 0
    right = len(arr)-1
    while left<right:
        if arr[left] == arr[right]:
            left +=1
            right -= 1
        else:
            if left < right-1:
                temp = arr[:right] + arr[right+1:]
                if temp[:] == temp[::-1]:
                    return 1
            if left + 1 < right:
                temp = arr[:left] + arr[left+1:]
                if temp[:] == temp[::-1]:
                    return 1
            return 2
    return 0

N = int(input())

print([twopointer(input().strip()) for i in range(N)])
import sys
input = sys.stdin.readline


def strfry(a, b):
    if sorted(a) == sorted(b):
        return True
    return False
    
N = int(input())

for i in range(N):
    A, B = map(str, input().split())
    
    if strfry(A,B) == True:
        print("Possible")
    else:
        print("Impossible")    
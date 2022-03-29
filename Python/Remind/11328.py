import sys
input = sys.stdin.readline


def strfry(a, b):
    if sorted(a) == sorted(b):
        return True
    return False

N = int(input())
for i in range(N):
    a, b = map(str, input().split())
    
    if strfry(a, b) == True:
        print("Possible")
    else:
        print("Impossible")
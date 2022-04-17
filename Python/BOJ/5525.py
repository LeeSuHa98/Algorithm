'''
KMP
'''

import sys
input = sys.stdin.readline


N = int(input())
M = int(input())
S = input()
    
count = 0
check = 0
idx = 0

while idx < M - 2:
    if S[idx] == 'I' and S[idx+1] == 'O' and S[idx+2] == 'I':
        check += 1
        if check == N:
            count +=1
            check -=1
        idx += 2
    else:
        check = 0
        idx += 1

print(count)
import sys
input = sys.stdin.readline


def VPS(paren):
    stack = []
    for i in paren:
        if len(stack) != 0:
            if i == ')' and stack[-1] == '(':
                stack.pop()
            else: stack.append(i)
        else: stack.append(i)
        
    if len(stack) > 0:
        return 'NO'
    else: return 'YES'

T= int(input())

for i in range(T):
    paren = input().strip()
    
    print(VPS(paren))
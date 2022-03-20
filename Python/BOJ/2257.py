import sys

N = input()

chemi = {
    'H' : 1,
    'C' : 12,
    'O' : 16
}

stack = []
for i in N:
    if i in chemi:
        stack.append(chemi[i])
    elif i == '(':
        stack.append(i)
    elif i == ')':
        temp = 0
        while True:
            tag = stack.pop()
            
            if tag == '(':
                break
            temp += tag
            
        if temp == 0:
            continue
        else:
            stack.append(temp)
    else:
        n = stack.pop()
        temp = n*int(i)
        stack.append(temp)
print(sum(stack))
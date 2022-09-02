import re

call = 'ABCabcA'

def solution(call):
    
    temp = []
    max = 1
    for i in range(len(call)):
        for j in range(i, len(call)):
            div = call[i:j+1]
            div2 = call[:i+1]
            
            M = re.match(".*"+div+".*", div2)
            if M:
                if max < len(div) and len(div) != len(call):
                    max = len(div)
                    temp.append(div)
    return temp

print(solution(call))
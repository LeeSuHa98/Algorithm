
from collections import deque


def solution(path):
    answer = []
    path = list(map(str, str(path).strip()))
    queue = deque([i for i in path])
    
    navi = []
    count = 0
    stack = [queue[0]]
    direction = []
    for i in range(len(path)):
        top = queue[0]
        
        if stack[0] != top:  
            direc = queue[0]
            if stack[0] == 'E':
                if direc == 'N': direction.append('left')
                else: direction.append('right')
            elif stack[0] == 'S':
                if direc == 'E': direction.append('left')
                else: direction.append('right')
            if stack[0] == 'W':
                if direc == 'S': direction.append('left')
                else: direction.append('right')
            if stack[0] == 'N':
                if direc == 'W': direction.append('left')
                else: direction.append('right')
                
            stack.pop()
            stack.append(top)
            navi.append(count)
            count = 0

        if stack[0] == top:
            count += 1
            if len(queue) != 0: queue.popleft()
            
    navi.append(count)
    print(navi)
    print(direction)

    m = 0
    for i in range(len(direction)):
        time = 0
        if i == 0:
            m = navi[i]*100
            if i == 0 and navi[i] > 3:
                time = 1
                m = navi[i]*100 - 100
        if i > 0 and navi[i] > 3:
            time = navi[i]-1
            m = navi[i]*100 - 100
        elif i > 0 and navi[i] <= 3:
            time += navi[i-1]
            m = navi[i]*100 
        
        sentence = "Time " + str(time) + ":" + " Go straight " + str(m) + "m" + " and turn " + str(direction[i])
        answer.append(sentence)
            
    return answer

path = input().strip()
print(solution(path))
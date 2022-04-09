def solution(answers):
    answer = []
    arr = [[1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]]
    
    for i in range(3):
        arr[i] = (arr[i]*(len(answers)//len(arr[i]))) + (arr[i][:len(answers)%len(arr[i])])

    count = {1:0, 2:0, 3:0}
    
    for i in range(len(answers)):
        if answers[i] == arr[0][i]:
            count[1] += 1
        if answers[i] == arr[1][i]:
            count[2] += 1
        if answers[i] == arr[2][i]:
            count[3] += 1 

    check = max(count, key=lambda i: count[i])
    for key, values in count.items():
        if values == count[check]:
            answer.append(key)
    return answer

# 문자열 만큼 반복해서 같은 숫자가 있으면 count 증가 
# 6은 9로 9는 6으로 대체 가능
# 0 - 9 까지 0으로 초기화
# 반복되면 +1 증가
# 가장 큰 값이 최종 값

N = input()

array = [0] * 10

for i in range(len(N)):
    index = int(N[i])
    if index == 6 or index == 9:
        if array[6] <= array[9]:
            array[6] += 1
        else:
            array[9] += 1
    else:
        array[index] += 1
        
print(max(array))
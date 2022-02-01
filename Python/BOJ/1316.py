N = int(input())

count = 0

for i in range(N):
    word = input()
    error = 0
    for i in range(len(word)-1):
        #연속된 문자가 다른 값일 때
        if word[i] != word[i+1]:
            #이후 문자 새로운 단어 생성
            result = word[i+1:]
            #남은 문자열에 현재 글자가 있다면
            if result.count(word[i]) > 0:
                error += 1

    if error == 0:
        count += 1
        
print(count)
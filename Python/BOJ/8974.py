# 122333444455555 순으로 리스트 형성
# 반복문의 i만큼 리스트에 추가
# i만큼 반복할 횟수는 check, 
# num은 리스트로 저장
# num == check 되면 check 초기화, num은 1 추가

A, B = map(int, input().split())

array = []
num = check = 1
for i in range(B):
    array.append(num)
    if num == check:
        num += 1
        check = 0
    check += 1
print(sum(array[A-1:B]))
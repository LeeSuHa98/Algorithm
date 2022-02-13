# A랑 B 리스트 비교 B를 우선으로 일치하는 리스트 번호 찾음
# A는 B랑 일치하는 문자열이 위치한 번호에서 가로로 출력
# B는 A랑 일치하는 문자열이 위치한 번호에서 세로로 출력

A, B = input().split()

for i in A:
    if i in B:
        a = B.index(i)
        b = A.index(i)
        break
    
for i in range(len(B)):
    for j in range(len(A)):
        if i == a:
            print(A, end='')
            break;
        elif j == b:
            print(B[i], end='')
        else:
            print('.', end='')
    print()
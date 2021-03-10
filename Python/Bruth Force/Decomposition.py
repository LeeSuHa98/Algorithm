N = int(input())

result = 0;
check = 0
for i in range(1, N+1):
    a = list(map(int, str(i)))
    check = i + sum(a)
    if check == N:
        result = i
        break
    elif i == N:
        result = 0
    
print(result)

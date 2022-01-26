# solve 1
# sort code and effective

N = input().split()
result = []
for i in range(1, 8):
    check = int(N[i]) - int((N[i-1]))
    if abs(check) == 1:
        result.append(check)
    else:
        result.append(0)

if result.count(1) == 7:
    print('ascending')
elif result.count(-1) == 7:
    print('descending')
else:
    print('mixed')
    
# solve 2
# first code uneffective

N = list(map(int, input().split()))

if N == sorted(N):
    print('ascending')
elif N == sorted(N, reverse=True):
    print('descending')
else:
    print('mixed')
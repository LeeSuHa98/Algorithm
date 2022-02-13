N = int(input())

a = [1, 0]
b = [0, 1]

for i in range(2, N+1):
    aCount = a[i-1] + a[i-2]
    a.append(aCount)
    bCount = b[i-1] + b[i-2]
    b.append(bCount)
    
print(a[N], b[N])
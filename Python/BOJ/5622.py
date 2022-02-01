N = input()
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
count = 0
for i in range(len(N)):
    for j in dial:
        if N[i] in j:
            count += dial.index(j) + 3
print(count)
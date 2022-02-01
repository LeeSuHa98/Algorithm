alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

N = input()

for i in alphabet:
    if i in N:
        N = N.replace(i, '*')
    
print(len(N))
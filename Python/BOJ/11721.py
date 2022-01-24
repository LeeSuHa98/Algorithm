N = input()

mystring = len(N)

count = mystring//10

for i in range(count+1):
    print(N[10*i:10*(i+1)])
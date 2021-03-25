N = input()
list = []
value = 0

for i in N:
    if i.isalpha():
        list.append(i)
    else:
        value += int(i)

list.sort()

if value != 0:
    list.append(str(value))

print(''.join(list))
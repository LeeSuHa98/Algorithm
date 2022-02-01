X = int(input())

line = 0
max = 0

while X > max:
    line += 1
    max += line
    
gap = max - X
#사선라인이 짝수일 때
if line % 2 == 0:
    top = line - gap
    bottom = gap + 1
else:
    top = gap + 1
    bottom = line - gap

print(f'{top}/{bottom}')
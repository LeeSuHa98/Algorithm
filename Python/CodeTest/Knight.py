knight = input()
row = int(knight[1])
col = int(ord(knight[0])) - int(ord('a')) + 1

move = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

result = 0
for i in move:
    dx = row + i[0]
    dy = col + i[1]

    if dx >= 1 and dx <= 8 and dy >= 1 and dy <= 8:
        result += 1

print(result)
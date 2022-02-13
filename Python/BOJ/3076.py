R, C = map(int, input().split())
A, B = map(int, input().split())

for col in range(R):
    for _ in range(A):
        for row in range(C):
            if (col+row)%2:
                print('.'*B, end='')
            else:
                print('X'*B, end='')
        print()
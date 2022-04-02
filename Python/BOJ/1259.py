import sys
input = sys.stdin.readline


while True:
    command = input().strip()
    length = len(command)//2
    check = command[::-1]
    if command == '0':
        exit()
    if command[:length] == check[:length]:
        print('yes')
    else:
        print('no')
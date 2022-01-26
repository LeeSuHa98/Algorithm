from string import ascii_lowercase

S = input()

for i in list(ascii_lowercase):
    print(S.find(i))
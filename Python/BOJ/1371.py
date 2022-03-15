import sys

sentence = sys.stdin.read().replace('\n', '').replace(' ', '')

alphabet = [0 for i in range(26)]

for i in sentence:
    if i.islower():
        alphabet[ord(i) - 97 ] += 1

for i in range(26):
    if alphabet[i] == max(alphabet):
        print(chr(i + 97), end='')
import sys

name = input()
count = [0 for i in range(26)]

for i in name:
    count[ord(i) - 65] += 1
    
odd = 0
odd_alphabet = ""
alphabet = ""

for i in range(26):
    if count[i] % 2 == 1:
        odd += 1
        odd_alphabet += chr(i + 65)
    alphabet += chr(i + 65) * (count[i] // 2)
    
if odd > 1:
    print("I'm Sorry Hansoo")
else:
    print(alphabet + odd_alphabet + alphabet[::-1])      
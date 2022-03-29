import sys
input = sys.stdin.readline


comA = [0] * 26
comB = [0] * 26

for i in input().strip():
    comA[ord(i) - 97] += 1
for i in input().strip():
    comB[ord(i) - 97] += 1
    
result = 0
for i in range(26):
    result += abs(comA[i] - comB[i])
    
print(result)
import sys

X = [0] * 26
Y = [0] * 26
result = 0

for i in sys.stdin.readline().strip():
    X[ord(i) - 97] += 1
for i in sys.stdin.readline().strip():
    Y[ord(i) - 97] += 1
for i in range(26):
    result += abs(X[i] - Y[i])

print(result)
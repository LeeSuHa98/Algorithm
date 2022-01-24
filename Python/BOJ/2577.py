A = int(input())
B = int(input())
C = int(input())

max = A * B * C

result = list(str(max))

for i in range(10):
    print(result.count(str(i)))

# max = str(max)

# count = [0,0,0,0,0,0,0,0,0,0]
# for i in range(len(max)):
#     if(max[i] == '0'):
#         count[0] += 1
#     elif(max[i] == '1'):
#         count[1] += 1
#     elif(max[i] == '2'):
#         count[2] += 1
#     elif(max[i] == '3'):
#         count[3] += 1
#     elif(max[i] == '4'):
#         count[4] += 1
#     elif(max[i] == '5'):
#         count[5] += 1
#     elif(max[i] == '6'):
#         count[6] += 1
#     elif(max[i] == '7'):
#         count[7] += 1
#     elif(max[i] == '8'):
#         count[8] += 1
#     else:
#         count[9] += 1

# for i in range(len(count)):
#     print(count[i])
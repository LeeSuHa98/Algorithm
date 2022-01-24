N = int(input())
# for i in range(N, 0, -1):
#     print(("*"*i).rjust(N))
for i in reversed(range(1, N+1)):
    print(("*"*i).rjust(N))
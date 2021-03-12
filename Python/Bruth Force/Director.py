#baekjoon 1436

N = int(input())

count = 0;
end_num = 666;

while True:
    if '666' in str(end_num):
        count += 1
    if count == N:
        print(end_num)
        break;
    end_num += 1
import sys
input = sys.stdin.readline


N = int(input())

score = []
for i in range(N):
    team, time = map(str, input().split())
    
    time = list(map(int, time.split(":")))
    
    score.append([team, int(time[0]), int(time[1])])

print(score)

check = 0
one = 0
two = 0
check_team = ""
for i in range(N):
    t, h, m = score.pop()
    
    if i == 0:
        check = h*60+m
        check_team = team
    else:
        if 
        if check_team == team:
            if team == '1':
                one += h*60+m
            else:
                two += h*60+m
        else:
            
                
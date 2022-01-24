days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week = 0

x, y = input().split()

x = int(x)
y = int(y)

for i in range(x):
   week += days[i]

week += y

if(week % 7 == 1):
    print("MON")
elif(week % 7 == 2):
    print("TUE")
elif(week % 7 == 3):
    print("WED")
elif (week % 7 == 4):
    print("THU")
elif(week % 7 == 5):
    print("FRI")
elif(week % 7 == 6):
    print("SAT")
else:
    print("SUN")
    
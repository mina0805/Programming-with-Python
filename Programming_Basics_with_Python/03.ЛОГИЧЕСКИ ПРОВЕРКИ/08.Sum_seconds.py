# time1 = int in sec
# time2 = int in sec
# time3 = int in sec

# output >> time1 + time2 + time3 in min and sec

time1 = int(input())
time2 = int(input())
time3 = int(input())

min = 0
sec = 0

total_time = time1 + time2 + time3



min = total_time// 60
sec = total_time % 60

if total_time <= 9:
    print(str(min) + ":0" + str(sec))

elif total_time <= 59:
    print(str(min) + ":" + str(sec))

elif min >= 1 and sec <= 9:
    print(str(min) + ":0" + str(sec))
elif min >= 1 and sec >= 10:
        print(str(min) + (":") + str(sec))





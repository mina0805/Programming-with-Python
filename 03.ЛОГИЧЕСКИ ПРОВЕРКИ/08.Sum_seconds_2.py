time1 = int(input())
time2 = int(input())
time3 = int(input())

min = 0
sec = 0

total_time = time1 + time2 + time3


min = total_time//60
sec = total_time % 60

if sec <=9:
    print(str(min) + ":0" + str(sec))
else:
    print(str(min) + ":" + str(sec))



#     • Първият ред съдържа час на изпита – цяло число от 0 до 23.
#     • Вторият ред съдържа минута на изпита – цяло число от 0 до 59.
#     • Третият ред съдържа час на пристигане – цяло число от 0 до 23.
#     • Четвъртият ред съдържа минута на пристигане – цяло число от 0 до 59.
#    • “Late”, ако студентът пристига по-късно от часа на изпита.
#    • “On time”, ако студентът пристига точно в часа на изпита или до 30 минути по-рано.
#   • “Early”, ако студентът пристига повече от 30 минути преди часа на изпита.

exam_h = int(input("exam hour 0 - 23: "))
exam_m = int(input("exam minute 0 - 59: "))
arrival_h = int(input("arrival hour 0 -23: "))
arrival_m = int(input("arrival minute 0 - 59: "))

import math

# late if:
late_1 = (exam_h == arrival_h) and (exam_m < arrival_m)
late_2 = (exam_h < arrival_h) and (exam_m == arrival_m)
late_3 = (exam_h < arrival_h) and (exam_m < arrival_m)

#on time:
on_time_1 = (exam_h == arrival_h) and (exam_m == arrival_m)
on_time_2 = (exam_h == arrival_h) and ((exam_m - arrival_m) <= 30)
on_time_3 = ((exam_h - arrival_h) == 1) and (arrival_m > exam_m) and ((arrival_m - exam_m) >= 30)
on_time_4 = ((exam_h - arrival_h) == 1) and (exam_m > arrival_m) and ((exam_m - arrival_m) >= 30)

if late_1 or late_2 or late_3:
    print("late")
    if late_1:
        print((str(arrival_m - exam_m)) + ' minutes after the the start')
    if late_2:
        print(str(arrival_h - exam_h) + (":00 hours after the start"))
    if late_3 and ((arrival_m - exam_m) >= 10):
        print(str(arrival_h - exam_h) + ":" +(str(arrival_m - exam_m) + (" hours after the start")))
    if late_3 and ((arrival_m - exam_m)< 10):
        print(str(arrival_h - exam_h) + ":0" +(str(arrival_m - exam_m) + (" hours after the start")))

elif on_time_1 or on_time_2 or on_time_3 or on_time_4:
    print('on time')

# early - everything else




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


# late if:
late_1 = (exam_h == arrival_h) and (exam_m < arrival_m)
late_2 = (exam_h < arrival_h) and (exam_m == arrival_m)
late_5 = (arrival_h - exam_h) == 1 and exam_m > arrival_m
late_10 = (arrival_h - exam_h) == 1 and exam_m < arrival_m
late_6 = (arrival_h - exam_h) == 1 and exam_m < arrival_m and ((arrival_m - exam_m) < 9)
late_9 = (arrival_h - exam_h) == 1 and exam_m < arrival_m and ((arrival_m - exam_m) > 9)
late_7 = (arrival_h - exam_h) > 1 and exam_m > arrival_m
late_8 = (arrival_h - exam_h) > 1 and exam_m < arrival_m

#early if:

if late_1 or late_2 or late_5 or late_6 or late_7 or late_8 or late_9 or late_10:
    print("late")
    if late_1:
        print((str(arrival_m - exam_m)) + ' minutes after the the start')

    elif late_2:
        print(str(arrival_h - exam_h) + ":00 hours after the start")
    elif late_5:
        print((str(60 - (exam_m - arrival_m))) + " minutes after start")
    elif late_6:
        print("1:0") + (str(arrival_m - exam_m)) + " hours after the start"
    elif late_9:
        print("1:") + (str(arrival_m - exam_m)) + " hours after the start"
    elif late_7:
        print(str(arrival_h - exam_m - 1)), ":", (str(60 - (exam_m - arrival_m)) + " hours after the start")
    elif late_8:
        print(str(arrival_h - exam_h)) + ":" + (str(arrival_m - exam_m)) + " hours after the start"
    elif late_10:
        print(str(60 - (exam_m - arrival_m))) + " minutes after start"

#on time:

on_time_1 = (exam_h == arrival_h) and (exam_m == arrival_m)
on_time_2 = (exam_h == arrival_h) and ((exam_m - arrival_m) <= 30)
on_time_3 = ((exam_h - arrival_h) == 1) and (((60 - arrival_m) + exam_m) <= 30)

if on_time_1 or on_time_2 or on_time_3:
    print('on time')

    if on_time_1:
        pass
    elif on_time_2:
        print((str(exam_m - arrival_m)) + " minutes before the start")
    elif on_time_3:
        print((str((60 - arrival_m) + exam_m) + " minutes before the start"))

# early:

early_1 = ((exam_h - arrival_h) > 1) and (exam_m == arrival_m)
early_2 = ((exam_h - arrival_h) == 1) and ((60 - (exam_m - arrival_m)) < 30)
early_3 = ((exam_h - arrival_h) > 1) and exam_m > arrival_m and ((exam_m - arrival_m) > 9)
early_6 = ((exam_h - arrival_h) > 1) and exam_m > arrival_m and ((exam_m - arrival_m) < 9)
early_4 = ((exam_h - arrival_h) > 1) and exam_m < arrival_m and ((60 - (arrival_m - exam_m)) > 9)
early_7 = ((exam_h - arrival_h) > 1) and exam_m < arrival_m and ((60 - (arrival_m - exam_m)) < 9)
early_5 = (exam_h == arrival_h) and ((60 - arrival_m) > 30)

if early_1 or early_2 or early_3 or early_4 or early_5:
    print('early')

    if early_1:
        print((str(exam_h - arrival_h) + ":00 hours before the start"))
    elif early_2:
        print((str(60 - arrival_m)) + " minutes before the start")
    elif early_3:
        print((str(exam_h - arrival_h) + ":" + (str(exam_m - arrival_m) + " hours before the start")))
    elif early_4:
        print(str(exam_h - arrival_h - 1) + ":" + (str(60 - (arrival_m - exam_m)) + " hours before the start"))
    elif early_6:
        print((str(exam_h - arrival_h) + ":0" + (str(exam_m - arrival_m) + " hours before the start")))
    elif early_7:
        print(str(exam_h - arrival_h - 1) + ":0" + (str(60 - (arrival_m - exam_m))+ " hours before the start"))


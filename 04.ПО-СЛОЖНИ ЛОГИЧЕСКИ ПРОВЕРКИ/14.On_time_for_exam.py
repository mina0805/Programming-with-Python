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

on_time_exact = exam_h == arrival_h and exam_m == arrival_m
# on_time_early =
   #1 if exam_h //exam_m == 0 and exam

# late if:
late_1 = exam_h <= arrival_h or exam_m < arrival_m
late_2 = exam_h < arrival_h and exam_m == arrival_m
late_3 = exam_h == arrival_h and exam_m < arrival_m

if late_1 or late_2 or late_3:
    print("late")
    if late_1 and (arrival_m - exam_m) >= 10:
        print((str(arrival_m - exam_m)) + ' minutes after the the start')

    elif late_1 and (arrival_m - exam_m) < 10:
        print((str(arrival_m - exam_m)), 'minutes after the the start')
    if late_2:
        print(str(arrival_h - exam_h) + (" hours after the start"))





# on time if:
#1. exam_h == arrival h and exam_m 30 or less bigger than arrival_m
#2. exam_h bigger than arrival_h with 0.5 hour or less and exam_m == arrival_m
#3. exam_h == arrival_h and exam_m bigger than arrival_m with 30 min or less

# early -> everything else




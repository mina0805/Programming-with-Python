age = float(input())
gender = input()

if age >= 16:
    if gender == "m" or gender == "M":
        print("Mr.")
    elif gender =="f" or gender == "F":
        print("Ms.")
elif age < 16:
    if gender == "m" or gender == "M":
        print("Master.")
    elif gender =="f" or gender == "F":
        print("Miss.")




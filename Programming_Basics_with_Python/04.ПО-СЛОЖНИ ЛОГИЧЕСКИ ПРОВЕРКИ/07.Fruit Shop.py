fruit = input().lower()
day = input().lower()
quantity = float(input())
total = ""

if day == 'monday' or day == 'tuesday' or day == 'wednesday' or day == 'thursday' or day == 'friday':
    if fruit == "banana":
        total = quantity * 2.50
    elif fruit == "apple":
        total = quantity * 1.20
    elif fruit == "orange":
        total = quantity * 0.85
    elif fruit == "grapefruit":
        total = quantity * 1.45
    elif fruit == "kiwi":
        total = quantity * 2.70
    elif fruit == "pineapple":
        total = quantity * 5.50
    elif fruit == "grapes":
        total = quantity * 3.85
    else:
        total = "error"
elif day == 'saturday' or day == 'sunday':
    if fruit == "banana":
        total = quantity * 2.70
    elif fruit == "apple":
        total = quantity * 1.25
    elif fruit == "orange":
        total = quantity * 0.9
    elif fruit == "grapefruit":
        total = quantity * 1.6
    elif fruit == "kiwi":
        total = quantity * 3
    elif fruit == "pineapple":
        total = quantity * 5.60
    elif fruit == "grapes":
        total = quantity * 4.2
    else:
        total = "error"
else:
    total = 'error'
if total == 'error':
    print(total)
else:
    print("%.2f" % total)

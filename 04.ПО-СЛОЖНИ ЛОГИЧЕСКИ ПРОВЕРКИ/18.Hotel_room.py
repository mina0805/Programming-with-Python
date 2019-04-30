room = input().lower()
month = input().lower()
nights = int(input())

price = 0

if room == 'studio':
    if month == 'may' or month == 'october':
        if nights <= 7:
            price = nights * 50
        elif 7 < nights <= 14:
            price = (nights * 50) * 0.95
        elif nights > 14:
            price = nights * 50 * 0.7

    elif month == 'june' or month == 'september':
        if nights <= 14:
            price = nights * 75.20
        elif nights > 14:
            price = nights * 75.2 * 0.8

    elif month == 'july' or month == 'august':
        price = nights * 76

elif room == 'apartment':
    if month == 'may' or month == 'october':
        if nights <= 14:
            price = nights * 65
        elif nights > 14:
            price = nights * 65 * 0.9
    elif month == 'june' or month == 'september':
        if nights <= 14:
            price = nights * 68.7
        elif nights > 14:
            price = nights * 68.7 * 0.9
    elif month == 'july' or month == 'august':
        if nights <= 14:
            price = nights * 77
        elif nights > 14:
            price = nights * 77 * 0.9

print("%.2f" % price)





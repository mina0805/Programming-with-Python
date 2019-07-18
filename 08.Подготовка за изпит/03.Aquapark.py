month = input().lower
hours = float(input())
people = int(input())
day_night = input().lower()
per_h = 0

if month == "march" or month == "april" or month == "may":
    if day_night == "day":
        per_h = 10.5
    elif day_night == "night":
        per_h = 8.4
        price_per_person = per_h * hours
        total_price = price_per_person * people

elif month == "june" and month == "july" or month == "august":
    if day_night == "day":
        per_h = 12.6
    elif day_night == "night":
        per_h = 10.2
        price_per_person = per_h * hours
        total_price = price_per_person * people

price_per_person = hours * per_h
total_price = price_per_person * people
if people >= 4:
    price_per_person *= 0.9
if hours >= 5:
    price_per_person *= 0.5

print("%.2f" % price_per_person)
print("%.2f" % total_price)

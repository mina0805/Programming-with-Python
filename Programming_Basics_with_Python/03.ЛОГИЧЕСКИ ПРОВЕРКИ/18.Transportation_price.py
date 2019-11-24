
#    • Tакси. Начална такса: 0.70 лв. Дневна тарифа: 0.79 лв. / км. Нощна тарифа: 0.90 лв. / км.
# • Автобус. Дневна / нощна тарифа: 0.09 лв. / км. Може да се използва за разстояния минимум 20 км.
#    • Влак. Дневна / нощна тарифа: 0.06 лв. / км. Може да се използва за разстояния минимум 100 км.

# enter int km
# enter day or night

# if distance <= 20 and day >> cab + 0.70
# if distance <= 20 and night  >> cab + 0.79
# if 20 < distance <= 100  >> bus
# if distance > 100 >> train

km = int(input())
time = input()

price_day = 0.7 + km * 0.79
price_night = 0.7 + km * 0.90

if 1 <= km < 20 and time == "day":
    print("%.2f" % price_day)

elif 1 <= km < 20 and time == "night":
    print("%.2f" % price_night)

elif 20 <= km < 100 and time == "day":
    print("%.2f" % (km * 0.09))

elif 20 <= km < 100 and time == "night":
    print("%.2f" % (km * 0.09))

elif km >= 100 and time == "day":
    print("%.2f" % (km * 0.06))

elif km >= 100 and time == "night":
    print("%.2f" % (km * 0.06))

else:
    print("invalid entry")



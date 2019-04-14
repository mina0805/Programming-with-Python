# playtime >= 30000 min >> tom sleeps well
# playtime < 30000 min >> tom will run away
# workday >> 63 min
# dayoff >> 127 min
# 365 days a year
# Пример: 20 почивни дни -> работните дни са 345 (365 – 20 = 245).
# Реалното време за игра е 24 275 минути (345 * 63 + 20 *127).
# Разликата от нормата е 5 725 минути (30 000 – 24 275 = 5 725) или 95 часа и 25 минути.

# b = a % 60 -> min
# c = a // 60 -> h

daysoff = int(input())
workdays = 365 - daysoff
play = workdays * 63 + daysoff * 127
dif = 30000 - play
if dif >= 0:
    h_over = dif // 60
    min_over = dif % 60
    print("Tom sleeps well")
    print(str(h_over) + " hours and " + str(min_over) + " minutes less for play")


elif dif < 0:
    neg_dif = dif * (-1)
    h_under = (neg_dif // 60)
    min_under = (neg_dif % 60)
    print("Tom will run away")
    print(str(h_under) + " hours and " + str(min_under) + " min more for play")
elif workdays < 0:
    print("invalid entry")
elif workdays > 365:
    print("invalid entry")






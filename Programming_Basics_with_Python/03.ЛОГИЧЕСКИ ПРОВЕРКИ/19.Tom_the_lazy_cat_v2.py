daysoff = int(input())
workdays = 365 - daysoff
play = workdays * 63 + daysoff * 127
dif = 30000 - play

if daysoff < 0 or daysoff > 365:
    print("invalid entry")

elif dif >= 0:
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






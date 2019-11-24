budget = float(input())
season = input()

if budget <= 100:
    print("Somewhere in Bulgaria")
    if season == "summer":
        budget *= 0.3

    elif season == "winter":
        budget *= 0.7

elif 100 < budget <= 1000:
    print("Somewhere in Balkans")
    if season == "summer":
        budget *= 0.4

    elif season == "winter":
        budget *= 0.8
if season == 'summer:':
    print('Camp -' + str("% .2f" % budget))
elif season == 'winter':
    print("Hotel - " + str("% .2f" % budget))

if budget > 1000:
    print('Somewhere in Europe')
    budget *= 0.9
    print("Hotel - " + str("% .2f" % budget))

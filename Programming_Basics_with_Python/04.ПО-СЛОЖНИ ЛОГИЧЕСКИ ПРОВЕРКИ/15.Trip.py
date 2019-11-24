budget = float(input())
season = input()

# output
# Бюджета определя дестинацията,
# а сезона определя колко от бюджета ще изхарчи.
# Ако е лято ще почива на къмпинг,
# а зимата в хотел.
# Ако е в Европа, независимо от сезона ще почива в хотел.
# Всеки къмпинг или хотел, според дестинацията,
# има собствена цена която отговаря на даден процент от бюджета:
#     • При 100лв. или по-малко – някъде в България
#         ◦ Лято – 30% от бюджета
#         ◦ Зима – 70% от бюджета
#     • При 1000лв. или по малко – някъде на Балканите
#         ◦ Лято – 40% от бюджета
#         ◦ Зима – 80% от бюджета
#     • При повече от 1000лв. – някъде из Европа
#        ◦ При пътуване из Европа, независимо от сезона ще похарчи 90% от бюджета.
if budget <= 100:
    print("Somewhere in Bulgaria")
    if season == "summer":
        budget *= 0.3
        print("Camp - " + str("% .2f" % budget))
    elif season == "winter":
        budget *= 0.7
        print("Hotel - " + str("% .2f" % budget))


elif 100 < budget <= 1000:
    print("Somewhere in Balkans")
    if season == "summer":
        budget *= 0.4
        print("Camp - " + str("% .2f" % budget))
    elif season == "winter":
        budget *= 0.8
        print("Hotel - " + str("% .2f" % budget))

elif budget > 1000:
    print("Somewhere in Europe")
    budget *= 0.9
    print("Hotel - " + str("% .2f" % budget))

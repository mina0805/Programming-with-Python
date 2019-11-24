
# Входът e сума за конвертиране + входна валута + изходна валута.
# Изходът е едно число – преобразуваната сума по посочените по-горе курсове,
# закръглен до 2 цифри след десетичната точка.
# 1 BGN
# 1.79549 = 1 USD
# 1.95583 = 1 EUR
# 2.53405 = 1 GBP
################
BGN = 1
USD = 1.79549 * BGN
EUR = 1.95583 * BGN
GBP = 2.53405 * BGN


amount_in = float(input())
currency_from = input()
currency_to = input()

if currency_from == "USD" and currency_to == "BGN":
    amount_out = USD * amount_in
    print(str(round(amount_out, 2)) + " BGN")
elif currency_from == "EUR" and currency_to == "BGN":
    amount_out = EUR * amount_in
    print(str(round(amount_out, 2)) + ' BGN')
elif currency_from == "GBP" and currency_to == "BGN":
    amount_out = GBP * amount_in
    print(str(round(amount_out, 2)) + ' BGN')

elif currency_from == "BGN" and currency_to == "USD":
    amount_out = amount_in/USD
    print(str(round(amount_out, 2)) + " USD")
elif currency_from == "EUR" and currency_to == "USD":
    amount_out = EUR/USD * amount_in
    print(str(round(amount_out, 2)) + " USD")
elif currency_from == "GBP" and currency_to == "USD":
    amount_out = GBP/USD * amount_in
    print(str(round(amount_out, 2)) + " USD")

elif currency_from == "BGN" and currency_to == "EUR":
    amount_out = BGN/EUR * amount_in
    print(str(round(amount_out, 2)) + " EUR")
elif currency_from == "USD" and currency_to == "EUR":
    amount_out = USD/EUR * amount_in
    print(str(round(amount_out, 2)) + " EUR")
elif currency_from == "GBP" and currency_to == "EUR":
    amount_out = GBP/EUR * amount_in
    print(str(round(amount_out, 2)) + " EUR")

elif currency_from == "BGN" and currency_to == "GBP":
    amount_out = BGN/GBP * amount_in
    print(str(round(amount_out, 2)) + " GBP")
elif currency_from == "EUR" and currency_to == "GBP":
    amount_out = EUR/GBP * amount_in
    print(str(round(amount_out, 2)) + " GBP")





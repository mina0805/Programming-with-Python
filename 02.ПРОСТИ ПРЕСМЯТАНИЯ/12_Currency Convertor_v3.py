
# Входът e сума за конвертиране + входна валута + изходна валута.
# Изходът е едно число – преобразуваната сума по посочените по-горе курсове,
# закръглен до 2 цифри след десетичната точка.
# 1 BGN
# 1.79549 = 1 USD
# 1.95583 = 1 EUR
# 2.53405 = 1 GBP
################
currency_from = input()
amount = float(input())
currency_to = input()
amount_out = " "

if currency_from == "USD":
    amount_out = amount/ 1.79549
elif currency_from == "EUR":
    amount_out = amount/1.95583
elif currency_from == "GBP":
    amount_out = amount/ 2.53405
elif currency_from == "BGN":
    amount_out = amount * 1
elif currency_to == "USD":
    amount_out = amount * 1.79549

if currency_to == "EUR":
    amount_out = amount * 1.95583
if currency_to == "GBP":
    amount_out = amount * 2.53405
if currency_to == "BGN":
    amount_out = amount * 1

print(round(amount_out, 2))








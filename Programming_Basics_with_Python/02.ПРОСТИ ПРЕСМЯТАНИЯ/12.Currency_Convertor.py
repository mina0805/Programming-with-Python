amount = float(input())
currencyFrom = input()
currencyTo = input()

amountInLeva = amount

if(currencyFrom == "USD"):
    amountInLeva *= 1.79549
elif(currencyFrom == "EUR"):
    amountInLeva *= 1.95583
elif(currencyFrom == "GBP"):
    amountInLeva *= 2.53405


if(currencyTo == "USD"):
    amount /= 1.79549
elif(currencyTo == "EUR"):
    amount /= 1.95583
elif(currencyTo == "GBP"):
    amount /= 2.53405


print("%.2f" % amount)
print(round(amount, 2), currencyTo)




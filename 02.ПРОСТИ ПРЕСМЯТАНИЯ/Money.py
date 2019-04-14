Bitcoin = int(input("Enter bitcoin: "))
Chinese = float(input("Enter Chinese: "))
commision = float(input("Enter commision: "))
# bitcoin_to_EUR == 1168/1.95
# Chinese_to_EUR = 0.15 * 1.76 /1.95

Bitcoin_to_EUR = Bitcoin * 1168/1.95

Chinese_to_EUR = Chinese * 0.15 * 1.76/1.95

TotalBitcoin = Bitcoin_to_EUR * (100 - commision)/100
TotalChinese = Chinese_to_EUR * (100 - commision)/100

TotalMoney = TotalBitcoin + TotalChinese
print(TotalMoney)



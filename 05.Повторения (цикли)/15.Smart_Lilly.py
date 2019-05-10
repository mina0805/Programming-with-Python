age = int(input())
laundry_m_price = float(input())
toy_price = int(input())
toy_number = 0
money = 0

for i in range(1, age +1):
    if i % 2 == 1:
        toy_number += 1
    elif i % 2 == 0:
        money += 9

tot_money = money + toy_number * toy_price
print(money)
print(tot_money)
print(toy_number)

if tot_money >= laundry_m_price:
    print('Yes ', str(tot_money - laundry_m_price))
else:
    print('No, ', str(laundry_m_price - tot_money))







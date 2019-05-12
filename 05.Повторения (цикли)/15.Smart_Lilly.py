age = int(input())
laundry_m_price = float(input())
toy_price = int(input())
toy_number = 0
money = 0

for i in range(1, age +1):
    if i % 2 == 1:
        toy_number += 1
    elif i % 2 == 0:
        money = ((money + (i*5))-1)

tot_money = money + (toy_price * toy_number)

if tot_money >= laundry_m_price:
    print('Yes!', str("%.2f" % (tot_money - laundry_m_price)))
else:
    print('No', str("%.2f" % (laundry_m_price - tot_money)))







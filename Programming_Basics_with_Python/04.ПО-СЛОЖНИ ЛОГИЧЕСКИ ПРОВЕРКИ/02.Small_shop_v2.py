product = input().lower()
town = input().lower()
quantity = float(input())
price = ''
if product == 'coffee':
    if town == 'sofia':
        price = 0.5 * quantity
    elif town == 'plovdiv':
        price = 0.4 * quantity
    elif town == 'varna':
        price = 0.45 * quantity

if product == 'water':
    if town == 'sofia':
        price = 0.8 * quantity
    elif town == 'plovdiv':
        price = 0.7 * quantity
    elif town == 'varna':
        price = 0.7 * quantity

if product == 'beer':
    if town == 'sofia':
        price = 1.2 * quantity
    elif town == 'plovdiv':
        price = 1.15 * quantity
    elif town == 'varna':
        price = 1.1 * quantity

if product == 'sweets':
    if town == 'sofia':
        price = 1.45 * quantity
    elif town == 'plovdiv':
        price = 1.3 * quantity
    elif town == 'varna':
        price = 1.35 * quantity

if product == 'peanuts':
    if town == 'sofia':
        price = 1.6 * quantity
    elif town == 'plovdiv':
        price = 1.5 * quantity
    elif town == 'varna':
        price = 1.55 * quantity

print("%.2f" % price)


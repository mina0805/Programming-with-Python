input_list = input()
inventory = {}

while not input_list == "shopping time":

    stock, product, quantity = input_list.split(" ")

    if product in inventory:
        inventory[product] = inventory.get(product) + int(quantity)
    else:
        inventory[product] = int(quantity)
    input_list = input()

input_list = input()

while not input_list == "exam time":

    buy, product, quantity = input_list.split(" ")

    if product not in inventory:
        print(f'{product} doesn\'t exist')

    elif product in inventory and inventory.get(product) <= 0:
        print(f'{product} out of stock')
    else:
        inventory[product] = inventory.get(product) - int(quantity)

for item in inventory:
    if inventory[item] > 0:
        print(f'{item} -> {inventory[item]}')


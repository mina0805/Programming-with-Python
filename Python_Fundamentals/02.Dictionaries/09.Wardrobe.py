n = int(input())

clothes_list = []
clothes_dict = {}

for i in range(n):
    user_entry = input()
    data = user_entry.split(" -> ")
    color = data[0]
    clothes_list = data[1].split(",")

    if color not in clothes_dict:
        clothes_dict[color] = {}

    for item in clothes_list:
        if item in clothes_dict[color]:
            clothes_dict[color][item] = clothes_dict[color].get(item) + 1
        else:
            clothes_dict[color][item] = 1
searched_item = input().split()

for key in clothes_dict:
    print(f'{key} clothes:')
    for value in clothes_dict[key]:
        if searched_item[0] == key and searched_item[1] == value:
            print(f'* {value} -{clothes_dict[key][value]} (found!)')
        else:
            print(f'* {value} - {clothes_dict[key][value]}')



n = int(input())

clothest_list = []
clothes_dict = {}

for i in range(n):
    data = input().split(" -> ")
    color = data[0]
    clothest_list = data[1].split(",")

    if color not in clothes_dict:
        clothes_dict[color] = {}

    for item in clothest_list:
        if item in clothes_dict:
            clothes_dict[color][item] = clothes_dict[color].get(item) + 1
        else:
            clothes_dict[color][item] = 1
searched_item = input().split()

for key in clothes_dict:
    print(f'{key} clothes:')
    for value in clothes_dict:
        if searched_item[0] == key and searched_item[1] == value:
            print(f'*{value} -{clothes_dict[key][value]} (found!)')
        #else:
            #print(f'* {value} - {clothes_dict[key][value]}')
#
            #print(f'* {value} - {clothes_dict[key][value]}')

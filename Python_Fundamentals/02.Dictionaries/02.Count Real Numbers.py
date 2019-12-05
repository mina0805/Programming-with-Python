list_num = list(map(float, input().split(" ")))
my_dict = {}

for item in list_num:
    if item in my_dict:
        my_dict[item] += 1
    else:
        my_dict[item] = 1
for item in sorted(my_dict.keys()):
    print(f'{item} -> {my_dict[item]} times')





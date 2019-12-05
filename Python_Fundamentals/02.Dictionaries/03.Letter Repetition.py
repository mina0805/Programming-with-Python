single_string = input()
dict_count = {}
for item in single_string:
    if item in dict_count:
        dict_count[item] += 1
    else:
        dict_count[item] = 1
for item in dict_count:
    print(f'{item} -> {dict_count[item]}')

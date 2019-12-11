data = input()
my_dict = {}

while data != "end":

    lst = list(map(str.strip, data.split("=")))
    dict_key = lst[0]
    dict_value = lst[1]

    if dict_value.isnumeric():
        my_dict[dict_key] = int(dict_value)
    else:
        value_to_replace = my_dict.get(dict_value)
        if value_to_replace:
            my_dict[dict_key] = value_to_replace

    data = input()

for item in my_dict:
    print(f'{item} === {my_dict[item]}')





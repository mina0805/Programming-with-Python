raw_data = input()
phone_dict = {}

while raw_data != "Over":
    lst = list(map(str.strip, raw_data.split(":")))
    dict_key = lst[0]
    dict_value = lst[1]

    if dict_value.isnumeric():
        phone_dict[dict_key] = int(dict_value)
    elif dict_key.isnumeric():
        phone_dict[dict_value] = int(dict_key)

    raw_data = input()

for item in sorted(phone_dict):
    print(f'{item} -> {phone_dict[item]}')



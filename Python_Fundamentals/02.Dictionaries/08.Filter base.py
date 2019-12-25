data = input()
dict_age = {}
dict_salary = {}
dict_position = {}
master_dict = {}
while data != "filter base":
    key, value = data.split("->")
    master_dict[key] = value
    data = input()
    print(master_dict)
    try:
        master_dict[value]

    except ValueError:
        print('bla')










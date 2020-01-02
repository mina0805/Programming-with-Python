raw_data = input().lower()
shells = {}


while raw_data != "aggregate":
    lst = list(map(str.strip, raw_data.split(" ")))
    dict_key = lst[0]
    dict_value = lst[1]
    if dict_key not in shells:
        shells[dict_key] = {}
    if dict_value.isnumeric():
        shells[dict_key] = int(dict_value)
    raw_data = input()


print(shells)






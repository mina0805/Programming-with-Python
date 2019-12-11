data = input()
name = data.split()[0]
num = data.split()[1]
my_dict = {}
while not input() == "end":
    if name not in my_dict.keys():
        my_dict[name] = num
print(my_dict)

        # if key not in d.keys():
#     d[key] = value





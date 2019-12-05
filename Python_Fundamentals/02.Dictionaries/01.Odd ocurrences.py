input_list = input().split(" ")
my_dict = {}

for item in input_list:
    if item.lower() in my_dict:
        my_dict[item.lower()] += 1
    else:
        my_dict[item.lower()] = 1
result = ""
for item in my_dict:
    if my_dict[item] % 2 != 0:
        result += item + ", "

print(result.strip(", "))




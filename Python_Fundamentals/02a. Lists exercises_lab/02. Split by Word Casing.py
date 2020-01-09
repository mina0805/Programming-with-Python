raw_data = input()

lower_list = []
upper_list = []
mixed_list = []
seperator_list = [',', ';', ':', '.', '!', '(', ')', '"','\'', '\\', '/', '[', ']']

for i in seperator_list:
    raw_data = raw_data.replace(i, " ")

new_list = raw_data.split()

for i in new_list:
    if i == i.lower() and i.isalnum():
        lower_list.append(i)
    elif i.upper() and i.isalnum():
        upper_list.append(i)
    else:
        mixed_list.append(i)

print(lower_list)
print(upper_list)
print(mixed_list)

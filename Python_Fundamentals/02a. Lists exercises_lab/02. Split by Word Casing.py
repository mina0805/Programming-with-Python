raw_data = input()

lower_list = []
upper_list = []
mixed_list = []
seperator_list = [',', ';', ':', '.', '!', '(', ')', '"','\'', '\\', '/', '[', ']']

for i in seperator_list:
    raw_data = raw_data.replace(i, " ")

new_list = raw_data.split()

for i in new_list:
    if i == i.lower() or i.isalpha():
        lower_list.append(i)
    elif i == i.upper() and i.isalpha():
        upper_list.append(i)
    else:
        mixed_list.append(i)

print('Lower-case:', ', '.join(lower_list))
print('Upper-case:', ', '.join(upper_list))
print('Mixed-list:', ', '.join(mixed_list))



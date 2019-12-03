input_list =list(input().split("|"))
output_list =[]

for item in reversed(input_list):
    temp_list = item.split(" ")
    for item2 in temp_list:
        if item2 != "":
            output_list.append(item2)

for i in output_list:
    print(f' {i }', end ="")




my_list = input().split(" ")
output_list = []

def right_rotate(my_list, num):
    output_list = []

    # Will add values from n to the new list
    for item in range(len(my_list) - 1, len(my_list)):
        output_list.append(my_list[item])

        # Will add the values before
    # n to the end of new list
    for item in range(0, len(my_list) - 1):
        output_list.append(my_list[item])

    for item in output_list:
        print(item, end=" ")


right_rotate(my_list, 1)
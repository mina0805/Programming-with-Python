my_list = input().split(" ")

output_list = []


def rightRotate(my_list, num):
    output_list = []

    # Will add values from n to the new list
    for item in range(len(my_list) - num, len(my_list)):
        output_list.append(my_list[item])

        # Will add the values before
    # n to the end of new list
    for item in range(0, len(my_list) - num):
        output_list.append(my_list[item])

    for item in output_list:
        print(item, end=" ")

rightRotate(my_list, 1)
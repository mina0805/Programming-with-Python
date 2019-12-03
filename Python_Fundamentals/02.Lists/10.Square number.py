list_num = list(map(int, input().split(" ")))
output_list = []
import math

for item in list_num:
    root = math.sqrt(item)
    if int(root + 0.5) ** 2 == item:
        output_list.append(item)
output_list.sort(reverse = True)
for item in output_list:
    print(f'{item} ', end ="")

# # Taking the input from user
# number = int(input("Enter the Number"))
#
# root = math.sqrt(number)
# if int(root + 0.5) ** 2 == number:
#     print(number, "is a perfect square")
# else:
#     print(number, "is not a perfect square")
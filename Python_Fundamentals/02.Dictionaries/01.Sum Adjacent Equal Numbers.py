list_num = list(map(int, input().split(" ")))
print(list_num)
for i in list_num:
    if list_num[0] == list_num[1]:

        list_num[0] = list_num[0]+list_num[1]
        list_num.remove(list_num[1])
print(list_num)


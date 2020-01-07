list_num = list(map(int, input().split(" ")))
print(list_num)
#for i in list_num:
    #if list_num[0] == list_num[1]:

        #list_num[1] = list_num[0]+list_num[1]
        #list_num.remove(list_num[0])

i = 0
while i < (len(list_num) - 1):
    if list_num[i] == list_num[i + 1] and i >= 0:
        list_num[i] += list_num[i + 1]
        list_num.remove(list_num[i + 1])
        i -= 1
    else:
        i += 1

for item in list_num:
    print(" ".join(["{:g}".format(item)]), end=" ")


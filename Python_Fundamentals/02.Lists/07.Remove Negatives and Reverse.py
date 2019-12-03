list_num = list(map(int, input().split(" ")))
postives_list = []
for i in range(len(list_num)):
    if list_num[i] > 0:
        postives_list.append(list_num[i])
postives_list.reverse()
if len(postives_list) > 0:
    print(postives_list)
else:
    print('empty')








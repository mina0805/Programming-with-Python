list_num = list(map(int, input().split(" ")))
sum_odd = 0
for item in list_num:
    if item % 2 != 0:
        sum_odd += 1
print(sum_odd)

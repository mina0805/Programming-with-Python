n = int(input())

sum = int(input())
biggest_num = sum

for i in range(1, n):
    num = int(input())
    sum += num
    if num > biggest_num:
        biggest_num = num


final_sum = sum - biggest_num
if final_sum == biggest_num:
    print('Yes')
    print('Sum = ' + str(biggest_num))
else:
    print('No')
    print('Diff = ' + str(abs(biggest_num - final_sum)))




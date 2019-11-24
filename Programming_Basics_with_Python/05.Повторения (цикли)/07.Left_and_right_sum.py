n = int(input())

left_sum = 0
right_sum = 0

for i in range(1, (2*n)+1):
    curr_num = int(input())
    if i <= n:
        left_sum += curr_num
    elif i > n:
        right_sum += curr_num
if left_sum == right_sum:
    print('Yes, sum = ' + (str(left_sum)))
else:
    print('No, diff = ' + (str(abs(left_sum - right_sum))))




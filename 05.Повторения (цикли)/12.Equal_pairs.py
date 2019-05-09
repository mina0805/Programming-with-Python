n = int(input())

first_pair = int(input()) + int(input())
prev_pair = first_pair
diff = 0

for i in range(1, n):
    curr_pair = int(input()) + int(input())
    diff = curr_pair - prev_pair
    if curr_pair > prev_pair:
        prev_pair = curr_pair
        diff = curr_pair - first_pair
    elif curr_pair == prev_pair:
        diff = 0
if diff == 0:
    print('Yes, value = ' + str(prev_pair))
else:
    print('No, maxdiff = ' + str(abs(diff)))








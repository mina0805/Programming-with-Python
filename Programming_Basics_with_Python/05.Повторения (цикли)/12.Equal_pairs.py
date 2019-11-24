n = int(input())

first_pair = int(input()) + int(input())
prev_pair = first_pair
max_diff = 0

for i in range(1, n):
    curr_pair = int(input()) + int(input())
    temp_diff = abs(prev_pair - curr_pair)
    prev_pair = curr_pair
    if temp_diff > max_diff:
        max_diff = temp_diff


if max_diff == 0:
    print("Yes, value = ", prev_pair)
else:
    print("No, maxdiff = ", max_diff)


n = int(input())

min_num = 999999999999999

for i in range(1, n+1):
    num = int(input())
    if num < min_num:
        min_num = num
print(min_num)

n = int(input())


sum_p1 = 0
sum_p2 = 0
sum_p3 = 0
sum_p4 = 0
sum_p5 = 0
total = 0

for i in range(0, n):
    num = int(input())

    if 0 < num < 200:
        sum_p1 += i
    elif 200 <= num <= 399:
        sum_p2 += i
    elif 400 <= num <= 599:
        sum_p3 += i
    elif 600 <= num <= 799:
        sum_p4 += i
    elif 800 <= num:
        sum_p5 += i

total = sum_p1 + sum_p2 + sum_p3 + sum_p4 + sum_p5

print('{0:.2%}'.format(sum_p1/total))
print('{0:.2%}'.format(sum_p2/total))
print('{0:.2%}'.format(sum_p3/total))
print('{0:.2%}'.format(sum_p4/total))
print('{0:.2%}'.format(sum_p5/total))





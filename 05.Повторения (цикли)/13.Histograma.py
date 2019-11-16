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
        sum_p1 += 1
    elif 200 <= num <= 399:
        sum_p2 += 1
    elif 400 <= num <= 599:
        sum_p3 += 1
    elif 600 <= num <= 799:
        sum_p4 += 1
    elif 800 <= num:
        sum_p5 += 1

print('{0:.2%}'.format(sum_p1/n))
print('{0:.2%}'.format(sum_p2/n))
print('{0:.2%}'.format(sum_p3/n))
print('{0:.2%}'.format(sum_p4/n))
print('{0:.2%}'.format(sum_p5/n))





n = int(input())
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
sum_p = p1 + p2 +p3 + p4 + p5

for i in range(1, n+1):
    num = int(input())
    if num < 1 or num > 1000:
        print('invalid entry, enter a number between 1 and 1000')
    elif 1 < num <= 200:
        p1 = 1 + p1
    elif 200 < num <= 399:
        p2 = 1 + p2
    elif 399 < num <= 599:
        p3 = 1 + p3
    elif 599 < num <= 799:
        p4 = 1 + p4
    elif 799 < num <= 1000:
        p5 = 1 + p5
print('{0:.2%}'.format(p1/n))
print('{0:.2%}'.format(p2/n))
print('{0:.2%}'.format(p3/n))
print('{0:.2%}'.format(p4/n))
print('{0:.2%}'.format(p5/n))








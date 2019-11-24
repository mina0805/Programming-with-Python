n = int(input())

p1 = 0
p2 = 0
p3 = 0

for i in range(0, n):
    num = int(input())
    if num % 2 == 0:
        p1 += 1
    if num % 3 == 0:
        p2 += 1
    if num % 4 == 0:
        p3 += 1

print('{0:.2%}'.format(p1 /n))
print('{0:.2%}'.format(p2 /n))
print('{0:.2%}'.format(p3 /n))

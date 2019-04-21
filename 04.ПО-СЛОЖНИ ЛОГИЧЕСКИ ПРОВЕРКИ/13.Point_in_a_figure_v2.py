h = int(input())
x = int(input())
y = int(input())

#1
one = (0 <= x <= 3 * h and y == 0)
#2
two = (x == 0 and 0 <= y <= h)
#3
three = (0 <= x <= h and y == h)
#4
four = (x == h and h <= y <= 4 * h)
# 5
five = (h <= x <= 2 * h and y == 4 * h)
# 6
six = (x == 2 * h and h <= y <= 4 * h)
# 7
seven = 2 * h <= x <= 3 * h and y == h
# 8
eight = x == 3 * h and 0 <= y <= h

if (0 < x < 3*h and 0 < y < h) or (h <x <2*h and 0 < y < 4*h):
    print('inside')
elif one or two or three or four or five or six or seven or eight:
    print('border')
else:
    print('outside')

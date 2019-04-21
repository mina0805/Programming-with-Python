h = int(input())
x = int(input())
y = int(input())

# inside if:
# square 1: (0 < x < 3h and 0 < y < h)
        # or
# square 2: h <x <2h and 0 < y < 4h

# border:
# 0 <= x <= 6 and y == 0
# x == 0 and  0<= y <= 2
# 0 <= x <= 2 and y == 2
# x == 2 and 2 <= y <= 8
# 2 <= x <= 4 and y == 8
# x == 4 and 2<= y <= 8
# 4 <= x <= 6 and y == 2
# x == 6 and 0<= y <= 6

# else -> outside

if ((0 < x < 3*h and 0 < y < h)) or (h <x <2*h and 0 < y < 4*h):
    print('inside')

elif (0 <= x <= 3*h and y == 0) or (x == 0 and 0 <= y <= h) or 0 <= x <= h and h <=y <= 4*h or h <= x <= 2*h and y == 4*h or x == 2*h and h <= y <= 4*h or 2*h <= x <= 3*h and y == h or x == 3*h and 0<= y <= h:
    print('border')
else:
    print('outside')

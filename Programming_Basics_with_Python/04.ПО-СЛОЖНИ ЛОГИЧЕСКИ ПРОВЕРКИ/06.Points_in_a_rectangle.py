x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x = float(input())
y = float(input())

border1 = (x1 <= x <= x2) and (y == y2)
border2 = (y1 <= y <= y2) and (x == x2)
border3 = (x1 <= x <= x2) and (y == y1)
border4 = (y1 <= y <= y2) and (x == x1)


if border1 or border2 or border3 or border4:
    print("Border")
else:
    print("Inside / Outside")

x = float(input("enter house height: "))
y = float(input("enter length of house: "))
h = float(input("enter height of roof: "))

fron_side = (x * x) - (1.2 *2)
back_side = x * x
sides = (x * y * 2) - (1.5*1.5*2)
green = (front_side+back_side+sides)/3.4

roof = x*y*2 + x*h
red = roof/4.3
print('%.2f' % green)
print('%.2f' % red)
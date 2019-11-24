# square, rectangle, circle или triangle

# enter figure
# if Square
# enter a
# S = a * a
#print S

import math

figure = input()
if figure == "square":
    a = float(input())
    S_square = a * a
    print("%.3f" % S_square)

elif figure == "rectangle":
    a = float(input())
    b = float(input())
    S_rectangle = a * b
    print("%.3f" % S_rectangle)

elif figure == "circle":
    r = float(input())
    S_circle = r * r * math.pi
    print("%.3f" % S_circle)

elif figure == "triangle":
    a = float(input())
    ha = float(input())
    S_triangle = (a * ha)/2
    print("%.3f" % S_triangle)

import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def calc_side_c(a, b):
    c = math.sqrt(a**2 + b**2)
    return c

first_point_input = list(map(float,input().split()))
second_point_input = list(map(float, input().split()))

x1 = first_point_input[0]
y1 = first_point_input[1]
x2 = second_point_input[0]
y2 = second_point_input[1]

first_point_object = Point(x=x1, y=y1)
second_point_object = Point(x=x2, y=y2)

side_a = abs(first_point_object.x - second_point_object.x)
side_b = abs(first_point_object.y - second_point_object.y)

side_c = calc_side_c(side_a, side_b)
print(side_c)


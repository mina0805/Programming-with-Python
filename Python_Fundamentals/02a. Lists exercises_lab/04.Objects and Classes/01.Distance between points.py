import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


raw_data = list(map(float, input().split(" ")))
x1 = raw_data[0]
y1 = raw_data[1]
x2 = raw_data[2]
y2 = raw_data[3]

first_point = Point(x1, y1)
second_point = Point(x2, y2)

side_a = abs(first_point.x + second_point.x)
side_b = abs(first_point.y + second_point.y)
side_c = math.sqrt(pow(side_a,2) + pow(side_b,2))

print(side_c)


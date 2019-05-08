w = float(input())
h = float(input())

import math
rows = math.floor(w /1.2)
print(rows)
desks_per_row = math.floor((h - 1)/0.7)
print(desks_per_row)
seats = (rows * desks_per_row) - 3
print(seats)

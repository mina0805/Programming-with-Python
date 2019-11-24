n = int(input())
row = 0
star = "* "
space = " "
sec_part_star = n-1

for row in range(1, n+1):
    print(space * (n-row) + (star * row))

for row2 in range(1, n):
    print(space * row2 + star * (n - row2))

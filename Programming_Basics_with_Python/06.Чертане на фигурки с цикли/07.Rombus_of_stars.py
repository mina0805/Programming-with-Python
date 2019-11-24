n = int(input())
row = 0
star = "* "
space = " "
sec_part_star = n-1

for row in range(1, 2*n):
    if row <= n:
        print(space * (n-row) + (star * row))
    else:
        space = row - n
        print(" " * space + "* " * sec_part_star)
        sec_part_star -= 1





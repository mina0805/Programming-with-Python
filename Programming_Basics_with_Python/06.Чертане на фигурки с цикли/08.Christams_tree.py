n = int(input())

space = " "
star = "*"
post = " | "
print(space * n + post + space * (n+1))

for row in range(1, n+1):
    print(space * (n-row) + star * row + post + star * row)

n= int(input())
star = "*"
space = " "

for row in range(0,n):
    if row == 0:
        print(star + star*(n-2) + star)
    elif 0 < row < n-1:
        print(star + space * (n-2) + star)
    if row == n-1:
        print(star + star*(n-2) + star)


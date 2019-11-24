n = int(input())

stars = 2*n
space = n
slash = (2*n)-2
pole = n

print("*" * stars + " " * space + "*" * stars)

for row in range(1,n-1):
    if n % 2 == 0 and row == (n-2)//2:
        print("*" + slash * "/" + "*" + "|"* space + "*" + slash * "/" + "*")
    elif n % 2 == 1 and row == (n-1)//2:
        print("*" + slash * "/" + "*" + "|"* space + "*" + slash * "/" + "*")
    else:
        print("*" + slash * "/" + "*" + " " * space + "*" + slash * "/" + "*")
print("*" * stars + " " * space + "*" * stars)






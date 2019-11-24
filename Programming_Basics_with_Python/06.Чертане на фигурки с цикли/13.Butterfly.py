n = int(input())
star = n-2
dash = n-2
space = n-1
for row in range(1, n-1):
    if row %2==1:
        print(star * "*" + "\\" + " " + "/" + star * "*")
    else:
        print(dash * "-" + "\\" + " " + "/" + dash * "-")
print(space * " " + "@" + space * " ")

for row2 in range(1, n-1):
    if row2 %2==1:
        print(star * "*" + "/" + " " + "\\" + star * "*")
    else:
        print(dash * "-" + "/" + " " + "\\" + dash * "-")

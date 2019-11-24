n = int(input())
underscore = ((((2*n) - n//2)-n//2)-4)
print("/" + ((n//2) * "^") + "\\" + underscore * "_" + "/" + ((n//2) * "^") + "\\")
for row in range(1,n-2):
    print("|" + (((2*n)-2) * " ") + "|")

print("|" + (((n//2) + 1) * " ") + underscore * "_" + (((n//2) +1) * " ")+ "|")
print("\\" + ((n//2) *"_") + "/" + underscore * " " + "\\" + ((n//2) *"_") + "/")


dot_left = 1
dot_right = 1
pound = 1
row1 = 1
n = int(input())
for row1 in range(n+1):
    if row1 < n//2:
        dot_left = n + row1
        dot_right = n + row1
        pound = 3*n - row1 *2
        inside_dot = 0
        print(dot_left * (".") + (pound * ("#")) + (dot_right * (".")))
    elif row1 >= n//2:
        dot_left = n+row1
        dot_right = n+row1
        pound = 1
        inside_dot = (5*n) - (dot_left + 2 + dot_right)
        print((dot_left * (".") + (pound * ("#")) + (inside_dot * (".")) + (pound * ("#")) + (dot_right * ("."))))
for row2 in range(n//2 + 1):
    dot = (".")
    pound2 = ('#')
    if row2 == 0:
        print(2*n* '.' + (n * "#") + (2*n * (".")))
    elif 0 < row2 <= n//2 +1:
        print((2*n - 2)* '.' + ((n+4) * "#") + ((2*n -2 )* "."))

dot4 = ((((5*n)-10)//2)* ".")
d = "D^A^N^C^E^"
print(f"{dot4}{d}{dot4}")

for row3 in range(1,n//2 +2):
    print((2 * n - 2) * ('.') + ((n + 4) * ("#")) + ((2 * n - 2) * (".")))




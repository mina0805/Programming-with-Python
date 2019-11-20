dot_left = 1
dot_right = 1
pound = 1
row1 = 1
n = int(input())
for row1 in range(n//2):
    dot_left = n + row1
    dot_right = n + row1
    pound = 3*n - row1 *2
    print(dot_left * (".") + (pound * ("#")) + (dot_right * (".")))
for row2 in range(n//2+1):
    dot_left2 = n + n//2 +row2
    dot_right2 = n + n//2 +row2
    inside_dot = (((n*5)-2)-dot_left2-dot_right2)
    pound2 = 1
    print(dot_left2 * ("."))






n = int(input())
left_dash = 1
right_dash = 1
row = 1
row2 =1

if n % 2 == 1:
    left_dash = (n // row - 1) // 2
    right_dash = (n // row - 1) // 2
    inside_dash = n - 2 - left_dash - right_dash
    left_dash2 = row2
    right_dash2 = row2
    inside_dash2 = n - 2 - left_dash2 - right_dash2

    for row in range(1, n // 2 + 2):
        if row == 1:
            print(("-" * left_dash) + "*" + (right_dash * "-"))
        else:
            print(("-" * left_dash) + "*" + ("-" * inside_dash) + "*" + (right_dash * "-"))
        left_dash -= 1
        right_dash -= 1
        inside_dash += 2

    for row2 in range(1, n//2+1):
        left_dash2 = row2
        right_dash2 = row2
        inside_dash2 = n - 2 - left_dash2 - right_dash2
        if row2 < n//2:
            print(left_dash2 * "-" + "*" +inside_dash2 * "-"+ "*" + right_dash2 * "-")
        elif row2 == n//2:
            print(left_dash2 * "-" + "*" + right_dash2 * "-")

if n%2 == 0:
    left_dash3 = n//2 -1
    right_dash3 = n//2 - 1
    inside_dash3 = n - 2 - left_dash3 - right_dash3
    for row3 in range(1, n//2):
        print(left_dash3 * "-" + "*" + inside_dash3 * "-" + "*" + right_dash3 * "-")
        left_dash3 -= 1
        right_dash3 -= 1
        inside_dash3 += 2

    print("*" + ((n-2)* "-") + "*")

    for row4 in range(1, n//2):
        left_dash4 = row4
        right_dash4 = row4
        inside_dash4 = n - 2 - left_dash4 - right_dash4
        print(left_dash4 * "-" + "*"+inside_dash4 * "-"+"*"+right_dash4 * "-")



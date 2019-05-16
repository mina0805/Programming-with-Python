n = int(input())
left_dash = 1
right_dash = 1
dash = 1
row = 1

if n % 2 == 1:
    left_dash = (n // row - 1) // 2
    right_dash = (n // row - 1) // 2
    inside_dash = n - 2 - left_dash - right_dash
    for row in range(1, n // 2 + 2):
        if row == 1:
            print(("-" * left_dash) + "*" + (right_dash * "-"))
        else:
            print(("-" * left_dash) + "*" + ("-" * inside_dash) + "*" + (right_dash * "-"))
        left_dash -= 1
        right_dash -= 1
        inside_dash += 2



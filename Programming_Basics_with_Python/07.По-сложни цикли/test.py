n = int(input())

num = 0

for row in range(n):
    for col in range(n):
        num = row + col + 1
        if num <= n:
            print(num)
        else:
            num = 2 * n - num
            print(num)
    print("")



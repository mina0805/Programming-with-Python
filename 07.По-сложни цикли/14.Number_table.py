n = int(input())

num = 0

for row in range(n):
    for col in range(n):
        num = row + col + 2
        if num <= n:
            print(num, end=" ")
        else:
            num = 2 * n - num
            print(num, end=" ")
    print("")

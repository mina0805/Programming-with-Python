n = int(input())

if 2 <= n <= 100:
    print("*" * n)

    print(("*" + ' ' * (n - 2) + "*\n")*(n-2), end="")

    print("*" * n)



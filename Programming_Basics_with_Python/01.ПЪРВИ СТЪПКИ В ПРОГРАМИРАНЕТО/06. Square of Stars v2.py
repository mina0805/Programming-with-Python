raw_input = input()
n = int(raw_input)
if 2 <= n <= 100:
    print("*" * n)
    for i in range(0, (n - 2)):
        print(("*" + ' ' * (n - 2) + "*"))
    print("*" * n)



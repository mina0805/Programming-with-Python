n = int(input())

count = 0

for row in range(n):
    for col in range(row + 1):
        count += 1
        print(count, "", end="")
        if count == n:
            break
    if count == n:
        break
    print("")



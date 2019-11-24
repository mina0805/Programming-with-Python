n = int(input())

if n%2 == 0:
    dash = n-2
    star = n-dash
    for row in range(1,n//2 +1):
        print("-" * (dash // 2) + "*" * star + "-" * (dash // 2))
        star += 2
        dash -= 2
elif n%2 == 1:
    dash = n-1
    star = n-dash
    for row in range(1, n // 2 + 2):
        print("-" * (dash // 2) + "*" * star + "-" * (dash // 2))
        star += 2
        dash -= 2
for row2 in range (0,n//2):
    print("|" + "*"* (n-2) + "|")

n = int(input())

plus = "+ "
minus = "- "
post = "| "

for row in range(n):
    if row == 0:
        print(plus + minus * (n-2) + plus)
    elif 0 < row < n-1:
        print(post + minus * (n-2) + post)
    elif row == n-1:
        print(plus + minus * (n - 2) + plus)

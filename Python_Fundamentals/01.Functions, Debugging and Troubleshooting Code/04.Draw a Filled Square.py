num = int(input())

def print_triangle(n):

    for i in range(1, 2*n +1):
        if i ==1:
            print(2*n*"-")
        elif 1 < i <= n-1:
            print("-"+(str("\/" *((2*n -2)//2)))+"-")
        elif i == n+1:
            print(2 * n * "-")


print_triangle(num)



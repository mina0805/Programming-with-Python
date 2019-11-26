num = int(input())


def integer_number(n):
    if n < 0:
        print(f'The number {n} is negative.')
    elif n == 0:
        print(f'The number {n} is zero.')
    else:
        print(f'The number {n} is positive.')


integer_number(num)

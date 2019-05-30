n = int(input())
is_prime = True
import math

if n < 2:
    is_prime = False

else:
    square_n = math.floor(math.sqrt(n))
    for i in range(2,square_n+1):
        if n/i == n//i:
            is_prime = False
        else:
            is_prime = True

if is_prime:
        print('Prime')

else:
        print('Not Prime')




n = float(input('Enter even number: '))

while n%2 != 0:
    print('Invalid number')
    print('The number is not even')
    n = float(input('Enter even number: '))
if n%2 == 0:
    print(str("Even number entered: ") + (str("%.0f" % n)))





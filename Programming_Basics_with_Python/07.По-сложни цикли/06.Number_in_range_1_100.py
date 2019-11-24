n = int(input("Еnter a number in the range [1...100]: "))
while not 1 <= n <= 100:
    print('Invalid number!')
    n = int(input("Еnter a number in the range [1...100]: "))
if 1 <= n <= 100:
    print("The number is: " + str(n))
